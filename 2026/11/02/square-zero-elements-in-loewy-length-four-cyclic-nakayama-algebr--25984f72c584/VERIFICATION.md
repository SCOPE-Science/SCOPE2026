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

Run `python3 nakayama_square_zero_verify.py` with an ordinary Python 3 standard-library installation. Expected closing line:

`CYCLIC_NAKAYAMA_LENGTH4_SQUARE_ZERO_OK 11 6x13`

The checker calculates square-zero elements by direct path multiplication (not by calling the main formula) and enumerates every possible pair of degree-one and degree-two coefficient vectors at eleven small finite-field configurations. It independently computes matrix ranks, weighted independent-set sums, transfer traces, and recurrence values for fields of sizes 2, 3, 4, 5, 7, and 9. Its \(\mathbb F_4\) computation uses arithmetic modulo \(t^2+t+1\), not integer arithmetic modulo four. There are 11 exhaustive configurations and 78 transfer/recurrence tests over six sizes and thirteen cycle lengths.

The proof in RESULT.md is the general-field justification. Exhaustive checks on small instances do not establish the full infinite-parameter theorem. No third-party independent audit has been completed.
