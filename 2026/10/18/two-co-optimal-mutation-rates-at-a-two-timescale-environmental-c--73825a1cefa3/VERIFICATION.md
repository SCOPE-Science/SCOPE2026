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
# Reproducibility and limits

Run `python verify.py` in the directory containing the extracted files (Python 3.10+; `sympy` installed). The program checks symbolic identities, all rational sign brackets and comparison thresholds, and numerically encloses the unique crossing. The infinite zero count uses Descartes' sign rule with three disjoint verified sign changes. Numerical root finding is not a substitute for the proof of the universal claims in RESULT.md. No independent scientific validation has been performed.
