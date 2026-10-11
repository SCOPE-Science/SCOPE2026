"""Exact finite-case checks for Boolean-halfspace concentration projections.

The infinite-family theorem is proved analytically; these tests are not a substitute.
Uses only the Python standard library.
"""
import itertools
import math
import random

PRIME = 1000003


def popcount(mask):
    return mask.bit_count()


def rank_mod_p(matrix, p=PRIME):
    if not matrix:
        return 0
    a = [[v % p for v in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((j for j in range(rank, rows) if a[j][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        for j in range(rank + 1, rows):
            if a[j][col]:
                t = a[j][col] * inv % p
                for k in range(col, cols):
                    a[j][k] = (a[j][k] - t * a[rank][k]) % p
        rank += 1
        if rank == rows:
            break
    return rank


def check_case(weights):
    n = len(weights)
    vertices = list(itertools.product((-1, 1), repeat=n))
    linear = [sum(a*x for a, x in zip(weights, vertex)) for vertex in vertices]
    if not all(linear):
        return 0
    signs = [1 if v > 0 else -1 for v in linear]
    m, M = min(map(abs, linear)), max(map(abs, linear))
    assert m >= 1 and M == sum(map(abs, weights))
    # Compute the (integer) Walsh coefficients of the threshold sign.
    coefficients = []
    for mask in range(1 << n):
        coefficients.append(sum(s * math.prod(vertex[i] for i in range(n) if mask >> i & 1)
                                for s, vertex in zip(signs, vertices)))
    assert coefficients[0] == 0
    assert all(coefficients[mask] == 0 for mask in range(1 << n)
               if popcount(mask) % 2 == 0)
    count = 0
    for L in range(n + 1):
        even = [i for i in range(1 << n) if popcount(i) <= L and popcount(i) % 2 == 0]
        odd = [i for i in range(1 << n) if popcount(i) <= L and popcount(i) % 2 == 1]
        small, big = (odd, even) if L % 2 == 0 else (even, odd)
        assert len(big) - len(small) == (math.comb(n - 1, L) if L < n else 0)
        cross = [[coefficients[r ^ c] for c in small] for r in big]
        assert rank_mod_p(cross) == len(small), (weights, L)
        # Exact positive quadratic-form witness for several test Walsh polynomials g.
        for t in range(3):
            coeff = [(-2,1,3)[(i+t)%3] for i in range(len(small))]
            gvals = [sum(z * math.prod(v[i] for i in range(n) if mask >> i & 1)
                         for z,mask in zip(coeff,small)) for v in vertices]
            q = sum(abs(l)*g*g for l,g in zip(linear,gvals))
            sq = sum(g*g for g in gvals)
            assert q >= m*sq
            assert q <= M*sq
        count += 1
    return count


def main():
    rng = random.Random(2119208)
    cases = 0
    for n in range(1, 8):
        families = [tuple(1 << j for j in range(n))]
        if n % 2:
            families.append((1,)*n)
        families += [tuple(rng.randint(1, 15) for j in range(n)) for _ in range(14)]
        for weights in families:
            cases += check_case(weights)
    assert cases > 100
    print(f'VERIFY_OK exact_cutoff_cases={cases} dimensions=1..7 rank_mod_prime={PRIME} parity_and_margin=checked')

if __name__ == '__main__':
    main()
