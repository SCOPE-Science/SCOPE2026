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

The standalone `verify.py` computes GF(2) ranks and fixed-space dimensions from explicit adjacency updates for all 33 dimension–distance cases with dimensions 3 through 8. It separately enumerates 262,912 labeled initial configurations on dimensions 3 and 4, checking first-entry times and primitive period populations. The deterministic recorded standard output in `verification_output.txt` is `TWO_FEEDBACK_HYPERCUBE_CHECKS_PASSED`. These checks are corroborative: all-dimensional assertions depend on the proof in `RESULT.md`. No independent audit was performed.
