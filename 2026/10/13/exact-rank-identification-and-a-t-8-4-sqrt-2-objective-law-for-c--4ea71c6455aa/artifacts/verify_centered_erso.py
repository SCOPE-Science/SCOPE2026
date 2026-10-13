import sympy as sp

q = sp.sqrt(2)
# Source parameters for f(X)=1/2 ||X-I/2||_F^2 on S^2.
L = mu = sp.Integer(1)
lambda_star = sp.Rational(1,2)
T0 = sp.simplify(72*L/(mu*lambda_star**2))
T0p = T0 + 2
assert T0 == 288 and T0p == 290

# After the source simple step eta_1=1, the first iterate is the opposite vertex.
# eta_2=2/3 then gives |s_2|=1/6.
s1 = -sp.Rational(1,2)
s2 = sp.simplify((1-sp.Rational(2,3))*s1 + sp.Rational(2,3)*sp.Rational(1,2))
assert s2 == sp.Rational(1,6)

d2 = q*abs(s2)
lam2 = sp.Rational(1,2)-abs(s2)
assert sp.simplify(lam2-d2) > 0  # thresholding rank is 2 at t=3

# Once |s|<=1/6, the full-rank spectral oracle sends s to -(1+sqrt(2))s.
s = sp.symbols('s', nonzero=True, real=True)
y = -(1+q)*s
t = sp.symbols('t', integer=True, positive=True)
eta = 2/(t+1)
coeff = sp.simplify((1-eta)*s + eta*y)
assert sp.simplify(coeff/s - (t-3-2*q)/(t+1)) == 0

# Every multiplier from t=3 onward has modulus < 1, so |s_t|<=1/6 remains invariant.
for k in range(3,200):
    c = sp.N(abs((sp.Integer(k)-3-2*q)/(sp.Integer(k)+1)), 50)
    assert c < 1
# Analytically for k>=6 numerator is positive and strictly below denominator;
# k=3,4,5 are checked exactly below.
for k in [3,4,5]:
    assert sp.simplify(1-((sp.Integer(k)-3-2*q)/(sp.Integer(k)+1))**2) > 0
assert sp.simplify(sp.Rational(1,2) - (1+q)*sp.Rational(1,6)) > 0

# Gamma-product closed form agrees with finite products for several horizons.
for N in range(3,15):
    prod = sp.prod((sp.Integer(k)-3-2*q)/(sp.Integer(k)+1) for k in range(3,N+1))
    gamma_form = 6*sp.gamma(N-2-2*q)/(sp.gamma(-2*q)*sp.gamma(N+2))
    assert sp.simplify(prod-gamma_form) == 0

# Exact line search from any nonzero s0 reaches zero along the segment to the opposite vertex.
r = sp.symbols('r', positive=True)
eta_star = sp.simplify(r/(r+sp.Rational(1,2)))
line_value = sp.simplify((1-eta_star)*r + eta_star*(-sp.Rational(1,2)))
assert line_value == 0
assert sp.simplify(eta_star) > 0
assert sp.simplify(1-eta_star) >= 0

print('VERIFY_OK')
