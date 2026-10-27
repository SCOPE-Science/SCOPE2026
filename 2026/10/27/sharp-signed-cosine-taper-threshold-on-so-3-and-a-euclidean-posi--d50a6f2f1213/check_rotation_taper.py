"""Reproducible algebraic and numerical checks for the rotation-taper theorem.

Dependencies: Python 3, sympy, mpmath. The proof in RESULT.md is analytic;
finite numerical comparisons here are only checks of normalization and identities.
"""
import sympy as s
import mpmath as mp

n = s.symbols('n', integer=True, positive=True)
p = s.pi

def F(k):
    if k == 0:
        return p / 3
    return 2 / (p * k * k)

def H(k):
    if k == 0:
        return F(1)
    return (F(k - 1) + F(k + 1)) / 2

def A(k):
    return s.simplify(F(k) - F(k+1))

def B(k):
    return s.simplify(H(k) - H(k+1))

A_general = 2 / p * (1 / n**2 - 1 / (n+1)**2)
B_general = (1/p) * (1/(n-1)**2 + 1/(n+1)**2 - 1/n**2 - 1/(n+2)**2)
R_general = (n-1)**2 * (n+2)**2 / (n**4 + 2*n**3 + 3*n**2 + 2*n - 2)
assert s.simplify(A_general/B_general-R_general) == 0
assert s.simplify(p*(23*A_general-8*B_general) - 6*(n-2)*(n+3)*(2*n+1)*(5*n*n+5*n-6)/(n*n*(n-1)**2*(n+1)**2*(n+2)**2)) == 0
for k in range(2, 12):
    assert s.simplify(A(k)-A_general.subs(n,k)) == 0
    assert s.simplify(B(k)-B_general.subs(n,k)) == 0
assert s.simplify(A(2)/B(2)-s.Rational(8,23)) == 0
assert s.simplify(A(0)-s.Rational(8,23)*B(0)-3*(3*p*p-20)/(23*p)) == 0
assert s.simplify(A(1)-s.Rational(8,23)*B(1)-(745-24*p*p)/(414*p)) == 0
assert all(float(A(k)-s.Rational(8,23)*B(k)) > 0 for k in list(range(2))+list(range(3,30)))


# The compactly supported radial extension on R^3 fails Euclidean Bochner positivity.
r = s.symbols('r', nonnegative=True)
profile = (1-r/p)**2 * (1-s.Rational(8,23)*s.cos(r))
radial_frequency_three = s.simplify((4*p/3)*s.integrate(r*profile*s.sin(3*r),(r,0,p)))
assert radial_frequency_three == -s.Rational(361,3726)

mp.mp.dps = 30
checks = 0
max_residual = mp.mpf(0)
for b in [mp.mpf(-8)/23, mp.mpf(1)/7, mp.mpf(3)]:
    for ell in [0,1,2,3,7,15]:
        def f(t):
            return (1-t/mp.pi)**2 * (1+b*mp.cos(t))
        # Direct integration against SO(3) character under Haar measure.
        def chi(t):
            if t == 0:
                return 2*ell+1
            return mp.sin((ell+mp.mpf('0.5'))*t)/mp.sin(t/2)
        direct = mp.quad(lambda t: (2/mp.pi)*mp.sin(t/2)**2*f(t)*chi(t), [0,mp.pi])
        expected = (mp.mpf(str(s.N(A(ell),40))) + b*mp.mpf(str(s.N(B(ell),40))))/mp.pi
        residual = abs(direct-expected)
        max_residual = max(max_residual, residual)
        assert residual < mp.mpf('1e-24'), (b,ell,residual)
        checks += 1
print('Exact symbolic identities: PASS')
print('Direct SO(3) character-integral comparisons:',checks)
print('Maximum absolute residual:',mp.nstr(max_residual,12))
print('Critical degree: 2; critical parameter: -8/23')
print('At critical parameter all other degrees have strictly positive character coefficients.')

print('Euclidean radial Fourier value at norm 3:',radial_frequency_three)
