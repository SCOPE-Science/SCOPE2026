"""Exhaustive small-field checks for rank-one Nijenhuis maps on free class-two Lie algebras.

Requires Python 3.10+ and NumPy. Run: python verification/verify.py
The full theorem is proved symbolically; finite checks do not prove arbitrary dimensions.
"""
from itertools import combinations, product
import numpy as np


def expected_counts(n, q):
    c = n * (n - 1) // 2
    m = n + c
    character = (q**m - 1) * (q**n - 1) // (q - 1)
    exotic_central = q**n * (q**c - 1) * (q**(c - 1) - 1) // (q - 1)
    exotic_noncentral = (q**n - 1) * q**(m - 1) * (q**(c - n + 1) - 1) // (q - 1)
    nonzero_trace = (q**n - 1) * q**(m - 1)
    return character + exotic_central + exotic_noncentral, exotic_central + exotic_noncentral, nonzero_trace


def check_prime_field(n, q):
    c = n * (n - 1) // 2
    m = n + c
    vectors = np.array(list(product(range(q), repeat=m)), dtype=np.int16)
    vectors = vectors[(vectors != 0).any(axis=1)]
    bracket = np.zeros((m, m, m), dtype=np.int16)
    for k, (i, j) in enumerate(combinations(range(n), 2)):
        bracket[i, j, n + k] = 1
        bracket[j, i, n + k] = -1
    count = 0
    noncharacter = 0
    nonzero_trace = 0
    disagreements = 0
    # Evaluate the tensor identity for every nonzero (u, phi), independently
    # of the algebraic classification, and compare to the predicted criterion.
    for u in vectors:
        phi = vectors
        psi = (np.einsum('j,jik->ik', u, bracket) @ phi.T).T % q
        lam = (phi @ u) % q
        functional_bracket = np.einsum('ijk,pk->pij', bracket, phi) % q
        torsion_coeff = (
            phi[:, :, None] * psi[:, None, :]
            - phi[:, None, :] * psi[:, :, None]
            - lam[:, None, None] * functional_bracket
        ) % q
        actual = (torsion_coeff == 0).all(axis=(1, 2))
        sees_commutator = (phi[:, n:] != 0).any(axis=1)
        predicted = (~sees_commutator) | ((lam == 0) & (psi == 0).all(axis=1))
        disagreements += int((actual != predicted).sum())
        count += int(actual.sum())
        noncharacter += int((actual & sees_commutator).sum())
        nonzero_trace += int((actual & (lam != 0)).sum())
    assert disagreements == 0
    actual = (count // (q - 1), noncharacter // (q - 1), nonzero_trace // (q - 1))
    predicted = expected_counts(n, q)
    assert actual == predicted, (n, q, actual, predicted)
    print(f'prime q={q}, generators={n}: exact {actual}, pairs_tested={len(vectors)**2}')
    return len(vectors)**2


def check_four_element_field():
    # GF(4) = GF(2)[a] / (a^2+a+1), encoding c0+c1*a by c0+2*c1.
    q = 4
    def add(a, b):
        return a ^ b
    def mul(a, b):
        raw = 0
        if b & 1:
            raw ^= a
        if b & 2:
            raw ^= a << 1
        if raw & 4:
            raw ^= 7  # a^2 = a+1
        return raw
    def bracket(x, y):
        return (0, 0, add(mul(x[0], y[1]), mul(x[1], y[0])))
    vectors = list(product(range(q), repeat=3))[1:]
    total = noncharacter = nonzero_trace = 0
    for u in vectors:
        for phi in vectors:
            lam = 0
            for a, b in zip(u, phi):
                lam = add(lam, mul(a, b))
            correct = True
            for i in range(3):
                ei = tuple(int(j == i) for j in range(3))
                ne_i = tuple(mul(phi[i], t) for t in u)
                for j in range(i + 1, 3):
                    ej = tuple(int(t == j) for t in range(3))
                    ne_j = tuple(mul(phi[j], t) for t in u)
                    b_ij = bracket(ei, ej)
                    phi_bij = 0
                    for k in range(3):
                        phi_bij = add(phi_bij, mul(phi[k], b_ij[k]))
                    nb_ij = tuple(mul(phi_bij, t) for t in u)
                    # In characteristic two, subtraction equals addition.
                    a = bracket(ne_i, ej)
                    b = bracket(ei, ne_j)
                    v = tuple(add(add(a[k], b[k]), nb_ij[k]) for k in range(3))
                    functional_v = 0
                    for k in range(3):
                        functional_v = add(functional_v, mul(phi[k], v[k]))
                    right = tuple(mul(functional_v, t) for t in u)
                    left = bracket(ne_i, ne_j)
                    if right != left:
                        correct = False
            total += correct
            noncharacter += correct and phi[2] != 0
            nonzero_trace += correct and lam != 0
    actual = (total // 3, noncharacter // 3, nonzero_trace // 3)
    assert actual == expected_counts(2, 4), (actual, expected_counts(2, 4))
    print(f'extension q=4, generators=2: exact {actual}, pairs_tested={len(vectors)**2}')
    return len(vectors)**2


if __name__ == '__main__':
    total_pairs = sum(check_prime_field(n, q) for n, q in [(2, 2), (2, 3), (2, 5), (3, 2), (3, 3)])
    total_pairs += check_four_element_field()
    print(f'NIJENHUIS_RANK_ONE_FREE_CLASS_TWO_OK 6 {total_pairs}')
