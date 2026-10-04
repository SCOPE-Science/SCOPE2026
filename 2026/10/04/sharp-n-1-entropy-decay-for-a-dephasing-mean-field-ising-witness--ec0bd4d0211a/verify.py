#!/usr/bin/env python3
import cmath
import math


def energy(bits, J):
    n = len(bits)
    s = [1 if b == 0 else -1 for b in bits]
    pair_sum = sum(s[i] * s[j] for i in range(n) for j in range(i + 1, n))
    return (J / n) * pair_sum


def direct_x(n, r0, gamma, J, t, site=0):
    # Direct computational-basis sum for Tr[rho(t) X_site].
    # The initial tensor product has matrix element r0/2^n between
    # bit strings differing only at the selected site. Local Z dephasing
    # multiplies that coherence by exp(-2 gamma t).
    total = 0j
    scale = r0 * math.exp(-2.0 * gamma * t) / (2 ** n)
    for z in range(2 ** n):
        bits = tuple((z >> k) & 1 for k in range(n))
        flipped = list(bits)
        flipped[site] ^= 1
        flipped = tuple(flipped)
        phase = cmath.exp(-1j * t * (energy(bits, J) - energy(flipped, J)))
        total += scale * phase
    return total.real


def closed_x(n, r0, gamma, J, t):
    rt = r0 * math.exp(-2.0 * gamma * t)
    return rt * math.cos(2.0 * J * t / n) ** (n - 1)


def entropy_per_site(n, r0, gamma, J, t):
    rt = r0 * math.exp(-2.0 * gamma * t)
    beta = math.atanh(rt)
    c = math.cos(2.0 * J * t / n) ** (n - 1)
    return rt * beta * (1.0 - c)


def trace_distance_one_site(n, r0, gamma, J, t):
    rt = r0 * math.exp(-2.0 * gamma * t)
    c = math.cos(2.0 * J * t / n) ** (n - 1)
    return rt * abs(1.0 - c)


def check_case(r0, gamma, J, t):
    for n in range(2, 11):
        dx = direct_x(n, r0, gamma, J, t)
        cx = closed_x(n, r0, gamma, J, t)
        assert abs(dx - cx) < 2e-12, (n, dx, cx)
        rt = r0 * math.exp(-2.0 * gamma * t)
        beta = math.atanh(rt)
        direct_D_per_site = beta * (rt - dx)
        assert abs(direct_D_per_site - entropy_per_site(n, r0, gamma, J, t)) < 2e-12

    rt = r0 * math.exp(-2.0 * gamma * t)
    entropy_limit = 2.0 * rt * math.atanh(rt) * J * J * t * t
    trace_limit = 2.0 * rt * J * J * t * t
    for n in (10000, 20000):
        scaled_entropy = n * entropy_per_site(n, r0, gamma, J, t)
        scaled_trace = n * trace_distance_one_site(n, r0, gamma, J, t)
        assert abs(scaled_entropy / entropy_limit - 1.0) < 5e-4
        assert abs(scaled_trace / trace_limit - 1.0) < 5e-4


def main():
    check_case(0.37, 0.23, 1.2, 0.73)
    check_case(0.62, 0.41, -0.8, 1.1)
    check_case(0.21, 0.07, 2.0, 0.35)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
