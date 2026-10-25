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

# Reproducible checks and boundaries

Execute `python3 verify.py` from the extracted file directory. This checker uses only the Python 3 standard library and reports `VERIFY_OK exact_profiles 80 rejection_dimensions 3` on successful completion. It checks exact rational moment and determinant identities in 76 dimension-parameter profiles, independently integrates four planar polygons by exact triangle moments, and performs three direct-rejection covariance comparisons against the defining inequalities, with fixed random seeds. Numerical asymptotic diagnostics use dimensions 1,000, 10,000, and 100,000.

The symbolic identities, measure-preserving tile decomposition, and the central limit theorem in `RESULT.md` are the actual evidence for arbitrary dimension. The finite numerical comparisons are corroborative only. Total-variation convergence is proved by an explicit coupling rather than statistical testing. No independent mathematical audit has occurred.
