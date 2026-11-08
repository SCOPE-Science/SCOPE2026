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

# Reproducibility and scope

The proof is self-contained in `RESULT.md`. Run the accompanying standalone program `python3 check_area.py` with Python 3 standard library only. The program performs exact rational matrix-identity checks and finite independent shoelace tests of the physical-coordinate polygonal area at 134 reduced rational angles. Expected marker: `STOCK_CENTER_AREA_EXACT_Q_AND_POLYGON_OK angles=134`.

These computations do not prove the irrational-density assertion, the rational-denominator limit, or any quantifier over infinitely many parameters. Those are addressed in the written proof through planar rotations, irrational density, and the asymptotic of the tangent function. No external independent mathematical audit was performed.
