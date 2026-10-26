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

The accompanying standalone `verify.py` was executed with Python, SymPy and SciPy and printed `VERIFICATION_OK`. It checks the general algebraic identity \(\Phi'/\Phi=W/[x(1-x)d]\), the exact threshold \(K_c=18\), the critical resource integral and quadratic solution, and numerical trajectories of the original nonlinear differential equations at capacities \(K=12,18,30\). The numerical runs reproduce the three terminal regimes and the invariant \(Nx^2/(1-x)^3=36\) to the stated tolerances.

The theorem for arbitrary finite capacity and arbitrary positive strict Prisoner's-dilemma payoffs is proved analytically, not by finite experiments. The ODE checks are finite-horizon tests and do not certify all solutions or all parameters. Literature comparisons are best-knowledge searches, not a mathematical proof of novelty; independent audit has not been performed.
