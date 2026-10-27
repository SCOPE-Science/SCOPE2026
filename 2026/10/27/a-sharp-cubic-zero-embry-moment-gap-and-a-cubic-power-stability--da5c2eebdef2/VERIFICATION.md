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

# Reproducibility and proof boundaries

The analytic derivation uses only Hilbert-space Cauchy–Schwarz, application to a normalized image vector, a norm-maximizing sequence and the intersection of two scalar monotone functions. It does not require finite-dimensionality. A direct matrix calculation gives the exact extremizer \(\tau=(\sqrt5-1)/2\) and \(\Delta(T)=(3-\sqrt5)/2\).

Execute `python verify.py` with NumPy to check the numerical sharp example and the 7,403 recorded finite assertions. The checker is a consistency diagnostic, not a proof of an infinite-dimensional assertion. The inequality is proved for all bounded real and complex Hilbert-space operators, while parameterwise sharpness is proved at the two endpoints only. The full text of one recent potentially related article was not obtained, so the historical-priority comparison has a residual risk. No independent audit has been performed.
