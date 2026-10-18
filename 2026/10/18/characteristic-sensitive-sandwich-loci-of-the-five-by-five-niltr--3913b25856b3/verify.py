#!/usr/bin/env python3
"""Finite-field checks for the reduced square-adjoint locus in n_5.

Use: python3 verify.py. No external dependencies.
Finite checks are evidence, not a proof of the arbitrary-field statements.
"""
from itertools import product

PAIRS = [(r, c) for r in range(5) for c in range(r + 1, 5)]


def field(q):
    if q == 4:
        # F_2[u]/(u^2+u+1), encoded as 0, 1, u, 1+u.
        add = lambda x, y: x ^ y
        def mul(x, y):
            v = 0
            for i in range(2):
                if (y >> i) & 1:
                    v ^= x << i
            for i in (2,):
                if v & (1 << i):
                    v ^= (1 << i) | (1 << (i-1)) | (1 << (i-2))
            return v
        neg = lambda x: x
    else:
        add = lambda x, y: (x + y) % q
        mul = lambda x, y: (x * y) % q
        neg = lambda x: (-x) % q
    return add, mul, neg


def algebraic(v, q):
    a, b, e, f, h, i, j = v
    add, mul, _ = field(q)
    # The three other coefficients c,d,g are free, so this is the core test.
    equations = (mul(a,e), add(mul(a,f),mul(b,h)), mul(e,h),
                 add(mul(e,i),mul(f,j)), mul(h,j))
    if q % 2:
        equations += (mul(a,h),mul(a,i),mul(a,j),mul(b,j),mul(e,j))
    return all(x == 0 for x in equations)


def geometric(v, q):
    a, b, e, f, h, i, j = v
    add, mul, _ = field(q)
    if q % 2 == 0:
        c1 = (e == j == 0 and add(mul(a,f),mul(b,h)) == 0)
        c2 = (a == h == 0 and add(mul(e,i),mul(f,j)) == 0)
        c3 = (e == f == h == 0)
        return c1 or c2 or c3
    return (a == b == e == j == 0 or
            a == h == e == j == 0 or
            a == h == i == j == 0 or
            e == f == h == i == j == 0 or
            a == b == e == f == h == 0)


def operator_square_zero(v10, q):
    add, mul, neg = field(q)
    x = dict(zip(PAIRS, v10))
    rows = len(PAIRS)
    m = [[0] * rows for _ in range(rows)]
    for k, (r, t) in enumerate(PAIRS):
        for z in range(r):
            pos = PAIRS.index((z, t))
            m[pos][k] = add(m[pos][k], x.get((z, r), 0))
        for z in range(t + 1, 5):
            pos = PAIRS.index((r, z))
            m[pos][k] = add(m[pos][k], neg(x.get((t, z), 0)))
    for i in range(rows):
        for j in range(rows):
            s = 0
            for k in range(rows):
                s = add(s, mul(m[i][k], m[k][j]))
            if s != 0:
                return False
    return True


def expand(v, c=0, d=0, g=0):
    a,b,e,f,h,i,j = v
    return (a,b,c,d,e,f,g,h,i,j)


def run():
    for q in (2,3,4,5):
        good = 0
        for v in product(range(q), repeat=7):
            a = algebraic(v,q)
            g = geometric(v,q)
            assert a == g, (q, v, a, g)
            good += int(a)
        total = good * q**3
        target = 3*q**7-q**6-q**5 if q % 2 == 0 else 3*q**6-2*q**4
        assert total == target, (q, total, target)
        print('FIELD', q, 'COUNT', total, 'FORMULA', target)
    # Operator-level checks with all binary matrices and a deterministic
    # collection of higher-field matrices, independent from locus equations.
    for q in (2,3,4,5):
        if q == 2:
            candidates = product(range(q),repeat=10)
        else:
            candidates = []
            for k in range(2048):
                # Mixed radix plus a non-linear permutation of coefficients.
                seed = k*1039 + 71
                v = []
                for t in range(10):
                    seed = (1103515245*seed+12345) % (2**31)
                    v.append(seed % q)
                candidates.append(tuple(v))
        n=0
        for v10 in candidates:
            core = (v10[0],v10[1],v10[4],v10[5],v10[7],v10[8],v10[9])
            assert operator_square_zero(v10,q) == algebraic(core,q), (q,v10)
            n+=1
        print('OPERATOR',q,'CHECKED',n)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
