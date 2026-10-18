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

Run `python3 verify_zonotope.py` from the folder containing that file. Python 3, NumPy and SciPy are required by this independent finite checker. It constructs candidate zonotope vertices from all subset sums, computes exposed polyhedral edges from three-dimensional convex hull facets, and labels edges by exact integral generator vectors. For each prescribed normal it calculates the width and sums the exact offset-length-weighted section vertex counts, comparing them to zone-multiplicity predictions using rational arithmetic. Three integer test sets and twenty-one orientation comparisons passed, together with six generic region-count checks.

Observed output:
```
generic_four generators 4 vertices 14 edges 24 zone_r [6, 6, 6, 6] normal_checks 7
balanced_two_planes generators 6 vertices 28 edges 48 zone_r [8, 8, 8, 8, 8, 8] normal_checks 7
unbalanced_prism generators 4 vertices 12 edges 18 zone_r [4, 4, 4, 6] normal_checks 7
ZONOTOPE_OFFSET_MEAN_OK cases=3 normals=21 generic_region_checks=6
```

This check does not exhaust all dimensions, directions, polyhedral degeneracies or generator configurations. The manuscript separately proves these universal statements using finite edge-zone correspondences, exact interval integration and a rigidity argument across each orthogonality hyperplane.
