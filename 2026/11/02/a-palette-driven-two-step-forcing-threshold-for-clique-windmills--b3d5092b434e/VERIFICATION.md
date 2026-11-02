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

# Reproducibility

Run `python3 verify.py` with Python 3 standard library only. The verifier enumerates every possible initially assigned colour or blank at each labelled windmill vertex in eight instances, applies the actual graph-neighbour compulsory-colour rule until no further vertex can be assigned, and independently computes the two theoretical counts by inclusion–exclusion. Its expected line starts `VERIFY_OK nonchromatic_palettes`. The eight cases include a palette larger than the entire vertex set, for which an initially blank hub cannot be forced. Only these small cases are exhaustively computationally checked. The universal threshold and the growing-palette occupancy limit are proved mathematically in RESULT.md, not experimentally inferred. Independent validation has not occurred.
