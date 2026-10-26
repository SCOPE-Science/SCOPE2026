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

# Verification record

Run `python verify.py` with Python 3, SciPy and NumPy installed (SciPy quadrature, beta function, normal tail). The code tests state-resolved normalization for the bounded, critical and power-law pump regimes, the stationary flux-generator identity, exact positive integer moment formulas, and the asymptotic Gaussian-mixture probability tail constants. The final supercritical Pareto-tail ratio at homodyne level 160 was 0.9998510743842594. The critical and bounded tail log-slopes were checked against their limiting values using finite numerical thresholds. These finite checks support but do not prove any statement over all parameters or an infinite limit. The proof is the analytical stationary flux calculation and regular-variation/Laplace analysis in RESULT.md. No independent external scientific audit or certification was performed.
