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

The source verifier `verify_return.py` uses only Python standard-library exact `fractions.Fraction` and integer binomial arithmetic, together with finite numerical checks of the scaling profile. The baseline direct recurrence comes from affine branch image intersections, independently of the Catalan generating-function derivation. Running `python3 verify_return.py` produces `PASS: 934 exact/rational and numerical assertions`.

The checked finite rational parameters are 1/5, 1/3, 1/2, 2/3, 3/4, with all return lengths up to eleven; there are forty exact critical-binomial tails and fifteen near-critical numerical comparisons. Assertions cannot certify asymptotic limits: the proof does so via a first-passage equation, Stirling bounds, uniform summability and Riemann sums.

Independent audit has not been performed.
