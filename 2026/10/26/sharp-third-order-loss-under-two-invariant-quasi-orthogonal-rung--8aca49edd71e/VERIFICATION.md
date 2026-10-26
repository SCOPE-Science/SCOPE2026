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

Install packages from `verification/requirements.txt` and execute `python verification/check.py` from the extracted package root. The standalone program checks the polynomial factorization, RK3 tableau algebra and the example's exact rational constants. It then solves actual frozen projected-gradient equations for decreasing steps and reproduces the claimed local and global constants. Expected completion begins `VERIFY_OK`.

The Python computation is finite and diagnostic only. The implicit-function existence, sharp lower bound and all positive-time global limits rely on the analytic arguments in RESULT.md. No independent audit or formal certification has been performed.
