"""Independent finite enumeration of Leibniz endomorphism and retraction ranks.

The algebra has basis u,v,w_1,...,w_r and sole nonzero bracket [v,u]=u.
Brute-force checks use prime fields; the symbolic count is valid for all finite fields.
Run with: python verify.py
"""
from itertools import product
from math import prod


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))


def rank_maps(rows, cols, k, q):
    if k < 0 or k > min(rows, cols):
        return 0
    return gaussian(rows, k, q) * prod(q**cols-q**i for i in range(k))


def rank_idempotents(n, k, q):
    return gaussian(n, k, q) * q**(k*(n-k))


def predicted(n, q):
    assert n >= 2 and q >= 2
    r = n-2
    m = n-1
    e = [0]*(n+1)
    j = [0]*(n+1)
    for k in range(m+1):
        e[k] += 2*rank_maps(m, m, k, q)
        j[k] += rank_idempotents(m, k, q)
    for k in range(r+1):
        e[k] -= rank_maps(r, m, k, q)
        e[k+2] += (q-1)*q**r*rank_maps(r, r, k, q)
        j[k] += rank_idempotents(r, k, q)*(q**(2*k)-q**k)
        j[k+2] += rank_idempotents(r, k, q)*q**(r-k)
    return e, j


def row_rank(a, p):
    rows = [list(row) for row in a]
    i = 0
    for col in range(len(rows[0])):
        pivot = next((k for k in range(i, len(rows)) if rows[k][col] % p), None)
        if pivot is None:
            continue
        rows[i], rows[pivot] = rows[pivot], rows[i]
        inv = pow(rows[i][col], -1, p)
        rows[i] = [(x*inv) % p for x in rows[i]]
        for k in range(len(rows)):
            if k != i:
                factor = rows[k][col]
                rows[k] = [(x-factor*y) % p for x, y in zip(rows[k], rows[i])]
        i += 1
        if i == len(rows):
            break
    return i


def independent_census(n, p):
    """Enumerate all linear maps, testing preservation of every basis bracket."""
    assert p in (2, 3, 5, 7)  # prime-field arithmetic
    end = [0]*(n+1)
    idem = [0]*(n+1)
    for entries in product(range(p), repeat=n*n):
        columns = [entries[i*n:(i+1)*n] for i in range(n)]
        valid = True
        for x in range(n):
            for y in range(n):
                left = columns[0] if (x, y) == (1, 0) else (0,)*n
                right0 = columns[x][1]*columns[y][0] % p
                for h in range(n):
                    if left[h] != (right0 if h == 0 else 0):
                        valid = False
                        break
                if not valid:
                    break
            if not valid:
                break
        if not valid:
            continue
        rank = row_rank([[columns[j][i] for j in range(n)] for i in range(n)], p)
        end[rank] += 1
        square_is_self = all(
            sum(columns[j][h]*columns[h][i] for h in range(n)) % p == columns[j][i]
            for j in range(n) for i in range(n)
        )
        if square_is_self:
            idem[rank] += 1
    return end, idem


def main():
    cases = ((2, 2), (2, 3), (2, 5), (3, 2), (3, 3), (4, 2))
    for n, q in cases:
        predicted_end, predicted_idem = predicted(n, q)
        brute_end, brute_idem = independent_census(n, q)
        assert predicted_end == brute_end, (n, q, 'endomorphism', predicted_end, brute_end)
        assert predicted_idem == brute_idem, (n, q, 'idempotent', predicted_idem, brute_idem)
        r = n-2
        expected_total = 2*q**((n-1)**2)+(q-2)*q**((n-2)*(n-1))
        expected_aut = (q-1)*q**r*prod(q**r-q**i for i in range(r))
        assert sum(predicted_end) == expected_total
        assert predicted_end[n] == expected_aut
        print(f'n={n}, q={q}: endomorphism ranks={predicted_end}, idempotent ranks={predicted_idem}')
    # Check symbolic formulas beyond the feasible exhaustive search range.
    for q in (2, 3, 4, 5, 7, 9):
        for n in (2, 3, 5, 8, 12):
            end, idem = predicted(n, q)
            r = n-2
            assert all(x >= 0 for x in end+idem)
            assert sum(end) == 2*q**((n-1)**2)+(q-2)*q**((n-2)*(n-1))
            assert end[n] == (q-1)*q**r*prod(q**r-q**i for i in range(r))
            assert idem[n] == 1
    print('VERIFY_OK: 6 exhaustive prime-field cases and 30 algebraic consistency cases')


if __name__ == '__main__':
    main()
