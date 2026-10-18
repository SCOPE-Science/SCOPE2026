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
The direct vertex-level checker `scripts/check_marked_boolean.py` uses the Python standard library, constructs upward and downward directed cover lists for each Boolean lattice and performs synchronous counting colour refinement from distinct marker colours. It independently computes the orbit signature by grouping ground-set coordinates according to their entire marker-membership bit vector and counting selected coordinates within each group. Its assertion compares equality of vertex colours with equality of orbit signatures for every tested pair of vertices.

Command: `python3 scripts/check_marked_boolean.py`.

Recorded result: `checks/marked_boolean.txt`. It successfully checked 2,047 distinct-marker configurations across sizes one to seven, including complete enumerations for small sizes and deterministic samples for larger ones, with maximum observed five refinement rounds. The source and output are included as independent package files. The mathematical proof establishes the all-order result; exhaustive enumeration here is bounded and makes no claim to cover higher dimensions or every marker configuration for sizes four to seven.
