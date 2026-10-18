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

Run `python3 verify.py` in a directory containing the accompanying standalone source file. It uses only Python's standard library and does not download external material.

The program enumerates direct column intersections for all integer parameters \(1\le n\le14\), \(0\le k<n\), compares resulting concept extents with the independently built endpoint-pair family, and checks every coefficient of the extent-size histogram. It also verifies the exact chain-product order in all dense cases, brute-forces the modular and distributive identities in 35 cases with \(2\le n\le8\), and compares the optimal radius in orders \(2\)–\(10\).

Observed execution output:

```
VERIFY_OK endpoint_profiles_cases= 105 subset_intersections= 425986 dense_grid_posets=PASS modularity_distributivity_cases= 35 optimal_radius_n_2_to_10=PASS all_equalities=PASS
```

The direct subset enumeration is finite and cannot by itself prove statements for unbounded parameter values. All such statements have symbolic arguments in RESULT.md. The originality comparison is based on accessible literature and mathematical-record searching; it does not establish publication priority. No external independent verification has been performed.
