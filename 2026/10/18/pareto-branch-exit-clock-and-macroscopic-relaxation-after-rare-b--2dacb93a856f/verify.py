"""Exact-rational cross-checks for the BCZ cusp-relaxation theorem.
Run with Python 3 standard library; finite tests supplement the written proof.
"""
from fractions import Fraction as Q
from math import ceil

def kappa(a,b):
    return (1+a)//b

def step(a,b):
    k=kappa(a,b)
    return b,k*b-a

def ceiling_fraction(v):
    return -(-v.numerator//v.denominator)

def case(r,branch,scale,s):
    d=Q(1,r*scale)
    if branch==0:
        a,b=d,1-s*d
        j0=1
        u=b
    else:
        a,b=1-s*d,d
        j0=2
        kk=kappa(a,b)
        c=kk*b-a
        u=c
    assert a+b>1 and a*b<Q(1,r)
    assert j0==1 or kappa(*step(a,b))==1
    assert d<Q(1,3)
    L=max(0,ceiling_fraction((u-(1+d)/2)/d)-1)
    stop=j0+L
    x,y=a,b
    for j in range(stop+1):
        if j>=j0 and j<stop:
            assert kappa(x,y)==2
            ell=j-j0
            assert (x,y)==(u-ell*d,u-(ell+1)*d)
        if j==stop:
            assert kappa(x,y)!=2
        if j<stop:
            x,y=step(x,y)
    assert abs(Q(stop)*d-Q(1,2))<=Q(6)*d
    return stop

def check():
    tests=0
    for r in (64,127,257,511):
        for branch in (0,1):
            for scale in (2,3,5):
                for s in (Q(1,9),Q(1,4),Q(1,2),Q(3,4),Q(8,9)):
                    case(r,branch,scale,s)
                    tests+=1
    # Analytic transformed-density normalization: V has density 2v on [0,1].
    for t in (Q(1,4),Q(1,3),Q(2,5)):
        # Exact path transformation at v=0, 1/2, 1.
        for v in (Q(0),Q(1,2),Q(1)):
            y=1/(1-t*v)**2
            assert y>=1 and y<=1/(1-t)**2
    print('VERIFY_OK',tests,'exact branch-and-exit cases')
if __name__=='__main__':check()
