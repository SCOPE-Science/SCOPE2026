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

# Reproduction and limits

The `verify.py` program uses `sympy` and `mpmath` and can be run directly with `python verify.py`. It checks exact identities for the two conditional payoff gaps, strict threshold increases on representative parameter values, the rational witness using its analytical root, the universal limiting coefficient and its defining transcendental equation, convergence at rescaled strengths, and 995 sampled instances of the uniform endpoint bound.

Its output on the packaged source was:

```text
PASS: symbolic payoff identities, intensity monotonicity, witness transition,
      universal crossover and uniform-tail bound, 995 bound cases
critical_s 1.48157763404041879720317714072
z_star 0.957504024077268740676501530502
C 0.138081611719414379492109806899
```

Symbolic identities are exact; arbitrary-precision checks use 55 decimal digits and comparisons with explicitly stated error margins. The general monotonicity, existence/uniqueness, global convergence, and inverse-intensity optimization are independently established by inequalities and compactness arguments in `RESULT.md`; finite numerical checks alone would not establish them. The calculation is for the specified shared-environment/composition-averaged-payoff protocol and does not test other stochastic imitation mechanisms. Independent scientific audit has not been performed.
