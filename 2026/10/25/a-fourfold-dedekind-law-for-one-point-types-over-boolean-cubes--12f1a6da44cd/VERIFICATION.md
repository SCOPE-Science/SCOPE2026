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

The attached standard-library program `verify.py` computes the downsets of the named Boolean cube directly, complements them to enumerate upper sets, checks all cross-relations as strict inclusions, and compares their counts with the binomial convolution through dimension four. The resulting values are `3,6,18,86,808`. Dedekind-number inputs for dimensions five through eight give additional output values, but they are not exhaustive tests of those dimensions. The all-dimension identity follows from the displayed mathematical proof; its asymptotic uses the classical Dedekind estimate. No external/independent certification has occurred.
