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

# Reproducibility and verification

The complete theorem is proved by an explicit classification of uncovered row-column-cross intersections; no finite computation is needed for the universal formulas. The standalone script `total_sequence_checker.py` is an independent check using the original adjacency and legal-next-vertex conditions.

Run `python total_sequence_checker.py 6` with Python 3 standard library. This checks every unordered dimension pair \(2\le m\le n\le6\). It enumerates each full ordered sequence by recursive legal-extension search; there are exactly 1,469,556 completed sequences across all 15 test cases, with 1,438,200 length-four histories. Independently, it checks inclusion-minimal four-sets by vertex deletion, tests the count of redundant four-step histories, and calculates the uniform-online law with exact rational dynamic programming. All assertions passed. Exact case-by-case results are in `CHECK_RESULTS.json`.

The numerical tests are finite and do not prove the formula for unbounded factor sizes. Independent mathematical review has not occurred.
