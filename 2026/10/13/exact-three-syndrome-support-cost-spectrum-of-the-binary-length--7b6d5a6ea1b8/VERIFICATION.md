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

Compile `verify.cpp` with a C++17 compiler, for example `g++ -O2 -std=c++17 verify.cpp -o verify`, and invoke `./verify`. No external mathematical libraries or input datasets are needed.

The deterministic run enumerates the multiplicative cyclic group of the sixteen-element field, constructs all fifteen check columns, the XOR-closed syndrome spans of each coordinate subset of size three through seven, and all unique echelon bases of dimension-three subspaces of the eight-dimensional binary syndrome space. An exact four-word 256-bit containment test determines the least feasible subset size for each space.

Observed complete output:

```
COUNT 97155
HIST 3:330 4:6510 5:39885 6:49230 7:1200
WITNESS 81,2,4
VERIFY_OK
```

A separately written subset-first enumeration produced the same histogram. The checksum and packaging check applies to the embedded code text; the verifier certificate concerns exact finite enumeration, not an infinite family or independent scientific audit. The already published generalized covering radius seven is not being claimed anew.
