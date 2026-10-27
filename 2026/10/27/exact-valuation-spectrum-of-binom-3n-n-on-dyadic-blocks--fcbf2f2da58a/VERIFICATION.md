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

# Verification of finite examples
The standalone `verify.py` uses integer and rational arithmetic to compute the valuation spectrum directly and from the closed depth recurrence for 13 blocks, and tests exact expectation and variance identities, including boundary levels. It independently checks 1023 binary carry computations with the terminal correction. The matrix identity and analytic eigenvalue argument in RESULT.md prove the universal claim; the finite test is not infinite certification. The full text of Barat–Grabner (2001) was not available, so comparison to that prior source remains a priority limitation.
