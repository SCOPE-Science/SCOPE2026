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

Run `python3 verify.py` with Python 3 standard library. It constructs every multiplication table from the group presentation, uses a polynomial-basis multiplication for the four-element field, and exhaustively evaluates the square-zero predicate for all five group algebras over fields of orders two and four. It also tests all square-zero ordered pairs for commutation in the binary dihedral and quaternion cases and all unit-conjugacy orbits for the binary dihedral case.

Expected final marker: `ORDER8_GROUP_ALGEBRA_SQZERO_OK`.

The printed exhaustive tests do not certify the theorem over every field. The uniform justification is the coefficient and commutator proof in RESULT.md. The full result has not undergone independent validation.
