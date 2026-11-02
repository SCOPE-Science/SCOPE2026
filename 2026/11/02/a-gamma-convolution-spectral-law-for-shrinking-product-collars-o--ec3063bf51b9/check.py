#!/usr/bin/env python3
"""Supplementary, self-contained finite checks for product-collar spectra.

The analytic proof and hypotheses are in RESULT.md. This code deliberately
checks finite examples and independent integral identities only.
"""
import math

assertions = 0

def check(ok, name):
    global assertions
    assertions += 1
    if not ok:
        raise AssertionError(name)


def simpson(fun, lo, hi, steps):
    assert steps % 2 == 0
    width = (hi - lo) / steps
    total = fun(lo) + fun(hi)
    for k in range(1, steps):
        total += (4 if k % 2 else 2) * fun(lo + k * width)
    return total * width / 3


def profile(u, v, a):
    mid = (u + v) / 2
    half = abs(u - v) / 2
    if half < 1.e-9:
        return math.exp(-a * mid) * (1 + a * mid)
    return math.exp(-a * mid) * (
        math.cosh(a * half) + mid * math.sinh(a * half) / half)


def exact_eigen(m, n, N, a):
    check(m > n >= 0 and m + n - 1 <= N, 'indices')
    return profile((m + 1) / N, (n + 1) / N, a)


def independent_convolution(r, s, t):
    # Direct convolution integral for independent Exp(r), Exp(s),
    # not the closed-form expression used in profile().
    cdf = simpson(lambda x: r * math.exp(-r * x) *
                  (-math.expm1(-s * (t - x))), 0., t, 600)
    return 1. - cdf


def C(a):
    # Coordinates: u=t(1+w)/2, v=t(1-w)/2, Jacobian t/2.
    def f(t):
        return simpson(lambda w: (
            lambda q: q * (1 - q) * t / 2)(
            profile(t * (1 + w) / 2, t * (1 - w) / 2, a)
        ), 0, 1, 160)
    return simpson(f, 0, 1, 160)


def trace_defect(N, a):
    result = 0.0
    count = 0
    for m in range(1, N + 2):
        for n in range(m):
            if m + n - 1 <= N:
                value = exact_eigen(m, n, N, a)
                check(-1.e-13 <= value <= 1 + 1.e-13, 'spectrum [0,1]')
                result += value * (1. - value)
                count += 1
    check(count == ((N + 2) ** 2 // 4), 'two-row partitions')
    return result / (N * N)


for N in (5, 14, 30):
    for a in (.4, 2., 5.):
        for m, n in ((1, 0), (3, 1), (N - 1, 0),
                     ((N + 2) // 2, (N - 1) // 2)):
            if m <= n or m + n - 1 > N:
                continue
            value = exact_eigen(m, n, N, a)
            other = independent_convolution(m + 1, n + 1, a / N)
            check(abs(value - other) < 3.e-9,
                  'independent convolution vs diagonal formula')

c2 = C(2.)
check(.020 < c2 < .023, 'nontrivial positive continuum defect')
for N in (30, 80, 160, 240):
    approx = trace_defect(N, 2.)
    check(abs(approx - c2) < 0.32 / N, 'finite-trace Riemann convergence')

small = C(.10)
check(abs(small / (.10 ** 2 / 96.) - 1) < .035,
      'small-collar coefficient in the ordinary symmetrized bidisc')
large = C(70.)
check(abs(70. * large - .5) < .035,
      'large-collar coefficient in the ordinary symmetrized bidisc')

for p in (1, 2, 3, 4):
    def q(v):
        return math.exp(-v) * sum(v ** j / math.factorial(j)
                                  for j in range(p))
    integral = simpson(lambda v: q(v) * (1 - q(v)), 0., 45., 24000)
    expected = math.gamma(p + .5) / (math.sqrt(math.pi) * math.gamma(p))
    check(abs(integral - expected) < 1.e-8,
          'gamma-tail absolute-difference identity')

print('PASS: {} supplementary assertions; C_{{1,2}}(2)≈{:.12f}; '
      'C_{{1,2}}(0.1)≈{:.12f}; 70 C_{{1,2}}(70)≈{:.12f}'.format(
      assertions, c2, small, 70. * large))
