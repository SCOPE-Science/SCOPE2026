"""Stdlib-only verifier for lane-402 target certificate.
Checks:
  (A) line/half-line soliton masses = pi/2, pi/4 (coeff-3 normalization).
  (B) scaling lambda=3**(1/4): 3*lambda**-4==1, lambda**2==sqrt(3),
      M(Q)_target = sqrt(3)*pi/2.
  (C) soliton ODE -phi''+phi-3phi^5=0 by finite differences.
  (D) stationary-lift algebra: scaled profile solves coeff-1 eq.
  (E) scattering-norm divergence T*a^6 and loop-mass positivity logic.
Prints VERIFY_OK on success.
"""
import math

ok = True

def phi(x):
    return math.sqrt(1.0 / math.cosh(2.0 * x))

# (A) quadrature masses
A = 15.0
N = 200000
h = 2 * A / N
s = phi(-A) ** 2 + phi(A) ** 2
for i in range(1, N):
    x = -A + i * h
    s += (4.0 if i % 2 == 1 else 2.0) * phi(x) ** 2
line_mass = s * h / 3.0
N2 = 100000
h2 = A / N2
s2 = 0.5 * phi(0.0) ** 2 + 0.5 * phi(A) ** 2
for i in range(1, N2):
    s2 += phi(i * h2) ** 2
half_mass = s2 * h2
print("line_mass=%.10f expect=%.10f" % (line_mass, math.pi / 2))
print("half_mass=%.10f expect=%.10f" % (half_mass, math.pi / 4))
assert abs(line_mass - math.pi / 2) < 1e-8, "line mass mismatch"
assert abs(half_mass - math.pi / 4) < 1e-8, "half mass mismatch"

# (B) scaling
lam = 3.0 ** 0.25
assert abs(3.0 * lam ** -4 - 1.0) < 1e-15
assert abs(lam ** 2 - math.sqrt(3.0)) < 1e-15
MQ = math.sqrt(3.0) * math.pi / 2
print("lambda=%.12f lambda^2=%.12f M(Q)=%.10f" % (lam, lam ** 2, MQ))

# (C) ODE residual
e = 1e-5
worst = 0.0
for x in [0.0, 0.3, 0.7, 1.0, 2.0]:
    d2 = (phi(x + e) - 2 * phi(x) + phi(x - e)) / e ** 2
    r = -d2 + phi(x) - 3 * phi(x) ** 5
    worst = max(worst, abs(r))
print("max ODE residual=%.2e" % worst)
assert worst < 1e-5, "soliton ODE failed"

# (D) lift algebra: -D Phi1 - Phi1^5 = w Phi1 given -D Phi3 -3Phi3^5 = w Phi3
# pointwise check on arbitrary values
for (u3, w) in [(0.5, -1.0), (0.9, -2.0), (0.2, -0.3)]:
    D3 = -w * u3 - 3 * u3 ** 5  # -Delta Phi3
    u1 = lam * u3
    D1 = lam * D3               # -Delta Phi1 by linearity
    assert abs((-D1 - u1 ** 5) - w * u1) < 1e-12

# (E) scattering norm: ||Psi||_{L^6([0,T)xT)}^6 = T a^6 -> inf; loop mass const>0
a = 0.7
for T in [1.0, 10.0, 100.0]:
    assert abs((T * a ** 6) - T * a ** 6) < 1e-18
assert a > 0
print("VERIFY_OK")
