#!/usr/bin/env python3
"""Standalone exact/numeric checks for lossy Johnson-graph no-jump spectrum.
Requires Python 3, NumPy, SciPy, SymPy. Run: python verify.py
"""
from itertools import combinations
from math import comb
import cmath
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment
import sympy as sp


def matrices(n,k):
    vertices=list(combinations(range(n),k)); D=len(vertices)
    a=np.zeros((D,D),dtype=np.int64)
    for i,s in enumerate(vertices):
        s=set(s)
        for j in range(i+1,D):
            if len(s.intersection(vertices[j]))==k-1:
                a[i,j]=a[j,i]=1
    p=np.diag([int(0 in v) for v in vertices]).astype(np.int64)
    return a,p


def data(n,k,j):
    N=n-1
    mul=comb(N,j)-(comb(N,j-1) if j else 0)
    a=(k-1-j)*(n-k-j)-j
    c=(k-j)*(n-k-1-j)-j
    b2=(k-j)*(n-k-j)
    return mul,a,c,b2


def spectrum(n,k,J,gamma):
    vals=[]
    for j in range(k):
        mult,a,c,b2=data(n,k,j)
        disc=(J*(a-c)-1j*gamma)**2+4*J*J*b2
        root=cmath.sqrt(disc)
        val0=(J*(a+c)-1j*gamma-root)/2
        val1=(J*(a+c)-1j*gamma+root)/2
        vals.extend([val0,val1]*mult)
    d=comb(n-1,k)-comb(n-1,k-1)
    vals.extend([-J*k]*d)
    return np.array(vals,complex)


def survival_formula(n,k,J,gamma,t):
    D=comb(n,k)
    total=comb(n-1,k)-comb(n-1,k-1)
    for j in range(k):
        mult,a,c,b2=data(n,k,j)
        delta=(J*(a-c)-1j*gamma)/2
        omega=cmath.sqrt(delta*delta+J*J*b2)
        u=cmath.cos(omega*t)
        v=t if abs(omega)<1e-12 else cmath.sin(omega*t)/omega
        F=np.exp(-gamma*t)*(2*abs(u)**2+2*(abs(delta)**2+J*J*b2)*abs(v)**2)
        total+=mult*F
    return total/D


def exact_char_polynomial(n,k,gamma):
    A,P=matrices(n,k); z=sp.symbols('z')
    H=sp.Matrix(A.tolist())-sp.I*gamma*sp.Matrix(P.tolist())
    polynomial=sp.Poly(H.charpoly(z).as_expr(),z)
    rhs=sp.Poly((z+k)**(comb(n-1,k)-comb(n-1,k-1)),z)
    for j in range(k):
        d,a,c,b2=data(n,k,j)
        block=(z-a+sp.I*gamma)*(z-c)-b2
        rhs*=sp.Poly(sp.expand(block)**d,z)
    assert sp.expand(polynomial.as_expr()-rhs.as_expr())==0,(n,k,gamma)


def exact_ep(n,k,j):
    A,P=matrices(n,k)
    gamma=2*(k-j)
    mult,a,c,b2=data(n,k,j)
    assert n==2*k and a==c and b2==(k-j)**2
    lam=sp.Rational(a+c,2)-sp.I*gamma/2
    H=sp.Matrix(A.tolist())-sp.I*gamma*sp.Matrix(P.tolist())
    M=H-lam*sp.eye(H.rows)
    kernel=H.rows-M.rank()
    assert kernel==mult,(n,k,j,lam,kernel,mult)
    # Characteristic polynomial multiplicity is exactly 2 * mult.
    z=sp.symbols('z')
    polynomial=sp.Poly(H.charpoly(z).as_expr(),z)
    val=lam
    order=0
    while sp.simplify(polynomial.eval(val))==0:
        order+=1;polynomial=polynomial.diff()
    assert order==2*mult,(n,k,j,order,mult)


def main():
    count=0
    for n in range(4,11):
      for k in range(1,min(n//2,4)+1):
        A,P=matrices(n,k)
        D=A.shape[0]
        assert D==comb(n,k)
        assert sum(data(n,k,j)[0] for j in range(k))*2 +comb(n-1,k)-comb(n-1,k-1)==D
        for gamma in (.73,1.37):
          H=A.astype(complex)-1j*gamma*P
          actual=np.linalg.eigvals(H)
          predicted=spectrum(n,k,1,gamma)
          cost=abs(actual[:,None]-predicted[None,:])
          row,col=linear_sum_assignment(cost)
          assert np.max(cost[row,col])<1e-7,(n,k,gamma,np.max(cost[row,col]))
          count+=1
        for t in (.1,.7,2.):
          gamma=1.37
          H=A.astype(complex)-1j*gamma*P
          U=expm(-1j*H*t)
          actual=np.linalg.norm(U,'fro')**2/D
          predicted=survival_formula(n,k,1,gamma,t)
          assert abs(actual-predicted)<1e-10,(n,k,t,actual,predicted)
          count+=1
    for n,k in [(4,1),(4,2),(5,2),(6,2),(6,3),(7,3)]:
       exact_char_polynomial(n,k,sp.Rational(3,2))
       count+=1
    for n,k,j in [(4,2,0),(4,2,1),(6,3,0),(6,3,1),(6,3,2)]:
       exact_ep(n,k,j)
       count+=1
    print('VERIFY_OK checks='+str(count))

if __name__=='__main__':
    main()
