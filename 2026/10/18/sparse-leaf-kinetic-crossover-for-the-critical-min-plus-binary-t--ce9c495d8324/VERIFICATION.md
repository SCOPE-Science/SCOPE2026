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

## Reproducibility

Run `python verify.py` using Python 3 and its standard library. The checker independently propagates two constructions: the full random binary-tree recursion on nonnegative integers, and the positive-conditional recursion. It uses exact `fractions.Fraction` values for the finite-state identities.

The run returned `PASS: 804 exact/finite-check assertions and kinetic diagnostics`. It covers five rational leaf probabilities through six depths, three additional exact CDF recurrence families, finite stochastic-dominance comparisons, and four scalar finite-clock checks against an independent Riccati solution. The result is a deterministic test, not a Monte Carlo calculation.

The full infinite-state total-variation estimate, probability-flow existence, and diverging-clock escape claim are proved mathematically in `RESULT.md` using the exact conditional identity, Lipschitz estimates and stochastic monotonicity; these are not inferred from finite experiments. The tests do not establish priority or independent mathematical validation.
