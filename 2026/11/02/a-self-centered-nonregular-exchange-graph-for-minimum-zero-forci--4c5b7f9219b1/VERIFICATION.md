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

# Reproduction and limits

The standard-library Python program `verify_primary.py` enumerates all 7- and 8-element subsets, tests the standard forcing predicate, constructs exact one-token exchanges, reduces its all-pairs breadth-first searches through the full 384-element cube symmetry group and checks exact distance and Johnson-excess histograms.

The independent C++17 implementation `verify_alt.cpp` uses a sequential forcing predicate, separate generation of exchange edges and all-source breadth-first searches, and checks the entire ordered-pair census without relying on symmetry reduction. The programs terminate on finite, fully specified state spaces, use exact integer arithmetic, and require no network access or supplemental data.

```sh
python3 verify_primary.py
g++ -O2 -std=c++17 -Wall -Wextra verify_alt.cpp -o verify_alt
./verify_alt
```

The programs respectively print `PRIMARY_CERTIFICATE_PASS` and `INDEPENDENT_CERTIFICATE_PASS`. Checks cover all 2360 reconfiguration states, all edges and all source/target pairs. They do not prove any higher-dimensional generalization, or establish absolute novelty. Independent scholarly audit has not been performed.
