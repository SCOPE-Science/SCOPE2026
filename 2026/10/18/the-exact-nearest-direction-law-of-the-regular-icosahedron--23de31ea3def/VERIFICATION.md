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

Run `python3 check.py` using Python 3 and the standard library only. The checker independently evaluates twenty-one radii using numerical radial integration, compares an analytical mean with angular quadrature, checks monotonicity and four endpoint coefficient tests, and draws 100,000 seeded independent random points on the sphere. It prints `ICOSAHEDRAL_NEAREST_LAW_OK` if all assertions pass. The cap and Voronoi derivations in RESULT.md are the proof; the finite checks are corroboration only. Historical priority and independent audit have not been established.
