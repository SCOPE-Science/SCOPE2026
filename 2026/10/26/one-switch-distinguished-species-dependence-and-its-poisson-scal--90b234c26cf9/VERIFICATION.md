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

Run `python verify.py` using Python 3.10 or later. The script enumerates 48 complete rational-valued categorical sample spaces and checks exact covariance identities without floating-point arithmetic. It tests a full-support conditional-extremes witness and compares large-sample critical roots with a transcendental prediction by numerical bisection. These checks do not establish the theorem for all parameters; that conclusion follows from the strict-concavity proof and uniform expansion in RESULT.md. All profile weights in the proof are fixed and strictly positive. No external independent audit or validation has been performed.
