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

## Reproducible checks

Run `python3 verify.py` using only Python's standard library. Successful output begins `VERIFY_OK` and records 24 rays, 24 facets, 72 diagonal options, 288 unimodular tetrahedra, refined face vector `(24,120,192,96)`, Betti vector `(1,20,54,20,1)` and 24 exceptional product surfaces.

The checker uses exact integer determinant arithmetic, not numeric convex-hull tolerances. It verifies all 24 facets and every candidate refinement cone, and it recomputes the face vector. The projectivity of one pulling refinement, the classification of all small toric subdivisions and the \(\mathbb P^1\times\mathbb P^1\) star identification are proved in RESULT.md using toric geometry, not asserted solely from test output.

No independent audit or independent validation was performed. Inaccessible or unidentified historical treatments may cover equivalent forms of the claim.
