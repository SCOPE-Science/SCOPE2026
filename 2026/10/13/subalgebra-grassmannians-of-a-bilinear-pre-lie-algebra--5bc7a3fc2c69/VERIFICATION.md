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

Running `python3 verify_subalgebra_census.py` enumerates every linear subspace in RREF and directly verifies closure under the displayed multiplication, the exact geometric subalgebra criterion, and the recursive rank polynomial. The twelve cases cover `GF(3)` in generator dimensions 1–4 and `GF(5)` in dimensions 2–3, each for diagonal nonsquare and square representatives. Output ends in `VERIFY_OK`; the examples include both discriminant signs in the even ambient-dimensional case. The primary infinite-dimensional-parametric proof is algebraic, not empirical. Prime-power extension fields, characteristic two, and degenerate symmetric forms have not been exhaustively checked, even though the structural theorem covers the latter two.

The source inspection and scientific evaluation are same-model only. Independent audit remains not performed.
