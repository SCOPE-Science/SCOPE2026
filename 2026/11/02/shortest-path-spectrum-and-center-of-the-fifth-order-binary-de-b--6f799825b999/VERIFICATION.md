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

# Verification notes

The two included Python programs use only standard libraries, no external data files, and fully enumerate their finite domains. They were executed from the final artifact paths. No external independent audit was performed.

`python3 verify_truth_table.py`: checks all \(65536\) Boolean truth tables, exactly \(2048\) one-cycle tables, all cross-join edges, the decreasing-distance move for all ordered distinct table pairs, all \(2096128\) unordered pair distances, the eccentricity distribution and the uniqueness of all \(736\) eccentricity-seven antipodes. Ends with these markers:

```
TRUTH_TABLE_65536_CANDIDATES_2048_FULL_CYCLES_PASS
CROSS_JOIN_38704_EDGES_AND_ALL_PAIR_GEODESIC_DESCENT_PASS
DISTANCES_38704_305376_758800_710976_254800_27104_368_PASS
RADIUS5_CENTER48_DIAMETER7_ANTIPODE_PAIRS368_PASS
```

`python3 verify_hamiltonian_cycles.py`: independently enumerates Hamiltonian cycles via a depth-first traversal of the directed binary de Bruijn state graph, tests chord-interlacement to generate cross joins, and performs breadth-first search from all \(2048\) Hamiltonian cycles; it does not reuse the first program's validity enumeration or edge construction. Ends with:

```
DIRECT_HAMILTONIAN_DFS_2048_CYCLES_AND_92636_PREFIX_NODES_PASS
CIRCULAR_CONJUGATE_CHORD_INTERLACEMENT_38704_CROSS_JOINS_PASS
ALL_2048_BFS_HAMMING_METRIC_AND_DISTANCE_SPECTRUM_PASS
INDEPENDENT_RADIUS5_CENTER48_DIAMETER7_PASS
```

**Proof boundary.** The finite census is exhaustive for order-five binary cycles and their two-suffix cross joins. The structural equality of graph distance with half the Boolean table Hamming distance follows from the established cross-join descent argument. No assertion is made for general order, alternate equivalence relations, or nonbinary alphabets. A log without source code or a partial search would not suffice; the two standalone exhaustive programs are the reproducible certificates.
