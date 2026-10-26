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

# Verification notes

The companion `verify_rank.py` uses exact fractions and direct 2-by-2 determinant tests over every possible sequence of rounded four-type rows for bounded sizes. It ran 242 baseline checks, 480 grid-geometry checks and 105 inhomogeneous-geometry checks, for 827 passing checks. The computations test the exact finite formulas, equal-probability examples and limiting expressions at sampled sizes. The proof of the universal formula is the explicit four-row-type collinearity classification; numerical limits and finite enumeration alone are not proofs. Historical novelty remains subject to broader human literature examination. No independent mathematical audit has been performed.
