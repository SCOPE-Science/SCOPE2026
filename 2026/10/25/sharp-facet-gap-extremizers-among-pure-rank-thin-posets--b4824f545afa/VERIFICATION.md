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

# Verification record

Run `python3 verify_facet_gap.py` with the standalone embedded script. It uses the standard Python library only, enumerates all adjacent-rank cover matrices of rank sizes one/two at heights one to seven with no isolated rank vertices, and computes exact chain counts and cover counts by integer dynamic programming. The run checked 206,516 patterns over 254 rank profiles and passed all asserted inequalities, extremal-profile formulas, and equality classifications at heights at least three.

The unbounded result is established by the completion argument and binary-placement/counting proof in RESULT.md. The finite checker is evidence for implementation and small instances, not an exhaustive proof for arbitrary height. Primary-source comparisons concern known identities and extremal statement implications; other equivalent literature remains possible. Independent audit: not performed.
