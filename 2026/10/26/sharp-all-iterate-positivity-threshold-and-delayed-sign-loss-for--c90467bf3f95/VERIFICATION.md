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

The coefficients of the source rule were independently reduced to the rational recurrence used in the proof. Exact symbolic checks verify the rational root comparison and derivative at the positivity threshold; numerical tests compare the first-negative index against direct recurrence iterates and evaluate the inverse-distance scaling. Execute `python check.py` after extracting the files.

The proof, not finite enumeration, establishes the all-step criterion. Results assume exact exponential initialization and no floating-point roundoff. The published rule is A-stable but its positive-semigroup behavior is an additional property. Independent audit is not performed.
