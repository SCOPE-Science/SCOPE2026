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

# Mathematical verification

The stationary characteristic function is a product of standard-Laplace factors. The central ratio identity is established algebraically for arbitrary parameters and frequencies, and the Bernoulli/Laplace variance sum is finite; see RESULT.md. The Lévy exponent formula is obtained by differentiating the convergent logarithmic integral or integrating the Fourier formula. Strict peakedness comes from unimodality plus unbounded independent symmetric noise, not from computational approximations.

Run `python3 checker.py` with Python 3 and the standard library. It performs exact rational checks for many finite products and Bernoulli/Laplace weights and numerical checks of the elementary Lévy exponent integral. Exact rational tests and numerical quadrature are independent consistency checks only; the infinite parameter and threshold quantifiers require the proof.

Limitations: No extension to nonsymmetric diffusion, finite-time laws or survival-conditioned processes. An independent scientific audit and full priority verification have not been performed.
