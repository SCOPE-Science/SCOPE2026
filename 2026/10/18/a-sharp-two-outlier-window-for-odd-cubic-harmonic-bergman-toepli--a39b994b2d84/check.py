"""Standalone symbolic checks for the odd-cubic harmonic-Bergman spectral calculation.

Requires SymPy. This checker verifies algebraic identities; the analytic Fredholm,
root-count, and noncoverage arguments are contained in RESULT.md.
"""
import sympy as sp

z, w, u, v, a, alpha, s = sp.symbols('z w u v a alpha s')
h = lambda x, y: x**2 + sp.Rational(3, 2)*x*y + sp.Rational(3, 2)*y**2 + a
D = sp.expand(h(u,u)*h(v,v) - h(u,v)*h(v,u))
assert sp.factor(D + sp.Rational(3,4)*(u-v)**2*(-2*a+2*u**2+9*u*v+2*v**2)) == 0
# The two-inside-root determinant and the cubic Vieta condition imply 7s^2+3a=0.
t = sp.symbols('t')
assert sp.expand((2*s*s+5*t-2*a).subs(t,a+s*s)) == 7*s*s+3*a
# One-root condition, factorization of the eigenfunction numerator, and candidate value.
assert sp.simplify(h(alpha,alpha).subs(a,-4*alpha**2)) == 0
assert sp.factor(h(z,alpha).subs(a,-4*alpha**2) - (z-alpha)*(z+sp.Rational(5,2)*alpha)) == 0
lmb = alpha**3+a*alpha
assert sp.simplify((lmb-sp.Rational(3,4)*a*alpha).subs(a,-4*alpha**2)) == 0
# Critical double root: determinant of confluent matching conditions.
confluent = sp.det(sp.Matrix([
 [h(z,w), sp.diff(h(z,w),w)],
 [sp.diff(h(z,w),z), sp.diff(h(z,w),z,w)]
])).subs({z:alpha,w:alpha})
assert sp.simplify(confluent.subs(alpha**2,-a/3)-sp.Rational(19,4)*a) == 0
assert sp.factor((z**3+a*z-lmb).subs(a,-3*alpha**2)-(z-alpha)**2*(z+2*alpha)) == 0
# Sharp lower parameter threshold, from the middle-modulus exterior root.
r0=(14+2*sp.sqrt(13))/9
assert sp.simplify(r0-16/(sp.sqrt(13)-1)**2)==0
assert sp.simplify(sp.Rational(3,8)*r0**sp.Rational(3,2)-(r0-1))==0
# Exact inequalities determining the two-inside exclusion and the open phase interval.
R=sp.sqrt(19)+sp.sqrt(3)
assert float(R/(2*sp.sqrt(7))) > float(sp.sqrt(sp.Rational(3,7)))
for aval in [sp.Rational(2), sp.Rational(5,2), sp.Rational(3),sp.Rational(7,2), sp.Rational(4),sp.Rational(5)]:
    b1=sp.sqrt(aval)/2
    b2=(sp.sqrt(13)-1)*sp.sqrt(aval)/4
    b3=(sp.sqrt(13)+1)*sp.sqrt(aval)/4
    assert b1<=b2<=b3
    expected=(aval>r0 and aval<4)
    observed=(b1<1 and b2>1 and b3>1)
    assert bool(expected)==bool(observed)
print('PASS: 11 identity/inequality groups and six exact parameter samples.')
