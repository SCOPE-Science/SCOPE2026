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

# Reproducibility and scope

The exact proof is in `RESULT.md`. With dependencies in `requirements.txt`, run `python verify.py`. The checker performs exact Fraction arithmetic for dimension-indexed chi-square/beta moment identities, leave-one-out correlation and variance formulas, then independently constructs Gaussian column sketches and computes all leave-one-out residual norms to compare their sample mean, trace variance, and diagnostic mean against the exact expressions.

The checks cover finite integer dimensions and fixed seeded finite simulations. Neither numerical agreement nor a lack of apparent counterexamples proves the infinite-dimensional limit. The proof's fourth-moment and probability arguments are analytic. Rounding stability, residual-normalized test vectors, arbitrary input matrices, relative-error adaptive guarantees, and external validation remain outside this result.
