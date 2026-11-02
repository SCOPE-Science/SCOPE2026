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

The exact argument is in `RESULT.md`, including the finite-dimensional integrated-density identity, the parity-constrained Fourier-sum factorization, and strict convex optimization. Numerical support is reproducible with `python check_even_flux.py`, using NumPy and SciPy.

The checker constructs the physical Hamiltonian independently and verifies 150 full complex Lyapunov solutions, 168 direct spectral-gap sums, 14 bounded numerical flux optimizations, and 28 exceptional-flux spectral multiplicity counts. All checks passed on the supplied version. These experiments are finite and do not serve as proof of the universal quantifier over even ring sizes.

Only the stated Hamiltonian, Markovian loss, and maximally mixed initial state were checked; no inference is made about decoherence, disorder, multi-excitation dynamics or localized-source optimization. Independent scientific validation has not been performed.
