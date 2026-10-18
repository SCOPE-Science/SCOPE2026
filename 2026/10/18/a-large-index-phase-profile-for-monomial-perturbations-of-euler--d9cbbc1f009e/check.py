#!/usr/bin/env python3
"""Reproducible checks for the large-index perturbed partition product."""
from math import exp, log, pi, sqrt, log1p, isclose


def partitions(N):
    p = [0] * (N + 1)
    p[0] = 1
    for k in range(1, N + 1):
        for n in range(k, N + 1):
            p[n] += p[n - k]
    return p


def euler_coefficients(N):
    e = [0] * (N + 1)
    e[0] = 1
    for k in range(1, N + 2):
        for m in (k * (3 * k - 1) // 2, k * (3 * k + 1) // 2):
            if m <= N:
                e[m] = -1 if k % 2 else 1
    return e


def coefficients_by_denominator(a, j, N):
    d = euler_coefficients(N)
    d[j] -= a
    c = [1] + [0] * N
    for n in range(1, N + 1):
        c[n] = -sum(d[i] * c[n-i] for i in range(1, n + 1))
    return c


def coefficients_by_partition_blocks(a, j, N):
    p = partitions(N)
    power = [1] + [0] * N
    c = [0] * (N + 1)
    for k in range(N // j + 1):
        new = [0] * (N + 1)
        for i in range(N+1):
            if power[i]:
                for l in range(N-i+1):
                    new[i+l] += power[i] * p[l]
        power = new  # Coefficients of Q(z)^(k+1)
        for n in range(j*k, N+1):
            c[n] += (a**k) * power[n-j*k]
    return c


def logQ(t):
    total = 0.0
    for k in range(1, max(100, int(45/t))):
        q = exp(-t*k)
        if q < 1e-19:
            break
        total -= log1p(-q)
    return total


def solve_t(j, loga):
    lo, hi = 1e-9, 5.0
    for _ in range(90):
        mid = (lo + hi)/2
        if j*mid - loga - logQ(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def two_moments(t):
    E = V = 0.0
    for k in range(1, max(100, int(45/t))):
        q = exp(-k*t)
        if q < 1e-19:
            break
        E += k*q/(1-q)
        V += k*k*q/(1-q)**2
    return E, V


def main():
    N = 64
    count = 0
    for a in (1, 2, 3):
        for j in (1, 2, 3, 5, 8):
            x = coefficients_by_denominator(a, j, N)
            y = coefficients_by_partition_blocks(a, j, N)
            for n in range(N + 1):
                assert x[n] == y[n], (a, j, n)
                count += 1
    print('EXACT_COEFFICIENT_COMPARISONS', count)
    A = pi*pi/6
    numerical = 0
    for gamma in (-1.0, 0.0, 1.0):
        s = (gamma + sqrt(gamma*gamma + 4*A))/2
        target_theta = s*s/(s*s+A)
        target_variance = 2*A*s**3/(s*s+A)**3
        prev_t_err = prev_theta_err = prev_var_err = float('inf')
        for j in (100, 400, 1600):
            t = solve_t(j, gamma*sqrt(j))
            E,V = two_moments(t)
            eq = j*t-gamma*sqrt(j)-logQ(t)
            assert abs(eq) < 2e-10, (j,gamma,eq)
            t_err = abs(t*sqrt(j)-s)
            theta_err = abs(j/(j+E)-target_theta)
            var_err = abs(j**1.5*V/(j+E)**3-target_variance)
            assert t_err < prev_t_err and theta_err < prev_theta_err and var_err < prev_var_err
            prev_t_err, prev_theta_err, prev_var_err = t_err, theta_err, var_err
            numerical += 4
    print('ROOT_AND_PROFILE_NUMERICAL_CHECKS', numerical)
    previous = float('inf')
    for j in (25, 100, 400, 1600):
        t = solve_t(j, 0.0)
        approximation = sqrt(A/j) - log(j)/(8*j) - log(2*sqrt(6))/(4*j)
        scaled_error = abs(t-approximation)*j**1.5/(log(j)**2)
        assert scaled_error < 0.01, (j,scaled_error)
        E, _ = two_moments(t)
        K = exp(j*t)/(j+E)
        K_approx = exp(sqrt(A*j))/(2*(2*sqrt(6))**0.25*j**1.125)
        assert abs(K/K_approx - 1) < previous
        previous = abs(K/K_approx - 1)
        numerical += 2
    print('ADDITIONAL_ASYMPTOTIC_CHECKS', numerical-36)
    print('CHECKS_PASS')

if __name__ == '__main__':
    main()
