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

The general theorem is proved symbolically in `RESULT.md`. The standalone Python 3 script `verify.py` checks its finite implications without external dependencies and without loading other research files.

The script exhaustively tests all self-functions on each of 15 complete two-level frames with total cardinality 2 through 6. It derives boundedness directly from successor-set equality at every point, independently derives modal-algebra preservation from the definition of \(\Diamond\) through four worlds, explicitly tests idempotence and stable image cardinality, and compares observed rank distributions with the six closed expressions.

Successful replay:

`VERIFY_OK cases=15 candidate_functions=246606 bounded_maps=9514 direct_modal_checks=826 exact_comparisons=444`

The 444 comparisons include the three spectra for all small frames and total-identity checks across \(1\leq p\leq19\), \(1\leq q\leq7\). Exhaustive checks stop at six worlds; arbitrary cardinalities follow from the written proof and the matrix-tree determinant, not by extrapolating numerical data.

Run: `python3 verify.py`
