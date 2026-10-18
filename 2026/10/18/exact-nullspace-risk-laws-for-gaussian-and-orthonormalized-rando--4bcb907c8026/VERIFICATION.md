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

# Reproducibility and verification scope

The included standalone Python source `verification/check.py` directly implements the Gaussian coefficient-minimal and thin-QR orthonormalized physical-minimal exact correction rules. Install packages listed in `verification/requirements.txt` and run `python verification/check.py`.

The recorded run passed **3 exact-rational assertions**, **1,681 deterministic matrix assertions**, and **58 distributional or gamma-moment consistency assertions** (1,742 total). These use arbitrary full-row-rank linear residual matrices, identical Gaussian sketches for both solvers, and batched independent Gaussian sketches for empirical CDF comparisons. Fixed seeds and explicit numerical tolerances are in the source.

The following conclusions are verified analytically, not experimentally: the independent chi-squared factors in each marginal ratio; the all-real-order moment formula and divergence for \(p\ge\ell-r+1\); the expected squared-norm formulas and exact denominator boundaries; and the samplewise physical-norm ordering. Monte Carlo tests cannot establish tail divergence, asymptotic priority, or results for arbitrary random matrices. No independent scientific audit has been performed.
