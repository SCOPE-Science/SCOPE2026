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

# Reproducibility

The standalone `check_circular_gap_triplets.py` uses only the Python standard library. It enumerates all distinct circular factors of lengths from one up to the full word length and records all circular positions intersected by any occurrence of each factor. It independently tests all two-element position subsets for every parameter triple with `1 <= a < b < c <= 12`, then verifies the exact asserted pair family and the constructive three-position witness. A separate direct-occurrence implementation independently checks all candidate pairs at `c <= 7` without using the factor masks.

Executed command: `python check_circular_gap_triplets.py 12`.

Observed output: `ALL_DISTINCT_GAP_CIRCULAR_ATTRACTOR_CHECKS_PASSED triples 220 two_phase 70 three_phase 150 max_gap 12`.

The code is an exhaustive *finite-range* checker only. The proof in `RESULT.md` establishes the statement for every admissible integer triple. The user may rerun the program with a different maximum gap. No independent audit has been performed.
