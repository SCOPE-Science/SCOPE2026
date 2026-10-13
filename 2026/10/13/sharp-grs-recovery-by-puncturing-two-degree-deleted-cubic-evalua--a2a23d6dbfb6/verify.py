"""Exact finite-field regression checks for two degree-deleted cubic codes.

Uses only Python 3's standard library.  Finite tests here supplement,
but do not replace, the all-field algebraic proof in RESULT.md.
"""
from itertools import combinations
from math import comb, prod


def rank_mod(rows, p):
    a = [[v % p for v in row] for row in rows]
    if not a:
        return 0
    m, n, r = len(a), len(a[0]), 0
    for j in range(n):
        pivot = next((i for i in range(r, m) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [(v * inv) % p for v in a[r]]
        for i in range(m):
            if i != r and a[i][j]:
                v = a[i][j]
                a[i] = [(a[i][k] - v * a[r][k]) % p for k in range(n)]
        r += 1
        if r == m:
            break
    return r


def column(t, r, p):
    assert r in (1, 2)
    return (1, pow(t, 1 if r == 1 else 2, p), pow(t, 3, p))


def determinant3(a, b, c, p):
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0])) % p


def quadratic_monomials(pt, p):
    u, v, w = pt
    return (u*u % p, u*v % p, u*w % p,
            v*v % p, v*w % p, w*w % p)


def elem5(six, p):
    assert len(six) == 6
    return sum(prod(six[j] for j in range(6) if j != i)
               for i in range(6)) % p


def arc(p, values, r):
    pts = [column(x, r, p) for x in values]
    return all(determinant3(pts[i], pts[j], pts[k], p)
               for i,j,k in combinations(range(len(values)), 3))


def classify(p, values, r):
    assert 5 <= len(values) <= p and len(set(values)) == len(values)
    assert arc(p, values, r), 'MDS arc assumption not satisfied'
    table = {}
    blocks = []
    for m in range(5, len(values) + 1):
        grs = 0
        for T in combinations(values, m):
            rank = rank_mod([quadratic_monomials(column(t, r, p), p)
                             for t in T], p)
            # Rank < 6 means a quadratic passes through every projective
            # column. For a projective arc of >=5 points it is nonsingular.
            is_grs = rank < 6
            predicted = (m == 5 or (m == 6 and
                         (sum(T) % p == 0 if r == 1 else elem5(T, p) == 0)))
            assert is_grs == predicted, (p, r, T, rank, predicted)
            if is_grs:
                grs += 1
                if m == 6:
                    blocks.append(T)
        table[m] = (grs, comb(len(values), m))
    assert all(len(set(a) & set(b)) <= 4
               for a,b in combinations(blocks,2)), 'five-subset uniqueness'
    return table, blocks


def main():
    # Both puncturing-depth regimes are attained for r=1 on the same
    # integer evaluation set after changing the prime field.
    for p, expected in [(19, 1), (23, 0)]:
        counts, blocks = classify(p, tuple(range(7)), r=1)
        assert counts[5] == (21,21)
        assert counts[6] == (expected,7)
        assert counts[7] == (0,1)
        print('r1',p,'zero_sum_six',blocks,'counts',counts)
        if p == 19:
            for t in (0,1,3,4,5,6):
                x,y,z = column(t,1,p)
                assert (x*y + 14*x*z + 18*y*y + 4*y*z + z*z) % p == 0
            assert arc(p,(0,1,3,4,5,6),1)
            # Direct nonsingularity: polar symmetric matrix of the conic.
            assert determinant3((0,10,7),(10,18,2),(7,2,1),p) == 1

    # r=2 may include evaluation zero. Other choices exhibit both regimes.
    examples = [(19, (1,10,13,5,4,16,18), 1),
                (17, (0,1,2,3,4,7,11), 0)]
    for p, values, expected in examples:
        counts, blocks = classify(p, values, r=2)
        assert counts[5] == (21,21) and counts[6] == (expected,7)
        assert counts[7] == (0,1)
        print('r2',p,'e5_zero_six',blocks,'counts',counts)

    # Independent exhaustive 5-, 6- and 7-set census over small primes:
    expected = {
       (11,2): {5:(212,212), 6:(5,77), 7:(0,5)},
       (11,1): {5:(112,112), 6:(7,7), 7:(0,0)},
       (13,2): {5:(639,639), 6:(24,360), 7:(0,72)},
       (13,1): {5:(432,432), 6:(36,108), 7:(0,0)},
    }
    for (p,r), want in expected.items():
        tally = {}
        for n in (5,6,7):
            feasible, grs = 0, 0
            for T in combinations(range(p), n):
                if not arc(p, T, r):
                    continue
                feasible += 1
                rank = rank_mod([quadratic_monomials(column(t,r,p),p)
                                 for t in T],p)
                good = rank < 6
                pred = n == 5 or (n == 6 and
                      (sum(T)%p==0 if r==1 else elem5(T,p)==0))
                assert good == pred, (p,r,T)
                grs += int(good)
            tally[n] = (grs,feasible)
        assert tally == want, (p,r,tally,want)
        print('ALL_MDS_SUBSETS',p,r,tally)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
