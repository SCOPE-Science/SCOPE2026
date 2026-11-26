---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and exact checks

The graph theorem is proved analytically by a Haar-preserving change of coordinates on each forest and by contraction of second moment matrices on cycles. The unchanged standard-library script `artifacts/verify.py`, run from the package directory, checks the exact constant Laurent coefficient of the centered product over triangles and four-cycles with two or three columns. It also contains consistency checks of previously known second and third purity moments on six rectangular grids. None of these finite tests proves the graph theorem in general or establishes priority.
