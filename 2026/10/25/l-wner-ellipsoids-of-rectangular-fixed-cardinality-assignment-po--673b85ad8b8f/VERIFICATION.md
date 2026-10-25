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

The proof uses direct matrix projections, exact vertex covariance, a global arithmetic–geometric mean determinant bound, and integer inequalities. A separate standard-library exact-arithmetic checker `verify.py` enumerated 25 small polytope cases with 1016 vertices and made 110920 rank-spectrum comparisons, ending in `VERIFY_OK exact_enumerated_cases=25 exact_vertex_contacts=1016 rank_spectral_order_comparisons=110920`.

Run `python verify.py` next to this file to reproduce the finite checks. Their ranges are not an exhaustive infinite proof; the all-parameter arguments and the dimension changes are stated in RESULT.md. Bibliographic priority is not independently certified.
