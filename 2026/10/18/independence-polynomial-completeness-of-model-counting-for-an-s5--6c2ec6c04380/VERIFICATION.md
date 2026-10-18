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

# Verification

Use Python 3 with only its standard library. In the same directory as the packaged files, run `python verify_modal.py`.

The program tests the exact model-count formula by separately enumerating all \(q^n\) possible world-label assignments for complete S5 frames, evaluates graph-independent image sets, and compares direct answers to the Stirling-number expression. It uses all labelled graphs on two or four Boolean types (the one- and two-atom cases), sixteen reproducible graph instances with eight types, and the four-vertex path/triangle-isolate collision. It also inverts the triangular Stirling transform and checks the nonexistence of nonisomorphic polynomial-equivalent graphs on at most three vertices.

Observed execution:

`VERIFY_OK graphs=82 complete_frame_valuations=162300 inversion=PASS min_collision=4 path_triangle_isolate=PASS`

The general result, asymptotic and counting-hardness claims rely on their mathematical arguments, not on an enumerative extrapolation. No external independent audit or publication-priority certification is asserted.
