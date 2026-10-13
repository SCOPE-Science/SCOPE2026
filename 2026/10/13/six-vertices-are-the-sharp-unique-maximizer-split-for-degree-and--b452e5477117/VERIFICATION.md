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
The embedded `verify_centrality_unique_boundary.py` performs an exact finite replay using only the Python standard library.

Every connected labeled simple graph through six vertices is generated directly.

All-pairs distances are independently computed by:
1. breadth-first search from every source;
2. Floyd--Warshall.

Closeness is reconstructed from both distance matrices.

Freeman betweenness is independently computed by:
1. exact shortest-path counting over unordered endpoint pairs;
2. the exact Brandes dependency recurrence.

The replay verifies:
- connected labeled counts \(1,1,4,38,728,26704\);
- degree-versus-betweenness maximizing-set disagreement counts \(0,0,0,0,150,9150\);
- distinct unique degree-versus-betweenness maximizer counts \(0,0,0,0,0,720\);
- distinct unique closeness-versus-betweenness maximizer counts \(0,0,0,0,0,720\);
- that every first unique conflict has the same unique degree and closeness maximizer;
- exactly one six-vertex conflict isomorphism class;
- orbit size \(720\);
- representative edges \(\{01,03,05,12,13,14,23,24\}\);
- degree vector \((3,4,3,3,2,1)\);
- closeness vector \((5/7,5/6,5/8,5/7,5/9,5/11)\);
- betweenness vector \((4,7/2,1/2,1,0,0)\).

Run:

`python3 verify_centrality_unique_boundary.py`

The first output line must be:

`VERIFY_OK`

The exhaustive classification stops at six vertices.
