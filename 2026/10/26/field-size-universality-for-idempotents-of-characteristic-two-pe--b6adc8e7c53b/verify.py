"""Independent small-field enumeration and exact Gaussian-Mobius checks.

Run with Python 3: python verify.py
No external libraries or network requests are required.
"""
from collections import Counter
from itertools import product
from math import prod

PRIMITIVE = {1: 0b11, 2: 0b111, 3: 0b1011}

def make_multiplication_table(m):
    q = 1 << m
    polynomial = PRIMITIVE[m]
    table = [[0] * q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            x, y, result = a, b, 0
            while y:
                if y & 1:
                    result ^= x
                y >>= 1
                x <<= 1
                if x & q:
                    x ^= polynomial
            table[a][b] = result
    return table

def invertible(flat, n, q, mul):
    matrix = [list(flat[i*n:(i+1)*n]) for i in range(n)]
    rank = 0
    for c in range(n):
        pivot = next((i for i in range(rank, n) if matrix[i][c]), None)
        if pivot is None:
            return False
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        val = matrix[rank][c]
        inverse = next(i for i in range(1, q) if mul[val][i] == 1)
        matrix[rank] = [mul[inverse][v] for v in matrix[rank]]
        for i in range(rank+1, n):
            factor = matrix[i][c]
            if factor:
                matrix[i] = [a ^ mul[factor][b] for a, b in zip(matrix[i], matrix[rank])]
        rank += 1
    return True

def observed_distribution(n, m):
    q = 1 << m
    mul = make_multiplication_table(m)
    vectors = tuple(product(range(q), repeat=n))
    counts = Counter()
    invertibles = 0
    for flat in product(range(q), repeat=n*n):
        if not invertible(flat, n, q, mul):
            continue
        invertibles += 1
        count = 0
        for x in vectors:
            images = [0] * n
            for i in range(n):
                for j in range(n):
                    images[i] ^= mul[flat[i*n+j]][x[j]]
            if all(mul[x[i]][x[i]] == images[i] for i in range(n)):
                count += 1
        assert count >= 1 and (count & (count-1)) == 0, (n, q, count)
        counts[count-1] += 1
    expected_group_order = prod(q**n-q**i for i in range(n))
    assert invertibles == expected_group_order
    return counts, invertibles

def gaussian(n, k, q=2):
    if k<0 or k>n:
        return 0
    numerator = prod(q**n-q**i for i in range(k))
    denominator = prod(q**k-q**i for i in range(k))
    assert numerator % denominator == 0
    return numerator // denominator

def gl(n, q=2):
    return prod(q**n-q**i for i in range(n))

def exact_distribution(n):
    # Möbius inversion on the lattice of subspaces above a fixed d-space.
    out = {}
    for d in range(n+1):
        s = sum((-1)**j * 2**(j*(j-1)//2) * gaussian(n-d,j) *
                2**((d+j)*(n-d-j)) * gl(n-d-j)
                for j in range(n-d+1))
        out[2**d-1] = gaussian(n,d)*s
    assert sum(out.values()) == gl(n)
    assert all(v>=0 for v in out.values())
    return out

def test():
    for n,m in ((1,1),(1,2),(2,1),(2,2),(2,3),(3,1)):
        observed, total = observed_distribution(n, m)
        expected_base = exact_distribution(n)
        expected = {v: gl(n, 2**m)*c//gl(n) for v,c in expected_base.items()}
        assert all(gl(n, 2**m)*c % gl(n) == 0 for c in expected_base.values())
        assert {v:c for v,c in observed.items() if c} == {v:c for v,c in expected.items() if c}
        # Expected number of nonzero idempotents is one.
        assert sum(v*c for v,c in observed.items()) == total
        print(f'n={n} q={2**m} matrices={total} counts={dict(sorted(observed.items()))}')
    for n in range(1, 13):
        counts = exact_distribution(n)
        assert sum(c*(2**d-1) for d,c in enumerate(counts.values())) == gl(n)
    print('VERIFY_OK')

if __name__ == '__main__':
    test()
