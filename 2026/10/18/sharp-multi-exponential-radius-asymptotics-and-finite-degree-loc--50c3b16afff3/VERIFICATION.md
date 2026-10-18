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
# Verification notes

The general expansion follows from a Schur complement and the even closed-walk expansion of a tail Jacobi resolvent; this is an analytic argument, not an empirical interpolation. For \(s\ge16\) the normalized tail norm is less than one half, so the remainder is bounded uniformly by a geometric series. The scalar eigenvalue equation has one positive solution above the tail spectrum. This supplies the infinite-dimensional justification.

The checked code in `checker.py` constructs finite Jacobi sections with the correct first offdiagonal \((3/2)^{s/2}\), then normalizes and diagonalizes. The archived output in `checker_output.txt` shows numerical residuals at ten negative-weight magnitudes, the exact Bergman consistency test, and four finite-section comparisons. All 25 programmed assertions passed.

Computational limits: finite diagonalization is not an exhaustive/infinite proof; machine floating-point agreement cannot certify the full asymptotic remainder by itself. No external audit or independent validation was performed.
