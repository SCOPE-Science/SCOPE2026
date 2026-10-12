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

Compile each source independently with a C++17 compiler:

```sh
c++ -std=c++17 -O3 verify_transfer.cpp -o transfer
./transfer
c++ -std=c++17 -O3 verify_direct.cpp -o direct
./direct
```

Both binaries were executed and returned `VERIFY_OK`. `verify_transfer.cpp` enumerates all 40320 total rankings and counts charged windows using rank-filtered directed-walk dynamic programming. `verify_direct.cpp` counts the four- and nine-window objective scores by explicit examination of every binary word of length seven (128 cases) or twelve (4096 cases). Both independently check the complete two-dimensional Pareto list, its multiplicities, and absence of a joint scalar minimizer. The transfer program also checks all-width two-through-eight simultaneous optima. No external solver or randomization is used. Independent audit remains unperformed.
