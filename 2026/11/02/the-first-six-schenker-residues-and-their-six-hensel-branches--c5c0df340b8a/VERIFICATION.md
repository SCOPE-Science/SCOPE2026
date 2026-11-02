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

## Reproducible computational checks

Compile `verify_schenker.cpp` using a C++17 compiler:

```sh
c++ -O2 -std=c++17 verify_schenker.cpp -o verify_schenker
./verify_schenker
./verify_schenker --census > recomputed.csv
cmp recomputed.csv schenker_census.csv
```

Execution performed from the complete embedded source reported:

```
VERIFY_OK odd_primes=345 tested_indices=369924 monomials_per_method=280932418 independent_methods=2 second_level_lifts=6
histogram_lambda_0_to_6: 121 139 65 14 4 1 1
first_primes_for_lambda_at_least_1_to_6: 5 41 179 593 593 2339
p=2339 six_roots: 156 470 520 589 1092 2170
```

The verifier generates all primes through the exact cutoff, checks every possible nonzero index below each prime by two independent arithmetic recurrences, compares the complete residue lists, confirms the full root-count histogram, and checks six nonzero lifted differences and all six level-two roots modulo \(2339^2\). The 345-row `schenker_census.csv` is a complete reproducible enumeration, not an extrapolated sample. The nondegenerate all-depth lifting consequence is a mathematical deduction from Miska's published Theorem 1 and is not claimed to have been computationally enumerated at every depth. No independent mathematical audit has been performed.
