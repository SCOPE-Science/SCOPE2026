"""Reproduction checks for positive-part stability in complete-graph energy norms.
Requires only Python 3 and NumPy. Run: python CHECK.py
"""
import itertools
from fractions import Fraction
import numpy as np


def gram(n, gamma):
    return (1.0 + n * gamma) * np.eye(n) - gamma * np.ones((n,n))

def formula(n,gamma):
    return 1.0 + gamma**2 * ((n*n)//4) / (1 + gamma*n)

def mask_operator_squared(M, active):
    n=len(M)
    D=np.diag([float(i in active) for i in range(n)])
    L=np.linalg.cholesky(M)
    # M=L L^T. Under input x=L^{-T} z, denominator = z^T z.
    LinvT=np.linalg.inv(L.T)
    K=LinvT.T @ D @ M @ D @ LinvT
    return max(np.linalg.eigvalsh(K))

def explicit_ratio(n,gamma,k):
    ell=n-k
    if k==0 or k==n:return 0.0 if k==0 else 1.0
    b=gamma*k/(1+gamma*k)
    x=np.array([1.0]*k + [b]*ell)
    D=np.array([1.0]*k + [0.0]*ell)
    M=gram(n,gamma)
    return ((D*x)@M@(D*x))/(x@M@x)

def run():
    count=0
    for n in range(2,9):
        for gamma in (0.1,1/3,1.,2.5):
            M=gram(n,gamma); target=formula(n,gamma)
            r=[]
            for bits in itertools.product((0,1),repeat=n):
                S=[i for i,b in enumerate(bits) if b]
                got=mask_operator_squared(M,S)
                should= 1+gamma**2*len(S)*(n-len(S))/(1+gamma*n) if 0<len(S)<n else (1 if len(S)==n else 0)
                assert abs(got-should)<2e-10,(n,gamma,S,got,should)
                r.append(got); count+=1
            assert abs(max(r)-target)<2e-10
            for k in range(1,n):
                got=explicit_ratio(n,gamma,k)
                should=1+gamma**2*k*(n-k)/(1+gamma*n)
                assert abs(got-should)<1e-10
                count+=1
    # exact rational check of Schur-complement derived ratio
    for n in range(2,18):
        for gamma in (Fraction(1,7),Fraction(2,3),Fraction(3,1)):
            for k in range(1,n):
                ell=n-k
                b=gamma*k/(1+gamma*k)
                num=k*(1+gamma*ell)
                den=k+ell*b*b+gamma*k*ell*(1-b)**2
                target=1+gamma*gamma*k*ell/(1+gamma*n)
                assert num/den==target
                count+=1
    print('PASS',count,'mask eigenvalue, witness, and exact rational identities')

if __name__=='__main__':run()
