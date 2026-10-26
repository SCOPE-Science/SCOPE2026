"""Exact rational checks for the finite-mixture nonlinear public-goods theorem.

Run: python3 verify.py (Python standard library only).
The analytic global-root and Taylor assertions are proved in RESULT.md;
finite checks below are consistency checks, not substitutions for proof.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product


def multiply(a,b):
    o=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            o[i+j]+=x*y
    return o


def evaluate(p,x):
    z=Q(0)
    for a in reversed(p):
        z=z*x+a
    return z


def derivative(p):
    return [(i+1)*p[i+1] for i in range(len(p)-1)]


def response(groups):
    """groups entries = (normalized weight, group size, response multiplier)."""
    ans=[Q(0)]*(max(n for w,n,d in groups))
    for w,n,d in groups:
        q=(d-Q(1))
        for k in range(n):
            ans[k]+=(w/Q(n))*Q(comb(n-1,k))*q**k
    while len(ans)>1 and ans[-1]==0:
        ans.pop()
    return ans


checks=0

def check(actual,expected,label):
    global checks
    if actual!=expected:
        raise AssertionError(f'{label}: got {actual}, expected {expected}')
    checks+=1


def tri(t):
    theta=Q(57,176)-t
    return [(Q(5,8)-theta,2,Q(1,2)),
            (theta,3,Q(2)),(Q(3,8),4,Q(1,2))]

# Polynomial identity: two evaluations suffice because each coefficient is affine in t.
for t in [Q(0),Q(1,10),Q(1,100)]:
    got=response(tri(t))
    want=[Q(31,88)+t/6,-Q(11,12)*t,Q(251,1408)-t/3,-Q(3,256)]
    check(got,want,'explicit polynomial')
    check(evaluate(derivative(got),Q(0)),-Q(11,12)*t,'left slope')
    check(evaluate(derivative(got),Q(1)),Q(905,2816)-Q(19,12)*t,'right slope')

p0=response(tri(Q(0)))
check(evaluate(derivative(derivative(p0)),Q(0)),Q(251,704),'edge curvature')
check(evaluate(p0,Q(0)),Q(31,88),'edge payoff')
K=(Q(11,12)**2)/(2*Q(251,704)*Q(31,88)**2)
check(K,Q(20614528,2170899),'quadratic onset coefficient')

# A strict explicit interior pair and its opposite stability signs.
fixed=response([(Q(3,8),2,Q(1,2)),(Q(1,4),3,Q(2)),(Q(3,8),4,Q(1,2))])
check(fixed,[Q(280,768),Q(-52,768),Q(118,768),Q(-9,768)],'witness response')
F=[Q(11,4)*c for c in fixed]
F[0]-=1
check(F,[Q(8,3072),Q(-572,3072),Q(1298,3072),Q(-99,3072)],'witness selection gradient')
check(evaluate(F,Q(0))>0,True,'two root bracket left')
check(evaluate(F,Q(1,4))<0,True,'two root bracket middle')
check(evaluate(F,Q(1))>0,True,'two root bracket right')
check(evaluate(derivative(derivative(fixed)),Q(0))>0,True,'strict convexity left')
check(evaluate(derivative(derivative(fixed)),Q(1))>0,True,'strict convexity right')

# Rational-grid stress tests over mixtures and positive parameters.
# This tests curvature and the endpoint slopes independently of the proof.
for d2,d3,d4 in product([Q(1,2),Q(1),Q(3,2),Q(2)], repeat=3):
    for w1,w2 in [(Q(1,4),Q(1,4)),(Q(1,2),Q(1,4)),(Q(1,4),Q(1,2))]:
        groups=[(w1,2,d2),(w2,3,d3),(Q(1)-w1-w2,4,d4)]
        g=response(groups)
        gp=derivative(g)
        gpp=derivative(gp)
        A=sum((w*Q(n-1,n)*(d-1) for w,n,d in groups),Q(0))
        B=sum((w*Q(n-1,n)*(d-1)*d**(n-2) for w,n,d in groups),Q(0))
        check(evaluate(gp,Q(0)),A,'derivative A')
        check(evaluate(gp,Q(1)),B,'derivative B')
        for x in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
            check(evaluate(gpp,x)>=0,True,'convexity grid')
        check(evaluate(g,Q(0))>0 and evaluate(g,Q(1))>0,True,'positive endpoints')

print('PASS:',checks,'exact-rational assertions; general proof is separate')
print('K =',str(K),'~',float(K))
