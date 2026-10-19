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

# Checks reproduced

The bundled `verify.py` was executed with the ordinary Python 3 standard library. It explicitly constructs the characteristic-three fields of orders 3, 9, and 27; enumerates every ordered triple and its sum/square-sum fiber; verifies that all generic fiber sizes are exactly the field order and the exceptional fiber counts are 0, one copy or two copies of the field order; and checks the constant exact moment. It additionally tests 60 fixed-seed nonconstant complex inputs and two equality witnesses in each field against the four analytical bounds. See `verify_output.txt` for captured exact output.

The all-field theorem uses symbolic identities, not extrapolation from the finite cases. Critical proof steps are the translated generic-fiber orbit cardinalities; the arithmetic-progression parametrization of sum-zero fibers; the \(q\)-term Cauchy--Schwarz bound; the ordered-pair bijection for the remaining correlation; and the final constant-modulus Cauchy--Schwarz bound.

Limits: the tests do not certify uniqueness of equality-phase structure, quantitative stability or independent external verification.
