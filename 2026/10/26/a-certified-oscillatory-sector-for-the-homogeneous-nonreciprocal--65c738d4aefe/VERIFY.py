"""Reproducible finite checks for an oscillation theorem in a planar tanh flow.

Only finite corroboration: the proof of global results is in RESULT.md.
Requires numpy and scipy. Run: python VERIFY.py
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root


def rhs(z, j, k):
    x, y = z
    return np.array([-x + np.tanh(j*x + k*y),
                     -y + np.tanh(j*y - k*x)])


def angular_rate(z, j, k):
    x, y = z
    dx, dy = rhs(z, j, k)
    return (x * dy - y * dx) / (x*x + y*y)


def main():
    rng = np.random.default_rng(61407)
    a, b = rng.uniform(-12., 12., size=(2, 50000))
    dot = a*np.tanh(a) + b*np.tanh(b)
    cross = a*np.tanh(b) - b*np.tanh(a)
    assert np.all(dot > np.abs(cross))
    print("PASS: 50,000 strict angular-inequality comparisons")

    params = ((1.25, .25), (1.5, .5), (2., 1.),
              (2., 2.), (2., 2.5), (3., 6.), (20., 21.))
    stationarity_checks = 0
    angular_checks = 0
    for j, k in params:
        equilibria = []
        for x0 in np.linspace(-.95, .95, 5):
            for y0 in np.linspace(-.95, .95, 5):
                s = root(lambda z: rhs(z, j, k), (x0, y0),
                         tol=1.e-11)
                if s.success and np.max(np.abs(s.x)) < 1.:
                    if not any(np.linalg.norm(s.x - w) < 1.e-7
                               for w in equilibria):
                        equilibria.append(s.x)
                stationarity_checks += 1
        assert len(equilibria) == 1
        assert np.linalg.norm(equilibria[0]) < 1.e-7
        sol = solve_ivp(lambda t, z: rhs(z, j, k), (0., 300.),
                        (.25, .13), atol=1.e-11, rtol=1.e-9,
                        max_step=.1)
        assert sol.success
        tail = sol.y[:, -1000:].T
        assert np.min(np.linalg.norm(tail, axis=1)) > .05
        rates = np.array([angular_rate(z, j, k) for z in tail])
        assert np.all(np.abs(rates) < np.hypot(j, k))
        if k >= j:
            assert np.all(rates < 0)
        if k > j:
            lower = (k - j) * np.tanh(j + k) / (j + k)
            assert np.all(-rates > lower)
        angular_checks += len(rates)
    print(f"PASS: {stationarity_checks} multistart finite root searches")
    print(f"PASS: {angular_checks} trajectory angular-speed comparisons")
    print("The finite checks do not establish global uniqueness or periodicity.")


if __name__ == "__main__":
    main()
