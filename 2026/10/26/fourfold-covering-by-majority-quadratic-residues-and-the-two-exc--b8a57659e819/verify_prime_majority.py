"""Exact finite checks for the stated prime-field quadratic-residue covering theorem.
Not a substitute for Cauchy--Davenport, Vosper, or the character-sum proof.
"""
from itertools import combinations


def primes_up_to(n):
    return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p**0.5) + 1))]


def sumset(A, p, h):
    s = {0}
    for _ in range(h):
        s = {(x + a) % p for x in s for a in A}
    return s


exhaustive = 0
for p in (7, 11, 13, 17, 19, 23, 29, 31):
    residues = sorted({(a * a) % p for a in range(1, p)})
    threshold = (len(residues) // 2) + 1
    target = 6 if p == 7 else (5 if p == 11 else 4)
    for size in range(threshold, len(residues) + 1):
        for A in combinations(residues, size):
            assert len(sumset(A, p, target)) == p, (p, A, target)
            exhaustive += 1

for p, A, h in ((7, (1, 2), 5), (11, (1, 3, 5), 4), (13, (1, 3, 4, 10), 3)):
    residues = {(a * a) % p for a in range(1, p)}
    assert set(A) <= residues and 2 * len(A) > len(residues)
    assert len(sumset(A, p, h)) < p
    assert len(sumset(A, p, h+1)) == p

character_checks = 0
for p in primes_up_to(127):
    if p < 7 or p % 4 != 3:
        continue
    chi = lambda x: 0 if x % p == 0 else (1 if pow(x % p, (p - 1)//2, p) == 1 else -1)
    predicted = (p - 5 - 2 * chi(2)) // 8
    assert (p - 5 - 2 * chi(2)) % 8 == 0
    for sign in (-1, 1):
        triples = sum(chi(x) == chi(x+1) == chi(x+2) == sign for x in range(p))
        assert triples == predicted, (p, sign, triples, predicted)
        character_checks += 1
    if p >= 19:
        target_length = (p - 3)//4 + 1
        Q = {(x*x) % p for x in range(1, p)}
        # No progression of the critical size inside the nonzero squares.
        for a in range(p):
            for d in range(1, p):
                assert not all((a+j*d) % p in Q for j in range(target_length)), (p,a,d)

print('CERTIFICATE_OK exhaustive_majority_subsets=%d character_sign_checks=%d' % (exhaustive, character_checks))
