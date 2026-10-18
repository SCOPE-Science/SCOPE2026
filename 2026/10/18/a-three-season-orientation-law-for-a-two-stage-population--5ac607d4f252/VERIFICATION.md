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

The symbolic checker `leslie_symbolic.py` was executed and returned PASS. It verified the exact formula for the difference between the traces of the two products, their identical negative determinants, and the rational witness for opposite sides of the unit-growth threshold.

The independent checker `leslie_fraction.py` was executed and returned PASS. It uses standard-library `Fraction` arithmetic and direct two-by-two multiplication. It reproduced all exact rational quantities and checked the identities and two cyclic classes on 1,728 additional parameter triples.

These computations supplement, rather than replace, the universal direct algebraic proof in `RESULT.md`. No finite numerical sample establishes originality, a long-run stochastic survival theorem, or a nonlinear population model. Independent audit has not been performed.
