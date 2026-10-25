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

An exact-rational standalone Python script `verify.py` checks 720 gain identities, 1,886 prescribed-size sign comparisons, equality of one- and two-voter distributions for the paired examples, and initial binomial tails. Execute `python verify.py` and compare its sole output line with `certificate.json`. Finite checks do not imply the unrestricted results; the mathematical proof is in RESULT.md.
