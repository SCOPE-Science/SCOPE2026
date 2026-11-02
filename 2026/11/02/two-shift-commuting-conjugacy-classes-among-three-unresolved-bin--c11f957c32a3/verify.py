"""Finite reproducibility checks for a conjugacy classification of three binary cellular automata.

The all-configuration assertions in the accompanying proof rest on local algebraic
identities, which the checker exhaustively tests over their complete finite supports.
"""
from itertools import product


def add(*args):
    v = 0
    for a in args:
        v ^= a
    return v


def local_a(a, b, c, d, e):
    return add(b, c, (a ^ b) & add(c & d, (c ^ d ^ 1) & e))


def local_b(a, b, c, d, e):
    return add(b, c, a & (c ^ 1) & d, b & (d ^ 1) & e)


def local_c(a, b, c, d, e):
    return add(b, (a ^ b) & add(c & d, c & e, c, d & e), c & (d ^ e), d & e)


def local_p(a, b, c, d):
    return b ^ (a & (c ^ 1) & d)


def local_p_inverse(a, b, c, d):
    return b ^ (a & (c ^ 1) & d)


def apply(x, offsets, local):
    n = len(x)
    return tuple(local(*(x[(i + off) % n] for off in offsets)) for i in range(n))


def d(x):
    return apply(x, (0, 1), lambda a, b: a ^ b)


def p(x):
    return apply(x, (0, 1, 2, 3), local_p)


def p_inverse(x):
    return apply(x, (-2, -1, 0, 1), local_p_inverse)


def f(x, local):
    return apply(x, (0, 1, 2, 3, 4), local)


def periodic_cycles(local, n):
    states = list(product((0, 1), repeat=n))
    nxt = {x: f(x, local) for x in states}
    found = set()
    cycles = []
    for x in states:
        if x in found:
            continue
        trail = []
        index = {}
        while x not in found and x not in index:
            index[x] = len(trail)
            trail.append(x)
            x = nxt[x]
        if x in index:
            cycles.append(trail[index[x]:])
        found.update(trail)
    return cycles


def check():
    # Every possible five-bit input, with the two exact local factorizations.
    for x in product((0, 1), repeat=5):
        a, b, c, d_, e = x
        z = (a ^ b, b ^ c, c ^ d_, d_ ^ e)
        assert local_a(*x) == local_p(*z)
        assert local_b(*x) == local_p(a, b, c, d_) ^ local_p(b, c, d_, e)
    print('32/32 five-bit contexts: both local factorizations verified')

    # The inverse identities have support [-2,+4] at most, so seven bits suffice.
    for x in product((0, 1), repeat=7):
        # At center i=2, sites 0..6 support P^{-1}P and Q^{-1}Q.
        assert p_inverse(p(x))[2] == x[2]
        assert p(p_inverse(x))[2] == x[2]
    print('128/128 seven-bit contexts: P two-sided local inverse verified')

    # Additional independent periodic-ring tests include all small rings.
    for n in range(1, 9):
        for x in product((0, 1), repeat=n):
            assert p_inverse(p(x)) == p(p_inverse(x)) == x
            assert f(x, local_a) == p(d(x))
            assert f(x, local_b) == d(p(x))
            assert f(p(x), local_a) == p(f(x, local_b))
    print('periodic-ring conjugacy/factorization/invertibility: lengths 1..8 verified')

    for label, rule, expected_lengths, expected_fixed_fifth in (
        ('A', local_a, [1, 10], 1),
        ('B', local_b, [1, 10], 1),
        ('C', local_c, [1, 5], 6),
    ):
        cycles = periodic_cycles(rule, 5)
        lengths = sorted(len(cycle) for cycle in cycles)
        assert lengths == expected_lengths, (label, lengths)
        count_fifth = sum(1 for cycle in cycles if 5 % len(cycle) == 0 for _ in cycle)
        assert count_fifth == expected_fixed_fifth
        print(f'period-five spatial ring, {label}: temporal cycle lengths {lengths}; '
              f'fixed by time-five = {count_fifth}')
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
