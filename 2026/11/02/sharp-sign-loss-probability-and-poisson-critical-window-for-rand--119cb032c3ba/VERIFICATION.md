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

# Verification of sign-law and Poisson window

The direct tableau calculation gives the rational multiplier and the quadratic numerator. Exact symbolic checks in `verify.py` reconstruct the tableau multiplier, endpoint values, critical tangency, discriminant, interior vertex and mean-multiplier derivative. The remaining proof uses positivity of the denominator, convexity of the numerator in the random tableau parameter, length of an interval under the uniform law, independent Bernoulli sign indicators, and the binomial Poisson limit.

Run `python verify.py` with Python 3.10+ and SymPy 1.10+. The actual execution passed 1041 rational/grid/critical-window/Monte-Carlo checks and 12 symbolic assertions. The seeded Monte Carlo run used 50,000 draws at each of six normalized steps. The result was independently recalculated in exact fractions for a dense grid of rational parameters. The standalone checks are illustrative and finite; the universal claim and weak limit require the written proof.

No external audit or independently performed validation is claimed. The result does not address positivity for systems or nonlinear dynamics.
