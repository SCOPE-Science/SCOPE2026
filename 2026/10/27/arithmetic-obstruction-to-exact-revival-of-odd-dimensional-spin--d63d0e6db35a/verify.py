"""Finite-matrix diagnostics for central harmonic Grover dynamics.
No finite-dimensional calculation is used as proof of the all-dimension claim.
"""
import numpy as np
from itertools import product
from math import sin, pi, comb

def matrix_M(d, eps):
    assert d>=3 and d%2==1 and eps in (-1,1)
    m=(d-1)//2; w=np.exp(-1j*eps*pi/d)
    a=np.zeros((8,8),complex)
    a[0,1]=-w**m/d; a[0,2]=2*(m+1)*w**m/d; a[0,3]=2*w**m/d
    a[1,0]=-w**(m-1)
    a[2,4]=-w**(m+1)
    a[3,4]=2*w**(m+1)/d; a[3,5]=w**(m+1)/d; a[3,6]=2*m*w**(m+1)/d
    a[4,1]=2*m*w**m/d; a[4,2]=w**m/d; a[4,3]=2*w**m/d
    a[5,3]=-w**m
    a[6,7]=-w**(m+2)
    a[7,4]=2*w**(m+1)/d; a[7,5]=2*(m+1)*w**(m+1)/d; a[7,6]=-w**(m+1)/d
    return a

def harmonic_f(d):
    m=(d-1)//2; f={}
    for choice in product((0,1),repeat=m):
        p=sum(1 << (2*i+choice[i]) for i in range(m))
        f[p]=(-1)**sum(choice)
    return f

def raising(f,d):
    g={}
    for p,v in f.items():
        for k in range(d):
            if not (p & 1<<k):g[p | (1<<k)]=g.get(p | (1<<k),0)+v
    return g

def lift(f,d,kind):
    out=np.zeros(2**d*d,complex)
    for p,v in f.items():
        for k in range(d):
            has=bool(p&(1<<k))
            if kind=='down' and has:out[(p^(1<<k))*d+k]+=v
            if kind=='up' and not has:out[(p^(1<<k))*d+k]+=v
            if kind=='minus' and has:out[p*d+k]+=v
            if kind=='plus' and not has:out[p*d+k]+=v
    return out

def full_step_matrix(d,eps):
    N=2**d; G=2*np.ones((d,d))/d-np.eye(d)
    U=np.zeros((N*d,N*d),complex)
    for p in range(N):
        phase=np.exp(-1j*eps*pi*p.bit_count()/d)
        for k in range(d):
            row=(p^(1<<k))*d+k
            U[row,p*d:p*d+d]=phase*G[k]
    return U

def diagnostic():
    checks=0
    for d in (3,5,7,9,11,13,15,21,33,55,101):
      for eps in (1,-1):
        M=matrix_M(d,eps)
        A=4*(1-d*np.sin(pi/d)**2)/d**2
        B=(2+2*(3-d*d)*np.cos(2*pi/d))/d**2
        poly=np.poly(M)
        target=np.array([1,0,A,0,B,0,A,0,1],float)
        assert np.max(np.abs(poly-target))<1e-8,(d,eps,poly,target)
        assert abs(-np.trace(M@M)/2-A)<1e-11
        assert abs(np.linalg.det(M)-1)<1e-10
        assert np.max(abs(abs(np.linalg.eigvals(M))-1))<1e-10
        assert abs(A)>1e-16
        checks+=5
    for d in (3,5,7):
      f=harmonic_f(d);g=raising(f,d);m=(d-1)//2
      for j in range(d):
        pass
      # Strict lowering harmonicity: A^- f = 0
      low={}
      for p,v in f.items():
        for k in range(d):
          if p&(1<<k):low[p^(1<<k)]=low.get(p^(1<<k),0)+v
      assert all(v==0 for v in low.values())
      # Upper harmonicity: A^+g=0
      upp=raising(g,d)
      assert all(v==0 for v in upp.values())
      L=np.column_stack([lift(f,d,'down'),lift(f,d,'minus'),lift(f,d,'plus'),lift(g,d,'down'),lift(f,d,'up'),lift(g,d,'minus'),lift(g,d,'plus'),lift(g,d,'up')])
      assert np.linalg.matrix_rank(L)==8
      for eps in (1,-1):
        U=full_step_matrix(d,eps)
        residual=np.max(abs(U@L-L@matrix_M(d,eps)))
        assert residual<2e-12,(d,eps,residual)
        assert np.max(abs(U.conj().T@U-np.eye(d*2**d)))<2e-12
        checks+=2
      checks+=3
    print('PASS',checks,'matrix identities and full-walk intertwinement checks')
    for d in (3,5,7,9,11,21,55):
        lo=4*(1-d)/d**2;hi=4/d**2
        assert max(abs(lo),abs(hi))<1
        print('d',d,'A=',4*(1-d*sin(pi/d)**2)/d**2,'conjugate_abs_bound=',max(abs(lo),abs(hi)))

if __name__=='__main__':diagnostic()
