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

# Reproducible checks and limits

Run `python artifacts/check.py` with NumPy and SciPy available. The script checks 134 finite assertions against the exact constant-drift absorbing/reflecting boundary-value solution, its drift-dependent large-rate normalization, deterministic Gauss–Hermite integration of the Gaussian reset-velocity factor, and discrete sampled-path monotonicity of the upper Skorokhod reflection map.

The decisive analytical steps are the exact constant-drift Laplace transform, a pathwise sandwich conditional on the velocity path, the choice of shrinking horizon \(T=r^{-1/3}\), exponential-moment dominated convergence and the complete-reset renewal equation. The finite checks do not establish convergence for all rates or uniqueness in the literature; those are assessed by the proof and literature comparison, respectively.

The independent audit state is unperformed.
