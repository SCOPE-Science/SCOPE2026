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

# Reproducibility and scope

Run `python verify.py` with Python 3, NumPy, and SciPy. The checker independently enumerates vertices of small Minkowski sums, recomputes finite support and width identities for constant, length-dependent, and nonseparable interval-weight profiles, and checks the exact finite-dimensional Gaussian mean formula against simulated Gaussian directions. An independent truncated-Poisson integral simulation illustrates the expected limiting correction for unit weights.

The observed run completed with `VERIFY_OK support_checks= 159 mean_checks= 12`. The truncated-process diagnostic mean was approximately `-0.85037` at mark cutoff 5, compared with the untruncated theoretical mean of approximately `-0.92278`. The approximation is not an equality and was not used in any mathematical proof.

No finite computation proves the limit theorem, the Gaussian extreme-point-process convergence, the absolute-moment diagonal bound, or bibliographic originality. These are addressed analytically in `RESULT.md`; independent scholarly validation remains unperformed.
