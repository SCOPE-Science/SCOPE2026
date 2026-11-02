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

The ordinary mathematical and computational checks are documented in `RESULT.md` and the two standalone source files under `checks/`. A genuine all-source distance search and a separate symmetry-reduced distance search agree on all \(7{,}494{,}256\) unordered pairs. The two graph representations and forcing procedures are independent implementations. Exhaustive computation establishes the fixed finite claim, but it is not a general theorem about arbitrary folded cubes. Historical priority and external scholarly validation are not certified by these checks.

Run the programs with a C++17 compiler and Python 3:

```text
c++ -O2 -std=c++17 checks/clebsch_full.cpp -o clebsch_full
./clebsch_full
python3 checks/clebsch_orbits.py
```

Successful runs display `ALL_SOURCE_FOLDED_CUBE_EXHAUSTIVE_PASS`, `SYMMETRY_REDUCED_CLEBSCH_CERTIFICATE_PASS`, and `SEVEN_INDUCED_TYPES_AND_80_C6_PLUS_TWO_ISOLATES_PASS`.
