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

# Verification and limits

The proof uses exact graph-adjacency/occupancy equivalences, a complete case distinction on fully omitted lines, support-graph classification and disjoint counting. A reproducible standalone C++17 program named `verify.cpp` independently constructs each original rook graph. It enumerates all subsets, checks dominating and two-limited constraints by direct adjacency, separately checks the omitted-square classification, and compares the complete frequency histogram to the polynomial.

Command: `g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify.cpp -o verify && ./verify`.

Observed outputs:

```
DIRECT_ALL_SUBSETS_OK 4 4 65536 553 minimum 8 minimizers 12
DIRECT_ALL_SUBSETS_OK 4 5 1048576 1036 minimum 10 minimizers 6
DIRECT_ALL_SUBSETS_OK 5 4 1048576 1036 minimum 10 minimizers 6
DIRECT_ALL_SUBSETS_OK 5 5 33554432 2376 minimum 15 minimizers 20
VERIFY_OK
```

In total, 35,717,120 labelled subsets were tested. These checks are exhaustive only for the four specified finite grids. No finite enumeration is used as an infinite proof. The general statement follows from the proof in `RESULT.md`. No independent mathematical validation was commissioned or claimed.
