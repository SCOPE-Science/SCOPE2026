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

# Reproducible verification

Run `python3 check.py` with the standard Python 3 library. It verifies the exact exponential-mixture geometric law and normalization, independently evaluates the stationary-phase integral numerically and compares it with its closed logarithmic transform, checks the phase-boundary derivative, and compares exact one-period positive lattice masses against the analytic tail coefficient. The supplied checker completed 64 assertions successfully.

An additional independent numerical two-period convolution for the unit integrated mean rate yielded asymptotic ratios 1.0194 (displacement 10), 1.0109 (40), and 1.0058 (200). The singularity-transfer steps and uniform conditional phase estimates in `RESULT.md` constitute the infinite-displacement proof. The tests do not assert that finite enumeration proves a limit.

Literature comparisons are limited to accessible primary texts, supplemental discussions, published mathematical research search results, and prior accessible findings. Neither publication priority nor independent verification has been certified.
