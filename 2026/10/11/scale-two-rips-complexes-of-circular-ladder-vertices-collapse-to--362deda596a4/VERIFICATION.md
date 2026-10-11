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

## Reproducibility
Run `python3 verify.py` alongside this file. It enumerates all scale-two cliques directly from graph distances for each integer \(7\le n\le20\), compares the complete three-family maximal-tetrahedron classification, tests each claimed free face in its actual phase, and verifies that the remainder equals one rim cycle. Its terminal success marker is `VERIFY_OK`. The symbolic all-parameter argument appears in RESULT.md; finite tests alone do not certify it.

## Scientific limits
The checks do not address continuous points of the ladder graph, smaller \(n\), other scales, or novelty against inaccessible literature. Independent audit was not performed.
