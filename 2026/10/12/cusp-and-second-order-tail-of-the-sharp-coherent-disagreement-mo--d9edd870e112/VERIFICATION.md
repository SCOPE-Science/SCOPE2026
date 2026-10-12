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

`verify.py` performs two independent checks of the new calculations. First, it uses exact `Fraction` arithmetic to verify the Taylor series of \(\sqrt{1+6t+t^2}\), derive the logarithmic expansions of the upper optimizer branch, and recover the relative coefficients \(-3/2\), \(79/24\), and \(-145/16\). Second, it brackets the published crossover near \(2.2575078689\), computes the corresponding \(d_0\), and checks that \(\log(2d_0)\) is strictly positive and numerically agrees with the value stated in the result.

The finite numerical crossover check is not used as a proof of uniqueness of the crossover; uniqueness and the exact piecewise optimizer formula are taken from the cited theorem. The asymptotic proof is symbolic, not an inference from finite samples.
