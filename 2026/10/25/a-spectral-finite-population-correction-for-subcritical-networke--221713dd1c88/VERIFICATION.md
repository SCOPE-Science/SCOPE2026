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

# Reproducibility checks

Run `python verify.py` with a standard Python 3 interpreter, without third-party dependencies. It uses exact `fractions.Fraction` arithmetic to compute the resolvent coefficient for one-, two-, and three-patch mixing matrices, checks the analytical integrated second-moment equations, and independently enumerates all reachable states of small finite SIR chains to compute exact expected final sizes. For \(R=1/2\) and the two-patch swap-matrix interpolation, the expected exact coefficient values are \(32/9\), \(4\), and \(8\), respectively.

The program establishes consistency of finite examples, matrix algebra and claimed formula specializations. It is not an exhaustive test over all stochastic matrices or an infinite-population proof. The accompanying analytic coupling and moment proof carries those quantified conclusions. Independent audit has not been performed.
