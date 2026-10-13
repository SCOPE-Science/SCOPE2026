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

Run `python3 verify.py` with standard Python 3 (no third-party dependencies). The code independently enumerates the full Minkowski point set, all primitive facet normals, all old vertices, all local cone determinants, and every one of the four explicitly specified rational support perturbations. An invocation returned `VERIFY_OK 22 Minkowski lattice sums; 8 facets; 10 original vertices; 2 conifolds; 4 smooth projective small resolutions`.

Geometric deductions use the toric normal-fan correspondence, the four-generator Gorenstein conifold semigroup, and standard small-resolution and smooth-projective-toric cohomology results. The script certifies the exhaustive finite polyhedral assertions; it does not replace these geometric arguments or establish a broader classification of non-toric resolutions. Independent mathematical audit was not performed.
