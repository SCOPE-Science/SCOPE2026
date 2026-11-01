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

# Verification and scope

The derivation uses the critical Zak isometry, exact geometric-moment generating series and the Cayley conversion to a cubic polynomial. Critical algebraic identities are explicit in `RESULT.md`. The cubic discriminant, derivative signs, and Hurwitz determinant establish qualitative root information with exact formulas; finite sampling is not used as a universal root-count proof.

Execute `python3 checker.py` using the Python 3 standard library. This checks rational generating identities, polynomial root ordering for twelve representative damping values, stable-region Zak nonzero samples, and the local quadratic coefficient. The source program prints `PASS: 6631 supplementary checks`. The analytic proof remains necessary for all quantifiers and the full spectrum of parameters.

The claimed exact lower-bound formula holds only sufficiently close to the frame boundary for each fixed damping factor, not globally in the full frame half-line. No independent external mathematical audit has been conducted.
