#!/usr/bin/env python3
"""Illustrate (not prove) dense-line finite-Gram approximation."""
import math
PI = math.pi
ROOT2 = math.sqrt(2.0)
POINTS = ((0.0, 0.0), (PI, 0.0), (0.0, PI), (PI, PI))


def kernel(x, y):
    return (1.0 + math.cos(x)) * (1.0 + math.cos(y)) / 4.0


def closest_line_time(x, y, cutoff):
    best_t, best_e = 0.0, float('inf')
    for k in range(-cutoff, cutoff + 1):
        t = x + 2.0 * PI * k
        delta = math.remainder(ROOT2 * t - y, 2.0 * PI)
        err = abs(delta)
        if err < best_e:
            best_e, best_t = err, t
    return best_t, best_e


def gram_diff(times):
    return max(abs(kernel(times[j] - times[k], ROOT2 * (times[j] - times[k]))
                   - kernel(POINTS[j][0] - POINTS[k][0],
                            POINTS[j][1] - POINTS[k][1]))
               for j in range(4) for k in range(4))


assert all(abs(kernel(POINTS[j][0] - POINTS[k][0],
                      POINTS[j][1] - POINTS[k][1]) - float(j == k)) < 1e-14
           for j in range(4) for k in range(4))
assert kernel(0.0, 0.0) == 1.0
previous = float('inf')
for cutoff in (10, 100, 1000, 10000, 100000):
    result = [closest_line_time(x, y, cutoff) for x, y in POINTS]
    difference = gram_diff([entry[0] for entry in result])
    phase_tol = max(entry[1] for entry in result)
    assert difference <= previous + 1e-12
    assert difference <= 2.0 * phase_tol + 1e-10
    previous = difference
    print('cutoff', cutoff, 'max_phase_error', phase_tol,
          'max_Gram_error', difference)
assert previous < 1e-8
print('VERIFY_OK irrational-line Gram approximation at five cutoffs')
# A strictly positive, even, rapidly decaying, normalized smoothing of the
# one-dimensional quasiperiodic window, preserving the Gram data closely.
cutoff = 10000
T = [closest_line_time(x, y, cutoff)[0] for x, y in POINTS]
alpha, tau = 1e-7, 1e-16

def smooth_h(t):
    return math.exp(-tau*t*t) * (kernel(t, ROOT2*t)+alpha)/(1+alpha)
assert smooth_h(0.) == 1.0
err = max(abs(smooth_h(T[j]-T[k]) - float(j == k))
          for j in range(4) for k in range(4))
assert err < 1e-5
assert all(smooth_h(u)>0.0 for u in (0., 1., 8., 100.))
print('VERIFY_OK Gaussian-regularized strict-positive Gram approximation',err)
