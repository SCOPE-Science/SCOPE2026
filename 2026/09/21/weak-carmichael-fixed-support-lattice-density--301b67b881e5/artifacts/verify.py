#!/usr/bin/env python3
"""Exact finite checks for fixed-support weak Carmichael exponent lattices."""

from itertools import product
from math import gcd, log, pi


def lcm(a, b):
    return a // gcd(a, b) * b


def divisors(n):
    out = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def multiplicative_order(a, m):
    if m == 1:
        return 1
    assert gcd(a, m) == 1
    x = 1
    for k in range(1, m + 1):
        x = (x * a) % m
        if x == 1:
            return k
    raise RuntimeError("order not found")


def admissible(S):
    return all((pi - 1) % pj != 0 for i, pi in enumerate(S)
               for j, pj in enumerate(S) if i != j)


def image_tuple(S, exps):
    vals = []
    for i, p in enumerate(S):
        m = p - 1
        x = 1 % m
        for j, q in enumerate(S):
            if i != j:
                x = (x * pow(q, exps[j], m)) % m
        vals.append(x)
    return tuple(vals)


def weak(S, exps):
    return image_tuple(S, exps) == tuple(1 % (p - 1) for p in S)


def primitive_direct(S, exps):
    if not weak(S, exps):
        return False
    g = 0
    for e in exps:
        g = gcd(g, e)
    for f in divisors(g):
        if f >= 2 and weak(S, tuple(e // f for e in exps)):
            return False
    return True


def coordinate_periods(S):
    periods = []
    for j, q in enumerate(S):
        P = 1
        for i, p in enumerate(S):
            if i == j:
                continue
            P = lcm(P, multiplicative_order(q, p - 1))
        periods.append(P)
    return tuple(periods)


def lattice_index(S):
    periods = coordinate_periods(S)
    images = set()
    for exps0 in product(*[range(P) for P in periods]):
        images.add(image_tuple(S, exps0))
    return len(images), periods


def two_prime_prediction(S, exps):
    p, q = S
    a, b = exps
    u = multiplicative_order(p, q - 1)
    v = multiplicative_order(q, p - 1)
    is_w = (a % u == 0 and b % v == 0)
    is_prim = is_w and gcd(a // u, b // v) == 1
    return is_w, is_prim, u, v


def count_height(S, L):
    logs = [log(p) for p in S]
    maxes = [int(L // a) for a in logs]
    W = P = 0
    for exps in product(*[range(1, M + 1) for M in maxes]):
        if sum(e * a for e, a in zip(exps, logs)) > L + 1e-12:
            continue
        if weak(S, exps):
            W += 1
            if primitive_direct(S, exps):
                P += 1
    return W, P


def main():
    supports = [(3, 5), (5, 13), (3, 11, 17), (5, 13, 17), (7, 13, 19)]
    print("Fixed-support exact grid checks")
    total_points = 0
    total_weak = 0
    total_primitive = 0
    mismatches = 0

    for S in supports:
        assert admissible(S), S
        max_e = 18 if len(S) == 2 else 8
        index, periods = lattice_index(S)
        w = pr = 0
        local_mis = 0
        for exps in product(range(1, max_e + 1), repeat=len(S)):
            total_points += 1
            is_w = weak(S, exps)
            is_p = primitive_direct(S, exps)
            w += is_w
            pr += is_p
            if len(S) == 2:
                pw, pp, u, v = two_prime_prediction(S, exps)
                if (is_w, is_p) != (pw, pp):
                    local_mis += 1
        total_weak += w
        total_primitive += pr
        mismatches += local_mis
        check = str(local_mis) if len(S) == 2 else "not_applicable"
        print(f"S={S} max_exp={max_e} index={index} periods={periods} "
              f"weak={w} primitive={pr} two_prime_mismatches={check}")

    print(f"grid_points={total_points} weak={total_weak} primitive={total_primitive} mismatches={mismatches}")

    print("\nHeight-count checks")
    zeta2_inv = 6.0 / (pi * pi)
    zeta3_inv = 0.8319073725807075  # 1/zeta(3), for comparison only
    for S, limits, target in [
        ((3, 5), (30, 60, 120), zeta2_inv),
        ((3, 11, 17), (30, 45, 60), zeta3_inv),
    ]:
        index, _ = lattice_index(S)
        denom_const = 1.0
        for p in S:
            denom_const *= log(p)
        s = len(S)
        factorial = 1
        for j in range(2, s + 1):
            factorial *= j
        for L in limits:
            W, P = count_height(S, L)
            leading = L ** s / (factorial * index * denom_const)
            ratio = P / W if W else float('nan')
            print(f"S={S} L={L} W={W} P={P} W/leading={W/leading:.6f} "
                  f"P/W={ratio:.6f} target={target:.6f}")


if __name__ == "__main__":
    main()
