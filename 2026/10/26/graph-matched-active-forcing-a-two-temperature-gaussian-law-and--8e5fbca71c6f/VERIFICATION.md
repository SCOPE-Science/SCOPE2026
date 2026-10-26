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

# Reproducible verification

`verify.py` is a self-contained NumPy/SciPy script with a deterministic pseudo-random seed. Run `python verify.py` from a folder containing that file. It independently assembles the full drift and diffusion matrices of the projected \((y,v,f)\) process, solves their continuous Lyapunov equation using `scipy.linalg.solve_continuous_lyapunov`, and compares the returned stationary covariance against the theorem.

The verification script passed 80 independently drawn parameter sets: 40 connected randomly weighted graphs with \(n\in\{3,4,5,7,9\}\), and 40 cyclic rings with \(n\in\{3,4,5,8,12\}\). Each ring is additionally tested at five spatial force-correlation settings, including its exact cancellation threshold. Tests cover centered positional covariance, Gaussian velocity whiteness, displacement–velocity covariance, per-site active power, the exact temperature difference, the full covariance residual, and the sign of all distinct-site velocity pairs. The maximum absolute discrepancy was \(6.151\times10^{-14}\) for the tested parameter ranges. The tested critical \(\varepsilon_*\) values ranged from approximately \(-0.435480\) to \(-0.037695\).

The test computes the full linear-system covariance rather than recycling the proof's scalar mode equation, so it can detect a lost factor of mass, persistence, noise normalization, or graph eigenvalue. It is nonetheless a finite floating-point experiment: the analytic generator-moment identities, simultaneous diagonalization, and strictly positive Neumann inverse in `RESULT.md` establish the quantified result. The script does not test claims about detailed balance, temporal independence, or entropy production, and none of these are asserted.
