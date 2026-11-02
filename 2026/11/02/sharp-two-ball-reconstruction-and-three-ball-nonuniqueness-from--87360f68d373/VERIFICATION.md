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
# Verification and reproducibility

Run `python verify.py` using Python 3 (standard library only). The source is included alongside this document.

The checker performs: (i) exact rational comparisons for both support envelopes at \(2001\) sampled axial cosines and the common even width law; (ii) exact inequalities certifying that each three-ball configuration is pairwise disjoint and has a different exposed-radius multiset; (iii) an exact rational two-ball inverse grid; and (iv) a seeded simulation of the predicted three-dimensional atom and two uniform density pieces. It reports `ALL_CHECKS_PASSED`.

Critical infinite claims are proved analytically in RESULT.md: the support-function envelope; convex monotone quantile inversion using the strictly positive angular distribution; and the identity of the two piecewise-affine support sums for *all* axial cosines. The grid and simulation are numerical/finite sanity checks, not proofs of statements for all parameters. No external independent validation has been performed.
