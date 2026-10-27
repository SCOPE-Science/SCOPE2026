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

The accompanying `verify.py` uses only the Python 3 standard library. Execute `python verify.py` from the extracted package directory.

The script exhaustively inspects all 46,232 permutations of sizes \(2,\ldots,8\). For each permutation it independently reconstructs the cycle decomposition, counts all one-line successions and compares exact rational mixed moments with both the aggregate and positionwise stated formulas. It reports 183 direct comparisons. For dimensions \(5,\ldots,150\), it also evaluates the loop/path/disjoint-path expectations and their weighted sums using exact rational arithmetic, reporting 1,136,245 algebraic comparisons.

Finite enumeration is not an infinite proof. The all-size argument is the contraction bijection followed by the elementary formula for cycles containing zero, one or two marked vertices, detailed in RESULT.md. Small dimensions \(2,3\) have complete direct enumeration.

The mathematical novelty conclusion is based on comparisons with the cited source material and relevant research records; it has not been independently validated. Source-access and historical-priority uncertainty are documented separately in REVIEW.md and AUDIT.json.
