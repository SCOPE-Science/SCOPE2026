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

# Verification notes

The stated Fourier transform is derived from the explicit radial-exponential Gaussian subordination and differentiation at scale one; the positive constant and powers can be checked by evaluating at zero frequency. The finite-dimensional polynomial \(Q\) is then minimized on the full continuous interval \([0,1]\), with special attention to the vertex and both endpoints. Both spectral equality geometries follow by substituting the exact b-boundaries.

The standalone `CHECK.py` script uses Python's standard-library rational fractions only. It verifies parameter-differentiation coefficients in integer dimensions, the exact lower and upper quadratic thresholds, and positivity/nonpositivity at selected exact spectral points. The proof covering all dimensions and real parameter ranges is in RESULT.md; numerical or finite checks are not claimed as infinite certification.

Exact analytic limitations: one common spatial scale, degree at most two, Euclidean separation. Literature comparisons are bounded, and independent validation has not been performed.
