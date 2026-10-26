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
# Reproducible mathematical checks

Run `python verify.py` after installing the packages in `requirements.txt`. The program first confirms the exact symbolic equality between the mean-balance residual and the claimed inverse-coverage variance identity. It then integrates the vaccination equations for a normalized Erlang-2 delay (implemented using two coupled memory stages) and compares mean infection with the predicted discount over ten late apparent periods. Both tests passed in the reported execution, and the predicted/observed relative discount discrepancy was about \(2.24\times10^{-6}\).

The mathematical proof in RESULT.md establishes the theorem without relying on the integration, which does not certify a periodic orbit's exact existence or a global attracting set. The theorem assumes compact interior recurrence; this computation verifies numerical consistency only. The precise original model and equilibrium are independently re-derived in the written proof. No independent audit or external validation has been performed.
