"""Exact checks of the trapezoidal central-overlap formula.

Run with Python 3 and SymPy: python checker.py
The proof for all real parameters is presented separately.
"""
from fractions import Fraction as Q
from itertools import product
import sympy as sp


def cross(u, v):
    return u[0]*v[1]-u[1]*v[0]


def sub(a,b):
    return (a[0]-b[0],a[1]-b[1])


def clip(poly, a, b):
    """Exact clipping by the left halfplane of the oriented line a -> b."""
    if not poly:
        return []
    edge=sub(b,a)
    result=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp,fq=cross(edge,sub(p,a)),cross(edge,sub(q,a))
        if fp>=0:
            result.append(p)
        if (fp<0 and fq>0) or (fp>0 and fq<0):
            u=fp/(fp-fq)
            result.append((p[0]+u*(q[0]-p[0]),p[1]+u*(q[1]-p[1])))
    return result


def area(poly):
    if len(poly)<3:
        return Q(0)
    return abs(sum(cross(p,q) for p,q in zip(poly,poly[1:]+poly[:1])))/2


def overlap(t,cx,cy):
    poly=[(-Q(1),Q(0)),(Q(1),Q(0)),(t,Q(1)),(-t,Q(1))]
    reflected=[(2*cx-p[0],2*cy-p[1]) for p in poly]
    for a,b in zip(reflected,reflected[1:]+reflected[:1]):
        poly=clip(poly,a,b)
    return area(poly)


def max_area(t):
    if t<=Q(1,3):
        return Q(2)/(3*(1-t))
    return (1+3*t)/2


def maximizing_height(t):
    return Q(1)/(3*(1-t)) if t<=Q(1,3) else Q(1,2)


def expected_area(t,x,y):
    m=min(y,1-y)
    if m<0:
        return Q(0)
    return 4*m*(1-(1-t)*y)-2*(1-t)*m*m


for t in (Q(0),Q(1,7),Q(1,3),Q(2,3),Q(1)):
    y=maximizing_height(t)
    assert overlap(t,Q(0),y)==max_area(t), (t,y)
    for cy in [Q(i,12) for i in range(13)]+[y]:
        assert overlap(t,Q(0),cy)==expected_area(t,Q(0),cy),(t,cy)
        for cx in [Q(j,12) for j in range(-6,7)]:
            assert overlap(t,cx,cy)<=max_area(t), (t,cx,cy)
print('EXACT_POLYGON_CLIPPING_AND_CENTRAL_OVERLAP_PASSED')

t=sp.symbols('t',real=True)
f1=2/(3*(1-t*t));f2=(1+3*t)/(2*(1+t))
assert sp.factor((f1-f2)/(t-sp.Rational(1,3))**2)==sp.factor(sp.Rational(-3,2)/((t-1)*(t+1)))
# At the switch the two branches match through first order, not second.
b=sp.Rational(1,3)
assert sp.simplify(f1.subs(t,b)-f2.subs(t,b))==0
assert sp.simplify(sp.diff(f1,t).subs(t,b)-sp.diff(f2,t).subs(t,b))==0
assert sp.simplify(sp.diff(f2,t,2).subs(t,b)-sp.diff(f1,t,2).subs(t,b))==-sp.Rational(27,8)
assert sp.simplify(sp.diff(f1,t)-4*t/(3*(1-t*t)**2)) == 0
assert sp.simplify(sp.diff(f2,t)-(t+1)**(-2)) == 0
print('EXACT_BRANCH_SWITCH_AND_DERIVATIVES_PASSED')

k=sp.symbols('k',real=True)
inv1=sp.sqrt(1-2/(3*k));inv2=(2*k-1)/(3-2*k)
assert sp.simplify(f1.subs(t,inv1)-k)==0
assert sp.simplify(f2.subs(t,inv2)-k)==0
assert sp.limit((f1-sp.Rational(2,3))/t**2,t,0)==sp.Rational(2,3)
print('EXACT_INVERSE_FORMULAS_AND_SHARP_SQUARE_ROOT_ENDPOINT_PASSED')
print('ALL_CHECKS_PASSED')
