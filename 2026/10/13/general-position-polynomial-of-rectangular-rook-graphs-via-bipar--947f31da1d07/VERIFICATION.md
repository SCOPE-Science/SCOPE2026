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

The included `check.py` computes the coefficients from a labeled-component recurrence for bipartite star forests and independently inspects each rook-graph vertex subset using shortest-path distances. Both routes agree for 24 tested ordered pairs satisfying \(1\le m\le5\), \(1\le n\le6\), and \(mn\le16\); 146,762 subsets were tested. The script also checks the maximum subset size and leading-coefficient formulas for all nondegenerate pairs in this range.

Run `python3 check.py` from the extracted package. The output should begin `VERIFY_OK`. The proof in `RESULT.md`, not bounded computation, establishes the theorem for arbitrary \(m,n\ge2\). This package has no independent mathematical audit and does not claim that all historical sources have been exhausted.
