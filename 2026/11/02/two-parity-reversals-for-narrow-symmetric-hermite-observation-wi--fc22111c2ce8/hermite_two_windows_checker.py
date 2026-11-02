"""Reproducibility checks for parity crossings of three Hermite modes."""
from math import erf, exp, pi, sqrt
from scipy.optimize import brentq
import numpy as np
import sympy as sp


def exact_grams(a, e):
    lo, hi = a-e, a+e
    def F0(x): return sqrt(pi)*erf(x)/2
    def F2(x): return sqrt(pi)*erf(x)/4 - x*exp(-x*x)/2
    def F4(x): return 3*sqrt(pi)*erf(x)/8 - (x*x*x/2+3*x/4)*exp(-x*x)
    i0, i2, i4 = [F(hi)-F(lo) for F in (F0,F2,F4)]
    c2=1/sqrt(pi)
    B=2*c2*np.array([[i0,(2*i2-i0)/sqrt(2)],[(2*i2-i0)/sqrt(2),2*i4-2*i2+i0/2]])
    q=4*c2*i2
    return B,q

def F(a,e):
    B,q=exact_grams(a,e)
    return (np.linalg.eigvalsh(B)[-1]-q)/(4*e)

checks=0
x,y=sp.symbols('x y',real=True)
P=2*y*y-2*y+sp.Rational(3,2)
D=P-2*y
second=sp.simplify(sp.diff(sp.exp(-x*x)*D.subs(y,x*x),x,2)/sp.exp(-x*x))
assert sp.expand(second)==8*x**6-52*x**4+70*x*x-11
checks+=1
H2=sp.factor((second.subs(x*x,y)-16*y/P)/6)
assert H2.subs(y,sp.Rational(1,2))==sp.Rational(2,3)
assert H2.subs(y,sp.Rational(3,2))==-sp.Rational(2,3)
for yy in (sp.Rational(1,2),sp.Rational(3,2)):
    assert sp.simplify(-H2.subs(y,yy)/sp.diff(D,y).subs(y,yy))==sp.Rational(1,3)
    checks+=1
checks+=2
for e in (0.2,0.1,0.05,0.025):
    r1=brentq(lambda a:F(a,e),0.65,0.8,xtol=1e-12)
    r2=brentq(lambda a:F(a,e),1.15,1.3,xtol=1e-12)
    assert e<r1<r2
    assert F(0.5,e)>0 and F(0.9,e)<0 and F(1.45,e)>0
    checks+=4
    for val,t in [(r1,.5),(r2,1.5)]:
        assert abs((val**2-t)/e**2-1/3)<(0.018 if e==0.2 else .006 if e==0.1 else .002)
        checks+=1
        B,q=exact_grams(val,e)
        assert abs(np.linalg.eigvalsh(B)[-1]-q)<1e-10
        assert np.linalg.eigvalsh(B)[0]<.5*q
        checks+=2
    for a in np.linspace(e+.01,3,65):
        B,q=exact_grams(a,e)
        assert np.linalg.eigvalsh(B)[0]>-3e-13
        expected=(a<r1 or a>r2)
        assert (np.linalg.eigvalsh(B)[-1]>q)==expected
        checks+=2
print(f"PASS: {checks} symbolic/numeric assertions; independent audit not performed")
