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

# Exact verification

Run `python verify.py` with Python 3 standard library from the directory containing this file and the source program. The exact-rational code verifies the direct facet formula against the reciprocal-prefix formula in dimensions 2–6; its independent two-dimensional calculation computes \(K+s(-K)\) via convex hulls and confirms the first mixed-volume coefficient through the planar Minkowski identity. The general theorem and equality cases are proved in `RESULT.md`; finite tests do not certify an infinite theorem.

Priority check is limited by inaccessible full-text papers, especially earlier anti-blocking and aligned-simplex mixed-volume results. Independent audit: not performed.
