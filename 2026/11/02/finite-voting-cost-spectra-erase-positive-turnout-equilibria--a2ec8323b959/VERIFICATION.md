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

# Reproduction and boundaries

Run `python3 verify_cost_atoms.py` alongside the accompanying mathematical statement. The checker uses only the Python standard library and rational arithmetic. Expected output:

`VERIFY_OK active_strict_improvements=738 zero_turnout_profitable_deviations=1620 no_deviation_checks=30966 continuum_best_response_samples=2002 empirical_cost_distributions=99`

It exercises seven finite cost distributions, three full-support voter-CDF families, a thirteen-point rational policy grid, the continuous uniform-cost best-response inequalities on 1,001 policy positions per candidate, and empirical cost CDFs for \(2\leq m\leq100\). Every positive-turnout profile checked has a constructed strictly improving move that preserves its active cost set; every tested inactive candidate outside the exact equilibrium square has an endpoint deviation yielding positive turnout. All outcomes are recomputed from the specified vote-mass formulas.

The checker does not establish an infinite theorem or search all measurable electorates. The proof instead uses strictly increasing CDFs, finiteness of cost support, exact threshold geometry and a quadratic global-best-response argument. The empirical-CDF and payoff-uniformity bounds are analytical. The result concerns strict participation thresholds and unconditional vote-mass utility; changing either can change the game.
