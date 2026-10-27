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

# Verification and reproducibility

Run `python3 artifacts/verify_toric_example.py` with Python 3; the script uses only standard-library `fractions` and `collections`.

The script reconstructs the eight lattice generators and twelve maximal cones, verifies that each chosen maximal determinant has absolute value one, enumerates all eighteen codimension-one cones, identifies their two opposite rays, solves their exact integral relations, and compares \((-K)\)-degrees to the eighteen expressions listed in `RESULT.md`. It also checks the positive convex identity at \(v_7\), the five toric intersection numbers of the restricted canonical class, and the genus and zero-degree identities for example values \(d=0,1,2,3,4,5,6,11,31,103\) (with the nonvanishing and positivity checks applied only for \(d\ge2\)).

The expected successful output is:

```
VERIFY_OK smooth_cones=12 walls=18 sample_parameters=10 canonical_zero_walls_for_d_ge_2=0
VERIFY_OK ray7_convex_obstruction=true star_surface=blowup_P1xP1
VERIFY_OK restriction_intersections=true zero_degree_curves=true unbounded_genus=true
```

In this fan every ray varies only in its **third** coordinate, affinely in \(d\). Every three-vector determinant is therefore affine in \(d\); the listed maximal-cone determinants are constant \(\pm1\), and Cramer’s rule makes each wall coefficient and wall degree affine in \(d\). Consequently, checking their table at \(d=0,1\), together with this determinant argument, also gives an exact symbolic certificate of the wall formulas for all integral \(d\). The infinite range \(d\ge2\) is proved in `RESULT.md` through the **symbolic** wall table, the universally valid convex combination and the Picard intersection pairing. Checking finitely many values alone would not establish this infinite-range theorem. The fan's completeness and the canonical tensor-generation criterion rely on their cited published proofs; the script checks the explicit local calculations but not those general theorems or historical priority.
