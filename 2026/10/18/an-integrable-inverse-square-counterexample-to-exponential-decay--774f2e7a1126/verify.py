#!/usr/bin/env python3
"""Independent algebraic checks for a four-compartment mass-action construction."""
import math
import sympy as S

x, u, y, z = S.symbols('x u y z', positive=True)
flow = [-2*x*y, -u*y, (u-x)*y, 3*x*y]
assert S.expand(sum(flow)) == 0
assert S.simplify(flow[1]/S.sqrt(x) - u*flow[0]/(2*x**S.Rational(3, 2))) == 0
assert S.expand(flow[2] + flow[1] - flow[0]/2) == 0

r = S.symbols('r', positive=True)
s = r-S.Rational(1, 2)
coords = [r**2, r/2, s**2/2, 1-r**2-r/2-s**2/2]
dr = -r*s**2/2
assert [S.simplify(c.subs(r,S.Rational(3,5))) for c in coords] == [
    S.Rational(9,25), S.Rational(3,10), S.Rational(1,200), S.Rational(67,200)]
assert [S.simplify(c.subs(r,S.Rational(1,2))) for c in coords] == [
    S.Rational(1,4), S.Rational(1,4), S.Integer(0), S.Rational(1,2)]
for coordinate, rhs in zip(coords,flow):
    assert S.simplify(S.diff(coordinate,r)*dr-rhs.subs(dict(zip((x,u,y,z),coords)))) == 0
assert S.expand(dr + s**2*(1+2*s)/4) == 0
assert S.Rational(1,2)*4**2 == 8
# Exact time integral follows from d(log u)/dt=-y and the two values of u.
assert S.simplify(S.log(S.Rational(3,10)/S.Rational(1,4))-S.log(S.Rational(6,5))) == 0

# A supplementary finite-time test of the explicit implicit scalar solution.
for t in [10,100,1000,10000]:
    def g(s0):
        return 4/s0-40+8*math.log(12*s0/(1+2*s0))-t
    lo,hi=1e-6,0.1
    assert g(lo)>0 and g(hi)<0
    for _ in range(100):
        mid=(lo+hi)/2
        if g(mid)>0: lo=mid
        else: hi=mid
    st=(lo+hi)/2
    assert st>0 and st<=0.1
    assert abs(g(st)) < 1e-7
    if t==10000:
        assert 7.5 < t*t*(st*st/2) < 8
print('VERIFIED: polynomial identities, invariants, scalar reduction, initial/limit states, supplementary implicit-time checks')
