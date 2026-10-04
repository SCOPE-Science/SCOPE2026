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

The proof is structural and covers every finite connected chain graph and every integer \(k\ge1\). The two critical checks are: (1) the extreme-class propagation cascade when the relevant block-load maximum is at most \(k\); and (2) the twin-class obstruction showing that an unselected class larger than \(k\) cannot be entered, together with the initial stall for a selected nonextreme class larger than \(k\). The pair consisting of one vertex from \(A_p\) and one from \(B_1\) dominates the graph immediately, so the minimum is never larger than two.

The included `verify.py` independently constructs all canonical positive block profiles through order 11 with at most five block pairs. For each profile it executes the literal generalized power-domination process for \(k=1,2,3,4\), tests every singleton against the theorem, and checks the extreme two-vertex witness whenever no singleton works. The expected replay line is:

`VERIFY_OK profiles=4092 singleton_checks=19327 extreme_pair_checks=700 max_order=11 k_max=4`

This finite replay is a stress test only. It does not certify the infinite theorem beyond the proof. The literature comparison is also not a mathematical novelty certificate; residual indexing risk is stated in REVIEW.md and AUDIT.json.
