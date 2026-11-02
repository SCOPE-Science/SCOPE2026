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

## Exact arithmetic checks

Run `python verify_symbolic.py` with SymPy and `python verify_finite_fields.py` with a standard Python installation. The symbolic checker recomputes all coefficients and the squarefreeness, ideal, and gcd identities in characteristic five. The second checker computes Cartier blocks by fresh polynomial multiplication and iterates Frobenius-semilinear matrices, and checks curve smoothness by Euclidean gcd over the coefficient fields.

The successful symbolic output is `SYMBOLIC_GENUS6_OK`. The finite-field output includes `F 5 smooth 21`, `F 25 smooth 599`, and ends with `FINITE_FIELDS_GENUS6_OK`.

## Limits
The geometric proof for algebraically closed fields is in `RESULT.md`; enumeration over two finite fields is corroborative rather than an infinite proof. These checks have not undergone an independent external audit or validation. No Newton-polygon or complete isomorphism classification is asserted.
