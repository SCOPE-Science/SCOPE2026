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

# Reproducibility

Run `python verify.py` with Python 3 and NumPy, SciPy and SymPy. Actual replay was successful. It checks exact symbolic frequency equations, quadrature evaluation of the exact threshold, monotonicity over six resident imbalances, three near-boundary beta asymptotics, and six ODE trajectories under small/large inocula. The global classification, separatrix equality case, and asymptotic rate are proven analytically in RESULT.md rather than established by finite tests.

The ecological source is arXiv:2609.34956v1. Its numerical extinction cutoff is not imposed here, so positive dynamical states are allowed to tend continuously to zero.
