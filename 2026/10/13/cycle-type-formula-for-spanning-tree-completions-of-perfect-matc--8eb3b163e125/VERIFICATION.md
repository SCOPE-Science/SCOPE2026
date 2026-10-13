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

# Reproducibility

Run `python3 verify.py` from the directory containing this file. The checker uses only the Python standard library. It generates every derangement on \(3\leq n\leq7\), evaluates the claimed Chebyshev recurrence formula using integer arithmetic, and compares it with two independently assembled exact Laplacian cofactors of the contracted multigraph. For \(3\leq n\leq5\), it also enumerates every extension of the fixed matching to an original-graph spanning tree by selecting the remaining \(n-1\) edges and performing cycle/connectivity tests.

Observed successful output begins `VERIFY_OK tested_derangements=2174 brute_matchings=55 by_order={3: 2, 4: 9, 5: 44, 6: 265, 7: 1854}`. The cycle-type table includes \(N_3((1\,2\,3))=3\), \(N_4((1\,2)(3\,4))=32\), and \(N_4((1\,2\,3\,4))=36\). Integer determinants use the Bareiss fraction-free elimination algorithm, with exact-divisibility assertions. The code includes no heuristic tolerance or numerical floating-point step.

The finite checks are not infinite proofs. The proof for arbitrary \(n\) follows by edge contraction, exact Laplacian diagonalization, the matrix-tree theorem, and the Chebyshev characteristic-polynomial identity, as written in `RESULT.md`. Independent audit has not been performed.
