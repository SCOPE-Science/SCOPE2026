#!/usr/bin/env python3
"""Reproducible finite and quadrature checks for a three-level resetting model.

Only the Python standard library is required. All universal claims rest on the
analytic proof in RESULT.md, not on these sampled numerical assertions.
"""
import math

count = 0

def check(condition, label):
    global count
    count += 1
    if not condition:
        raise AssertionError(label)


def integrate_simpson(f, n=12000):
    if n % 2:
        raise ValueError("n must be even")
    h = 1.0 / n
    total = f(0.0) + f(1.0)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(j * h)
    return h * total / 3


def moment_integral(k, ell):
    exponent = (8 + k + ell) / 2
    integral = integrate_simpson(
        lambda u: (u ** (k + 2)) * ((1-u) ** (ell + 2))
        / ((u*u-u+1) ** exponent)
    )
    return .5 * 3 ** exponent * math.gamma(exponent) * integral

I00 = moment_integral(0, 0)
I10 = moment_integral(1, 0)
I01 = moment_integral(0, 1)
I11 = moment_integral(1, 1)
M = 27 / (8 * math.sqrt(math.pi))
H = 27 * math.sqrt(3) / (2 * math.pi) - 4
C = H - (8 / 9) * M*M
check(abs(I00 - 4*math.pi*math.sqrt(3)) < 1e-9, "normalizer")
check(abs(I10 - 27/2*math.sqrt(3*math.pi)) < 1e-9, "first-moment integral")
check(abs(I01 - I10) < 1e-9, "gap symmetry")
check(abs(I11 - (162 - 16*math.pi*math.sqrt(3))) < 1e-9, "mixed-moment integral")
check(abs(I10/I00 - M) < 1e-10, "mean")
check(abs(I11/I00 - H) < 1e-10, "mixed mean")
check(H - M*M < 0, "fixed-age repulsion")
check(C > 0, "renewal lower bound")
check(abs(C - (108*math.sqrt(3)-81-32*math.pi)/(8*math.pi))<1e-12,"closed-form lower bound")
check(abs(H - (math.pi/4)*M*M - .5952838381941927) < 1e-10,"Poisson coefficient")


def equilibrium_age_moments(discrete_law):
    """Return mean age and mean sqrt age for a finite-support renewal law."""
    ew = sum(p*w for p, w in discrete_law)
    ew2 = sum(p*w*w for p, w in discrete_law)
    ew32 = sum(p*w**1.5 for p, w in discrete_law)
    return ew2/(2*ew), 2*ew32/(3*ew)

for value in [.001, .03, .1, .5, 1, 3, 10, 100, 1000]:
    age, sage=equilibrium_age_moments([(1., value)])
    check(abs(age - value/2) < 1e-10 * max(1.,value), "periodic mean age")
    check(abs(sage-2*math.sqrt(value)/3) < 1e-10, "periodic sqrt age")
    check(abs(sage*sage/age - 8/9) < 1e-11, "periodic sharpness")
    check(abs((H*age-M*M*sage*sage) - C*age) < 1e-10, "periodic equality")

for probability in [.01, .05, .15, .3, .4, .5, .7, .85, .95, .99]:
    for large in [1.5, 2, 4, 10, 100, 1000]:
        law=[(probability, 1.),(1-probability,large)]
        age,sage=equilibrium_age_moments(law)
        check(sage*sage/age < 8/9+1e-10,"length-bias Jensen bound")
        check(H*age-M*M*sage*sage > C*age-1e-10,"strict universal covariance")
        check(H*age-M*M*sage*sage > 0,"strict positive renewal covariance")

for rate in [0.05,.1,.3,1.,3.,5.,11.,25.]:
    # Exponential W of mean 1/rate induces exponential stationary age.
    age=1/rate
    sage=math.gamma(1.5)/math.sqrt(rate)
    check(abs(H*age-M*M*sage*sage - (H-math.pi*M*M/4)/rate)<1e-10,
          "Poisson covariance identity")

print(f"PASS: {count} standard-library numerical assertions")
print("I00,I10,I11 =",I00,I10,I11)
print("m,h,fixed_cov,sharp_renewal_coefficient,Poisson_coefficient =",
      M,H,H-M*M,C,H-math.pi*M*M/4)
