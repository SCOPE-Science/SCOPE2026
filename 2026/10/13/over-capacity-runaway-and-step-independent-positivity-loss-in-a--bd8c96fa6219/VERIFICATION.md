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
# Reproducibility and mathematical checks

The exact-rational executable `verify.py` is included in this package, requires Python 3 and no third-party packages, and prints `VERIFY_OK`. It tests the fully admissible parameter witness, both first-step population fractions, the geometric lower factor, and the sample finite-exit inequality; a 65-digit decimal sample independently gives first nonpositive prey index 16, within the rigorous index bound 53.

The **proof**, rather than a finite numerical orbit, establishes the two universal statements: monotone invariant region for the ODE and finite positive-quadrant exit for every forward-Euler step. The key unbounded-time inputs are \(g'(v)=K(1+d)/(K+dv)^2>0\), the exponential lower/upper bounds on predator density, integrability of the exact logarithmic deficit, and the argument using geometric growth of predator density until the earliest Euler exit.

The model equations and time-step conventions were compared directly to the cited motivating primary article. There is no certified proof assistant, independent audit, finite-time clinical/ecological measurement, or empirical validation. The quantitative constant in the continuous limit depends on the initial conditions.
