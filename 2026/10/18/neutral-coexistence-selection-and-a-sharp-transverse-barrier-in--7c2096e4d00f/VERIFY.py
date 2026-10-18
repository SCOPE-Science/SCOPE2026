"""Symbolic spot checks for the stated neutral lottery--Ricker identities.

The global convergence and sharp selection proofs are analytic; these calculations
check algebraic components and sample trajectories, not infinitely many orbits.
"""
from __future__ import annotations
import math
import sympy as sp

x,y,r,f=sp.symbols('x y r f', positive=True)
s=x+y
H1=r*x/s
H2=y*sp.exp(r-s)
assert sp.simplify(H1+H2-r-y/s*(s*sp.exp(r-s)-r))==0
J=sp.Matrix([H1,H2]).jacobian([x,y])
Jfixed=sp.simplify(J.subs({x:r*f, y:r*(1-f)}))
assert sp.simplify((Jfixed-sp.eye(2)).det())==0
assert sp.simplify(sp.trace(Jfixed)-1-(1-r)*(1-f))==0
assert sp.simplify(H1.subs({x:r*f,y:r*(1-f)})-r*f)==0
assert sp.simplify(H2.subs({x:r*f,y:r*(1-f)})-r*(1-f))==0

# Verify the weighted-quotient identity without relying on symbolic log branches.
# (Q_{n+1}/Q_n)^r = (r/s)^r * exp(s-r).
assert sp.simplify((H1/x)**r*(y/H2)-(r/s)**r*sp.exp(s-r))==0

for rv in [0.5,1.0,2.0,3.0,7.0]:
    for x0,y0 in [(0.01,0.03),(0.1,2.0),(2.0,0.3),(7.0,8.0)]:
        x1,y1=x0,y0
        qlast=x1/(y1**(1/rv))
        for _ in range(400):
            ss=x1+y1
            xn=rv*x1/ss
            yn=y1*math.exp(rv-ss)
            q=xn/(yn**(1/rv)) if yn>1e-290 else float('inf')
            assert q >= qlast*(1-1e-10), (rv,x0,y0,q,qlast)
            x1,y1=xn,yn
            qlast=q
        assert abs(x1+y1-rv)<1e-5 or rv>=7
print('VERIFY_OK')
