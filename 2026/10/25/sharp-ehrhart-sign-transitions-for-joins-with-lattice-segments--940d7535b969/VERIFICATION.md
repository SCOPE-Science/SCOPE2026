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

The proof is by exact lattice-point layer counts, Pick's theorem, and elementary rational inequalities. `join_sign_checker.py` uses rational arithmetic and independent evaluation/interpolation of lattice-layer sums; it passed `LATTICE_JOIN_SIGN_PHASE_OK cases= 3388`. The checker is finite diagnostic evidence, not an exhaustive search over all polygons and segment lengths. Infinite claims rely on the explicit algebraic proof in RESULT.md. Historical priority has not been independently certified.
