#!/usr/bin/env python3
"""Independent finite checks of the sunlet partial Petrial rank enumerator.
Standard library only. All matrices are over the field with two elements.
"""
from collections import Counter


def rank2(rows, size):
    rows = list(rows)
    pivot = 0
    for col in range(size):
        chosen = next((i for i in range(pivot, size) if rows[i] & (1 << col)), None)
        if chosen is None:
            continue
        rows[pivot], rows[chosen] = rows[chosen], rows[pivot]
        for j in range(pivot + 1, size):
            if rows[j] & (1 << col):
                rows[j] ^= rows[pivot]
        pivot += 1
    return pivot


def direct_sunlet(n):
    size = 2 * n
    rows = []
    for i in range(n):
        rows.append((1 << ((i-1) % n)) | (1 << ((i+1) % n)) | (1 << (n+i)))
    for i in range(n):
        rows.append(1 << i)
    counts = Counter()
    for mask in range(1 << size):
        mrows = [rows[i] ^ ((mask & (1 << i))) for i in range(size)]
        counts[size - rank2(mrows, size)] += 1
    return dict(counts)


def reduced_sunlet(n):
    """Independent Schur-block enumeration over the retained cycle vertices."""
    counts = Counter()
    for retained_mask in range(1 << n):
        retained = [i for i in range(n) if (retained_mask >> i) & 1]
        local = {v: j for j, v in enumerate(retained)}
        m = len(retained)
        base = [sum(1 << local[j] for j in ((i-1) % n, (i+1) % n) if j in local)
                for i in retained]
        for diag in range(1 << m):
            rows = [base[i] ^ (diag & (1 << i)) for i in range(m)]
            counts[m - rank2(rows, m)] += 1 << (n - m)
    return dict(counts)


def add(a, b):
    z = Counter(a)
    for k, value in b.items():
        z[k] += value
    return dict(z)


def mul(a, b):
    z = Counter()
    for i, x in a.items():
        for j, y in b.items():
            z[i+j] += x * y
    return dict(z)


def formula_sunlet(limit):
    """Compute coefficients of the theorem's rational ordinary generating function."""
    h = [{} for _ in range(limit+1)]
    # F_l=(2^l-J_l)+J_l u; G_k=2^k, k>=1; H=F G.
    for n in range(2, limit+1):
        q = Counter()
        for l in range(1, n):
            j = (2**l - (-1)**l) // 3
            q[0] += 2**(n-l) * (2**l-j)
            q[1] += 2**(n-l) * j
        h[n] = dict(q)
    q = [{0: 1}] + [{} for _ in range(limit)]
    # 1/(1-H)=Q. Then tH'Q has coefficient R_n=sum_k k H_k Q_{n-k}.
    for n in range(1, limit+1):
        acc = {}
        for k in range(1, n+1):
            acc = add(acc, mul(h[k], q[n-k]))
        q[n] = acc
    profiles = {}
    for n in range(3, limit+1):
        r = {}
        for k in range(1, n+1):
            r = add(r, {i: k*v for i,v in mul(h[k],q[n-k]).items()})
        cn = {0: (2**n - (-1)**n)//3,
              1: 2**(n-1),
              2: (2**(n-1)+(-1)**n)//3}
        profiles[n] = add(add({0: 2**n}, cn), r)
    return profiles


def run():
    profiles = formula_sunlet(12)
    direct_total = 0
    for n in range(3,9):
        actual = direct_sunlet(n)
        direct_total += 4**n
        assert actual == profiles[n], (n, actual, profiles[n])
        assert sum(actual.values()) == 4**n
        print('DIRECT_OK', n, sorted(actual.items()))
    for n in range(3,11):
        actual = reduced_sunlet(n)
        assert actual == profiles[n], (n, actual, profiles[n])
        print('REDUCED_OK', n)
    for n, coeffs in profiles.items():
        assert sum(coeffs.values()) == 4**n
        assert max(coeffs) == (2 if n == 3 else n//2)
    print('RATIONAL_PROFILE_OK', 3, 12)
    print('DIRECT_DIAGONAL_ASSIGNMENTS', direct_total)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
