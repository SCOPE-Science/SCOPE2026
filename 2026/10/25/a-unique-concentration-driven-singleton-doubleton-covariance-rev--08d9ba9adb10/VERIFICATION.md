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

# Reproduction

Run `python verify.py` using Python 3 standard library. This independently enumerates finite symmetric Dirichlet–multinomial count vectors with exact rational weights and checks the marginal/joint factorial-moment identity and the sign ratio in concrete cases. It also checks a hand-transcribed derivative formula at selected rational arguments. Its finite coverage does not verify all parameters or replace the analytic coefficient-positivity proof in `RESULT.md`.
