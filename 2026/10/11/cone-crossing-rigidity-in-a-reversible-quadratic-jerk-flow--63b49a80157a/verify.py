#!/usr/bin/env python3
"""Exact symbolic checks of the published polynomial vector field and cone algebra."""
import sympy as S
x, y, z, a, s = S.symbols('x y z a s', real=True)
F = (z, x, a*x**2-y**2-y*z)
P=z+x*y
Q=(a+1)*x*x-y*y
lie=lambda f:S.expand(S.diff(f,x)*F[0]+S.diff(f,y)*F[1]+S.diff(f,z)*F[2])
assert S.simplify(lie(P)-Q)==0
assert S.simplify(lie(Q)-(2*(a+1)*x*z-2*x*y))==0
# y=e*s*x, z=e*x/s, a=s*s-1, where e is either sign.
for e in [-1,1]:
    cone={y:e*s*x,z:e*x/s,a:s*s-1}
    rhs=S.factor(F[2].subs(cone, simultaneous=True))
    tangent=S.factor((e*z/s).subs(cone, simultaneous=True))
    assert S.simplify(rhs+2*x*x)==0
    assert S.simplify(tangent-x/s**2)==0
    assert S.factor(tangent-rhs)==x*(1+2*s*s*x)/s**2
assert S.solve([F[0],F[1],F[2]],[x,y,z])==[(0,0,0)]
print('PASS: polynomial coboundary, cone branch tangency contradiction, unique equilibrium')
