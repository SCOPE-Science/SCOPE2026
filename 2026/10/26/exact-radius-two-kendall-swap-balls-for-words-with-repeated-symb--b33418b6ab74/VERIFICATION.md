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

The independent `verify_adjacent_swap_ball.py` routine generates all unique outcomes after zero, one, or two unequal adjacent swaps and compares their cardinality against a distinct local-counting implementation. It checked 88,397 words over the five alphabet-size/length grids documented in the result, plus the exact average, extremum, and extremizer multiplicity where applicable.

To reproduce, place `verify_adjacent_swap_ball.py` in the working directory and execute `python3 verify_adjacent_swap_ball.py`. The expected successful status begins `ADJACENT_SWAP_RADIUS2_PASS`.

The mathematical argument in `RESULT.md` independently proves the formula, extremal characterization, mean, and graph edge count for all stated lengths and alphabets; the finite program neither establishes infinity-range exhaustiveness nor proves absence of prior published coverage. Independent audit: not performed.
