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

The analytic proof and the exact domains are in `RESULT.md`. The runnable file `verify.py` evaluates the stationary-quantile even moments in both the edge-cluster and smooth regimes, verifies symbolic beta-polynomial expansions, and checks the cumulant identity and positive root. Command: `python verify.py` (Python 3 with SymPy and mpmath).

The source stationary measure is treated as a documented mathematical premise, as explicitly declared in the main result. The checker does not establish the microscopic large-population limit. Finite quadrature cannot establish an all-parameter, all-order theorem: that step follows from the covariance/likelihood-ratio argument in the proof. No separate independent scientific audit is represented by these checks.
