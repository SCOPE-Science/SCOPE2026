"""Exact-rational checks for the planar single-vector sketch-mixture theorem.

The infinite-family theorem follows from algebra in RESULT.md; finite checks
are diagnostic rather than a substitute for its proof.
"""
from fractions import Fraction as F
from math import gcd


def matvec(A,s):
    return (A[0][0]*s[0]+A[0][1]*s[1],
            A[1][0]*s[0]+A[1][1]*s[1])


def proj(A,s):
    v=matvec(A,s)
    z=sum(x*x for x in v)
    return (v[0]*v[0]/z, v[0]*v[1]/z, v[1]*v[1]/z)


def avg(P,Q):
    return tuple((x+y)/2 for x,y in zip(P,Q))


def mix(P,Q,t):
    return tuple((1-t)*x+t*y for x,y in zip(P,Q))


def spin_sq(M):
    return (M[0]-M[2])**2+4*M[1]*M[1]


def check(c,s,k,t):
    A=((k*c,k*s),(F(-1)*s,c))  # diag(k,1) R(theta)^T
    # Correct first row of R(theta)^T is (cos theta, sin theta).
    e1=(F(1),F(0)); e2=(F(0),F(1))
    plus=(F(1),F(1)); minus=(F(1),F(-1))
    P0=avg(proj(A,e1),proj(A,e2))
    P1=avg(proj(A,plus),proj(A,minus))
    M=mix(P0,P1,t)
    r=(k*k-1)/(k*k+1)
    u=2*c*s
    v=c*c-s*s
    d=(1-r*r*v*v)*(1-r*r*u*u)
    rhs=r*r/d*(u*u*v*v+(1-r*r)*(t-u*u)**2)
    assert spin_sq(M)==rhs, (c,s,k,t,M,spin_sq(M),rhs)
    assert sum((M[0],M[2]))==1
    # Also directly verify the completing-square identity for each rational t.
    tstar=u*u
    mstar=mix(P0,P1,tstar)
    assert spin_sq(M)-spin_sq(mstar)==r*r/d*(1-r*r)*(t-tstar)**2
    # Sparsified Bernoulli law conditioned on nonzero: p=2t/(1+t).
    p=2*t/(1+t)
    assert p/(2-p)==t
    return 3


def run():
    count=0
    for aa,bb in [(3,4),(4,3),(5,12),(12,5),(8,15),(15,8),
                  (7,24),(24,7),(20,21),(21,20),(0,1),(1,0)]:
        norm=aa*aa+bb*bb
        # All listed nontrivial pairs are Pythagorean triples.
        rt=int(norm**0.5)
        assert rt*rt==norm
        c,s=F(aa,rt),F(bb,rt)
        assert c*c+s*s==1
        for k in [F(3,2),F(2),F(5),F(11,4)]:
            for t in [F(0),F(1,7),F(1,3),F(1,2),F(2,3),F(7,8),F(1),4*c*c*s*s]:
                count+=check(c,s,k,t)
    print(f'PASS: {count} exact-rational matrix/projector/polarization identities')

if __name__=='__main__':
    run()
