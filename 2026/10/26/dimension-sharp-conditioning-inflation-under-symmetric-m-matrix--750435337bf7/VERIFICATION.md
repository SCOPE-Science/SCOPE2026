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
# Verification record

The mathematical verification consists of the explicit five-step proof in `RESULT.md` and a reproducible decimal test in `CHECK.py`, with its actual captured output in `CHECK_OUTPUT.txt`. The latter recomputes the positive solution of the hub/leaf balance equations and evaluates both the diagonal scaling condition number and the full balanced spectrum for multiple star sizes and coupling parameters. It checks the equations to a strict high-precision tolerance and the order of the eigenvalues.

These finite numerical checks do not constitute a proof for all dimensions or all positive definite symmetric \(M\)-matrices. The unlimited-range statements are proved analytically using strong convexity, the exact row-sum identity, spectral comparison, and a two-dimensional star quotient. An independent audit has not been performed.
