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

The analytic proof reduces the positive Helson operator to a polynomially weighted Toeplitz operator plus a remainder whose singular numbers decay exponentially. Its main nonstandard step is the counting function law for the weighted Toeplitz operator: this is proved by trigonometric-polynomial approximation, finite band removal, microscopic block freezing and an elementary finite Toeplitz moment argument.

The finite checks in `verify.py` use Python, NumPy and SciPy. They test the exact geometric Cauchy-kernel identity for indices in an explicitly stated range, the finite zeta remainder inequalities, Fourier-moment identities for the hyperbolic-secant symbol, and the observed truncation spectra at listed sizes. A finite matrix does not prove a full asymptotic. The theorem is conditional only on the stated positive parameters and standard analytic identities; there are no hidden data files or extrapolated computational certificates.

Independent audit: not performed.
