#!/usr/bin/env python3
import math
import cmath

def matvec(H, v):
    return [sum(H[i][j] * v[j] for j in range(len(v))) for i in range(len(H))]

def exp_action(H, t, v, terms=180):
    out = [complex(x) for x in v]
    term = [complex(x) for x in v]
    for k in range(1, terms + 1):
        Hv = matvec(H, term)
        term = [(-1j * t / k) * z for z in Hv]
        out = [out[i] + term[i] for i in range(len(v))]
        if max(abs(z) for z in term) < 1e-16:
            break
    return out

def chain_hamiltonian(N, lam=1.0):
    H = [[0.0 for _ in range(N)] for _ in range(N)]
    for n in range(1, N):
        J = 0.5 * lam * math.sqrt(n * (N - n))
        H[n - 1][n] = J
        H[n][n - 1] = J
    return H

def p_exact(m, s):
    central = math.exp(
        math.lgamma(2 * m + 1)
        - 2 * math.lgamma(m + 1)
        - m * math.log(4.0)
    )
    total = central
    ratio = 1.0
    for k in range(1, m + 1):
        ratio *= (m - k + 1) / (m + k)
        total += 2.0 * central * ratio * math.exp(-0.5 * k * k * s * s)
    return total

def normal_integral(m, s, panels=40000):
    # E[cos^(2m)(s Z / 2)] over Z~N(0,1), integrated on [-8,8].
    a, b = -8.0, 8.0
    if panels % 2:
        panels += 1
    h = (b - a) / panels
    norm = 1.0 / math.sqrt(2.0 * math.pi)
    def f(z):
        return norm * math.exp(-0.5 * z * z) * (math.cos(0.5 * s * z) ** (2 * m))
    acc = f(a) + f(b)
    for j in range(1, panels):
        acc += (4.0 if j % 2 else 2.0) * f(a + j * h)
    return acc * h / 3.0

def theta_constant(s):
    total = 1.0
    k = 1
    while True:
        term = math.exp(-0.5 * k * k * s * s)
        if term < 1e-16:
            break
        total += 2.0 * term
        k += 1
    return total / math.sqrt(math.pi)

def solve_target(m, eta):
    lo, hi = 0.0, 1.0
    while p_exact(m, hi) > eta:
        hi *= 2.0
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        if p_exact(m, mid) > eta:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def main():
    amplitude_checks = 0
    for N in (2, 3, 4, 6, 8):
        H = chain_hamiltonian(N)
        for t in (0.23, 0.81, 1.57, 2.71, math.pi):
            v = [0.0] * N
            v[0] = 1.0
            y = exp_action(H, t, v)
            direct = y[-1]
            formula = (-1j * math.sin(t / 2.0)) ** (N - 1)
            assert abs(direct - formula) < 2e-11
            amplitude_checks += 1

    quadrature_checks = 0
    max_quad_error = 0.0
    for m in (1, 2, 5, 12, 25):
        for s in (0.12, 0.45, 0.9):
            a = p_exact(m, s)
            b = normal_integral(m, s)
            err = abs(a - b)
            max_quad_error = max(max_quad_error, err)
            assert err < 2e-10
            quadrature_checks += 1

    monotonic_checks = 0
    for m in (1, 3, 10, 40):
        vals = [p_exact(m, s) for s in (0.0, 0.1, 0.3, 0.7, 1.4, 3.0)]
        assert all(vals[j + 1] < vals[j] for j in range(len(vals) - 1))
        monotonic_checks += len(vals) - 1

    scaling_checks = 0
    max_scaling_error = 0.0
    for c in (0.5, 1.0, 2.0, 3.0):
        target = 1.0 / math.sqrt(1.0 + 0.5 * c * c)
        vals = [p_exact(m, c / math.sqrt(m)) for m in (100, 500, 2000, 8000)]
        errs = [abs(v - target) for v in vals]
        assert errs[-1] < errs[0]
        assert errs[-1] < 6e-6
        max_scaling_error = max(max_scaling_error, errs[-1])
        scaling_checks += 1

    theta_checks = 0
    max_theta_error = 0.0
    for s in (0.5, 1.0, 2.0):
        target = theta_constant(s)
        vals = [math.sqrt(m) * p_exact(m, s) for m in (500, 2000, 8000)]
        errs = [abs(v - target) for v in vals]
        assert errs[-1] < errs[0]
        assert errs[-1] < 2e-3
        max_theta_error = max(max_theta_error, errs[-1])
        theta_checks += 1

    threshold_checks = 0
    max_threshold_error = 0.0
    for eta in (0.7, 0.9, 0.99):
        target = math.sqrt(2.0 * (eta ** -2 - 1.0))
        vals = [math.sqrt(m) * solve_target(m, eta) for m in (200, 1000, 5000)]
        errs = [abs(v - target) for v in vals]
        assert errs[-1] < errs[0]
        assert errs[-1] < 4e-4
        max_threshold_error = max(max_threshold_error, errs[-1])
        threshold_checks += 1

    print("VERIFY_OK")
    print("direct_chain_amplitude_checks =", amplitude_checks)
    print("gaussian_quadrature_checks =", quadrature_checks)
    print("max_quadrature_error =", max_quad_error)
    print("monotonicity_checks =", monotonic_checks)
    print("scaling_profile_checks =", scaling_checks)
    print("max_scaling_profile_error =", max_scaling_error)
    print("fixed_noise_theta_checks =", theta_checks)
    print("max_theta_constant_error =", max_theta_error)
    print("target_threshold_checks =", threshold_checks)
    print("max_target_threshold_error =", max_threshold_error)

if __name__ == "__main__":
    main()
