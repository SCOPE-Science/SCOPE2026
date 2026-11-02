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

# Verification

Run `python3 verify.py` in a directory containing the attached script. It requires only Python's standard library. The executed verifier reported:

`PASS: 793 exact rational checks; determinant, KKT, covariance and full cofactors verified.`

The script tests \(2\le n\le9\) at five positive rational parameters, including the budget identity, direct inverse of the tridiagonal Laplacian-plus-diagonal matrix, the exact AR(1) covariance and its constant diagonal, and the explicit determinant formula. For \(2\le n\le7\), it independently builds the full weighted two-rail graph Laplacian and computes its exact Kirchhoff cofactor. It compares 15 reproducible feasible alternative allocations for each parameter pair, and tests the separate rational point \(n=6,u=1,B=2,\tau=24\).

The proof in `RESULT.md`, rather than these finite checks, establishes all-size global optimality, boundary uniqueness and both asymptotic regimes. Specialist-priority comparison is only as strong as the literature actually inspected; no independent expert or formal verification is claimed.
