"""Supplementary exact-arithmetic checks for the two-row tent-spline Gabor minors.

Requires SymPy. Finite checks corroborate the identities; the general-q theorem
and global unit-circle bounds are established analytically in RESULT.md.
"""
import sympy as S
x, z = S.symbols('x z')
N = 0

def check(left, right):
    global N
    assert S.cancel(left - right) == 0, (left, right)
    N += 1

def finite_F(t, t0):
    out = S.Integer(0)
    for r in range(-7, 8):
        d0 = t0-r
        if abs(d0) >= S.Rational(5, 2):
            continue
        sign = S.Integer(1) if d0 > 0 else -S.Integer(1)
        out += (1-S.Rational(2,5)*sign*(t-r))*z**r
    return S.expand(out)

def minor(F, G):
    return S.cancel(F*G.subs(z,-z)-G*F.subs(z,-z))

pminus = z**6-2*z**4-z**2-1
pplus  = z**6+z**4+2*z**2-1
for q in (5,7,9,11,17):
    for label, point in [('left', S.Rational(1,8*q)),('right',S.Rational(7,8*q))]:
        if q == 5 and label == 'right':
            point=S.Rational(3,20)
        F=[finite_F(x-S.Rational(2*l,q), point-S.Rational(2*l,q)) for l in range(q)]
        if q==5 and label=='left':
            check(minor(F[0],F[4]),16*pminus/(125*z**5))
        elif q==5 and label=='right':
            check(minor(F[3],F[4]),16*pplus/(125*z**5))
        else:
            check(minor(F[0],F[q-1]),S.Rational(16,25*q)*pminus/z**5)

for point in (S.Rational(1,12),S.Rational(1,4)):
    F=[finite_F(x-S.Rational(2*l,3),point-S.Rational(2*l,3)) for l in range(3)]
    coeff=[12*x**2-16*x+5,-12*x**2-20*x+5,-12*x**2+4*x+17,-12*x**2+28*x-3,12*x**2+8*x+1]
    P=sum(v*z**(2*j) for j,v in enumerate(coeff))
    check(minor(F[0],F[2]),-S.Rational(2,75)*P/z**5)

v=S.symbols('v',real=True)
for P in (S.Symbol('y')**3-2*S.Symbol('y')**2-S.Symbol('y')-1,
          S.Symbol('y')**3+S.Symbol('y')**2+2*S.Symbol('y')-1):
    y=S.Symbol('y')
    expr=S.expand(P*P.subs(y,1/y))
    expr=S.expand(expr).subs(y**3+y**(-3),8*v**3-6*v)
    # use Laurent coefficient pairing instead of noncanonical substitutions
    A=S.expand(P*P.subs(y,1/y))
    poly=S.Poly(A*y**3,y)
    c={k[0]-3:val for k,val in poly.terms()}
    val=c.get(0,0)+2*c.get(1,0)*v + c.get(2,0)*(4*v*v-2)+c.get(3,0)*(8*v**3-6*v)
    check(val,-8*v**3+4*v**2+8*v+5)
check((-8*v**3+4*v**2+8*v+5).subs(v,(1-S.sqrt(13))/6),(173-26*S.sqrt(13))/27)
q=S.symbols('q',positive=True)
d=(173-26*S.sqrt(13))/27
check(S.cancel((S.Rational(16,125)/q)**2*d/(S.Rational(338,125)*q)), S.Rational(128,21125)*d/q**3)
check(S.cancel((S.Rational(2,125))**2/(S.Rational(338,125)*3)), S.Rational(2,63375))
print('CHECK_OK',N)
