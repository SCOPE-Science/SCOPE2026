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

Run `python verify.py` in this directory using Python 3.9 or later; only the standard library is needed. The observed result is:

```
VERIFY_OK filtration_facets 128 reflection_cases 89 explicit_fixed_faces 1988
```

The checker reconstructs every pure maximal facet independently from all strict vertex orders for cycle lengths 6, 7 and 8. It also constructs the same facets from the gap/root model, obtaining 128 total distinct facets over those three lengths. For each cycle length from 6 through 64 it computes every reflection conjugacy-class incidence orbit, determines maximal fixed faces directly from the complete pure facet list, and compares them with the symbolic orbit-range formula from the proof. There are 89 such tests, including both even-axis types. For lengths through 18 it independently enumerates fixed simplices and checks that their Euler characteristic is 2; the combined count of nonempty faces is 1988.

The general result does **not** follow merely from numerical checks. Its unrestricted proof is the combinatorial classification of all maximal facets, incidence orbits, forbidden boundary orbits, and impossible mixed-type signs in `RESULT.md`. The signed reduced homological Lefschetz number additionally uses the standard equivariant barycentric subdivision/Lefschetz identity. No external or independent audit was performed.
