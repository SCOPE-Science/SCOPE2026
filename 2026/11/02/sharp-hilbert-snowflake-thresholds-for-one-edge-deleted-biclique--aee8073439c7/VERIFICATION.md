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

# Reproducibility and limits

The included `verify.py` runs using Python 3 and only the standard library. Invoke `python3 verify.py`. It reconstructs unweighted graph distances by breadth-first search, tests the exact zero-sum quadratic reduction against direct powered-distance sums, diagonalizes centered Gram forms through a Jacobi iteration, brackets the threshold using the analytic Schur complement, and checks the balanced root and asymptotic coefficient numerically. In the original replay, the checker reported 5,414 passed comparisons and assertions.

The checker does not attempt to exhaust infinitely many parameters or to certify an infinite theorem numerically. The full proof is in `RESULT.md`. Analytical dependencies are the finite-metric strictness interval theorem, elementary matrix Schur complements, and elementary asymptotic expansion. Independent mathematical review has not been performed.
