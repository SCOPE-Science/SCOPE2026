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

Both standalone verifiers use only the Python standard library and enumerate finite structures independently.

- `python3 verify_rowmotion.py` enumerates every order ideal and applies the rowmotion map twice for wheel rim sizes 3 through 8; period-two orbit counts are 9, 34, 110, 347, 1064, 3234.
- `python3 verify_edgecovers.py` enumerates red-blue edge assignments on independently constructed wheels for rim sizes 3 through 10, checks the Lucas-number formula, and independently checks the all-graph period-two theorem over all connected labelled simple graphs with 2, 3, and 4 vertices.

The infinite results rest on the algebraic argument in RESULT.md, not on these finite tests. In particular, the algorithms do not establish exhaustive literature novelty, do not inspect larger instances, and do not constitute independent scholarly validation.
