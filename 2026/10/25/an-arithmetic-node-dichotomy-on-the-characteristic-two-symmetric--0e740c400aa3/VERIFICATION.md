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

The accompanying exact Python script enumerates all rational points in the projective five-coordinate model over \(\mathbb F_2\) and \(\mathbb F_4\), identifies its 45 \(\mathbb F_4\)-rational singularities and 15 \(\mathbb F_2\)-rational singularities, expands the local quadratic tangent forms at representative nodes, verifies rank-four polar matrices, and counts rational points on their exceptional quadrics. The executable prints `VERIFY_OK`, `NODE_QUADRATICS_OK`, and `QUADRIC_FIELD_COUNTS_OK`. The symbolic classification and zeta quotient are proved in RESULT.md and are not claimed to be machine-certified for all finite extensions. Independent audit and independent validation have not been performed.
