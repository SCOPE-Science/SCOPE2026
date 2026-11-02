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

# Reproducibility verification

Execute `python3 verify.py` using standard Python 3.8 or later. The program uses only `fractions`, `itertools`, `collections` and `functools` from the standard library. It verifies all ten exact strict-convexity bounds on admissible support sizes, counts the fifteen pair occurrences and six vertex degrees of the stated design, independently computes expected coverage times from inclusion-exclusion and a 64-state absorbing recursion, checks the full-model difference, and verifies the five-symbol cycle complement comparison.

Executed check: **PASS; 53 exact rational assertions**. Finite code is supplementary; the bound on all possible supports is proved by strict discrete convexity and the complete ten-case arithmetic in RESULT.md, and therefore does not rely on a sampling study or a partial search.

The original scientific sources were inspected for possible statement coverage. Priority and the proof have not been checked by an independent auditor. Multisets of blocks, unequal selection probabilities, larger ground sets and distributional ordering are outside the claim.
