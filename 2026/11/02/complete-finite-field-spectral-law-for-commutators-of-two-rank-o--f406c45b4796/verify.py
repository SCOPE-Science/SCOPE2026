"""Exhaustive finite-field checks for a rank-one commutator spectral enumeration.

Run: python verify.py
No dependencies beyond Python 3. The field of four elements is F_2[z]/(z^2+z+1).
"""
from collections import Counter
from itertools import product


def field(q):
    if q not in (2, 3, 4, 5):
        raise ValueError('Supported verification fields: 2,3,4,5')
    def add(a, b):
        return (a ^ b) if q == 4 else (a + b) % q
    def neg(a):
        return a if q == 4 else (-a) % q
    def mul(a, b):
        if q != 4:
            return (a * b) % q
        prod = 0
        for i in range(2):
            for j in range(2):
                prod ^= (((a >> i) & 1) & ((b >> j) & 1)) << (i + j)
        if prod & 8:
            prod ^= 14
        if prod & 4:
            prod ^= 7
        return prod
    return add, neg, mul


def dot(x, y, f):
    add, _, mul = f
    ans = 0
    for a, b in zip(x, y):
        ans = add(ans, mul(a, b))
    return ans


def all_rank_one(q, n, f):
    _, _, mul = f
    v = [p for p in product(range(q), repeat=n) if any(p)]
    u = []
    for p in v:
        first = next(x for x in p if x)
        inv = next(a for a in range(1, q) if mul(first, a) == 1)
        if tuple(mul(inv, x) for x in p) == p:
            u.append(p)
    ans = [(x, y) for x in u for y in v]
    assert len(ans) == (q**n-1)**2 // (q-1)
    return ans


def commutator(x, y, n, f):
    add, neg, mul = f
    u, v = x
    s, t = y
    a, b = dot(v, s, f), dot(t, u, f)
    return [[add(mul(a, mul(u[i], t[j])), neg(mul(b, mul(s[i], v[j]))))
             for j in range(n)] for i in range(n)]


def mm(A, B, f):
    add, _, mul = f
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = add(result[i][j], mul(A[i][k], B[k][j]))
    return result


def matrix_rank(M, q, f):
    add, neg, mul = f
    A = [row[:] for row in M]
    n = len(A)
    row = 0
    for col in range(n):
        p = next((i for i in range(row, n) if A[i][col]), None)
        if p is None:
            continue
        A[row], A[p] = A[p], A[row]
        inv = next(z for z in range(1, q) if mul(z, A[row][col]) == 1)
        A[row] = [mul(inv, a) for a in A[row]]
        for i in range(n):
            if i != row and A[i][col] != 0:
                factor = A[i][col]
                A[i] = [add(A[i][j], neg(mul(factor, A[row][j]))) for j in range(n)]
        row += 1
        if row == n:
            break
    return row


def second_char_coeff(M, f):
    add, neg, mul = f
    n = len(M)
    answer = 0
    for i in range(n):
        for j in range(i+1, n):
            minor = add(mul(M[i][i], M[j][j]), neg(mul(M[i][j], M[j][i])))
            answer = add(answer, minor)
    return answer


def verify_case(q, n):
    f = field(q)
    add, neg, mul = f
    mats = all_rank_one(q, n, f)
    Q = len(mats)
    N0 = (q**n-1)*(q**(n-1)-1)//(q-1)
    N1 = (q**n-1)*q**(n-1)
    A = (q**(n-1)-1)**2//(q-1)
    expected_rank = {
        0: Q*A+N1*(q-1),
        2: N0*(q-1)*q**(2*n-2) + N1*(q-1)*(q**(n-1)-1)**2,
    }
    expected_rank[1] = Q**2 - expected_rank[0] - expected_rank[2]
    got_rank = Counter()
    got_delta = Counter()
    semisimple_char2 = Counter()
    # Every pair is checked using the defining commutator matrix and independent
    # Gaussian elimination. For rank two, independently compute its second
    # characteristic-polynomial coefficient through principal minors.
    for x in mats:
        u, v = x
        trace_x = dot(u, v, f)
        for y in mats:
            s, t = y
            C = commutator(x, y, n, f)
            r = matrix_rank(C, q, f)
            got_rank[r] += 1
            if r == 2:
                a, b = dot(v, s, f), dot(t, u, f)
                d = dot(s, t, f)
                prod = mul(a, b)
                Delta = mul(prod, add(prod, neg(mul(trace_x, d))))
                assert second_char_coeff(C, f) == neg(Delta)
                got_delta[Delta] += 1
                C2 = mm(C, C, f)
                if Delta == 0:
                    assert n >= 3
                    assert any(x != 0 for row in C2 for x in row)
                    assert not any(x != 0 for row in mm(C2, C, f) for x in row)
                if q in (2, 4) and Delta:
                    c = next(c for c in range(q) if mul(c, c) == Delta)
                    semi = all(C2[i][j] == mul(c, C[i][j])
                               for i in range(n) for j in range(n))
                    semisimple_char2[c, semi] += 1
            elif r == 1:
                # Every rank-one commutator has trace zero, hence square zero.
                assert not any(x != 0 for row in mm(C, C, f) for x in row)
    assert got_rank == expected_rank, (q, n, got_rank, expected_rank)
    for delta in range(q):
        h = sum(1 for c in range(1, q) if mul(c, c) == delta)
        predicted = (N1*(q-1)*(q**(n-1)-1)*(q**(n-2)-1) if delta == 0 else
                     h*N0*q**(2*n-2) + N1*(q-1)*(q**(n-1)-1)*q**(n-2))
        assert got_delta[delta] == predicted, (q, n, delta, got_delta[delta], predicted)
    if q in (2, 4):
        for c in range(1, q):
            predicted_semi = N0*q**(2*n-3)
            predicted_nonsemi = (N0*(q-1)*q**(2*n-3) +
                                 N1*(q-1)*(q**(n-1)-1)*q**(n-2))
            assert semisimple_char2[c, True] == predicted_semi
            assert semisimple_char2[c, False] == predicted_nonsemi
    print(f'PASS q={q} n={n} Q={Q} ranks={dict(got_rank)} '
          f'nonzero_delta={dict(got_delta)}')


def main():
    for q,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)]:
        verify_case(q,n)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
