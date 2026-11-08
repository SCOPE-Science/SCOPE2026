"""Finite numerical checks for a periodic two-species competition law.

Requires scipy. A numerical experiment does not establish an asymptotic theorem.
"""
import math
from scipy.integrate import solve_ivp


def check_one(k):
    a, b, r1, r2, tau, x0, h = 1.1, 0.9, 0.7, 1.2, 0.8, 0.3, 1.3
    y0 = h * x0**k
    p = math.exp(-r1 * tau)
    q = math.exp(-r2 * tau)
    original = solve_ivp(
        lambda s, z: [z[0]*(r1-a*z[0]-b*z[1]),
                      z[1]*(r2-k*a*z[0]-k*b*z[1])],
        (0, tau), [x0, y0], rtol=1e-12, atol=1e-14,
    )
    xx, yy = original.y[:, -1]
    x1, y1 = p * xx, q * yy
    assert abs(y1/x1**k-h) < 5e-10
    x = x0
    n = 4000
    for _ in range(n):
        sol = solve_ivp(
            lambda s, z: [-a*math.exp(r1*s)*z[0]**2
                          -b*h*math.exp(r2*s)*z[0]**(k+1)],
            (0, tau), [x], rtol=1e-11, atol=1e-13,
        )
        x = sol.y[0, -1]
    y = h*x**k
    I1, I2 = math.expm1(r1*tau)/r1, math.expm1(r2*tau)/r2
    if k < 1:
        predicted_x = (k*b*h*I2)**(-1/k)
        predicted_y = 1/(k*b*I2)
        scaled_x, scaled_y = n**(1/k)*x, n*y
    elif k == 1:
        predicted_x = 1/(a*I1+b*h*I2)
        predicted_y = h*predicted_x
        scaled_x, scaled_y = n*x, n*y
        assert abs(1/x-(1/x0+n*(a*I1+b*h*I2))) < 1e-3
    else:
        predicted_x = 1/(a*I1)
        predicted_y = h*predicted_x**k
        scaled_x, scaled_y = n*x, n**k*y
    assert abs(scaled_x/predicted_x-1) < 0.025
    assert abs(scaled_y/predicted_y-1) < 0.025
    print('kappa=', k, 'scaled_x=', format(scaled_x,'.9g'),
          'target_x=', format(predicted_x,'.9g'),
          'scaled_y=', format(scaled_y,'.9g'),
          'target_y=', format(predicted_y,'.9g'))


if __name__ == '__main__':
    for kappa in (0.5, 1.0, 2.0):
        check_one(kappa)
    print('VERIFY_OK parameter_regimes=3 pulses_per_case=4000 exact_ratio_checked=3')
