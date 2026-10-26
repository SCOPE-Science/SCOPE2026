"""Exact finite arithmetic checks for Gauss-survivor complement geometry."""
from fractions import Fraction as F
from itertools import product

def branch(a,x):
    return 1/(F(a)+x)

def fold(w,x):
    for a in reversed(w):
        x=branch(a,x)
    return x

def primary(m,a):
    return F(1,a+1),F(m,a*m+1)

def length(m,w,a):
    l,r=primary(m,a)
    x,y=fold(w,l),fold(w,r)
    return abs(y-x)

def formula(m,w,a):
    qm1,q=0,1
    for b in w:
        qm1,q=q,b*q+qm1
    l,r=primary(m,a)
    delta=r-l
    # Formula q_k + q_{k-1}t, with q_-1=0, q_0=1.
    return delta/((q+qm1*l)*(q+qm1*r))

cases=0
for m in range(2,9):
    maximum=F(m*(m-1),(m*m+1)*(m+1)) # m times max primary gap
    assert F(m,2)*(primary(m,m)[1]-primary(m,m)[0]) == maximum/2
    for depth in range(4):
        for w in product(range(m,m+4),repeat=depth):
            for a in range(m,m+5):
                d=length(m,w,a)
                assert d==formula(m,w,a)
                if w: assert d<primary(m,m)[1]-primary(m,m)[0]
                else: assert d<=primary(m,m)[1]-primary(m,m)[0]
                cases+=1
    for a in range(m,m+25):
        assert primary(m,a)[1] < F(1,a)
        assert primary(m,a)[0] == F(1,a+1)
print('VERIFY_OK exact_rational_gap_checks=',cases)
