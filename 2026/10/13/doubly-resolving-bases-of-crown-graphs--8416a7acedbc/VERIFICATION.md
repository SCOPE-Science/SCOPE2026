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

The proof was reconstructed directly from the crown graph distance table. For each pair type, the difference map \(s\mapsto d(u,s)-d(v,s)\) was computed explicitly. The critical checks are:

- two omitted matched pairs make a same-side difference profile constant, proving that every doubly resolving set omits at most one pair;
- if one pair is omitted, its matched vertices require selected vertices on both bipartition sides;
- every adjacent cross pair has exactly two complementary transversal level sets, and these are the only cross-pair obstructions;
- a size-\(n-1\) transversal-with-one-hole avoids all cross-pair obstructions exactly when it has at least three selected vertices on each side;
- at size \(n\), a doubled pair automatically defeats every cross-pair transversal obstruction, while a full transversal fails exactly at side weights \(2\) and \(n-2\).

The bundled `verify.py` independently constructs the graphs, computes distances by breadth-first search, tests the defining condition, and exhausts all subsets smaller than and equal to the claimed optimum for \(3\le n\le9\). Expected output:

`VERIFY_OK n_range=3..9 subset_checks=142833 basis_checks=59467 bases=3096 max_order=18`

The finite computation does not establish the theorem beyond \(n=9\); the symbolic distance-level argument supplies the proof for every \(n\ge3\). No independent audit has been performed.
