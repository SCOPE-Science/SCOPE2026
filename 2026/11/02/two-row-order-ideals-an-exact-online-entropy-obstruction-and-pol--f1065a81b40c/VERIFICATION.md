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

Execute `python3 verify_grid_ideal_learning.py` from this folder. The verifier uses only the Python standard library, computes interval-bound Littlestone dimensions for 1 through 52, propagates 53 through 60 by embedding and the concept-count bound, checks twenty-four representative sizes independently using concept bitsets, and proves the seven-column upper obstruction by enumerating every query's branch cardinality. It asserts the exact threshold list and prints `TWO_ROW_GRID_IDEALS_ALL_NEW_CHECKS_PASS`.

The finite arithmetic sample for the two-bit inequality is not a proof for all integers; the inequality is proved in `RESULT.md`. Source comparisons establish qualified originality, not comprehensive historical priority. Independent audit has not been performed.
