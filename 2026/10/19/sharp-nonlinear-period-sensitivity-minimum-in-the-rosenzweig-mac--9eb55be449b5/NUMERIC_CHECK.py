"""Optional finite-parameter numerical corroboration, not a proof.
Requires NumPy and SciPy; run python NUMERIC_CHECK.py.
"""
import numpy as np
from scipy.integrate import solve_ivp


def period_slope(h, departure, integration_end):
    d_hopf = (1 - h) / (1 + h)
    d = d_hopf - departure
    equilibrium_x = h * d / (1 - d)
    equilibrium_y = (1 - equilibrium_x) * (h + equilibrium_x)

    def field(t, state):
        x, y = state
        return np.array([x * (1 - x) - x * y / (h + x),
                         y * (x / (h + x) - d)])

    def prey_peak(t, state):
        return field(t, state)[0]

    prey_peak.direction = -1
    prey_peak.terminal = False
    sol = solve_ivp(field, (0, integration_end),
                    (1.2 * equilibrium_x, 0.9 * equilibrium_y),
                    method='DOP853', rtol=1e-10, atol=1e-12,
                    dense_output=True, events=prey_peak, max_step=1)
    peaks = sol.t_events[0]
    peaks = peaks[peaks > 0.8 * integration_end]
    assert len(peaks) >= 3, 'Not enough late peaks to estimate period'
    t0, t1 = peaks[-2:]
    period = t1 - t0
    theta = 2 * np.pi * np.arange(2048) / 2048
    x_sample = sol.sol(t0 + period * theta / (2 * np.pi))[0]
    r = 2 * np.hypot(np.mean(x_sample * np.cos(theta)),
                     np.mean(x_sample * np.sin(theta)))
    trace = equilibrium_x * (-1 + (1 - equilibrium_x) / (h + equilibrium_x))
    determinant = equilibrium_x * equilibrium_y * h / (h + equilibrium_x)**3
    omega_linear = np.sqrt(determinant - trace**2 / 4)
    inferred = (period * omega_linear / (2 * np.pi) - 1) / r**2
    theory = ((1 + 5*h - 4*h**3 + 7*h**4 - h**5) /
              (6*h*(1-h)**2*(1+h)**3))
    return inferred, theory, abs(inferred / theory - 1)


if __name__ == '__main__':
    for h, departure, horizon in [(0.2, 0.001, 10000),
                                  (0.5, 0.001, 10000),
                                  (0.8, 0.001, 10000),
                                  (0.5, 0.003, 6000)]:
        measured, predicted, relative_error = period_slope(h, departure, horizon)
        print(f'h={h}, departure={departure}, observed={measured:.9g}, '
              f'predicted={predicted:.9g}, relative_error={relative_error:.5g}')
        assert relative_error < 0.025
    print('Numerical corroboration complete; asymptotic limits are established analytically.')
