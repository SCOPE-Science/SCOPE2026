"""Reproduce the exact recurrence boundary and period-two witness for a cosine-memory map.

Requires Python 3 with sympy and mpmath. Every tested equality has a separate
analytic proof in RESULT.md; finite tests are consistency checks, not proofs.
"""
import random
import sympy as s
import mpmath as mp

r = s.symbols('r', positive=True)
x = 1/(r-1)
C0 = -1
C1 = 1-2/r
# The period-two x update, with a=1 and bc=r.
assert s.simplify(1+r*C0*x+x) == 0
assert s.simplify(1+r*C1*(-x)-x) == 0
# The two inverse feedback constraints and their sharp magnitude gap.
B0, B1 = s.symbols('B0 B1', real=True)
assert s.simplify((-1-B0)+(1+B1)) == B1-B0
assert s.simplify((-1-B0)-(1+B1)).expand() == -2-B0-B1
# The two roots of the ballistic lower bound inequality.
u = s.symbols('u', real=True)
assert s.expand((1-r**2)*u**2-2*u+1+(r*u-u+1)*(r*u+u-1)) == 0
assert s.simplify((1-r**2)/(1+r)**2-2/(1+r)+1) == 0
assert s.simplify((1-r**2)/(1-r)**2-2/(1-r)+1) == 0
# Exact two-cycle invariant-measure balance for the constructed orbit.
sin_theta_squared=1-(1-2/r)**2
assert s.simplify((r**2-1)/(r-1)**2-r**2*sin_theta_squared/(2*(r-1)**2)-1)==0

mp.mp.dps = 65
for rr in ['1.0001','1.01','1.1','1.5','2','3.333333','7','20']:
    R=mp.mpf(rr); theta=mp.acos(1-2/R)
    aa=mp.mpf('1'); d=mp.mpf('1'); ee=(R-1)*(mp.pi-theta)
    pt0=(1/(R-1),mp.pi)
    pt1=(-1/(R-1),2*mp.pi-theta)
    def F(pt):
        xx,yy=pt
        return aa+R*mp.cos(d*yy)*xx,yy+ee*xx
    for p,q in [(pt0,pt1),(pt1,pt0)]:
        got=F(p)
        assert max(abs(got[j]-q[j]) for j in range(2)) < mp.mpf('1e-52')
        assert abs(p[0])>= abs(aa)/(R-1)
for rr in ['0.01','0.23','0.5','0.92','0.99']:
    R=mp.mpf(rr);a=mp.mpf('1'); x=a/(1+R)
    y=mp.pi;e=2*mp.pi*(1+R)
    for n in range(12):
        x1=a+R*mp.cos(y)*x
        y1=y+e*x
        assert abs(x1-x)<mp.mpf('1e-55')
        assert abs((y1-y)/e-a/(1+R))<mp.mpf('1e-55')
        x,y=x1,y1
    x,y=a/(1-R),mp.mpf('0')
    e=2*mp.pi*(1-R)
    for n in range(12):
        x1=a+R*mp.cos(y)*x
        y1=y+e*x
        assert abs(x1-x)<mp.mpf('1e-55')
        assert abs((y1-y)/e-a/(1-R))<mp.mpf('1e-55')
        x,y=x1,y1
# Arbitrary finite trajectories and asymptotic drift inequality: numerical probes.
random.seed(7341)
for r0 in [0.07,0.33,0.71,0.95]:
    a,e,d=1.1,0.71,1.3
    for trial in range(5):
        x,y=random.uniform(-2,2),random.uniform(-4,4)
        initial_y=y
        n=120000
        for j in range(n):
            x,y=a+r0*__import__('math').cos(d*y)*x, y+e*x
        rate=(y-initial_y)/(a*e*n)
        assert rate >= 1/(1+r0)-.001, (r0,trial,rate)
print('PASS: exact symbolic parameter reductions; 16 high-precision two-cycle leg checks; 120 sharp drift witness steps; 20 long finite drift probes')
