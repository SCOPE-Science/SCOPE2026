"""Exact symbolic checks for the positive period-three cycle threshold.

Run: python check_period3.py   (requires SymPy 1.10 or later).
The identities checked here support, but do not replace, the theorem's
inequality, sign, and orbit-existence arguments.
"""
import sympy as S

b, h, x, y, z, t = S.symbols('b h x y z t', real=True)
T = lambda a, c: (c, S.factor(h + b*c/(a-1)))
L = b*b - b + t
M = t*t - (1-b)*t - b*(1-b)
A = b*b - 2*b + b*t + t*t
B = -b**3 + b*(1-t) - (2-t)*t*t
C = S.expand(b*x**3 + A*x**2 + B*x - L*M).subs(t, 1-h).expand()
K = b*b - (x-1)*(x-h)
Q = x*x - (b+h+1)*x + h
Y = S.factor(S.solve([(x-1)*(z-h)-b*y, (y-1)*(x-h)-b*z], [y,z])[y])
Z = S.factor(S.solve([(x-1)*(z-h)-b*y, (y-1)*(x-h)-b*z], [y,z])[z])
assert S.cancel((Z-1)*(Y-h)-b*x + Q*C/K**2) == 0
E1 = (x-1)*(z-h)-b*y
E2 = (y-1)*(x-h)-b*z
E3 = (z-1)*(y-h)-b*x
E2after = S.together(E2.subs(z,h+b*y/(x-1)))*(x-1)
E3after = S.together(E3.subs(z,h+b*y/(x-1)))*(x-1)
res = S.factor(S.resultant(E2after,E3after,y))
assert S.simplify(res/((x-1)*Q*C)) in (1,-1)
P = S.expand(4*b**4 - 2*b**3*h - 2*b**3 + 3*b*b*h*h - 5*b*b*h + 3*b*b + b*h**3 - b*h*h - b*h + b + (h-1)**4)
assert S.factor(S.discriminant(C,x) - (h-1)**2*P**2) == 0
assert S.factor(S.resultant(C,K,x) + b**4*(1-h)**2*(b*h+b-h)) == 0
assert S.factor(S.resultant(C,Q,x) + b**2*(b*h+b-h)*P) == 0
sum_squares = b*b*(2*b-1+t/S.Integer(2))**2 + t*t*((t-b/S.Integer(2))**2 + S.Rational(5,2)*b*b + 2*b)
assert S.factor(P.subs(h,1-t) - sum_squares) == 0
assert S.factor(C.subs(x,0)+L.subs(t,1-h)*M.subs(t,1-h)) == 0
assert S.factor(C.subs(x,h-b) - b*(1-h)**3) == 0
assert S.factor(C.subs(x,1-b) + b*(1-h)**3) == 0
assert S.factor(C.subs(x,h) + b*b*(b*b-b-h+1)) == 0
assert S.factor(B - ((t-b-1)*M-t)) == 0
assert S.factor(B.subs(t,b*(1-b)) - b*(1-b)*(b*b-b+1)**2) == 0
assert S.factor(A.subs(t,b*(1-b)) - b*(b-2)*(b*b-b+1)) == 0

# Special case where K vanishes at a root of C; its orbit is explicit.
bs = h/(1+h)
xs = bs
ys = (h**3+h*h-1)/(h*(1+h))
zs = (1+h-h**3)/(1+h)
for E in (E1,E2,E3):
    assert S.cancel(E.subs({b:bs,x:xs,y:ys,z:zs})) == 0
assert S.factor((h-(1-bs+bs**2))*(1+h)**2-(h**3+h*h-1)) == 0

# Rational examples: each admissible case has three roots in (0,h).
for bb, hh in [(S.Rational(1,4),S.Rational(9,10)),
                (S.Rational(3,5),S.Rational(4,5)),
                (S.Rational(9,19),S.Rational(9,10))]:
    poly = S.Poly(C.subs({b:bb,h:hh}),x)
    roots = sorted([float(S.re(r)) for r in poly.nroots(maxsteps=100)])
    assert len(roots)==3 and 0<roots[0]<roots[1]<roots[2]<float(hh)
for bb, hh in [(S.Rational(1,4),S.Rational(4,5)),
                (S.Rational(3,5),S.Rational(7,10)),
                (S.Rational(3,2),S.Rational(9,10))]:
    assert not (0<bb<1 and hh>1-bb+bb**2)
print('PASS: all symbolic elimination, discriminant, sign and exceptional-case identities.')
print('PASS: three admissible rational parameter examples; three inadmissible controls.')
