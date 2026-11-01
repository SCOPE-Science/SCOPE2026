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

# Exact reproducibility

Execute `python3 verify_strip_boundary.py` in the directory containing this file. It requires only the Python 3 standard library. The output is JSON, with the marker `THREE_ROW_BOUNDARY_PERFECT_MATCHING_MORSE_OK`; the exact completed output is in `verification_output.json`.

The code constructs both open and periodic three-row strips for column counts 2, 4, 6, and 8. It recursively enumerates every perfect matching and verifies every vertex is covered once. It forms the complete face set by all submasks of the perfect-matchings' edge masks; there are no unexamined faces in these finite instances. Its deterministic toggle matching includes the empty face. The code independently traverses the entire face-poset Hasse graph after reversing matched incidences and verifies the number of processed arrows and vertices, rejecting directed cycles. Euler sums and all expected perfect-matching, face, and critical-cell counts are asserted exactly.

The largest case has 812,758 faces and 5,600,955 Hasse incidences. The proof derives a sphere wedge from Forman's acyclic-matching theorem and the absence of critical intermediate cells; a rank test alone would be insufficient. No tests of lengths above eight were performed or asserted, and no independent audit has been conducted.
