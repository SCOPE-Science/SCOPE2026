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

The mathematical argument establishes a strict kernel derivative and the full parameter-to-observation bijection under its stated assumptions. Execute `python3 check_claim.py` in this directory using only the Python 3 standard library to compare the analytical formulas with the stationary two-state Markov moment equations and an independent future-moment quadrature.

The checker tests 600 seeded physical parameter choices, each covering mean diffusivity, kurtosis, normalized square covariance and inverse reconstruction, including both sides of the trap and switching time scales. Its finite checks support but do not establish the theorem's universal monotonicity or the absence of overlooked earlier literature. No experimental-noise study or independent external audit is asserted.
