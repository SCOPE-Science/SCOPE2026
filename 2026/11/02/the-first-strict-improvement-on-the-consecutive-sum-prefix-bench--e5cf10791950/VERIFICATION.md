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

# Computation and scope

`verify_interval.cpp` enumerates all 33,554,406 nonempty masks across the 24 domains and performs exact positive-prefix-difference marking. Reproduce with `g++ -O3 -std=c++17 verify_interval.cpp -o verify_interval` followed by `./verify_interval`. The observed ending is `VERIFY_OK masks=33554406 first_strict_improvement_n=24 maximum=188 full=186 unique_omitted=11`. All intermediate asserted maxima passed. A second counting method agrees on selected instances for initial domain sizes through 17.

These finite checks are exhaustive only for the explicitly stated range, not for larger parameters. They are self-review results; independent audit has not been performed.
