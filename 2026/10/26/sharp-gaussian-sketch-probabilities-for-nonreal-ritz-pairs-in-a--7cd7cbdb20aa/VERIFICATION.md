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

# Reproducibility and verification

The supplied `verify.py` is a self-contained standard-library Python program. Execute `python3 verify.py` to repeat exact-rational checks of the sketched projection matrix, the nonreal discriminant witness, seeded Gaussian comparisons of the radial Student distribution and exact event probability, and numerical consistency checks for the Laplace prefactor.

The exact witness has \(A\) with diagonal entries \(5\) and off-diagonal couplings \(1\), \(2\); it is positive definite since its eigenvalues are \(5,5\pm\sqrt5\). The three specified sketch rows produce projected eigenvalues \(5\pm i\). Numerical tests include sketch sizes \(2,3,5,9\) and asymptotic tests at \(\nu=500,2000,8000\) under several coupling ratios. These checks are for transcription, independent arithmetic reconstruction, and computational reproducibility; the exact density, positivity of probability, and sharp asymptotic rely on the written proof, not the finite tests.

The analytical proof uses the two-variable Gaussian regression/Student distribution, an exact discriminant inequality, a circle intersection formula, and a one-sided Laplace expansion. No external mathematical certification or independent audit has been performed. The derivation is restricted to a three-state symmetric positive-definite Lanczos triple with iid real Gaussian sketching and exact arithmetic.
