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

# Verification steps and boundaries

Run `python verify_support.py` and `python verify_rank3.py` with standard Python in the same folder. `verify_support.py` constructs all points/lines explicitly and computes each ordered pair's set of third-element two-color extensions in 17 concrete geometries. It asserts pair-color uniformity within each geometry, checks the thin-to-thick bridge and the six profile classes. Its printed output must match `support_output.txt`; the six complete templates appear in `support_templates.json`. `verify_rank3.py` independently enumerates atomic point/line incidences and recursively forms rank-three first-order sentence types for eleven smaller examples; its output must match `rank3_output.txt`.

Both tools were executed from their listed source paths; the two recorded outputs were reproduced without differences. These are finite exact checks only. The theorem for unbounded size, arbitrary finite fields and non-Desarguesian affine/projective planes rests on the geometric constructions and plane axioms, not on the enumerations. Historical priority has not been exhaustively determined.
