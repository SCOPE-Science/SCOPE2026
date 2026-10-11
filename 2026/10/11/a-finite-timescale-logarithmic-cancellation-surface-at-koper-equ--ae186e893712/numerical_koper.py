"""Optional numerical sanity check of a local saddle-node asymptotic law."""
from math import sqrt, log
from scipy.integrate import solve_ivp

k, delta = 1.0, 1.0
r = sqrt((k + 3.0) / 3.0)
lam = (2.0 / 3.0) * (k + 3.0) * r
S = 1.0 + 2.0 / delta + 2.0 / delta**2
critical_epsilon = sqrt(6.0 * k * (k + 3.0) * S) - k * (1.0 + 1.0 / delta)

for epsilon in (2.0, critical_epsilon, 18.0):
    H = epsilon + k * (1.0 + 1.0 / delta)
    L = 1.0 / (3.0 * r) - 6.0 * k * r * S / H**2

    def rhs(t, state):
        x, y, z = state
        return ((k * y + 3.0 * x - x**3 - lam) / epsilon,
                x - 2.0 * y + z,
                delta * (y - z))

    trajectory = solve_ivp(rhs, (0.0, 1200.0),
                           (r + 0.1, r + 0.1, r + 0.1),
                           method="DOP853", rtol=5e-12, atol=5e-14,
                           dense_output=True, max_step=0.4)
    assert trajectory.success
    print("epsilon=", epsilon, "log_coefficient=", L)
    for t in (400.0, 1200.0):
        u = trajectory.sol(t)[0] - r
        corrected = 1.0/u - 3.0*r*t/H - L*log(t)
        print(" t=", t, "compensated_reciprocal=", corrected)
