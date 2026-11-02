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

# Reproducibility and mathematical limits
The analytical proof and complete domain assumptions are in `RESULT.md`. The package includes `verify_all_rank.py`, a standalone Python 3 script using NumPy and SciPy to reconstruct finitely truncated Fock localization matrices, compute exact rational second-variation coefficients, and verify the finite-offset summations that yield the large-rank asymptotic coefficient.

Executed command: `python3 verify_all_rank.py`.

Observed output: `474 finite arithmetic, truncated-spectrum, and asymptotic checks passed.` The full package's checker was executed successfully. The tests include 240 exact rational finite-curvature checks, 180 polynomial-sum identities, 36 numerical eigenvalue second-difference checks, and 18 large-rank convergence checks. Numerical finite truncations, finite-degree identities, and finite samples of an asymptotic do not constitute independent proofs of an infinite statement. The trace-norm perturbation and factorial asymptotic arguments in `RESULT.md` are the mathematical proof.

Limitations: the result gives a fixed-rank second-order shape expansion for smooth mean-zero deformations, and an ordered two-limit large-rank formula for fixed trigonometric polynomials. No claim of uniform simultaneous high-frequency convergence or global equality uniqueness is made. No independent mathematical audit has been performed.
