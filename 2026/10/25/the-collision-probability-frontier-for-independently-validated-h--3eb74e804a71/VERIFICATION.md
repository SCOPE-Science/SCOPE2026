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

The standalone `verify.py` requires Python 3 standard library only. Run `python3 verify.py` in the extracted file directory. It uses `Fraction` arithmetic to evaluate all ordered update/validation index pairs, compare the exact stochastic hypergradient expectation to the collision-polynomial formula, and check one-step raw and safeguarded squared-error multipliers. The seeded cases cover dimensions two through six and additional simplex-floor grids through dimension fourteen. It also explicitly enumerates exact validation-gated state distributions through four steps for the four-equally-sampled-component example. No numerical tolerance is used.

The complete infinite-dimensional-parameter claim is proved algebraically in `RESULT.md`. Finite verification does not establish asymptotic or all-parameter statements by itself. The acceptance review is self-review only; the independent audit status is not performed. The online-learned scalar step trajectory is not simulated or certified: the result applies only to a step frozen at the population feedback minimizer.
