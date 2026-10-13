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

Run from the directory containing the embedded files:

```
python3 verify.py
g++ -O2 -std=c++17 -Wall -Wextra verify_independent.cpp -o verify_independent
./verify_independent
```

Expected checks in the Python program:

```
VERIFY_OK Coxeter Fano-triangle graph vertices=28 edges=42 perfect_matchings=84
VERIFY_OK full_automorphism_count=336 transitive_matching_orbit=84
VERIFY_OK per_matching_forcing_polynomial=4:198,5:1018,6:2300,7:3124,8:2918,9:1988,10:1000,11:364,12:91,13:14,14:1
VERIFY_OK forcing_number=4 minimum_quartets_per_matching=198 global=16632
VERIFY_OK quartet_orbits=51 sizes=336x48+168x3
VERIFY_OK alternating_cycles=74 length_distribution=8:1,10:4,12:4,14:12,16:9,18:4,20:16,22:16,24:8
VERIFY_OK minmax_gap=2; quartet_orbits.csv checked
```

Expected independent C++ checks:

```
VERIFY_INDEPENDENT_OK vertices=28 edges=42 matchings=84
VERIFY_INDEPENDENT_OK forcing_counts=4:198,5:1018,6:2300,7:3124,8:2918,9:1988,10:1000,11:364,12:91,13:14,14:1
VERIFY_INDEPENDENT_OK alternating_cycles=74 pair_disjoint=true triple_disjoint=false
VERIFY_INDEPENDENT_OK local_forcing_number=4 cycle_packing=2 gap=2
```

The Python checker also emits `quartet_orbits.csv` and `alternating_cycles.csv` with deterministic lexical indexing. Both programs construct the graph from three-bit vectors and enumerate matchings by smallest-free-vertex recursion. For forcing subsets, Python uses explicit difference-mask intersection against every other perfect matching whereas C++ computes the number of extensions on the complement of each selected edge subset by independent residual matching-count DP. These are finite exhaustive verifications. Their agreement is not a claim of external or independent human validation.
