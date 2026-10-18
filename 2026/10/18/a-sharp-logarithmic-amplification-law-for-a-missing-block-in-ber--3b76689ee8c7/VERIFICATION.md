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

# Verification record
The analytical proof is fully supplied in `RESULT.md` and does not rely on finite numerics. `verify.py` is a Python-standard-library checker, executed successfully from this package: `PASS: 6200 exact-rational and numerical consistency assertions`.

It reconstructs the missing block from actual integer nodes, applies alternating signs in the new sorted order, verifies exact rational numerator and denominator decompositions at many interior sample points, and checks the uniform lower bound for ordinary cells. A separate numerical part computes the midpoint Lebesgue response and compares with a quadrature evaluation of the integral defining the logarithmic coefficient.

These tests cannot certify the uniform asymptotic theorem, historical novelty, or any assertion for a growing deletion length. The rigorous proof instead uses alternating-series remainders, reciprocal harmonic sums, and a strict integral minimum. The full primary literature could not be accessed here; potential equivalent prior work has not been eliminated.
