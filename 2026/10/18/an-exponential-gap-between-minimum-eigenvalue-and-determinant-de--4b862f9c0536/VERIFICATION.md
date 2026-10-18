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

The supplied `verify_fock.py` numerically reconstructs the finite Fock-polynomial normalized evaluation matrix for regular and perturbed angular configurations and checks its Hermitian Gram eigenvalues against the factorial-weighted Fourier spectrum. It also compares determinant/least-eigenvalue bounds for randomly perturbed configurations, solves the truncated-Poisson mean equation at moderate degrees and probes the asymptotic conditioning gap for larger degrees without numerically resolving exponentially small differences in the root.

Reproduction: install NumPy and SciPy for Python 3.10 or later, then run `python verify_fock.py`. The verified execution in `verify_fock_output.txt` reports `checked_cases 341`, maximal finite regular-spectrum absolute error `3.55e-15`, and `ALL CHECKS PASS`.

The proof of the all-degree statements is analytic (Gram identities, equality rigidity, strict one-variable optimization and Stirling expansion) and is presented in `RESULT.md`. Floating-point tests do not prove infinite assertions, rule out earlier literature, or substitute for independent review.
