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

# Reproducible checks

The embedded `check.py` requires Python, `sympy`, `numpy`, and `mpmath`; run `python check.py` from the package directory. The program checks the exact Taylor polynomial determinant and principal-minor coefficients, the second derivative of the coefficient profile at the symmetric location, and the sixth-order symmetric eigenvalue expansion. It also runs finite spectral-grid checks and verifies identity Gram matrices at the first odd resonance.

The analytical proof, not the finite testing, establishes uniformity over the entire parameter interval, all sufficiently small apertures, and all resonant integers. The polynomial computations use exact rational arithmetic. A single high-precision numerical evaluation cannot certify uniqueness of an analytic optimizer.

Scientific limitations include the unspecified maximal small-aperture interval and unresolved exhaustive historical priority. No independent mathematical validation has been performed.
