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

The argument is analytical and applies to the infinite-dimensional Bargmann–Fock space. The critical nonstandard estimate is the Hilbert–Schmidt bound \(\|B_aB_b^*\|\le s\exp(-(d-2\sqrt{s})^2/2)\). The exact compressed leading interaction equals \(\lambda_0\langle k_a,k_b\rangle\), whose modulus is \(\lambda_0e^{-d^2/2}\). Schur-complement bounds control every other mode, producing an error at most \(\eta_d^2/(\delta-2\eta_d)\). These inequalities prove the asymptotic; computation is not required for the theorem.

To reproduce the supplementary numerical comparison, run `python CHECKER.py` in an environment with NumPy and SciPy installed (ordinary floating-point LAPACK). The recorded execution passed 16 deterministic assertions, checking convergence of two Fock-monomial Galerkin truncations and the predicted signed eigenvalue shifts for three separations. A second numerical run used larger radial/angular quadratures and a larger Galerkin space. The numerical tests verify neither exact transcendental identities nor the infinite-dimensional asymptotic and do not constitute independent mathematical validation.
