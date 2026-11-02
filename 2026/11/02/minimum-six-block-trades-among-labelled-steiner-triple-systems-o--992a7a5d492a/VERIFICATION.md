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

# Verification of the finite classification

The delivered package contains two **standalone** standard-library Python 3 programs. From the package root:

```sh
python3 verify/exact_cover_bfs.py
python3 verify/group_cosets.py
```

The first must display `EXACT_COVER_840_DESIGNS_AND_15120_TRADES_PASS`, `ALL_840_ROOTS_METRIC_AND_INTERSECTION_LAW_PASS`, and `DISTANCES_1_36_395_408_DIAMETER_3_PASS`. It proves the exact-cover domain exhaustive by always filling an uncovered point pair with each eligible triple, with no duplicated leaf. It then compares all unordered pairs of distinct designs and carries out BFS from every root.

The second must display `S9_ORBIT_840_AND_AFFINE_AUTOMORPHISMS_432_PASS`, `TRANSPOSITION_15120_EDGES_AND_COSET_CYCLE_DISTANCE_PASS`, and `SIX_BLOCK_TRADE_DISTANCE_BY_INTERSECTION_PASS`. It generates all invertible affine \(2\)-by-\(2\) transformations over \(\mathbb F_3\), all \(9!\) point relabelings, each of the \(36\) transpositions, and calculates coset distances from the permutation-cycle formula over all \(432\) possible stabilizer factors. It checks the independent BFS distances against those coset lengths.

Exact claims verified: there are \(840\) labelled systems, \(36\) trades incident with each, \(15{,}120\) undirected trades, diameter \(3\), distance distribution \((1,36,395,408)\), and common-block/distance counts \((12,0,1)\), \((6,1,36)\), \((4,2,27)\), \((3,2,152)\), \((2,2,216)\), \((1,3,216)\), \((0,3,192)\). The six-block-trade graph is a proper-design graph; the previously studied chain with improper systems is different.

These checks are an exhaustive finite proof replay under the specified algorithms and point encoding, not a formal infinite certification. An independent scholarly audit has not been performed. The complete text of Griggs and Rosa's 2003 chapter on uniformly intersecting order-nine systems was not available; originality remains subject to that concrete risk.
