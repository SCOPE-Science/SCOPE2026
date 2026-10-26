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

The proof derives the normalized Gaussian STFT exactly, identifies the real three-line interference matrix and computes its two eigenvalues by summing rank-one unit-row projectors. The derived sine identity supplies both positive universal constants comparing the least eigenvalue with simultaneous distances to integers. For irrational line-spacing ratio, nearest-integer reduction to rational approximation yields both sides of the sharp limsup exponent. Rational ratios exhibit exact resonances, while badly approximable and Liouville ratios exhibit the stated opposite-rate cases.

The attached `checker.py` independently evaluates matrix Gram eigenvalues against the formula, verifies the two-sided trigonometric inequality and rational resonances on deterministic grids, numerically checks finite continued-fraction cases, tests interference reconstruction, and compares the closed Gaussian STFT against direct numerical integration. The saved `checker-output.txt` records 3624 finite assertions passed.

Finite experiments are not an exhaustive proof of an infinite theorem. The numerical diagnostic is not a verification of mathematical novelty, and no independent audit has been performed. This invariant refers to post-extraction interference data rather than a raw spectrogram inverse norm.
