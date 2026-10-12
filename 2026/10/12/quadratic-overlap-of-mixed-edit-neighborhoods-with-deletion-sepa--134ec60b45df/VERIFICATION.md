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

The standalone C++17 file `verify_mixed.cpp` constructs the deterministic scanner transitions, checks 64 reachable composite states, forms 64-by-64 matrices and verifies the first 4099 values in each of four residue classes. Cayley–Hamilton and the third difference of a quadratic make these finite checks sufficient for all \(n\ge4\). Run:

```
c++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_mixed.cpp -o verify_mixed
./verify_mixed
```

Expected: `VERIFY_OK states=64 matrix_dimension=4096 initial_terms_per_residue=4099 all_n_at_least_4=proved`.

Separately run `python3 verify_direct.py`. This enumerates the actual sets of output words, checks the scanner for every unordered binary pair through length eight, and checks deletion separation and exact overlap for the explicit families through length fourteen. Expected: `DIRECT_VERIFY_OK all_pairs_n_le_8= 43942 constructed_cases_4_through_14=11`.

Both checks use only standard language libraries and no external data, exact integers, and no random sampling. The finite enumeration alone does not establish an infinite claim; the 4096-dimensional recurrence argument is indispensable. No external independent scientific audit was performed.
