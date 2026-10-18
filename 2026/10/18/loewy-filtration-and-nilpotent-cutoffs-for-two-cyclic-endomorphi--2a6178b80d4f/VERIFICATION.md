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

# Reproducibility and logical boundaries

Run `python3 checker.py` using a standard Python 3 interpreter. The program explicitly constructs endomorphism matrices with their distinct row moduli, calculates radical-product additive closures independently of the stated symbolic ideal formulas, and compares the resulting sizes and exact nilpotency cutoffs for the included finite rings. It separately verifies equal-exponent matrix witnesses.

The recorded result of the package-path execution is `ALL_CHECKS_PASSED`. The exhaustive experiments only cover their listed finite parameter sets; the general conclusion depends on the proof by valuations and walks in `RESULT.md`. No external independent mathematical audit is supplied.
