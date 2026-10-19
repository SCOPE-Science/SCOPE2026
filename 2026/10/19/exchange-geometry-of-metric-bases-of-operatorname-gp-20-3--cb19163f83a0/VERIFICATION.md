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

# Reproducible finite checks

The source files `check_direct.cpp` and `check_masks.py` are standalone, require no third-party packages or external datasets, and construct the 40-vertex generalized Petersen graph directly. The C++ build must leave standard assertions enabled (do not compile with `-DNDEBUG`). Execute:

```sh
g++ -std=c++17 -O3 check_direct.cpp -o check_direct
./check_direct
python3 check_masks.py
```

Both compute \(\dim(G)=5\), \(41{,}040\) minimum bases, and \(670{,}930\) exchange edges. The C++ implementation verifies exhaustive BFS of all representative orbits under 40 known graph automorphisms, producing radius \(6\), diameter \(7\), and eccentricity counts \(40{,}180\) and \(860\). The Python implementation uses a distinct pair-coverage test and checks complete connectivity and explicit eccentricity witnesses, but its two witness searches alone do not certify global radius and diameter; the complete C++ orbit enumeration supplies those upper/lower bounds. Check the included plain-text outputs, each concluding in `VERIFY_OK`, or regenerate them from source.

No statement about graphs outside the specified 40-vertex case is established by these finite computations. External independent validation has not been performed.
