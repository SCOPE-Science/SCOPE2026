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

# Verification

The result is proved by explicit conditional-moment equations and an integrating-factor formula, rather than simulations. Run `python CHECK.py` in an environment with Python 3.10+ and SciPy. On the reviewed source the checker reported **78 passed assertions**; it covers exact rational event integrals, numeric ODE solutions for five reversal probabilities, the exactly soluble half-reversal case, the short-time cubic and large-time logarithmic increments, and independently sampled physical trajectories with a fixed random seed.

The exact scope is continuous-time one-dimensional motion with a fair initial sign, positive speed/rates, uniform-past position relocation, and independent Bernoulli reversal of the *current* sign at reset. The checker samples finite times only; asymptotic claims follow from the proof in `RESULT.md`. An independent audit has not been performed, and literary priority is not formally certified.
