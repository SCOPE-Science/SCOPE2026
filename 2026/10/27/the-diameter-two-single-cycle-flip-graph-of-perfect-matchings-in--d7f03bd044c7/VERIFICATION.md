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

# Reproducibility and verification

Run from a directory containing the scripts using Python 3 standard library:

```
python3 verify_cayley.py
python3 verify_matchings.py
```

`verify_cayley.py` constructs the base prism, enumerates every simple cycle using rooted depth-first search, spans the binary cycle space, checks its size \(2^{n+1}\), checks exactly \(2^n+n(n-1)\) simple cycles, and verifies every nonzero cycle-space element is either one generator or the XOR of two generators for \(3\le n\le9\).

`verify_matchings.py` independently expands each base vertex into three sockets, enumerates all perfect matchings via backtracking, reconstructs their binary even-subgraph coordinates, computes single-cycle adjacency directly from the connected components of each matching-pair symmetric difference, and compares every pair with the exact join/circular-interval rule for \(3\le n\le7\). This program does not use the simple-cycle enumeration from the first.

Both scripts were executed from the paths included with this package. Their recorded standard outputs are `verify_cayley.out` and `verify_matchings.out`; they reproduce the claimed state counts, cycle counts, and adjacency counts in the checked finite ranges.

The mathematical statements for arbitrary \(n\) follow from the written combinatorial proof, not from finite tests. No external independent audit has occurred, and none is implied by these checks.
