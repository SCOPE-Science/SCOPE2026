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

# Reproducible checks and proof boundaries

The analytic argument in `RESULT.md` is the evidence for the universal theorem. Its critical ingredients are the entire Laurent coefficient sequence of the two-cosine exponential, the triangle inequality for nonnegative Laurent coefficients on any radius, and explicit complex directions witnessing incompatible large-radius growth. The exact spectral support comes from positivity of all modified Bessel coefficients at a positive argument and integral Bézout representations. The strictness claim follows from a finite Vandermonde matrix in the active frequency lattice.

Execute `python3 checker.py` using the standard Python library. It performs 48 cross-comparisons of Fourier quadrature and modified-Bessel convolution with maximum error \(1.09\times10^{-15}\), five negative signed-coefficient examples, a negative \(32\)-site circulant eigenvalue, a small signed perturbation invisible to a \(16\)-site circulant test, and two complex-radius growth checks. These are numerical examples and finite certificates, not exhaustive proof of the all-indices sign theorem.

All cases \(a,b\ge0\) and their zero boundaries are included. The theorem is not asserted for three or more frequencies, phase-shifted cosine terms, or unrelated compact groups. The cited primary literature supports background and comparisons; a full priority and independent proof audit have not been performed.
