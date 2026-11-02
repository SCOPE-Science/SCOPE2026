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

The analytical proof uses the known stationary Gaussian orthant identity, the classical Rice intensity, a pathwise injection of strict lattice maxima into disjoint intervals containing continuous maxima, an explicitly checked sixth-order covariance expansion, and a weighted Jensen argument with strict equality conditions.

To reproduce finite calculations, run `python checks/check_gaussian_peak.py` with Python 3, SymPy and mpmath installed. The accompanying `checks/output.txt` is the output from the packaged source. It reports 128 passed numerical assertions including 96 deterministically seeded bandlimited spectra. Finite calculations support algebra and examples; they do not independently verify the infinite-dimensional process regularity, Rice formula, or all spectral measures.

The theorem assumes a finite sixth spectral moment. No external review, independent certification, or claim about unverified larger generalities is made.
