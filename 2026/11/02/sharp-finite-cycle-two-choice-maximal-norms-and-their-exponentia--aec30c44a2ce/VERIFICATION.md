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

The proof reconstructs the maximal norm by considering every binary active pattern, then reducing all pattern Gram matrices to a disjoint union of Jacobi blocks. The block-top-eigenvalue comparison, Perron rigidity, single-outlier spectral location and ground-state identity prove the exact theorem for arbitrary \(N\ge2\) and \(0<\theta<1\). An explicit hyperbolic boundary equation proves the exponential asymptotic coefficient.

Execution of `python CHECK.py` with the requirements installed verifies finite selector enumerations, exact characteristic polynomials, and the symbolic coefficient simplification. These computational checks are supplementary: exhaustive checks for bounded \(N\) cannot prove the all-order statement, and the floating-point eigenvalue comparisons are not exact certificates. The exact rational and symbolic checks address the algebraic subclaims, while the inequalities and asymptotic passage are justified in the written proof.

No independent audit has been performed. Earlier unindexed equivalent findings remain a literature risk.
