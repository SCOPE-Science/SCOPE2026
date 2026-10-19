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

The proof in `RESULT.md` is algebraic for all fields and all indicated dimensions. The script `verify.py` independently builds actual Lie brackets from defining matrices and counts joint-adjoint ranks and commuting tuples by exhaustive iteration over small prime fields. Run `python3 verify.py` in a directory containing this file; the expected terminal marker is `VERIFY_OK`.

Checks performed: the two distinct five-dimensional Lie algebras over fields of orders 2 and 3 for tuples of length two, and over the field of order 2 for length three; a four-dimensional rank-two instance over the field of order 3 for tuples of length two. The script also verifies the rank discrepancy of the squared defining endomorphisms. The finite computations cannot establish the arbitrary-field assertions or any publication priority. The irreducible-component proof uses the rank-one outer-product parametrization, not experimental enumeration.
