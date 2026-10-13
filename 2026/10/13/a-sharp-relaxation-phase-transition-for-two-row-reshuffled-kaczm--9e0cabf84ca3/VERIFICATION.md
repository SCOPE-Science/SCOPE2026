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

Execute `python verify.py` with the dependencies in `requirements.txt`. The verifier checks the exact averaged Gram identity over rational unit-row examples, the two polynomial derivatives, the critical-crossing reduction, and representative numerical minimizers. The infinite-domain assertions follow from the monotonicity and sign arguments in `RESULT.md`, not from finite sampling. No external audit or independent validation has been performed.
