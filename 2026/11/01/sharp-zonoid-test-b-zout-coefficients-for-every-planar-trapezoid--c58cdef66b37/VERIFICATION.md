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

The analytic proof identifies the exact affine normal form, six difference-body and polar vertices, fifteen determinant pairs, and the mixed-area formulas. The segment identity is universal, and positive Minkowski bilinearity plus continuity extends it to all planar zonoids. Independent of the finite checker, the coordinate segment pair proves optimality.

The bundled `verify.py` requires only Python 3 standard-library modules. Invoke `python3 verify.py`. It uses exact rational arithmetic to verify all displayed polar determinants and constraints over 276 positive rational parameters, the equality segment pair, and 25 random zonotope instances per parameter. Verified output:

`VERIFY_OK trapezoid zonoid Bezout: exact rational checks 21282`

The checker is finite and does not establish the universal theorem by enumeration. It also does not verify publication priority or treat arbitrary non-zonoid auxiliary sets. Independent mathematical audit: not yet performed.
