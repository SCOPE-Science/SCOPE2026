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

The supplied `verify_prism.py` is standalone and requires only Python 3 standard-library modules. Execute from the directory containing it using `python verify_prism.py`. It enumerates all nine prism edges and counts opposite-sign endpoint pairs over a deterministic, equal-area spherical midpoint grid. The three exact probabilities are evaluated by independent inverse-sine expressions, and six aspect ratios are compared. The maximum observed grid error was below \(0.000551\); the program also checks the unique stationary root and thin-prism leading asymptotics.

The analytic proof in RESULT.md does **not** depend on floating-point computation. Its exhaustive graph-sign table, Haar angular density, antiderivative, and strict derivative inequality justify the result for every positive aspect ratio. The finite spherical grids are not rigorous continuum certificates, and the derivative root is reported numerically only as a supplement to its exact unique-root definition. Historical priority remains subject to inspection of the complete Voss (1982) article. Independent audit has not been performed.
