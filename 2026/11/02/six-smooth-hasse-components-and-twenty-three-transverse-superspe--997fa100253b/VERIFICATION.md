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

# Reproducibility

Run `python3 verify_symbolic.py` with SymPy and `python3 verify_field.py` with Python 3. The symbolic script confirms the three Ciani plane-quartic Hasse coefficients in characteristic seven and factors them into the elliptic quotient expressions, emitting `CIANI_CHAR7_SYMBOLIC_FACTORIZATION_OK`. The finite-field script exhausts all \(49^3=117649\) ordered parameter triples in the explicit quadratic extension, checks smoothness and the three rank equations, and emits `CIANI_CHAR7_F49_EXHAUSTIVE_23_TRANSVERSE_POINTS_OK`; it also checks that all \(23\) intersection-gradient determinants are nonzero.

Completeness over the algebraic closure uses Ohashi's published field-of-definition theorem for superspecial standard Ciani quartics. The finite-field sweep alone would not justify that geometric implication. The result addresses coefficient-marked parameters, not geometric isomorphism classes. These checks constitute self-review only; independent external audit or validation has not occurred.
