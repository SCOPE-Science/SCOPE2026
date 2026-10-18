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

The derivation independently calculates the Gram kernel, its ODE and weighted-flux boundary conditions; it identifies the allowed Bessel branch, uses the positive-zero spectrum, and verifies exact second and fourth spectral moments by direct integration. The two boundary laws are deduced from normalized Bessel power series, continuity of nonzero roots and dominated convergence under uniform zero bounds. The first-singular-value correction uses the exact Hilbert--Schmidt sum and the limiting squared tail mass.

The accompanying `check_spectrum.py` independently constructs midpoint Nyström matrices for seven exponents and compares their five largest singular values against Bessel zero formulas, also computing small- and large-exponent scaled values. The finite-matrix comparisons test normalization and indexing; they cannot certify all exponents or infinitely many singular values. The literature comparison is limited by imperfect indexing and partial availability of the 2008 extension. No independent audit has been performed.
