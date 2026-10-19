#!/usr/bin/env python3
"""Recompute algebraic identities for a three-dimensional parabolic map."""
import sympy as S
B, v, lam, s, t = S.symbols('B v lam s t', real=True)
a, b, c = S.symbols('a b c', real=True, nonzero=True)
g = lambda y: -B*y + v*y**3
assert S.expand((g(s)-t)-(g(t)-s)-(s-t)*(v*(s*s+s*t+t*t)+1-B)) == 0
assert S.expand((g(s)-t)+(g(t)-s)-(s+t)*(v*(s*s-s*t+t*t)-B-1)) == 0
J = lambda y, z: S.Matrix([[0, 2*a*y, 0],
                            [0, b*(1-z), -b*y],
                            [-c, 0, 0]])
P = (lam*S.eye(3)-J(t, c*(1-a*t*t))*J(s, c*(1-a*s*s))).det()
P = S.factor(P.subs(a, v/(b*c)).subs(c, 1+B/b))
# Symmetric two-cycle, using v*r^2 = B-1.
r = S.symbols('r', real=True)
Ps = S.rem(S.Poly(P.subs({s:r,t:-r}),r),
           S.Poly(v*r*r-(B-1),r)).as_expr()
assert S.expand(Ps-(lam**3-lam**2+4*(B-1)*lam-4*(B-1)**2)) == 0
# Asymmetric two-cycle: st=-1/v, v(s^2+t^2)=B.
Pa = P.subs(t,-1/(v*s))
res = S.together(Pa-(lam**3-lam**2+2*(B*B-2)*lam-4)).as_numer_denom()[0]
assert S.rem(S.Poly(res,s),S.Poly(v*v*s**4-B*v*s*s+1,s)).is_zero
# Exact factor of the last Schur/Jury inequality.
d = S.symbols('d',real=True)
assert S.expand(1-4*d+4*d**2-16*d**4+
                (4*d*d-2*d+1)*(4*d*d+2*d-1)) == 0
# Test all state recurrences and 3D Floquet characteristic polynomials
# at a representative collection of exact rational parameters.
for Bb in [S.Rational(6,5),S.Rational(3,2),S.Rational(2),
           S.Rational(5,2),S.Rational(4)]:
    aa, bb, cc = S.Integer(1), S.Integer(1), Bb+1
    vv = aa*bb*cc
    state = lambda y_other,y: S.Matrix([aa*y_other**2, y, cc*(1-aa*y*y)])
    F = lambda X: S.Matrix([aa*X[1]**2,bb*X[1]*(1-X[2]),cc*(1-X[0])])
    rr = S.sqrt((Bb-1)/vv)
    cycles=[(rr,-rr)]
    if Bb>2:
        for eps in [-1,1]:
            total=eps*S.sqrt((Bb-2)/vv)
            diff=S.sqrt((Bb+2)/vv)
            cycles.append(((total+diff)/2,(total-diff)/2))
    for y0,y1 in cycles:
        X0,X1=state(y1,y0),state(y0,y1)
        assert all(S.simplify(q)==0 for q in F(X0)-X1)
        assert all(S.simplify(q)==0 for q in F(X1)-X0)
        Ja=J(y0,X0[2]).subs({a:aa,b:bb,c:cc})
        Jb=J(y1,X1[2]).subs({a:aa,b:bb,c:cc})
        actual=(lam*S.eye(3)-Jb*Ja).det()
        symmetric=S.simplify(y0+y1)==0
        expected=(lam**3-lam**2+
                  (4*(Bb-1) if symmetric else 2*(Bb*Bb-2))*lam-
                  (4*(Bb-1)**2 if symmetric else 4))
        assert S.simplify(actual-expected)==0
    print('B=',Bb,'prime-period-two cycles:',len(cycles),'verified')
print('PASS: symbolic identities and exact sample cycles')
