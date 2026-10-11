"""Independent exact integer certificate for the six-point seed determinant."""
from itertools import permutations

SUPPORT = (0, 2, 3, 6, 7, 9)
# Phi_15(X) = X^8 - X^7 + X^5 - X^4 + X^3 - X + 1.
PHI = [1, -1, 0, 1, -1, 1, 0, -1, 1]
EXPECT = [-35, 140, -35, -35, 70, 0, 35, 105]

def determinant_cyclic():
    counts = [0] * 15
    for p in permutations(range(6)):
        inversion = sum(p[i] > p[j] for i in range(6) for j in range(i+1, 6))
        exponent = sum(SUPPORT[i] * SUPPORT[p[i]] for i in range(6)) % 15
        counts[exponent] += -1 if inversion & 1 else 1
    return counts

def modulo_phi(v):
    v = list(v)
    for k in range(len(v)-1, 7, -1):
        q = v[k]
        for j in range(9):
            v[k-8+j] -= q * PHI[j]
    return v[:8]

if __name__ == '__main__':
    remainder = modulo_phi(determinant_cyclic())
    assert remainder == EXPECT, (remainder, EXPECT)
    assert all(v % 35 == 0 for v in remainder)
    assert any(v != 0 for v in remainder)
    # Degree < deg(Phi_15) certifies the complex determinant is nonzero.
    print('SEED_IDENTITY_OK: 35*(3X^7+X^6+2X^4-X^3-X^2+4X-1)')
