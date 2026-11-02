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

Both standalone programs are written for standard Python 3 and require no third-party packages.

```
python3 verification/direct_all_pairs.py
python3 verification/independent_orbits.py
```

The direct program loops through all \(2^{16}=65536\) possible identifying-code candidates, records the minimum size and its \(960\) solutions, constructs all legal one-for-one exchanges and runs BFS from all \(960\) solutions. The independent program instead checks sensor-index response signatures on all candidate subsets of size up to seven, reconstructs the 960-vertex exchange graph with set operations, enumerates all \(384\) signed-coordinate-permutation cube automorphisms, and checks BFS from one source in each of its three solution orbits.

Actual completed outputs included `DIRECT_ALL_PAIRS_PASS` and `INDEPENDENT_ORBIT_CERTIFICATE_PASS`; both confirmed \(4320\) edges, 9-regularity, connectivity and the common eight-shell sequence \((1,9,35,132,300,338,130,15)\).

The proof is exact for the fixed sixteen-vertex graph, not an empirical statement about arbitrary cube sizes. A full-text historical-priority comparison of one closely relevant article is unavailable, and no independent scholarly audit has yet occurred.
