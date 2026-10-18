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

# Verification of the Laplace Gabor spectral law

The proof and definitions appear in RESULT.md. The reproducibility program CHECK.py evaluates 27 independent direct Zak-series comparisons, six logarithmic spectral-density coefficient comparisons, three one-sided square-root cusp comparisons, and two cubic-transition checks. All 38 assertions completed. It uses Python and SciPy and calculates derivatives and limiting coefficients independently of the stated symbolic formula for the spectral multiplier. The checker applies finite truncation to rapidly converging Zak series and numerical quadrature; these are finite sanity checks and do not establish the infinite-dimensional theorem.

At decay parameter \(\lambda=1\), the saddle energy is about \(3.68269437683117\), the corner energy is about \(1.16005131677195\), the logarithmic coefficient is about \(0.05440379193087\), and the cusp coefficient is about \(0.34571316447133\). At the crossing, \(\cosh\lambda_*=1+2\cos(2\pi/7)\). No independent external audit has been performed.
