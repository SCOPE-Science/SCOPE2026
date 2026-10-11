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

The proof is symbolic and applies to every finite graph satisfying the stated hypotheses. The computational artifact is a stress test only.

`verify.py` reconstructs every connected labeled nonbipartite square-free graph on at most six vertices, constructs its Lovász neighborhood complex, and replays the proposed descending-cardinality elementary collapses. It checks the free-face condition against the complete current face set before each removal; it then checks exact equality with the root-selected target graph, the edge count, connectedness, and the cycle-rank formula.

All root choices are tested through five vertices. On six vertices, one deterministic root choice per graph is tested. The saved run reports \(3{,}610\) qualifying labeled graphs, \(7{,}916\) root assignments, and \(19{,}974\) elementary collapses, ending with `VERIFY_OK`.

The verifier does not establish novelty and does not replace the universal proof. The literature comparison remains subject to the residual risk stated in `REVIEW.md` and `AUDIT.json`.
