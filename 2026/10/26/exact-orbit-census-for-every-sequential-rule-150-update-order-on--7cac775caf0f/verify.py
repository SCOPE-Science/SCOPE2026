"""Exact finite checks of sequential parity dynamics on rings. Python 3, stdlib only."""
from itertools import permutations
from math import gcd, lcm
import random


def one_sweep(x, n, order):
    for j in order:
        x ^= (((x >> ((j - 1) % n)) ^ (x >> ((j + 1) % n))) & 1) << j
    return x


def wall_cycles(n, order):
    # P[pos] tracks which initial wall bit arrives at the position.
    p = list(range(n))
    for j in order:
        left = (j - 1) % n
        p[left], p[j] = p[j], p[left]
    cycles, used = [], set()
    for j in range(n):
        if j not in used:
            cycle = []
            k = j
            while k not in used:
                used.add(k)
                cycle.append(k)
                k = p[k]
            cycles.append(cycle)
    return cycles


def rank2(q):
    bits = [(x << 1) | y for x, y in q]
    nonzero = {x for x in bits if x}
    return 0 if not nonzero else 1 if len(nonzero) == 1 else 2


def predicted_fixed(a, b, t):
    r, s = gcd(a, t), gcd(b, t)
    q = ((a // r % 2, b // s % 2), (t // r % 2, t // s % 2))
    return 2 ** (1 + r + s - rank2(q))


def predicted_order(a, b):
    g = gcd(a, b)
    L = lcm(a, b)
    return L if (a + b) // g % 2 == 0 else 2 * L


def mobius(k):
    value, p = 1, 2
    while p * p <= k:
        if k % p == 0:
            k //= p
            if k % p == 0:
                return 0
            value = -value
        p += 1
    return -value if k > 1 else value


def predicted_cycles(a, b, t):
    return sum(mobius(t // d) * predicted_fixed(a, b, d) for d in range(1, t + 1) if t % d == 0) // t


def direct_cycles(n, order):
    f = [one_sweep(x, n, order) for x in range(1 << n)]
    seen = set()
    census = {}
    for x in range(len(f)):
        if x in seen:
            continue
        y, duration = x, 0
        while y not in seen:
            seen.add(y)
            y = f[y]
            duration += 1
        assert y == x, "each sweep must be bijective"
        census[duration] = census.get(duration, 0) + 1
    return census


def run():
    fixed_checks = 0
    order_checks = 0
    orbit_checks = 0
    for n in range(3, 10):
        if n <= 6:
            orders = list(permutations(range(n)))
        else:
            orders = [tuple(range(n))] + [tuple(random.Random(100000 * n + k).sample(range(n), n)) for k in range(100)]
        for oi, order in enumerate(orders):
            cycles = wall_cycles(n, order)
            assert len(cycles) == 2
            a, b = (len(c) for c in cycles)
            assert a + b == n
            states = list(range(1 << n))
            images = states[:]
            for t in range(1, 2 * n + 2):
                images = [one_sweep(x, n, order) for x in images]
                assert sum(x == y for x, y in zip(states, images)) == predicted_fixed(a, b, t), (n, order, t, a, b)
                fixed_checks += 1
            global_order = predicted_order(a, b)
            for v in (1 << j for j in range(n)):
                y = v
                for _ in range(global_order):
                    y = one_sweep(y, n, order)
                assert y == v
            # Since each local gate is invertible, equality at the predicted
            # order and failure at every prime-factor quotient prove minimality.
            prime_factors = [p for p in range(2, global_order + 1) if global_order % p == 0 and all(p % d for d in range(2, int(p**0.5) + 1))]
            for p in prime_factors:
                exponent = global_order // p
                assert any((lambda v: iterated(v, n, order, exponent))(1 << j) != (1 << j) for j in range(n))
            order_checks += 1
            if n <= 7 and (n <= 6 and oi < 35 or n == 7 and oi < 10):
                empirical = direct_cycles(n, order)
                for t in range(1, global_order + 1):
                    assert empirical.get(t, 0) == predicted_cycles(a, b, t), (n, order, t)
                    orbit_checks += 1
        print("n", n, "orders", len(orders), "fixed_checks_so_far", fixed_checks)
    print("VERIFY_OK fixed_comparisons", fixed_checks, "map_order_comparisons", order_checks, "primitive_period_comparisons", orbit_checks)


def iterated(v, n, order, count):
    for _ in range(count):
        v = one_sweep(v, n, order)
    return v


if __name__ == "__main__":
    run()
