"""Exact arithmetic checks for four-view planar shadow reconstruction."""
import sympy as sp

x, y, z = sp.symbols('x y z')
r2 = x*x + y*y + z*z
harmonics = (
    z*(5*z*z-3*r2),
    x*(5*z*z-r2),
    y*(5*z*z-r2),
    z*(x*x-y*y),
    x*y*z,
    x*(x*x-3*y*y),
    y*(3*x*x-y*y),
)
for H in harmonics:
    assert sp.expand(sum(sp.diff(H, v, 2) for v in (x,y,z))) == 0

frames = (
    ((1,0,0), (0,1,0)),
    ((1,0,0), (0,0,1)),
    ((0,0,-1), (0,1,0)),
    ((sp.Rational(1,3), sp.Rational(2,3), -sp.Rational(2,3)),
     (sp.Rational(2,3), sp.Rational(1,3), sp.Rational(2,3))),
)
c, s = sp.symbols('c s')
Mrows = []
for e,f in frames:
    ee, ff = sp.Matrix(e), sp.Matrix(f)
    assert (ee.dot(ee), ff.dot(ff), ee.dot(ff)) == (1,1,0)
    crow, drow = [], []
    for H in harmonics:
        substituted = H.subs({x:e[0]*c+f[0]*s, y:e[1]*c+f[1]*s, z:e[2]*c+f[2]*s}, simultaneous=True)
        P = sp.Poly(sp.expand(substituted), c, s)
        A = P.coeff_monomial(c**3)
        B = P.coeff_monomial(c**2*s)
        C = P.coeff_monomial(c*s**2)
        D = P.coeff_monomial(s**3)
        cc, dd = sp.factor((A-C)/4), sp.factor((B-D)/4)
        # Independent complex-null-frame formula for the third mode.
        w = [e[k]-sp.I*f[k] for k in range(3)]
        complex_coeff = sp.expand(H.subs({x:w[0],y:w[1],z:w[2]},simultaneous=True))/4
        assert sp.simplify(cc-sp.re(complex_coeff)) == 0
        assert sp.simplify(dd+sp.im(complex_coeff)) == 0
        crow.append(cc)
        drow.append(dd)
    Mrows.extend([crow,drow])
M = sp.Matrix(Mrows)
expected = sp.Matrix([
 [0,0,0,0,0,1,0],
 [0,0,0,0,0,0,1],
 [0,-sp.Rational(5,4),0,0,0,sp.Rational(1,4),0],
 [-sp.Rational(5,4),0,0,sp.Rational(1,4),0,0,0],
 [-sp.Rational(5,4),0,0,-sp.Rational(1,4),0,0,0],
 [0,0,sp.Rational(5,4),0,0,0,sp.Rational(1,4)],
 [sp.Rational(20,27),sp.Rational(20,27),sp.Rational(10,27),sp.Rational(1,9),-sp.Rational(5,54),sp.Rational(1,27),-sp.Rational(8,27)],
 [sp.Rational(20,27),-sp.Rational(10,27),-sp.Rational(20,27),-sp.Rational(1,9),-sp.Rational(5,54),-sp.Rational(8,27),sp.Rational(1,27)],
])
assert M == expected
V=M[:7,:]
assert V.det() == sp.Rational(625,6912)
assert V*V.inv()==sp.eye(7)
assert M[:6,:].rank()==6
assert M[:6,4]==sp.zeros(6,1)
infty_operator_norm = max(sum(abs(z) for z in V.inv().row(i)) for i in range(7))
assert infty_operator_norm == sp.Rational(164,5)
# Seven scalar measurements reconstruct all seven harmonics; a fourth sine
# coefficient is not needed, although the full fourth shadow supplies it.
print('VERIFY_OK det=625/6912 inverse_infinity_norm=164/5 rank=7')
