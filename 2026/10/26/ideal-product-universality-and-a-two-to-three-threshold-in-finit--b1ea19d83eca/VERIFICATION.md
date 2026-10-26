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

# Reproducibility and verification

Run `python3 artifacts/verify.py` using standard Python 3; there are no third-party dependencies. It constructs the algebra with basis consisting of a unit, radical generators and one socle generator. It enumerates **all** subspaces in reduced-row-echelon form, rejects those not closed under multiplication, and directly checks every pair and triple of remaining ideals. The checker uses the predicted Gaussian-binomial formulas only for comparison with independently enumerated ideals and products.

Actual runs succeeded for rank two, both alternating and diagonal bilinear forms over characteristic two, both hyperbolic and diagonal forms over characteristic three, a hyperbolic form over characteristic five, and rank three with a diagonal form over characteristic two. Counts: `(p,r,ideals,zero_pairs,zero_triples)` = `(2,2,7,25,288)` twice, `(3,2,8,30,430)` twice, `(5,2,10,40,846)`, `(2,3,18,101,5213)`. Terminal output: `VERIFY_OK`.

The checker only covers the listed prime fields and finite ranks. It does not independently establish arbitrary prime-power or mixed-characteristic cases; those are covered by the theoretical proof and ring-module argument. No independent audit or external certification is asserted.
