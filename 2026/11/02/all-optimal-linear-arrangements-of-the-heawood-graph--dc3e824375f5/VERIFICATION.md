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

# Reproducibility and scope

Run the supplied scripts from the artifact directory with a standard Python 3 installation:

```
python3 verify_subset_dp.py
python3 verify_fano_structure.py
```

The first script uses a cyclic difference-set construction of the fourteen-vertex Fano incidence graph. It checks every one of the \(16{,}384\) vertex subsets, determines the entire edge-boundary profile, counts all prefix-minimizing permutations by dynamic programming, and independently minimizes the total arrangement cost by a different subset recurrence. The assertions check \(69\) for the minimum cost and \(1{,}548{,}288\) for the optimizer count.

The second script independently constructs the graph from \(\mathbb F_2^3\), checks the Fano incidence axioms, enumerates all six-cycles as noncollinear point triples and every disjoint pair, verifies that both uncovered vertices meet each hexagon once and each other once, enumerates the permitted \(96\) cyclic-arc orders for each hexagon, and checks a complete optimal layout for each ordered pair. It verifies the product count \(28\cdot3\cdot96^2\cdot2\).

Recorded successful output from the actual scripts:

```
EXHAUSTIVE_HEAWOOD_SUBSET_DP_PASS
subsets=16384 minLA=69 optimal_orders=1548288
profile=0,3,4,5,6,7,6,7,6,7,6,5,4,3,0
minimizer_counts=1,14,21,42,98,252,28,168,28,252,98,42,21,14,1
FANO_DISJOINT_HEXAGON_STRUCTURE_PASS
Fano_triangles=28 disjoint_ordered_pairs=84
arc_orders_per_hexagon=96 middle_orders=2 total=1548288
```

The theorem's exact universal quantifiers concern all permutations of this **one** finite fourteen-vertex graph. These enumerations are exhaustive for that finite instance. The written proof separately establishes the structural characterization and the lower bound, rather than inferring an unbounded statement from sample computations. There is no independent scholarly audit or independent validation claim.
