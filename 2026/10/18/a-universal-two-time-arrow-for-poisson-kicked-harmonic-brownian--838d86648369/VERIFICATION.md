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

The independently implemented `verify.py` runs using Python's standard library and prints `passed 2310 exact rational checks; quartic peak at a=1/sqrt(3)` when all assertions pass. The checker builds exact stationary cumulants, generates raw moments via the moment-cumulant recurrence, constructs independent OU innovations, and checks the two different temporal orderings via a separate binomial moment convolution. It covers biased and symmetric discrete kicks, zero and positive thermal diffusivity, multiple decay rates, and lag factors. The global distributional nonexchangeability conclusion is a proof from the uniquely determined bivariate Lévy measure, not an extrapolation from finite calculations. No human or independent expert validation has been performed.
