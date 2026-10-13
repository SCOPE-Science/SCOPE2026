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

The proof was checked symbolically and against a standalone finite verifier. The verifier reconstructs each crown graph from the definition, enumerates its dominating vertex pairs, and then exhausts every edge-deletion subset for \(n=3,4,5\). For every deletion subset it compares direct survival of a dominating pair with the auxiliary index-cover condition and matches the full coefficient vector against the inclusion-exclusion formula. It also checks the coefficient formula and minimum multiplicities through \(n=12\).

Recorded replay:

`VERIFY_OK n_exhaustive=3..5 subset_checks=1052736 pair_survival_checks=5218737 coefficient_checks=580 formula_range=3..12`

The bounded computation is only a consistency check. The infinite statement rests on the proof that the deleted-matching pairs are exactly the dominating two-sets and that such a pair survives precisely when its index is isolated in the auxiliary graph.
