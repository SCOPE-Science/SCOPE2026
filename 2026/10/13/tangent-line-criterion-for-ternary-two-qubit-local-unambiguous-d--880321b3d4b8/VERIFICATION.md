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

The universal check is analytic. For each state, the orthogonal complement of the other two states is a two-dimensional plane. In an adapted basis \((C,D)\), the overlap with the target state is proportional to the \(D\)-coordinate, while the product-state condition is the homogeneous quadratic \(\det(sC+tD)\). The target is undetectable exactly when this quadratic has only the state-orthogonal point as a double projective root.

The bundled `verify.py` was executed from its packaged path. It reconstructs the adapted plane data for the Bell-pair-plus-product obstruction and checks the coefficient criterion against direct roots of the determinant polynomial for one thousand random linearly independent complex triples. The execution returned:

`VERIFY_OK random_triples=1000 known_obstruction=passed`

The random computation is a regression check only; it does not establish the universal statement. The proof in `RESULT.md` supplies the exact quantifiers and covers the degenerate case in which the determinant restriction vanishes identically.
