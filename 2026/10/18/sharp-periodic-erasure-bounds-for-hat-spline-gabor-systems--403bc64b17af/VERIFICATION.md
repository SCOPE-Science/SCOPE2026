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

# Computational verification

Execute `python3 checker.py` using only Python 3 standard library. The checker is bundled with this result and reproduces these performed checks:

- `EXACT_SUBSET_CHECKS 2035`: exact rational evaluation of every nonempty subset of the cyclic grid for all sizes \(2\le m\le10\), comparing independently coded piecewise-interval maximization of the Zak quadratic symbol against the cyclic-cut variance expression. Every case also verifies the proposed universal lower value and exact cyclic-block equality classification; for \(k\ge2\), every tested lower bound is positive.
- `NUMERICAL_SYMBOL_CHECKS 1300`: seeded independent evaluations of the complex two-term Zak polynomial and its trigonometric quadratic expansion for randomly selected masks and unit-torus coordinates.
- The checker ended with `VERIFY_OK`.

No Monte Carlo experiment establishes the all-size result; the proof is the Zak multiplier identity, exact lift-cut equivalence, and integer-spacing variance bound. Calculations use Python `Fraction` for combinatorial values and floating-point arithmetic only for the supplementary phase comparisons.
