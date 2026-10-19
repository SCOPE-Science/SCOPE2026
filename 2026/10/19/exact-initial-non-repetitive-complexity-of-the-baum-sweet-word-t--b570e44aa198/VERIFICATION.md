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

The table gives a finite exact claim for factor lengths 1 through 8192. The mathematical reduction verifies only two endpoints per constant interval, using monotonicity of first-collision position and uniqueness of the earlier match.

C++17 commands:

```sh
g++ -O2 -std=c++17 profile.cpp -o profile
./profile 8192 > recomputed.csv
cmp recomputed.csv profile8192.csv
g++ -O2 -std=c++17 verify_endpoints.cpp -o verify_endpoints
./verify_endpoints 8192 profile8192.csv
```

Observed: `CALC_COMPLETE length=8192 longest prefix=65536` and `VERIFY_OK M=8192 intervals=25 boundary_cases=50`. The direct endpoint verifier uses the ordinary binary zero-run arithmetic definition and compares bytes exactly after hash filtering, so its correctness does not assume collision-free hashing. The independent suffix-array construction uses the four-state substitution and a length-65536 prefix. Neither calculation proves the displayed patterns for factor lengths above 8192. No independent audit has been performed.
