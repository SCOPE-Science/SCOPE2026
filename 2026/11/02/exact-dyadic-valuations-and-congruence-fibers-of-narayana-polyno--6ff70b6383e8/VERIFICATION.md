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

# Reproducibility checks

Execute `python verify.py` using Python 3.8 or newer. This standalone program uses standard-library integer binomial coefficients, constructs each Narayana polynomial from its defining coefficient formula, separately constructs the Coker gamma expression, compares their values and the predicted two-adic valuation, and exhausts residue sets modulo powers of two.

The completed replay returned `VERIFY_OK direct_vs_gamma_and_valuations=1908 full_residue_count_tests=864`. All checks passed. These finite computations establish only the tested cases, not the universal assertions. The proof of the universal assertions is the exact minimum-valuation argument in `RESULT.md`. No independent audit has been performed.
