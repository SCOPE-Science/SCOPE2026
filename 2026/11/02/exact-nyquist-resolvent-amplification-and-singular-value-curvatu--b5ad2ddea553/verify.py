"""Reproduce exact finite-sum identities and test the BPF discrete Green operator.
Run: python bpf_nyquist_verify.py (requires NumPy; math derivation in RESULT.md).
"""
from fractions import Fraction
import math
import numpy as np


def theta(s):
    return s*s/(4*math.sin(s/2)**2)


def green(n,s,L=1.0):
    h=L/n
    m=n-1
    q=np.arange(1,n)
    K=np.exp(-1j*s*np.abs(q[:,None]-q[None,:]))
    return -h*h/(2j*theta(s)*math.sin(s))*K


def full_solution(n,s,f,L=1.0):
    h=L/n
    t=theta(s)
    A=np.zeros((n+1,n+1),dtype=complex)
    b=np.zeros(n+1,dtype=complex)
    A[0,0]=-np.exp(1j*s)
    A[0,1]=1
    A[n,n-1]=1
    A[n,n]=-np.exp(1j*s)
    for i in range(1,n):
        A[i,i-1]=t/h**2
        A[i,i]=-2*t*math.cos(s)/h**2
        A[i,i+1]=t/h**2
        b[i]=f[i-1]
    return np.linalg.solve(A,b)[1:n]


def curvature(m):
    return Fraction((m*m-1)*(2*m*m+7),90*m*m)


def check_sums(m):
    r=[sum(abs(i-j) for j in range(m)) for i in range(m)]
    rs=sum(r)
    rr=sum(x*x for x in r)
    sq=sum((i-j)**2 for i in range(m) for j in range(m))
    assert Fraction(rs)==Fraction(m*(m*m-1),3)
    assert Fraction(rr)==Fraction(m*(m*m-1)*(7*m*m-8),60)
    assert Fraction(sq)==Fraction(m*m*(m*m-1),6)
    lam2=Fraction(2*rr,m)-Fraction(rs*rs,m*m)-sq
    assert lam2==-Fraction((m*m-1)*(2*m*m+7),45)
    assert -lam2/Fraction(2*m*m)==curvature(m)


def main():
    for m in range(1,128):
        check_sums(m)
    rng=np.random.default_rng(11703)
    solve_count=0
    norm_count=0
    for n in range(2,18):
        for s in (0.13,0.7,1.43,2.41,3.04):
            f=rng.standard_normal(n-1)+1j*rng.standard_normal(n-1)
            u0=full_solution(n,s,f)
            u1=green(n,s)@f
            assert np.linalg.norm(u0-u1)<2e-10*(1+np.linalg.norm(u1))
            G=green(n,s)
            h=1/n
            fro=np.linalg.norm(G,'fro')
            want=(n-1)*h*h/(2*theta(s)*math.sin(s))
            assert abs(fro-want)<1e-11*max(1,want)
            solve_count+=1
    for m in range(1,36):
        n=m+1
        delta=0.0008
        s=math.pi-delta
        q=np.arange(m)
        K=np.exp(1j*delta*np.abs(q[:,None]-q[None,:]))
        ratio=np.linalg.svd(K,compute_uv=False)[0]/m
        approx=1-float(curvature(m))*delta**2
        # fourth-order remainder O(m^4 delta^4), tested in stable range m delta<0.03
        assert abs(ratio-approx)<6e-7
        norm_count+=1
    print(f'PASS: {127} exact integer-sum identities; {solve_count} full-system Green comparisons and Frobenius identities; {norm_count} singular-curvature probes')

if __name__=='__main__':
    main()
