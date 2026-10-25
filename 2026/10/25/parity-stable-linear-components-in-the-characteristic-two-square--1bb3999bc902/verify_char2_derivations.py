#!/usr/bin/env python3
"""Direct exhaustive check of square-zero derivations on truncated polynomial rings."""
from itertools import product


def multiply(x, y, q):
    if q == 2:
        return x & y
    assert q == 4
    p = 0
    if y & 1:
        p ^= x
    if y & 2:
        p ^= x << 1
    if p & 8:
        p ^= 0b1100
    if p & 4:
        p ^= 0b111
    return p


def dd(g, f, n, q):
    # Derivation of a polynomial with generator image f; q has characteristic 2.
    output = [0] * n
    for k in range(1, n, 2):
        if not g[k]:
            continue
        for j in range(n-k+1):
            output[j + k - 1] ^= multiply(g[k], f[j], q)
    return tuple(output)


def rank(columns, n, q):
    rows = [[v[i] for v in columns] for i in range(n)]
    row = 0
    for col in range(len(columns)):
        pi = next((i for i in range(row, n) if rows[i][col]), None)
        if pi is None:
            continue
        rows[row], rows[pi] = rows[pi], rows[row]
        pivot = rows[row][col]
        inv = next(x for x in range(1, q) if multiply(pivot, x, q) == 1)
        rows[row] = [multiply(inv, a, q) for a in rows[row]]
        for i in range(n):
            if i != row and rows[i][col]:
                c = rows[i][col]
                rows[i] = [v ^ multiply(c, w, q) for v, w in zip(rows[i], rows[row])]
        row += 1
        if row == n:
            break
    return row


def testcase(m, q):
    c = (m + 1) // 2
    predicted = q**m + (m//2)*(q-1)*q**(m-1)
    for n in (2*m, 2*m+1):
        observed = [0] * (m+1)
        acyclic = 0
        for ab in product(range(q), repeat=2*m):
            a, b = ab[:m], ab[m:]
            f = [0]*n
            for i in range(m):
                f[2*i+(n%2)*2] = a[i] if 2*i+(n%2)*2 < n else 0
                f[2*i+1] = b[i]
            z = tuple(0 for _ in range(n))
            cols = [dd(tuple(1 if j == k else 0 for j in range(n)),f,n,q) for k in range(n)]
            squarezero = all(dd(v, f, n, q) == z for v in cols)
            component = any(all(a[i] == 0 for i in range(m-j)) and
                            all(b[i] == 0 for i in range(j)) for j in range(c,m+1))
            assert squarezero == component, (n,q,ab)
            if squarezero:
                rr = rank(cols,n,q)
                ord_a = next((i for i in range(m) if a[i]),m)
                ord_b = next((i for i in range(m) if b[i]),m)
                assert rr == m-min(ord_a,ord_b), (n,q,ab,rr)
                observed[rr] += 1
                if n % 2 == 0 and rr == m:
                    acyclic += 1
        assert sum(observed) == predicted, (n,q,observed,predicted)
        if n % 2 == 0:
            assert acyclic == (q-1)*q**(m-1)
        print(f'PASS n={n} q={q} components={m-c+1} points={predicted} ranks={observed} acyclic={acyclic}')


if __name__ == '__main__':
    for m in range(1,6):
        testcase(m,2)
    for m in range(1,4):
        testcase(m,4)
    print('CHAR2_DERIVATION_SQUARE_ZERO_OK')
