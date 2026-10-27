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

`python3 verify.py` exhaustively checks each subset of each \(\operatorname{Cr}_n\) for integers \(3\le n\le8\), using an edge-scan disjoint-set test of induced cycles and a separate one-vertex extension test for maximality. It compares cardinality profiles with the claimed polynomial formulas without applying the claimed forest classification to decide acyclicity.

Actual run: 87,360 total vertex subsets processed; each of the six graph orders matched both complete coefficient profiles. Maximal-size profiles were \(\{5:6\}\), \(\{5:32\}\), \(\{5:60,6:10\}\), \(\{5:120,7:12\}\), \(\{5:210,8:14\}\), and \(\{5:336,9:16\}\) for \(n=3,4,5,6,7,8\) respectively. Terminal status: `ALL_CHECKS_PASSED`.

The general statement is established mathematically in RESULT.md; these finite checks test, rather than prove, the universal statement. The verifier uses only the Python standard library. Source-priority assessment is separate from this mathematical computation. No independent audit has been performed.
