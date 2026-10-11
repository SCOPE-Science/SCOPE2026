import cmath
import math

q = 19.0 / 20.0

def data(k):
    assert -1.0 < k <= 0.0
    A = 1.0 - k
    C = (2.0 - k) / 3.0
    disc = A*A - 4.0*C
    assert disc < 0.0
    zplus = (-A + cmath.sqrt(disc)) / 2.0
    zminus = (-A - cmath.sqrt(disc)) / 2.0
    # Exact quadratic identities.
    assert abs(zplus + zminus + A) < 1e-14
    assert abs(zplus*zminus - C) < 1e-14
    omega = abs(zplus) ** (1.0 / q)
    theta = cmath.phase(zplus)
    tau_plus = (theta - q*math.pi/2.0) / omega
    tau_minus = (2.0*math.pi - theta - q*math.pi/2.0) / omega
    assert tau_plus > 0.0
    assert tau_minus > tau_plus
    return zplus, zminus, omega, tau_plus, tau_minus

zplus, zminus, omega, tau, tau_other = data(-0.5)
assert abs(zplus.real + 0.75) < 1e-14
assert abs(zplus.imag - math.sqrt(13.0/48.0)) < 1e-14
assert abs(omega - (5.0/6.0)**(10.0/19.0)) < 1e-14
exact_tau = (21.0*math.pi/40.0 - math.atan(math.sqrt(13.0/27.0))) / ((5.0/6.0)**(10.0/19.0))
assert abs(tau - exact_tau) < 1e-14
assert abs(omega - 0.9085015235955970) < 5e-15
assert abs(tau - 1.1477399921500822) < 5e-15

# Direct characteristic residual at the corrected crossing.
s = 1j * omega
char = s**(2*q) + 1.5*s**q*cmath.exp(-s*tau) + (5.0/6.0)*cmath.exp(-2*s*tau)
assert abs(char) < 2e-12

# The published delay is not a crossing at the published/correct frequency.
tau_printed = 1.0229
char_printed = s**(2*q) + 1.5*s**q*cmath.exp(-s*tau_printed) + (5.0/6.0)*cmath.exp(-2*s*tau_printed)
assert abs(char_printed) > 1e-2

speed = q*omega**2 / (q*q + (tau*omega)**2)
assert abs(speed - 0.3940683275792386) < 5e-15
assert speed > 0.0

expected = {
    -0.2: 1.0064267224766907,
    -0.4: 1.0992129213228290,
    -0.6: 1.1995397463659176,
    -0.8: 1.3245320194363386,
}
for k, target in expected.items():
    _, _, _, t, t2 = data(k)
    assert abs(t-target) < 5e-14
    assert t2 > t

print('VERIFY_OK')
