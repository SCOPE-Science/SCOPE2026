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

# Reproducibility and limits

Run `python VERIFY.py` with Python 3, NumPy and SciPy installed. The program is self-contained and builds the exact finite-dimensional cyclic matrices rather than relying on saved numerical arrays.

The verifier compares the closed sign criterion to the smallest eigenvalue of the diagonal form restricted to the mean-zero subspace for numerous mixed positive, negative, and zero coefficient patterns and lengths from 3 to 15. It then checks actual phase realizations, the individual oscillator frequency equations, stable/unstable spectra, and the additional algebraic zero eigenvalue at the nondegenerate fold. It also tests convergence of the scaled mixed-stability window to \(1/2\).

Numerical floating-point checks do not prove the universal theorem or certify all previous numerical assertions. The proof in RESULT.md, including the signed-form inertia reduction, strict concavity, and analytic asymptotics, provides the infinite-dimensional parameter and ring-length conclusions. The independent scientific audit remains unperformed.
