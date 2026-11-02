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

The graph is constructed from the two twelve-vertex layers with outer edges, inner step-five edges and spokes, as defined in `RESULT.md`. Both verifiers are standalone and use only the Python standard library or a C++17 compiler and standard library.

The full enumeration step assigns a free neighbor to the least unmatched vertex. This is an exhaustive, duplicate-free enumeration of perfect matchings by induction on the number of uncovered vertices. The Python verifier builds all simple cycles of lengths four, six and eight, then flips those alternating with each perfect matching. The C++ verifier independently inspects all unordered pairs of enumerated matchings and recognizes adjacency by the connectedness and size of their symmetric difference. Breadth-first searches and component traversals are applied to the complete finite graphs, not a sample.

Executed commands:

```
python3 verify.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_alt.cpp -o verify_alt
./verify_alt
```

Observed Python output:

```
CYCLES {4: 0, 6: 12, 8: 54}
FLIP 4 vertices 120 edges 0 components {1: 120} degrees {0: 120}
FLIP 6 vertices 120 edges 192 components {1: 9, 18: 3, 57: 1} degrees {0: 9, 2: 48, 4: 36, 5: 24, 8: 3}
FLIP 8 vertices 120 edges 414 components {120: 1} degrees {3: 6, 6: 39, 7: 54, 8: 18, 18: 3}
METRIC {4: 72, 5: 42, 6: 6}
ALL_VERIFY_OK
```

Observed independent C++ output:

```
INDEPENDENT_MATCHINGS_OK count=120
INDEPENDENT_FLIP_OK cycle=4 edges=0 components= 1:120
INDEPENDENT_FLIP_OK cycle=6 edges=192 components= 1:9 18:3 57:1
INDEPENDENT_FLIP_OK cycle=8 edges=414 components= 120:1
INDEPENDENT_DISTANCE_OK radius=4 diameter=6 ecc4=72 ecc5=42 ecc6=6
INDEPENDENT_VERIFY_OK
```

A witness of an isolated hexagon-flip matching, with vertices indexed as in the programs, is:

```
(0,1) (2,3) (4,5) (6,7) (8,9) (10,11)
(12,17) (13,20) (14,19) (15,22) (16,21) (18,23)
```

An explicit octagon-flip distance-six pair is:

```
A=(0,1) (2,3) (4,5) (6,7) (8,9) (10,11)
  (12,19) (13,18) (14,21) (15,20) (16,23) (17,22)
B=(0,11) (1,2) (3,4) (5,6) (7,8) (9,10)
  (12,17) (13,20) (14,19) (15,22) (16,21) (18,23)
```

The complete breadth-first distance shell from \(A\) is \((1,3,15,42,43,15,1)\), confirming that \(B\) lies at distance six. These displayed examples are witnesses, not a substitute for the full exhaustive computation. The proof makes no assertion about larger graphs, asymptotic behavior, unrestricted-cycle distances or independent external validation.
