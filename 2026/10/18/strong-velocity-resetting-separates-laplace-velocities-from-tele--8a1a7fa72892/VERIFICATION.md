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
# Mathematical and numerical verification

The proof uses (i) exact two-sided stationary Poisson-reset ages, (ii) a mean-square comparison with signed independent exponential age, (iii) exponentially decorrelated marked ages at separated observation times, (iv) the exact \(e^{-(r+2\lambda)t}\) product covariance for age and orientation, and (v) a finite-grid maximal inequality. Every step is explained in `RESULT.md` and is valid uniformly on fixed finite horizons under its stated assumptions.

The supplementary script `verify.py` uses event-driven resets and flips, fourth-order Runge–Kutta integration of the deterministic segment, and a fixed NumPy seed. The tests at rates 20 and 80 for both \(g(v)=\tan v\) and \(g(v)=\tanh v\), with flip rate 0.8, check \(\mathbb E|rV/\Sigma|\to1\), \(\mathbb E(rV/\Sigma)^2\to2\), a positive-lag covariance, and scaled finite-horizon spatial variance. They passed the script's explicitly programmed tolerances. Separate exact algebraic moment identities for linear drag furnish an independent check of the asymptotic amplitude. Monte Carlo samples are finite and neither prove convergence nor validate general-drag long-time diffusivity interchange.

The published motivating model and numerical results were inspected in its accessible full text. The comprehensive general partial-resetting work by Olsen and Löwen could not be inspected beyond abstract level, leaving documented originality uncertainty. Independent scientific validation is unperformed.
