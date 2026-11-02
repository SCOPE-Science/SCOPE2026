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

# Computational verification and limitations

Run `python verify.py` from this package with Python 3 and NumPy. The checker regenerates, without reading stored numerical answers, the killed-excursion renewal calculation; it separately solves a six-condition backward diffusion boundary-value problem and compares both with the closed formula on a grid of positive rates and distances. It tests dimensionless monotonic trends and the joint weak-rate asymptotics. It then simulates exact Brownian-bridge interval crossing at random gate/reset event times, with a fixed pseudorandom seed, reporting Monte Carlo deviations and sampling tolerances.

The event simulator is exact with respect to the continuous-time Brownian-bridge crossing probability between independently sampled switching/reset times. It is nevertheless a finite randomized check, not a substitute for the proof. The six-boundary linear systems are finite-dimensional numerical checks, not a proof of uniqueness. The exact result for all positive parameters follows from the closed-form renewal identity; the strict inequalities follow from elementary analytical bounds. The conditional initial-gate formulas are compared separately, before equilibrium averaging. No external certification, independent scientific review, or full literature-priority certificate is asserted.
