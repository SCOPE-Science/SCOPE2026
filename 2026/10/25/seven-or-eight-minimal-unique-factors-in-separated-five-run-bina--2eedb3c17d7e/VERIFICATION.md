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

The proof establishes the infinite separated-run classification, exact conditional generating functions, and an asymptotic unconditional distribution. `verify.py` computes actual contiguous factor multiplicities, including overlapping occurrences, without using the classification to decide uniqueness. It independently checks all 1,800 separated parameter tuples with coordinates at most seven, full unrestricted histograms at lengths 15, 20, and 25, and generating-function coefficient counts at lengths 13 through 32. Run with Python 3: `python verify.py`.

Finite enumeration is not a proof for unbounded run lengths. The classification does not include the finite-length exceptional tuples violating separation.
