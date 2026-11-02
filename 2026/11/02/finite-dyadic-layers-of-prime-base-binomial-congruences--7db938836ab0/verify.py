#!/usr/bin/env python3
"""Exact, dependency-free arithmetic checks for the four initial dyadic layers."""
from math import comb

def isprime(n):
    if n < 2: return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0: return False
    return True

def digit_sum(n, base):
    result = 0
    while n:
        result += n % base
        n //= base
    return result

def vp_factorial(n, p):
    out = 0
    while n:
        n //= p
        out += n
    return out

expected = {1: [], 2: [36], 3: [], 4: [400]}
expected_cells = {
    1: [],
    2: [(3, 1, 0), (3, 2, 1)],
    3: [(3, 1, 4), (3, 2, 5), (5, 1, 2), (7, 1, 0), (7, 2, 6)],
    4: [(3, 1, 4), (3, 2, 13), (5, 1, 10), (5, 2, 1), (7, 1, 8), (7, 2, 6), (11, 1, 8), (13, 1, 8)],
}
count = 0
for e in range(1, 5):
    cells, solutions = [], []
    for q in range(3, 2**e):
        if not isprime(q): continue
        maximum = digit_sum((q-1)*2**e, q)//(q-1)
        for t in range(1, maximum+1):
            n = 2**e*q**t
            residue = comb(q*n, n) % (2**e)
            cells.append((q, t, residue))
            # Independently check exact full modulus, not just the 2-adic projection.
            if comb(q*n, n) % n == pow(q, n, n):
                solutions.append(n)
            count += 1
    assert cells == expected_cells[e], (e, cells)
    assert solutions == expected[e], (e, solutions)

for q in range(3, 200, 2):
    h = (q - 1) & -(q - 1)
    assert q & h and q*(q-1) & h
    assert q & (q*(q-1))
    assert comb(q*q, q) % 2 == 0

for q in (3,5,7,11):
    for e in range(1, 5):
        for t in range(1, 4):
            n = q**t * 2**e
            left = vp_factorial(q*n,q)-vp_factorial(n,q)-vp_factorial((q-1)*n,q)
            right = digit_sum((q-1)*2**e,q)//(q-1)
            assert left==right, (q,e,t,left,right)

print('VERIFY_OK dyadic_layers=1..4 exact_candidate_cells=%s first_layers=%s carry_and_valuation=PASS finite_only=YES' % (count, expected))
