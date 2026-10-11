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

# Verification details

The principal evidence is the complete analytic proof in RESULT.md, including the exact weak-support Fourier polarization, positive-curvature probe construction, spectral cutoff inequalities, and a high-frequency lower witness showing sharpness of the logarithmic exponent.

Run the included `verification.py` and `verification_log.py` from the extracted directory with Python 3 using only the standard library. The first checks the exact angular mean and covariance by direct numerical integration of the support-area formula on four strictly positively curved examples. The second checks all coefficient normalizations, the positivity of the analytic curvature margin, the finite-mode low/high cutoff bounds in 1,223 finite mixtures, and the exact formula for the witnesses. The recorded results were `VERIFY_OK` and `VERIFY_LOG_OK`.

These finite checks cannot certify the behavior of infinitely many Fourier modes or exclude all earlier publications. Those aspects depend respectively on Parseval/Sobolev convergence and the documented literature comparisons. No independent mathematical audit has been performed.
