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

# Exact finite checks

The result concerns exactly the 50-vertex graph \(\operatorname{GP}(25,2)\) with three specified families of edges. Execute the accompanying self-contained Python 3 programs from their common directory:

```
python3 verify_bfs.py > bfs_output.json
python3 verify_floyd.py > floyd_output.json
```

The first script computes all shortest-path distances by breadth-first search, tests the MMD criterion on every one of the \(\binom{50}{2}=1225\) unordered vertex pairs, verifies 175 MMD edges, and directly verifies that the explicit 34-vertex set strongly resolves every pair. The second independently uses Floyd–Warshall, regenerates the 175-edge MMD graph, and verifies the exact five outer cliques, five disjoint inner five-cycles, and two matching independent-set witnesses. Both scripts assert all critical counts and certificate relations; their deterministic outputs are embedded in `bfs_output.json` and `floyd_output.json`.

The finite distance computation does not by itself prove an infinite-family statement. The mathematical argument establishes optimality at this order from finite and complete clique/odd-cycle coverings, not from solver timeouts or samples. No independent external scientific audit has been performed.
