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

# Reproduction and exact limits

Run `python3 check_points.py` and `python3 check_frames.py`. Both run with Python 3 standard-library modules and no external data. Their recorded outputs are `check_points.out` and `check_frames.out`; each checker verifies all distance layers from all vertices, not a sample. The point-set and frame constructions are independent implementations of the same finite incidence geometry. `RESULT.md` contains the structural counting argument, the exact domain, and the boundary on extrapolation.

The checkers establish finite claims in the specified plane only. They do not establish whether the result is unpublished in every source, nor do they amount to an independent external mathematical audit.
