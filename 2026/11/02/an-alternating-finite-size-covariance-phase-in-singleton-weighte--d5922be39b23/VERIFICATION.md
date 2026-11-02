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

# Verification

The exact checker `verify.py` implements set-partition enumeration and a four-index noncrossing test without using the profile formula to generate its samples. Its output on the delivered script is `VERIFIED 127 independent exact checks; alternating q=1/20 signs +,-,+,-`.

It verifies all partition-function and covariance numerator coefficients at orders five through eight, every observed block-profile count against a second published exact enumeration, and direct rational-moment evaluations. The proof's all-fugacity sign conclusions instead follow from polynomial coefficient signs and strict monotonicity; finite enumeration alone would not establish those assertions. All claims are finite-order. Independent validation has not been performed.
