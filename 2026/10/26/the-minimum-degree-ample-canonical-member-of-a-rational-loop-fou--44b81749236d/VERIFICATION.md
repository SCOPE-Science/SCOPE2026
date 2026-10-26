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

## Reproducibility checks

The standalone script `verify_minimum.py` was run from the package directory using Python's standard library. It checks the six degree equations, the primitive weight vector, pairwise coprimality, ambient well-formedness, the determinant condition, the ample canonical coefficient, and a noncanonical Reid--Tai age. It then exhausts all exponent multisets with product at most \(17280\), enumerating every ordering after fixing a minimum exponent in the first position. The search filters ambient well-formedness only, so it is a superset of the target well-formed hypersurfaces; the witness itself is well-formed.

Observed output:

sorted_exponent_multisets=11435
normalized_tuples_checked=537221
ambient_wellformed_numerical_candidates_with_product<=17280=8
minimum_weighted_degree=17279
witness_exponents=(4, 6, 5, 6, 6, 4)
witness_weights=(3723, 2387, 2957, 2494, 2315, 3389)
sum_weights=17265
canonical_class_coefficient=14
noncanonical_coordinate_age=2301/2315
VERIFY_OK

The bound is sufficient: any degree smaller than \(17279\) has exponent product smaller than \(17280\), so it is included in the enumeration. This is a finite reproducibility check, not independent validation or external certification. The literature comparison is limited by the possibility of unindexed sources.
