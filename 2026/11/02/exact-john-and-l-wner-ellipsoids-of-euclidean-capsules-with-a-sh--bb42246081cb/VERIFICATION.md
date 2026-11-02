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

The complete containment and optimality proof is in `RESULT.md`; the finite numerical checks do not replace it. Execute `python3 verify_capsule.py` with Python, NumPy and SciPy available. Its 42 dimension/shape configurations include positive half-lengths only, check the exact translated-ball quadratic maximum, the John support-function inequality, and numerical minimum-volume candidates. One recorded run gave maximum algebra/containment equality residual `4.440892098500626e-16` and maximum log-volume numerical discrepancy `3.669662559935283e-10`.

The isotropic outer-contact law is verified symbolically in the proof through rotational invariance and the two normalized latitude values. The script is not an independent formal proof, and no external independent scientific audit has been performed.
