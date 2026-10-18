"""Finite-sum diagnostics for the rotation/dilation spectral formula.

Run with Python 3.10 or newer: python checks/resonance_check.py
Only the standard library is required. Finite checks do not prove asymptotic claims.
"""
import cmath
import math


def amplitude(j, alpha, m, t, theta):
    descending = math.prod(j + k for k in range(1, m + 1))
    normalization = ((j + 1) / (j + m + 1)) ** ((1 - alpha) / 2)
    return descending * normalization * math.exp(-t * j) * abs(1 - cmath.exp(1j * j * theta))


def normalized_sum(t, theta, alpha, m, p):
    nmax = math.ceil(45 / (min(1.0, p) * t))
    return t ** (m * p + 1) * sum(
        amplitude(j, alpha, m, t, theta) ** p for j in range(nmax)
    )


def profile_integral(q, a, omega, m, p):
    # Midpoint quadrature, with a fixed refined grid for reproducible diagnostics.
    segments = 70000
    upper = 70.0 / p
    step = upper / segments
    total = 0.0
    for j in range(segments):
        x = (j + 0.5) * step
        carrier = (x ** (m * p)) * math.exp(-p * x)
        avg = sum(abs(1 - cmath.exp(1j * (2 * math.pi * a * s / q + omega * x))) ** p
                  for s in range(q)) / q
        total += carrier * avg
    return step * total


def near(actual, expected, tolerance, case):
    err = abs(actual - expected) / max(abs(expected), 1e-12)
    assert err < tolerance, (case, actual, expected, err)
    return err


def test():
    for alpha in (-0.4, 0.3, 1.8):
        for m in (1, 2, 3):
            for j in (0, 1, 4, 11):
                # Verify the ON-basis coefficient directly from its input/output weights.
                t, theta = .27, .43
                input_coeff = (j + m + 1) ** ((alpha - 1) / 2)
                output_coeff = input_coeff * math.prod(j + k for k in range(1, m + 1))
                output_coeff *= math.exp(-t * j) * abs(1 - cmath.exp(1j * j * theta))
                direct = output_coeff * (j + 1) ** ((1 - alpha) / 2)
                near(amplitude(j, alpha, m, t, theta), direct, 1e-12, 'basis')

    cases = [
        # (m, p, alpha, denominator, numerator, detuning, tolerance)
        (1, 2., .3, 1, 0, 2., .012),
        (1, 4., .3, 2, 1, 1.5, .022),
        (2, 1., .3, 3, 1, .5, .012),
        (1, 1., 1.8, 1, 0, 1., .009),
        (2, .75, -.4, 2, 1, 1.25, .02),
    ]
    for m, p, alpha, q, a, omega, tol in cases:
        target = profile_integral(q, a, omega, m, p)
        observed = normalized_sum(.006, 2 * math.pi * a / q + .006 * omega, alpha, m, p)
        error = near(observed, target, tol, (m,p,alpha,q,a,omega))
        print('detuning',m,p,alpha,q,a,omega,'observed',round(observed,9),
              'profile',round(target,9),'relative error',round(error,6))

    # Closed Fourier averages for quartic phase at rational and irrational angles.
    m,p,alpha,t = 1,4.,.3,.002
    exact_rational = math.gamma(5) * 8 / 4**5
    exact_haar = math.gamma(5) * 6 / 4**5
    irrational = 2 * math.pi * ((math.sqrt(5)-1)/2)
    near(normalized_sum(t, math.pi, alpha, m,p),exact_rational,.008,'rational pi')
    near(normalized_sum(t, irrational,alpha,m,p),exact_haar,.008,'irrational')
    omega = 1.5
    closed_profile = math.gamma(5) * (6 / 4**5 + 2 * ((4-2j*omega)**(-5)).real)
    near(closed_profile,profile_integral(2,1,omega,1,4.), 1e-8,'closed crossover')
    print('quartic pi-resonance',exact_rational,'haar',exact_haar,
          'detuning profile',closed_profile)
    print('All finite diagnostics passed; no infinite proof is claimed from them.')

if __name__ == '__main__':
    test()
