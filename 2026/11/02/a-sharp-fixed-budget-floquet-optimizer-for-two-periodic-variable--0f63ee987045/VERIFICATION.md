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

The embedded `verify.py` uses symbolic algebra to reconstruct two transfer matrices, validate the trace/determinant identities, the Schur inequalities and discriminant factorization, and the exact optimum. It compares the closed form with direct eigenvalues for 135 pairs and checks 12 numerical parameter grids. It also verifies that the \(s=4\) optimal monodromy is a nontrivial Jordan block with eigenvalue \(-1/11\), and checks the \(s=2\) square-root limiting scale. The proof in `RESULT.md`, not finite grids, establishes the universal statement. Run `python verify.py` after installing `requirements.txt`. This is not independent external validation.
