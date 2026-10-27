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

# Reproducible finite computation

The delivered `verify.cpp` is standalone C++17 and contains no external data, graph libraries, or precomputed tables. Build with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify.cpp -o verify` and then run `./verify`. It generates 1200 palette-orbit representatives, 7200 fully labelled proper three-colourings, enumerates all single-component Kempe swaps, checks undirected adjacency, runs breadth-first search from every state, and asserts both complete metric profiles before printing `VERIFY_OK`.

Checked output from the packaged source:

```text
QUOTIENT: V=1200 E=5360 radius=6 diameter=7 degrees=8:140,9:1020,10:20,11:20, eccentricities=6:460,7:740,
LABELED: V=7200 E=36120 radius=7 diameter=8 degrees=10:6960,11:240, eccentricities=7:5280,8:1920,
VERIFY_OK
```

The enumeration is exhaustive on this finite graph, not an infinite proof. The verification does not establish uniqueness against all possible unpublished prior computations and is not an independent audit.
