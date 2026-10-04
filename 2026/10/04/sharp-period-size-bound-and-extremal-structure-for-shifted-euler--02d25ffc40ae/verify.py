#!/usr/bin/env python3
import math


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def phi(n):
    if n == 1:
        return 1
    x = n
    out = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            out -= out // p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out -= out // x
    return out


def cot(n):
    return n - phi(n)


def F(n, k):
    return phi(n) + k


def get_cycle(start, k, max_steps=2000):
    seen = {}
    seq = []
    x = start
    for _ in range(max_steps):
        if x in seen:
            return seq[seen[x]:]
        seen[x] = len(seq)
        seq.append(x)
        x = F(x, k)
    raise AssertionError((start, k, 'no repeat within bound'))


def check_cycle(cyc, k):
    T = len(cyc)
    assert T >= 1
    assert len(set(cyc)) == T
    for i, x in enumerate(cyc):
        assert F(x, k) == cyc[(i + 1) % T]
    assert sum(cot(x) for x in cyc) == T * k
    M = max(cyc)
    B = T * (k - 1) + 1
    assert M <= B * B, (k, cyc, M, B * B)
    if M == B * B:
        q = B
        assert is_prime(q)
        want = [q*q - j*(k-1) for j in range(T-1, -1, -1)]
        # Rotations are equivalent; canonicalize by starting at the minimum.
        m = min(range(T), key=lambda i: cyc[i])
        rot = cyc[m:] + cyc[:m]
        assert rot == want, (k, cyc, want)
        assert all(is_prime(q*q - j*(k-1)) for j in range(1, T))
    return T, M


def verify_extremal(T, k, expected):
    q = T * (k - 1) + 1
    assert is_prime(q)
    vals = [q*q - j*(k-1) for j in range(T-1, -1, -1)]
    assert vals == expected
    assert all(is_prime(v) for v in vals[:-1])
    assert vals[-1] == q*q
    for i, v in enumerate(vals):
        assert F(v, k) == vals[(i+1) % T]
    check_cycle(vals, k)


def main():
    cycles = set()
    for k in range(2, 81):
        for start in range(1, 601):
            cyc = get_cycle(start, k)
            # canonical rotation for de-duplication
            m = min(range(len(cyc)), key=lambda i: cyc[i])
            can = tuple(cyc[m:] + cyc[:m])
            key = (k, can)
            if key in cycles:
                continue
            cycles.add(key)
            check_cycle(list(can), k)

    verify_extremal(2, 3, [23, 25])
    verify_extremal(3, 3301, [98023201, 98026501, 98029801])
    verify_extremal(4, 8401, [1129002001, 1129010401, 1129018801, 1129027201])

    print('VERIFY_OK')
    print('regression_k_max=80')
    print('regression_start_max=600')
    print('distinct_cycles_checked=' + str(len(cycles)))
    print('extremal_periods_checked=2,3,4')


if __name__ == '__main__':
    main()
