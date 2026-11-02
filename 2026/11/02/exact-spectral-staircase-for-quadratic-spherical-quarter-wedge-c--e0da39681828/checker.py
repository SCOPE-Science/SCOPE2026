"""Independent monomial Gram census for quadratic spherical quadrant concentration.

Usage: python checker.py
Requires numpy and scipy. The primary theorem is analytical; this program supplies
finite-dimensional numerical cross-checks, not an all-dimension proof.
"""
from itertools import combinations
from math import exp, lgamma, pi, sqrt
import numpy as np
from scipy.linalg import eigh


def moment_abs(d, powers):
    """Normalized absolute moment of coordinates on a uniform sphere."""
    return exp(lgamma(d/2.0)-lgamma((d+sum(powers))/2.0)
               +sum(lgamma((a+1)/2.0)-lgamma(0.5) for a in powers))


def full_basis(d):
    exponents=[]
    exponents.append((0,)*d)
    for i in range(d):
        e=[0]*d;e[i]=1;exponents.append(tuple(e))
    for i,j in combinations(range(d),2):
        e=[0]*d;e[i]=1;e[j]=1;exponents.append(tuple(e))
    for i in range(d-1):
        e=[0]*d;e[i]=2;exponents.append(tuple(e))
    assert len(exponents)==d*(d+3)//2
    return exponents


def matrix_full(d):
    base=full_basis(d)
    size=len(base)
    G=np.zeros((size,size)); K=np.zeros((size,size))
    for i,e in enumerate(base):
        for j,f in enumerate(base[:i+1]):
            p=tuple(a+b for a,b in zip(e,f))
            m=moment_abs(d,p)
            full=m if all(x%2==0 for x in p) else 0.0
            quad=m/4 if all(x%2==0 for x in p[2:]) else 0.0
            G[i,j]=G[j,i]=full
            K[i,j]=K[j,i]=quad
    return G,K


def two_var(d,a,b):
    return moment_abs(d,(a,b)+(0,)*(d-2))

scalar_plus=[{(0,0):1}, {(1,0):1,(0,1):1},
             {(2,0):1,(0,2):1}, {(1,1):1}]
scalar_minus=[{(1,0):1,(0,1):-1}, {(2,0):1,(0,2):-1}]
vector_plus=scalar_plus[:2]
vector_minus=scalar_minus[:1]


def block(d, basis, vector=False):
    n=len(basis)
    G=np.zeros((n,n)); K=np.zeros((n,n))
    for i,p in enumerate(basis):
        for j,q in enumerate(basis):
            for (a,b),c in p.items():
                for (e,f),h in q.items():
                    aa=a+e;bb=b+f
                    M=two_var(d,aa,bb)
                    if vector:M/=d+aa+bb
                    if aa%2==0 and bb%2==0:G[i,j]+=c*h*M
                    K[i,j]+=c*h*M/4
    return G,K


def predicted(d):
    m=d-2
    vals=[]
    for polynomials,vector,mult in [
       (scalar_plus,False,1), (scalar_minus,False,1),
       (vector_plus,True,m), (vector_minus,True,m)]:
        G,K=block(d,polynomials,vector)
        roots=eigh(K,G,check_finite=True,eigvals_only=True)
        for root in roots: vals += [root]*mult
    vals += [1/4]*(d*(d-3)//2)
    return np.sort(np.array(vals))


def run():
    count=0
    for d in range(3,13):
        G,K=matrix_full(d)
        w_full=eigh(K,G,check_finite=True,eigvals_only=True)
        w_blocks=predicted(d)
        assert w_full.size==w_blocks.size
        assert np.max(np.abs(w_full-w_blocks))<1.0e-10,(d,np.max(np.abs(w_full-w_blocks)))
        assert np.min(w_full)>0.0 and np.max(w_full)<1.0
        assert abs(sum(w_full)-len(w_full)/4)<1.0e-10
        assert sum(w_full>0.5+1e-9)==d-1
        assert sum((w_full>0.25+1e-9)&(w_full<0.5-1e-9))==2
        assert sum(abs(w_full-0.25)<1.0e-9)==d*(d-3)//2
        assert sum(w_full<0.25-1e-9)==2*d-1
        assert w_full[-1]>.75
        coeff=np.zeros(len(full_basis(d)))
        coeff[0]=1.0
        coeff[1]=sqrt(d)
        coeff[2]=sqrt(d)
        coeff[d+1]=d
        q=float(coeff@K@coeff/(coeff@G@coeff))
        mu=moment_abs(d,(1,)+(0,)*(d-1))
        q_formula=0.25+(sqrt(d)*mu*(2*d+1)/(d+1)+2/pi)/(4-2/(d+2))
        assert abs(q-q_formula)<1e-12 and q>0.75
        count+=len(w_full)+8
    print('QUADRANT_CHECKS_PASS',count)

if __name__=='__main__':run()
