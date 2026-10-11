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

# Verification of the sharp translated-sampling profile

The analytic argument proves the infinite-parameter claims. The finite standalone Python checks evaluate the exact Gramian and Zak multiplier in two independent ways (rational formulas and direct convergent sums), including asymmetric and symmetric decay values. They compare both tight phase constants, the unique bad offset, the strict interior lower-bound reduction, and the quadratic-onset coefficient. Reproduce with `python3 verify_sampling.py` using only the standard Python library.

The verifier is not a proof of positivity for all parameters, global sharpness for all Fourier frequencies, or nonexistence of equivalent earlier results. Those require the explicit monotonicity and fractional-linear arguments in RESULT.md and the cited full-source comparison. Same-model review passed; independent audit has not been performed.
