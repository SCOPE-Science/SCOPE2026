"""Reproduce finite checks for the fixed-Pauli CHSH swap-asymmetry frontier.

Run: python3 verify.py
Dependencies: Python 3 standard library only.
These tests do not replace the universal positive-semidefinite block proof.
"""
from fractions import Fraction
from math import sqrt
from random import Random

# B0 = XX + XZ - ZX + ZZ in the computational basis.
B = ((1, -1, 1, 1), (-1, -1, 1, -1),
     (1, 1, -1, 1), (1, -1, 1, 1))
SWAP = (0, 2, 1, 3)


def expectation(rho):
    return sum(B[i][j] * rho[j][i] for i in range(4) for j in range(4)).real


def swap_asymmetry(rho):
    # s=(0,1,-1,0)/sqrt(2); w=P_sym rho s.
    # The off-swap block has singular value ||w||.  Thus delta=2||w||.
    s = (0., 1 / sqrt(2), -1 / sqrt(2), 0.)
    rs = [sum(rho[i][j] * s[j] for j in range(4)) for i in range(4)]
    proj = sum(s[i] * rs[i] for i in range(4))
    w = [rs[i] - proj * s[i] for i in range(4)]
    return 2 * sqrt(max(0.0, sum(abs(x) ** 2 for x in w)))


def frontier(delta):
    return 2 * (delta + sqrt(max(0., 1 - delta * delta)))


def pure_rational(r, s, sign=-1):
    # State (r |Phi+> + sign*s |Psi->)/sqrt(r^2+s^2).
    v = (r, sign * s, -sign * s, r)
    d = 2 * (r * r + s * s)
    return [[Fraction(v[i] * v[j], d) for j in range(4)] for i in range(4)]


def random_density(rng, rank):
    a = [[complex(rng.gauss(0, 1), rng.gauss(0, 1))
          for _ in range(rank)] for _ in range(4)]
    rho = [[sum(a[i][k] * a[j][k].conjugate() for k in range(rank))
            for j in range(4)] for i in range(4)]
    z = sum(rho[i][i].real for i in range(4))
    return [[c / z for c in row] for row in rho]


def test():
    # Exact Bell-basis matrix: (Phi+,Psi+,Phi-,Psi-) ordering.
    # Basis entries = integer vectors divided by sqrt(2).
    bell = ((1, 0, 0, 1), (0, 1, 1, 0),
            (1, 0, 0, -1), (0, 1, -1, 0))
    mat = [[sum(bell[i][k] * B[k][ell] * bell[j][ell]
                 for k in range(4) for ell in range(4)) // 2
            for j in range(4)] for i in range(4)]
    assert mat == [[2, 0, 0, -2], [0, 0, 0, 0],
                   [0, 0, 0, 0], [-2, 0, 0, -2]]
    checks = 0
    for r in range(1, 41):
        for s in range(0, r + 1):
            n = r * r + s * s
            delta = Fraction(2 * r * s, n)
            root = Fraction(r * r - s * s, n)
            assert delta * delta + root * root == 1
            rho_plus = pure_rational(r, s, -1)
            rho_minus = pure_rational(r, s, 1)
            assert expectation(rho_plus) == 2 * (delta + root)
            assert expectation(rho_minus) == 2 * (root - delta)
            # Negative extremizer interchanges the weights on Phi+ and Psi-.
            v = (s, r, -r, s)
            rho_negative = [[Fraction(v[i] * v[j], 2 * n)
                             for j in range(4)] for i in range(4)]
            assert expectation(rho_negative) == -2 * (delta + root)
            assert abs(swap_asymmetry(rho_plus) - float(delta)) < 1e-12
            assert abs(swap_asymmetry(rho_negative) - float(delta)) < 1e-12
            checks += 2

    rng = Random(260401)
    for rank in (1, 2, 3, 4):
        for _ in range(3000):
            rho = random_density(rng, rank)
            delta = swap_asymmetry(rho)
            assert -1e-10 < delta < 1 + 1e-10
            assert abs(expectation(rho)) <= frontier(delta) + 5e-12
            # Independent direct computation of the signed swap difference:
            # it has rank at most two, eigenvalues ±delta and two zeros.
            diff = [[rho[i][j] - rho[SWAP[i]][SWAP[j]]
                     for j in range(4)] for i in range(4)]
            frob2 = sum(abs(diff[i][j]) ** 2 for i in range(4)
                        for j in range(4))
            assert abs(frob2 - 2 * delta * delta) < 5e-12
            checks += 1
    target = 1 / sqrt(2)
    assert abs(frontier(target) - 2 * sqrt(2)) < 1e-12
    assert frontier(0) == 2 and abs(frontier(1) - 2) < 1e-12
    print(f"VERIFY_OK {checks} exact-rational witness and numerical-state checks")


if __name__ == "__main__":
    test()
