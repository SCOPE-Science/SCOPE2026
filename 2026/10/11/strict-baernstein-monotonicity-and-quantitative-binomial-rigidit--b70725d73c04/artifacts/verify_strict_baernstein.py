#!/usr/bin/env python3
import sympy as sp

k,m,n,r,a = sp.symbols('k m n r a', positive=True)

# Exact partial fraction identity used in the radial integral.
term = 1/(k*(k+1)*(k+2*m))
rhs = 1/(2*m*k) - 1/((2*m-1)*(k+1)) + 1/(2*m*(2*m-1)*(k+2*m))
assert sp.simplify(term-rhs) == 0

# Finite telescoping check of the infinite-sum closed form for many exact m,N,
# plus exact limiting expression. This is an algebra audit, not the proof of the theorem.
for mv in range(1,21):
    H2m = sp.harmonic(2*mv)
    closed = sp.Rational(1,2*mv-1) - H2m/sp.Rational(2*mv*(2*mv-1))
    # Direct high-N rational partial sum converges upward to closed.
    sN = sum(sp.Rational(1, kk*(kk+1)*(kk+2*mv)) for kk in range(1,1000))
    assert sN < closed
    assert sp.N(closed-sN,30) > 0
    J = sp.Rational(1,2*mv) - closed
    target = (H2m-1)/sp.Rational(2*mv*(2*mv-1))
    assert sp.simplify(J-target) == 0

# Polar-factor coefficient and low-exponent constant algebra.
j = sp.symbols('j', integer=True, positive=True)
qcoeff = 1-j/n
assert sp.simplify(qcoeff-(n-j)/n) == 0

# Starting from the m-mode coefficient of g=q^a and the radial integral,
# simplify the derivative-gap constant.
H = sp.symbols('H', positive=True)
J = (H-1)/(2*m*(2*m-1)*(a+1))
gm2 = a**2*((n-m)/n)**2
integral_mode = 2*m**2*gm2*J
# (M_p/M_Q) Phi'(2a) >= integral/(2 a^2 n)
C = sp.simplify(integral_mode/(2*a**2*n))
C_expected = m*(n-m)**2*(H-1)/(n**3*(2*m-1)*(2*a+2))
assert sp.simplify(C-C_expected) == 0
C_r = sp.simplify(C_expected.subs(a,r/2))
C_r_expected = m*(n-m)**2*(H-1)/(n**3*(2*m-1)*(r+2))
assert sp.simplify(C_r-C_r_expected) == 0

print('VERIFY_OK')
print('partial_fraction_identity=exact')
print('radial_harmonic_number_identity=exact')
print('coefficient_constant_reduction=exact')
