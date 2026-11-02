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

# Reproducible checks

`verify_primary.py` uses Python's standard library; `verify_alt.cpp` uses C++17. Both source files are standalone. Execute from a directory containing both source files:

```sh
python3 verify_primary.py
c++ -O3 -std=c++17 verify_alt.cpp -o verify_alt
./verify_alt
```

The implementations enumerate all 4,368 five-subsets and 8,008 six-subsets of the sixteen labeled vertices of \(GP(8,3)\), check zero forcing, construct the feasible six-set exchange graph, and perform breadth-first search from every configuration. They use different forcing-loop and exchange-adjacency algorithms.

Observed outputs agree on 1,704 minimum sets, 16,560 edges, eccentricity six at all 1,704 vertices, degree histogram \((16:240,17:96,18:336,19:192,20:288,21:192,22:240,24:120)\), unordered distance counts \((1:16560,2:127008,3:417720,4:565488,5:276792,6:47388)\), Johnson excess counts \((0:1441284,1:9648,2:24)\) and Wiener index 5,453,976. The alternate checker also counts 48 distinct degree-sixteen endpoints of the 24 excess-two pairs.

All computations are exact finite enumerations; they neither validate any unexamined external publication nor prove an infinite-family claim. Independent scholarly validation has not occurred.
