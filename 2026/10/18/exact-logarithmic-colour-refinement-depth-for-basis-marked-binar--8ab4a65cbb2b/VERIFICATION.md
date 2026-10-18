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

# Verification and limits

To reproduce the finite checks using Python 3 (no external packages):

```sh
python checks/check_refinement.py
python checks/check_combinatorics.py
```

The direct checker builds each labelled point--line incidence graph for dimensions 2 through 9, performs full synchronous colour refinement, and checks exact point partitions at each round together with the first completely discrete round. The largest graph has 511 point vertices and 43,435 line vertices. The separate combinatorial checker constructs no graph and performs no colour refinement; it computes incidence-type multisets directly through binary addition, checks their predicted partition through dimension 10, and checks the explicit last-stage line-collision construction through dimension 17. Recorded exact outputs are `checks/refinement_output.txt` and `checks/combinatorics_output.txt`.

Finite tests do not establish an infinite-family theorem. The all-dimension statements are proved combinatorially in `RESULT.md`. Originality is qualified by imperfect access to specialized earlier literature. Independent scientific validation has not been performed.
