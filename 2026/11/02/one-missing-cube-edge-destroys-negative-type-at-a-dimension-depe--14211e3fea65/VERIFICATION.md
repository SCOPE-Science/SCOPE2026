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

# Finite supplementary verification

Run `python verify.py` using Python 3, NumPy, SciPy, and mpmath. The checker independently reconstructs all graph shortest-path distances for dimensions three through eight and checks the exact one-pair metric defect. It computes 65-digit roots of the scalar Walsh equation and checks strict dimension ordering for dimensions three through eight. For dimensions three through seven it also checks every eigenvalue of the full zero-sum powered-distance matrix below, at, and above the predicted threshold, including the one-dimensional critical kernel and explicit Walsh equality vector.

A fresh replay produced `PASS supplementary assertions: 88343`. The experiment does not cover arbitrarily many cube dimensions or establish the asymptotic statement; those rely on the analytic proof in `RESULT.md`. Only the available package code is replayed; no independent external audit or verification is represented.
