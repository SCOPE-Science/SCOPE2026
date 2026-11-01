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

Use Python with the dependencies in `requirements.txt`; run `python verify_biclique_corona.py` in the directory containing that file. The checker constructs the full powered-distance matrix of the weighted corona and calculates exact (rational) quadratic-form decompositions for integer powers on finite samples. It also evaluates high-precision roots of the explicit determinant, finite-dimensional centered-matrix inertia and endpoint rank, and large-branching diagnostics.

Observed local execution:

```
EXACT_POWER_DISTANCE_QUADRATIC_DECOMPOSITION_OK 180
FULL_POWERED_DISTANCE_INERTIA_AND_ENDPOINT_RANK_OK 32
TWO_SIDED_PENDANT_LENGTH_RESTORATION_DIAGNOSTICS_OK
BRANCHING_CONSTANT 1.0 1.0596156747030245 [1.0665776681373957, 1.0610027594416922, 1.0598928795231246]
NONCOMMUTING_SMALL_LENGTH_LARGE_BRANCH_LIMITS_OK
ALL_BIPARTITE_CORONA_NEGATIVE_TYPE_CHECKS_OK
```

All tests are finite checks; none replaces the proof of uniqueness, asymptotics or limit interchange. No independently produced evaluation or external certification is represented.
