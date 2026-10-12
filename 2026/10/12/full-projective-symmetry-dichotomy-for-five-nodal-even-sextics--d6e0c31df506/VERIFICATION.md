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

Exact algebraic checks use `verify.py` and SymPy polynomial arithmetic over the rationals, including Gröbner ideals, Hessian determinants, restrictions to coordinate lines, and squarefreeness at infinity. The output `VERIFY_OK` confirms these identities for both explicit complex examples and the general coefficient-swap relation.

These machine checks do not enumerate the infinite projective group. Completeness of the full group follows from the five-node projective-frame argument and the ordinary-node tangent comparison in the written proof. The intrinsic genus and quotient calculations use standard Riemann–Hurwitz theory. No independent mathematical review has been performed.
