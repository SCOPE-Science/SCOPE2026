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

Run `python verify.py` in this folder. The standalone Python 3 script enumerates all deletion triples for \(n=4,5,6,7\), directly recomputes the residual directed multigraph's divergence, active-vertex connectivity and three-edge shape classes, and asserts the predicted values; its successful output ends with `PASS (finite checks only; proof in RESULT.md)`. The tested lengths cover 560, 4,960, 41,664 and 341,376 distinct three-deletion choices. No finite check purports to establish a result for unbounded \(n\); the all-length proof uses the combinatorial classification and Xu–Lü super-edge-connectivity theorem cited in RESULT.md.
