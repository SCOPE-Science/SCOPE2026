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
# Reproducibility and limits

The supplied `verify.cpp` independently enumerates every Hamiltonian cycle of the explicitly displayed 24-edge Chvátal graph up to orientation reversal, constructs all unordered two-edge-switch pairs, and computes graph connectedness and every BFS distance. Standard compiler command:

```
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify
./verify
```

The replay produced `HAMILTONIAN_OK undirected_cycles=185 directed_oriented_cycles=370`, `SWITCH_OK vertices=185 edges=382 connected=1 diameter=9 radius=6`, `ALL_VERIFY_OK`; the degree histogram is `2:21 3:48 4:60 5:28 6:6 7:18 9:4`, the eccentricity histogram `6:12 7:104 8:53 9:16`, and unordered-pair distance histogram `1:382 2:1129 3:2694 4:4116 5:4876 6:2992 7:713 8:110 9:8`.

A second algorithm, `verify_independent.py`, exhaustively includes/excludes every edge subject to degree feasibility and filters spanning two-regular subgraphs for connectedness. Run `python3 verify_independent.py`. It produced `TWO_FACTORS_TOTAL 278` and `INDEPENDENT_VERIFY_OK two_factor_filter_hamiltonian=185 switch_edges=382 diameter=9 radius=6 connected=1`.

These are complete enumerations of the specified finite graph, not sample experiments or evidence for an infinite family. The two algorithms share the explicitly stated original graph and the mathematical definition of switching; their cycle generation algorithms are distinct. Previously known oriented Hamiltonian-cycle counts are not claimed as new. No external independent audit has been performed.
