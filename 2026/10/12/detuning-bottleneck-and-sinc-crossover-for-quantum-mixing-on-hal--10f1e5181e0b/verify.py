#!/usr/bin/env python3
"""Finite numerical checks of Fourier identities for flux-threaded even cycles.

These checks corroborate the analytic proof; they do not certify every cycle size.
Standard-library Python only.
"""
import cmath
import math

PI = math.pi


def sinc(z):
    return 1.0 if abs(z) < 1e-14 else math.sin(z) / z


def frequencies(n, delta):
    theta = PI / n + delta
    return [2 * math.cos(theta + 2 * PI * k / n) for k in range(n)]


def exact_integral(n, delta, T, distance):
    """Independent analytic integration of each Fourier-interference term."""
    lam = frequencies(n, delta)
    acc = 0j
    for k in range(n):
        for l in range(n):
            half = (lam[k] - lam[l]) * T / 2
            acc += (cmath.exp(2j * PI * (k-l) * distance / n)
                    * cmath.exp(-1j * half) * sinc(half))
    assert abs(acc.imag) < 2e-8, (n, delta, T, distance, acc)
    return acc.real / (n*n)


def direct_integral(n, delta, T, distance, steps=6000):
    """Unrelated trapezoid integration of squared Fourier walk amplitudes."""
    lam = frequencies(n, delta)
    a = [cmath.exp(2j * PI * k * distance / n) for k in range(n)]
    total = 0.
    for j in range(steps+1):
        t = T * j / steps
        amp = sum(a[k] * cmath.exp(-1j * t * lam[k]) for k in range(n)) / n
        total += (0.5 if j == 0 or j == steps else 1.) * abs(amp)**2
    return total / steps


def limit_antipodal(n, s):
    return (1 / n - 2 / (n*n) * sum(
        sinc(4*s*math.sin((2*k+1)*PI/n)) for k in range(n//2)
    ))


def average_at_half_flux(n, distance):
    lam = frequencies(n, 0.)
    val = 0j
    for k in range(n):
        for l in range(n):
            if abs(lam[k]-lam[l]) < 1e-11:
                val += cmath.exp(2j*PI*(k-l)*distance/n)/(n*n)
    assert abs(val.imag)<1e-10
    return val.real


cases = 0
pairs = 0
max_quad_error = 0.0
max_scaling_error = 0.0
for n in [4, 6, 8, 10, 12, 14, 16, 18]:
    for t in (0.2, 1.3, 10.7):
        w = frequencies(n, 0.)
        amp = sum((-1)**k * cmath.exp(-1j*t*w[k]) for k in range(n))/n
        assert abs(amp) < 3e-13, (n,t,amp)
    for d in range(n):
        expected = (1 + int(d == 0) - int(d == n//2)) / n
        assert abs(average_at_half_flux(n, d) - expected) < 1e-11, (n,d)
        cases += 1
    for delta in [-PI/(2*n), -0.021, -0.002, 0.002, 0.021, PI/(2*n)]:
        if abs(delta)>PI/(2*n)+1e-12: continue
        lam = frequencies(n,delta)
        bound = (8/PI)*math.sin(PI/n)*abs(delta)
        for k in range(n):
            for l in range(k+1,n):
                gap = abs(lam[k]-lam[l])
                assert gap + 1e-11 >= bound, (n, delta, k, l, gap, bound)
                pairs += 1
    if n<=10:
        for delta in [-.07,.015]:
            for d in [0,1,n//2]:
                T = 9.37
                fast = exact_integral(n,delta,T,d)
                slow = direct_integral(n,delta,T,d)
                err = abs(fast-slow)
                max_quad_error = max(max_quad_error,err)
                assert err < 2e-6, (n,d,delta,err)
    for s in [.17, .73, 2.2]:
        estimate = exact_integral(n,.0001,s/.0001,n//2)
        target = limit_antipodal(n,s)
        err = abs(estimate-target)
        max_scaling_error = max(max_scaling_error,err)
        assert err < 4e-4, (n,s,err)
        assert abs(limit_antipodal(n,0.)) < 1e-14

print("VERIFY_OK instantaneous_darkness=24 half_flux_distance_entries=%d gap_pairs=%d quadrature_checks=%d "
      "max_quadrature_error=%.3g max_scaling_error=%.3g "
      "critical_limit_n4_s073=%.12f" %
      (cases,pairs,4*2*3,max_quad_error,max_scaling_error,limit_antipodal(4,.73)))
