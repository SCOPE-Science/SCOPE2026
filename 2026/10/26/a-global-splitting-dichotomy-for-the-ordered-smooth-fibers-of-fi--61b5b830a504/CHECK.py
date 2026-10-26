#!/usr/bin/env python3
"""Check exact Picard-group presentations for ordered points on the projective line.

Requires SymPy. The mathematical proof covers every k; these finite calculations
are a reproducibility check, not the proof of the universal statement.
"""
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def picard_invariants(k):
    if k < 2:
        raise ValueError("k must be at least 2")
    m = k * (k - 1) // 2
    relations = zeros(k, m)
    col = 0
    for i in range(k):
        for j in range(i + 1, k):
            relations[i, col] = 1
            relations[j, col] = 1
            col += 1
    diag = smith_normal_form(relations, domain=ZZ)
    nonzero = [abs(int(diag[i, i])) for i in range(min(diag.rows, diag.cols)) if diag[i, i]]
    return k - len(nonzero), tuple(d for d in nonzero if d > 1)


if __name__ == "__main__":
    for k in range(2, 9):
        rank, torsion = picard_invariants(k)
        expected = (1, ()) if k == 2 else (0, (2,))
        assert (rank, torsion) == expected, (k, rank, torsion)
        print(f"k={k}: free_rank={rank}, torsion={torsion}")
    print("VERIFY_OK k_range=2..8 exact_integral_smith_forms=true")
