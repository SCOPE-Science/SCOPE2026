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

# Reproducible mathematical checks

Run `python3 verify_wheel_heat.py` with Python 3. No third-party package is needed. The program enumerates all integral graph-Lipschitz potentials with the hub fixed at zero for rim sizes five through ten and compares exact rational tight-spoke derivatives with the proved piecewise formula. The integrality of the vertices of the finite difference-constraint polytope justifies this exhaustive method in these **finite** cases.

It independently computes actual full wheel heat matrices by Poisson uniformization of a stochastic transition matrix, then evaluates the full graph-Lipschitz operator norm over the enumerated potentials. It tests examples on both sides of the contractivity thresholds, checks the exact commuting-factor identity against independent uniformizations, and checks the analytic peak formula at selected sizes and the tendency of those peaks toward two.

Expected final output: `ALL_WHEEL_HEAT_CHECKS_OK`. The full run's reported intermediate checks are `EXACT_SLOPE_OK`, `HEAT_UNIFORMIZATION_OK`, and `ENVELOPE_OK`.

The finite tests do not prove the result for every rim size, every conductance or all times; the required universal proofs are given in `RESULT.md`. The code uses ordinary floating-point tolerances for heat values and exact rational arithmetic for instantaneous derivative checks. No external or independent audit has been conducted.
