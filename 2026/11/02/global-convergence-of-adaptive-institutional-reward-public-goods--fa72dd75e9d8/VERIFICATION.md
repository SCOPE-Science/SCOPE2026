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

The accompanying `verify_adaptive_reward.py` was executed on the actual standalone script with SymPy, NumPy and SciPy installed. Its exact checks established Bernoulli relative-entropy derivative identities for each integer group size from 2 through 12, the rational N=5 equilibrium and linearization coefficients, and four exact timescale classifications. Nine log-odds-coordinate numerical integrations independently approached the predicted equilibrium for different positive timescales and initial states.

The general theorem is proved analytically using Lyapunov/LaSalle reasoning, not by simulation or finite symbolic sweeps. The numerical check uses logit state coordinates because direct floating-point integration of boundary-invariant polynomial flows can spuriously round an interior state onto an absorbing boundary. This is a numerical-stability safeguard, not a change to the mathematical ODE.

The publication comparison establishes best-knowledge originality under stated sources; no claim is made that every possible external paper is accessible. The theorem excludes boundary initial conditions and changes to the payoff or feedback functions.
