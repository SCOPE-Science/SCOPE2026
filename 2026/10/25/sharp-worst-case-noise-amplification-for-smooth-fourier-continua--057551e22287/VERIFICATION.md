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

# Reproducibility

The included `VERIFY_EB.py` is executable with `python3 VERIFY_EB.py` using the standard library. It checks exact binomial identities for the extrapolation weights, equality of the explicit row absolute sums and the closed formula, sign-vector witnesses attaining each row norm, constant-data reproduction, and critical integer examples. It also evaluates the integer-parameter symmetric-beta polynomial transition family using exact fractions; examples of even-length attainment and odd-length strict nonattainment agree with the theorem.

The run completed 1,482 finite exact-rational checks and the additional exact beta-family tests. The analytical proof, not finite enumeration, establishes universal existence/nonexistence and \(C\to\infty\) behavior. No independent audit has been performed, and no assertion about arbitrary floating-point implementation errors is made.
