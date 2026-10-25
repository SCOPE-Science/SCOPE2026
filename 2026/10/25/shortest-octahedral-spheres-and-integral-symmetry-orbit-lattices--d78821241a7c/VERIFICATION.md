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

# Reproducibility and scientific limits

Run `python3 verify_petersen_crosscycle.py` using Python 3.10+ with SymPy according to `requirements.txt`. It constructs the complete 331-face complex of the Petersen matching graph from five-symbol Kneser data, computes integral Smith forms of every boundary map, enumerates all induced six-vertex octahedra and their three automorphism orbits, computes three augmented integer Smith forms and representative primitivity, and calculates rational signed homology characters for all seven \(S_5\)-conjugacy types.

Observed principal output from the exact run:

```
VERIFY_OK_PETERSEN_MATCHING_MINIMUM_OCTAHEDRAL_SPHERES
PETERSEN_VERTICES_EDGES 10 15
MATCHING_COMPLEX_FACE_VECTOR (15, 75, 145, 90, 6)
INTEGRAL_BOUNDARY_RANKS (14, 61, 79, 6)
ALL_BOUNDARY_SMITH_FACTORS_UNIT True
INTEGRAL_H2_H3_RANKS 5 5
MINIMUM_SIX_VERTEX_OCTAHEDRAL_SPHERES 110
S5_OCTAHEDRAL_ORBIT_SIZES (10, 60, 40)
ORBIT_QUOTIENT_NONUNIT_SMITH ((2,), (), ())
ONE_SPHERE_FROM_EACH_ORBIT_PRIMITIVE True
S5_CHARACTER_ROWS [((1, 1, 1, 1, 1), 5, 5), ((2, 1, 1, 1), -3, 1), ((2, 2, 1), 1, 1), ((3, 1, 1), 2, -1), ((3, 2), 0, 1), ((4, 1), -1, -1), ((5,), 0, 0)]
H2_SIGN_TWIST_FIVE_POINT_PERMUTATION_H3_SPECHT_3_2 True
```

The flag six-vertex support lower bound is a general mathematical theorem, not established by searching only the test graph. The integer Smith computations enumerate the entire finite chain complex. A machine-checkable finite computation is not independent external review; independent audit and broader publication-priority verification have not been performed.
