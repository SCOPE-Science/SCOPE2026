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

The proof in `RESULT.md` is algebraic and universal for the stated parameter domain. The accompanying `verify.py` uses only exact rational arithmetic. It checks that the quotient-rule derivative of the susceptible prophylactic share agrees with the closed formula on multiple deterministic rational states; it verifies the signs of the threshold polynomial at zero and at the published opinion threshold; and it replays the exact default-parameter witness where the opinion-transfer term is negative but the prophylactic susceptible share is increasing.

The finite replay is a transcription and arithmetic check, not a substitute for the universal proof. No numerical ODE integration is used to establish the claim.
