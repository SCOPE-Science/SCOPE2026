#!/usr/bin/env python3
"""Independent exact finite checks for neighbor-XOR dynamics on Möbius ladders."""
from collections import Counter, deque
from math import gcd


def deg(a):
    return a.bit_length() - 1


def remainder(a, b):
    db = deg(b)
    while a and deg(a) >= db:
        a ^= b << (deg(a) - db)
    return a


def polynomial_gcd(a, b):
    while b:
        a, b = b, remainder(a, b)
    return a


def cyclic_product(a, b, degree):
    acc = 0
    while b:
        low = b & -b
        acc ^= a << (low.bit_length() - 1)
        b ^= low
    mask = (1 << degree) - 1
    return (acc & mask) ^ (acc >> degree)


def cyclic_power(a, power, degree):
    value = 1
    while power:
        if power & 1:
            value = cyclic_product(value, a, degree)
        a = cyclic_product(a, a, degree)
        power >>= 1
    return value


def update(x, n):
    degree = 2 * n
    mask = (1 << degree) - 1
    return (((x << 1) | (x >> (degree - 1))) ^
            ((x >> 1) | ((x & 1) << (degree - 1))) ^
            ((x << n) | (x >> n))) & mask


def prism_update(x, n):
    mask = (1 << n) - 1
    left, right = x & mask, (x >> n) & mask
    def ring_neighbors(y):
        return (((y << 1) | (y >> (n - 1))) ^
                ((y >> 1) | ((y & 1) << (n - 1)))) & mask
    return (ring_neighbors(left) ^ right) | ((ring_neighbors(right) ^ left) << n)


def predicted_prism_kernel(n, t):
    if n % 3:
        return 0
    e = n & -n
    if e == 1:
        return 0 if t == 0 else (2 if t == 1 else 4)
    return 4 * min(t, e)


def prism_comparison_checks():
    checked = 0
    for n in range(3, 49):
        dimension = 2 * n
        cols = [1 << i for i in range(dimension)]
        e = n & -n
        for t in range(1, max(5, 2 * e + 2) + 1):
            cols = [prism_update(c, n) for c in cols]
            nullity = dimension - gf2_rank(cols)
            assert nullity == predicted_prism_kernel(n, t), (n, t, nullity)
            checked += 1
    return checked


def gf2_rank(columns):
    pivots = {}
    for c in columns:
        while c:
            p = c.bit_length() - 1
            if p in pivots:
                c ^= pivots[p]
            else:
                pivots[p] = c
                break
    return len(pivots)


def polynomial_fixed_dimension(n, t):
    degree = 2 * n
    q = (1 << (n + 1)) | (1 << 2) | 1
    f = cyclic_product(q, 1 << (degree - 1), degree)
    f_t_plus_one = cyclic_power(f, t, degree) ^ 1
    return deg(polynomial_gcd((1 << degree) | 1, f_t_plus_one))


def max_tail(n):
    e = n & -n
    if n % 3:
        return 0
    return 1 if e == 1 else 2 * e


def predicted_kernel_dim(n, t):
    if n % 3:
        return 0
    if n & 1:
        return 0 if t == 0 else 4
    return 2 * min(t, 2 * (n & -n))


def predicted_fixed_dim(n):
    return 1 if n & 1 else (3 if n % 4 == 2 else 2)


def linear_checks():
    cases = 0
    for n in range(3, 49):
        dimension = 2 * n
        cols = [1 << i for i in range(dimension)]
        limit = max(24, max_tail(n) + 3)
        for t in range(1, limit + 1):
            cols = [update(c, n) for c in cols]
            actual_kernel = dimension - gf2_rank(cols)
            if n % 3 == 0:
                assert actual_kernel == predicted_kernel_dim(n, t), (n, t, actual_kernel)
            else:
                assert actual_kernel == 0, (n, t, actual_kernel)
            if t <= 16:
                for_fixed = [cols[i] ^ (1 << i) for i in range(dimension)]
                actual_fixed = dimension - gf2_rank(for_fixed)
                expected_fixed = polynomial_fixed_dimension(n, t)
                assert actual_fixed == expected_fixed, (n, t, actual_fixed, expected_fixed)
                if t == 1:
                    assert actual_fixed == predicted_fixed_dim(n), (n, actual_fixed)
            cases += 1
    return cases


def exact_state_checks():
    examined = 0
    for n in range(3, 9):
        total = 1 << (2 * n)
        successors = [update(x, n) for x in range(total)]
        indegrees = [0] * total
        for nxt in successors:
            indegrees[nxt] += 1
        queue = deque(i for i in range(total) if indegrees[i] == 0)
        peel_order = []
        while queue:
            u = queue.popleft()
            peel_order.append(u)
            v = successors[u]
            indegrees[v] -= 1
            if indegrees[v] == 0:
                queue.append(v)
        entry = [0] * total
        for u in reversed(peel_order):
            entry[u] = entry[successors[u]] + 1
        hist = Counter(entry)
        e = n & -n
        if n % 3:
            assert hist == {0: total}, (n, hist)
        elif n & 1:
            recurring = 1 << (2 * n - 4)
            assert hist == {0: recurring, 1: 15 * recurring}, (n, hist)
        else:
            recurring = 1 << (2 * n - 4 * e)
            wanted = {0: recurring}
            for t in range(1, 2 * e + 1):
                wanted[t] = 3 * recurring * (4 ** (t - 1))
            assert hist == wanted, (n, hist, wanted)
        expected_fixed = 1 << predicted_fixed_dim(n)
        fixed = sum(successors[x] == x for x in range(total))
        assert fixed == expected_fixed, (n, fixed, expected_fixed)
        examined += total
    return examined


def main():
    linear = linear_checks()
    states = exact_state_checks()
    prism = prism_comparison_checks()
    print('MOBIUS_XOR_EXACT_CHECKS_PASS')
    print('matrix_kernel_and_gcd_cases:', linear)
    print('independently_classified_binary_states:', states)
    print('prism_comparison_matrix_cases:', prism)
    print('graph_half_lengths_matrix_checked: 3..48')
    print('graph_half_lengths_exhaustive_states: 3..8')
    print('every_test: PASS')


if __name__ == '__main__':
    main()
