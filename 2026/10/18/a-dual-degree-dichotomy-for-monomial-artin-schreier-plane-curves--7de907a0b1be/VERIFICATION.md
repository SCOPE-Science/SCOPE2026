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
The standalone `verify_as_dual.py` uses exact polynomial elimination over prime fields. It checks \((p,m)=(2,5),(3,5),(3,7)\), computes the eliminated affine dual relation, verifies its total degree equals \(mp\), and tests that all its monomial exponents are multiples of \(p\) in the predicted inseparable cases. This is supplementary finite verification, not proof of the theorem for all parameters.

The general argument uses the unit-normalized cusp at infinity, its valuation semigroup, a generic polar intersection calculation, and function-field recovery from the Gauss coordinates. The case \(m=p+1\) is included as the smooth-at-infinity boundary. No independent audit was performed.
