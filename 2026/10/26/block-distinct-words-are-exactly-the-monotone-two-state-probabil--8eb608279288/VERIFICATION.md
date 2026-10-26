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
The symbolic proof uses monotone upper/lower envelopes of affine stochastic updates, a strict no-return argument for active affine lines, and an explicit rational crossing-point construction. The companion `CHECK.py` uses exact fractions and independently tests each constructed orbit against its word competitors for small profiles. It prints the total examined cases and raises an exception if any construction inequality, stochastic matrix condition, or strict maximality check fails.

These finite checks cannot establish an all-length theorem; the proof supplies the needed quantifiers. Independent mathematical validation has not been performed.
