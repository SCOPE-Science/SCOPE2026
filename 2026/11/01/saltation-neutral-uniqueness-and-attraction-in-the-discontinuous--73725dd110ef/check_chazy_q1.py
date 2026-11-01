#!/usr/bin/env python3
"""Independent algebraic diagnostics for a discontinuous Chazy flow.
These checks do not establish the global periodic orbit theorem."""
import sympy as S
x,y,w,t,lam,h=S.symbols('x y w t lam h', real=True, positive=True)
X,Y,W=S.symbols('X Y W',real=True)
H=X*W-Y**2/S.Integer(2)
for s in (-1,1):
    # Region s*X>0: |X|=sX, sgn(X)=s.
    F=S.Matrix([Y,W-s*X*Y,-s*Y**2])
    div=sum(S.diff(F[i],v) for i,v in enumerate((X,Y,W)))
    conservation=S.expand(S.diff(H,X)*F[0]+S.diff(H,Y)*F[1]+S.diff(H,W)*F[2])
    assert S.simplify(div+s*X)==0
    assert S.simplify(conservation)==0
    # Scaling x->lambda x, y->lambda^2 y, w->lambda^3 w,
    # time->lambda*t. The vector field scales with weighted +1 degrees.
    subs={X:lam*X,Y:lam**2*Y,W:lam**3*W}
    degrees=[2,3,4]
    for i,deg in enumerate(degrees):
        assert S.simplify(F[i].subs(subs)-lam**deg*F[i])==0
    assert S.simplify(H.subs(subs)-lam**4*H)==0
    print('half-space branch',s,'energy, divergence, scaling: exact PASS')
# At each negative-energy seam crossing X=0, Y^2=2h, thus Y !=0.
# Both sides share their X-component Y; their jump is only in W.
# Each forward or backward saltation matrix has det 1 (shear).
for k in (-1,1):
    normal=S.Matrix([[1,0,0]])
    jump=S.Matrix([0,0,-2*k*Y**2])
    saltation=S.eye(3)+jump*normal/Y
    assert S.simplify(saltation.det()-1)==0
    assert S.simplify((normal*jump)[0])==0
    print('crossing orientation',k,'normal continuity, saltation determinant: exact PASS')
assert S.simplify(H.subs({X:0,Y:S.sqrt(2*h)})+h)==0
assert S.simplify(H.subs({X:0,Y:-S.sqrt(2*h)})+h)==0
assert S.simplify(H.subs({X:-X,Y:-Y,W:-W})-H)==0
print('negative-energy crossings and central inversion: exact PASS')
print('LIMITS: These algebraic tests do not certify orbital existence, uniqueness, Poincare-Bendixson, or literature originality.')
