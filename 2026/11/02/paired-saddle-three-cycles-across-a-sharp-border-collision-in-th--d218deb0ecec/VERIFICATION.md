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

The finite exact check consists of `verify_period3.py` with Python 3 standard-library `fractions.Fraction`. Run `python3 verify_period3.py` from this package's directory. During preparation it printed `PASS: 444 exact candidate formulas / monodromies checked`. The script checks three actual map iterates for each itinerary with exact rational inputs in the zero, switching and double-cycle regimes, as well as trace/determinant and characteristic-polynomial sign claims.

The mathematical proof, not this finite test, establishes the statements for every real parameter in the stated domain. Results outside the strict determinant and saddle hypotheses have not been established. Independent audit is not performed.
