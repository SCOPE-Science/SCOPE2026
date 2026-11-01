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

Run `python3 verify.py` in a directory containing the embedded verifier. Python 3 standard library is the only dependency.

The executable enumerates all labeled triangle-free simple graphs on one to five vertices. For each, it constructs \(\operatorname{CF}_4(K_m\vee H)\) for \(m=2,3,4\) by enumerating all subsets and testing the four-clique exclusion directly. It independently constructs \(\operatorname{Ind}(H)\), verifies the exact union-and-intersection face decomposition used in the proof, and performs oriented simplicial boundary-matrix Gaussian elimination over the prime fields \(2,3,5\). It also tests four six-vertex examples, including \(C_6\), a path, and a three-edge matching, and the sharpness counterexample \(K_2\vee K_3=K_5\).

Executed output:

```
TRIANGLE_BOUNDARY_CASE_OK CF4(K5): four 2-spheres; the excluded extrapolation gives two
FACE_COVER_INTERSECTION_IDENTITY_OK 1329
FINITE_COMPLEXES_OK 1329
INDEPENDENT_FIELD_HOMOLOGY_CHECKS_OK 3987
ALL_VERIFY_OK
```

The finite tests establish only the stated small-size instances and field homology agreements. They do not establish the infinite homotopy equivalence, integral torsion assertions, or uniqueness. The all-parameter proof is the explicit cofibration and null-attachment argument in `RESULT.md`. This is not an independent external audit.
