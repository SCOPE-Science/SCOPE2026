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

Run `python verify_conjugate.py` with Python 3, NumPy, and SciPy. This run produced `PASS: 37 numerical identities and strict sample comparisons` and matched a non-exponential competitor's directly integrated mean gap to the positive double-integral formula within specified tolerances. The checker uses independently evaluated fixed-time Brownian survival integrals, Poisson-rate analytical formulas, and mixture rates. These finite tests support normalization and boundary behavior but cannot certify universal optimality.

The proof for all iid positive clocks is analytic: Brownian backward heat equation; renewal mean quotient; symmetric positive Green kernel; exact squared-ratio identity; uniqueness of Laplace transforms. It allows infinite competitor mean as a valid strict inequality. Independent scientific audit has not been performed.
