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

Run `python3 deep_hole_check.py` from the directory containing the attached source. The checker is self-contained and uses Python's `fractions.Fraction`, `itertools` and integer arithmetic only. Its exact computations, performed directly on the packaged source, output:

```
DEEP_HOLE_CERTIFICATE_OK candidates=4 chamber_vertices=41 invertible=455
site_stabilizer_orbits=3 orbit_sizes=192,192,192 local_holes=576
nearest_sites_per_hole=6 determinant_abs=1 global_hole_orbits=1
holes_per_D5_period=192 Delaunay_volume_fraction=4/5
```

The full proof includes the mathematical justification for the finite chambers, search radii, symmetry lifting and nonoverlap; finite computational output alone is not a proof for all points in ambient space. The checker establishes exactly rational finite claims used in that proof, not any assertion about other metrics, other periodic sets or independent scientific validation.
