#!/usr/bin/env python3
"""Independent exact arithmetic checks for a four-prime smooth modulus family.
No external Python packages are required. The infinite assertion additionally
uses the Frattini reduction proved in RESULT.md.
"""
from math import gcd
from itertools import product

PRIMES = (2, 3, 5, 7)
VALUES = (11, 13, 17, 19, 23)

def rank_mod(mat, p):
    if not mat:
        return 0
    A = [[x % p for x in row] for row in mat]
    h, w = len(A), len(A[0])
    r = 0
    for j in range(w):
        i = next((i for i in range(r, h) if A[i][j] != 0), None)
        if i is None:
            continue
        A[r], A[i] = A[i], A[r]
        inv = pow(A[r][j], -1, p)
        A[r] = [x * inv % p for x in A[r]]
        for k in range(h):
            if k != r:
                t = A[k][j]
                A[k] = [(x - t*y) % p for x, y in zip(A[k], A[r])]
        r += 1
        if r == h:
            break
    return r

def phi(n):
    out = n
    for p in PRIMES:
        if n % p == 0:
            out = out // p * (p - 1)
    return out

def log_table(base, prime):
    modulus = prime * prime
    order = prime * (prime - 1)
    powers = {pow(base, j, modulus): j for j in range(order)}
    assert len(powers) == order
    return powers

LOGS = {3: log_table(2, 3), 5: log_table(2, 5), 7: log_table(3, 7)}

def local_vector(x, a, b, c, d, ell):
    row = []
    if ell == 2:
        if a >= 2:
            row.append(int(x % 4 == 3))
        if a >= 3:
            row.append(int(x % 8 in (3, 5)))
    for p, e in ((3,b), (5,c), (7,d)):
        if ell == 2 or (ell == p and e >= 2) or (p == 7 and ell == 3):
            row.append(LOGS[p][x % (p*p)] % ell)
    return row

def verify_ranks(a, b, c, d):
    xs = [x for x in VALUES if x <= (19 if a <= 2 else 23)]
    for ell in (2,3,5,7):
        mat = [local_vector(x,a,b,c,d,ell) for x in xs]
        expected = len(mat[0])
        assert rank_mod(mat, ell) == expected, (a,b,c,d,ell,mat)

def subgroup_order(n, limit):
    # Closure via adding a generator to an existing subgroup; exact group ops.
    S = {1}
    for x in range(2, limit + 1):
        if gcd(x,n) != 1:
            continue
        # Multiply coset powers until the original subgroup reappears.
        old = list(S)
        y = x % n
        while y not in S:
            S.update((y*z) % n for z in old)
            y = (y*x) % n
    return len(S)

def main():
    for a,b,c,d in product((1,2,3),(1,2),(1,2),(1,2)):
        verify_ranks(a,b,c,d)
    print('CRT_FOUR_PRIME_RANK_CASES=24 PASS')
    for a,bound,before in ((1,19,17),(2,19,17),(3,23,19)):
        n = 2**a*3**2*5**2*7**2
        expected = phi(n)
        upper = subgroup_order(n,bound)
        lower = subgroup_order(n,before)
        assert upper == expected and lower < expected, (n,upper,lower,expected)
        print(f'n={n} phi={expected} before={before}:{lower} target={bound}:{upper}')
    for a,bound,before in ((1,19,17),(2,19,17),(3,23,19)):
        n=2**a*3*5*7
        expected=phi(n)
        assert subgroup_order(n,bound) == expected
        assert subgroup_order(n,before) < expected
        print(f'squarefree_odd_n={n} phi={expected} PASS')
    assert [LOGS[3][z%9] for z in VALUES] == [1,2,3,0,5]
    assert [LOGS[5][z%25] for z in VALUES] == [16,19,13,18,11]
    assert [LOGS[7][z%49] for z in VALUES] == [40,33,25,35,38]
    print('DISCRETE_LOG_TABLES PASS')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
