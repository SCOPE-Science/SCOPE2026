---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and proof checkpoints

Run `python check_mobius.py` with Python 3 and the documented `numpy` and `sympy` dependencies. The checker independently builds the Cayley graph of every \(M_{2n}\) for \(3\le n\le71\), computes all-pairs shortest-path distances by breadth-first search (not by the asserted distance formula), and compares all Fourier eigenvalues, inertia, and row sums with the theorem. For \(3\le n\le16\), it also computes exact integer determinants of the graph-distance matrices using rational-domain symbolic arithmetic. It separately verifies the Pell–Lucas trigonometric product through \(m=79\).

The replay passed 437 independent assertion groups, including exact determinants \(112,-99,-4352,-1127\) at \(n=3,4,5,6\). Numerical Fourier comparisons use a tolerance of \(2\times10^{-8}\); the determinant checks are exact integer equalities. The program does not certify the infinite family; its purpose is to cross-check the independently stated, complete analytic proof in RESULT.md.

The critical analytic checkpoints are the level-set decomposition for every positive integer distance, the exact finite cosine/sine summation identities, positivity and negativity of each eigenvalue denominator, the odd-sine product, and the Chebyshev-to-Pell product identity. The proof asserts nothing about the sharp negative-type exponent below one or independent validation.
