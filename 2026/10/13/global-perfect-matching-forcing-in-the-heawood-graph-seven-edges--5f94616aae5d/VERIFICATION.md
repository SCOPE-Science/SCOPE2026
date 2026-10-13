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

# Computational verification and limits

Execute `python3 verify.py` using Python 3.10 or later. The program has no third-party dependencies. It rebuilds the incidence graph, all perfect matchings, the 178 distinct differences, and all 170,544 relevant size-six or size-seven edge subsets. It checks Ryser's 7-by-7 permanent independently of the backtracking matching count and uses both symmetric-difference transversals and direct signature injectivity. It also generates every one of the 336 incidence automorphisms, checks preservation of all matchings, and exhaustively partitions the 812 hexagon transversals and 8064 optimum sets.

Expected main lines are:

```text
VERIFY_OK H_vertices=14 H_edges=21 matchings=24 ryser_permanent=24
VERIFY_OK matching_pair_differences=178 sizes=6:28,10:84,12:42,14:24
VERIFY_OK six_edge_subsets=54264 hexagon_hitters=812 all_obstructed_by_decagons=YES
VERIFY_OK seven_edge_subsets=116280 globally_forcing=8064 minimum_global_forcing=7
VERIFY_OK group=336 seven_orbits=30 sizes=168x12+336x18 six_hex_orbits=5
```

The complete output additionally gives all 30 optimum orbit representatives and all five hexagon-transversal orbit representatives, each with its exact orbit size. Binary-mask bit positions refer to the zero-indexed lexicographically ordered 21 incidence edges. The `orbit_representatives.csv` file encodes the same 30 optimum orbits. The proof is finite and exhaustive only for this one graph; no generalization to larger graphs is asserted. No independent external audit has been performed.
