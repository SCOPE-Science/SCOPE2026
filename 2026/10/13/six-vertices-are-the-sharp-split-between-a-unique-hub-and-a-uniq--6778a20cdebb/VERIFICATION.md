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
The embedded `verify_degree_center_boundary.py` performs an exact finite replay using only the Python standard library.

Every labeled simple graph through six vertices is generated. Connectivity is independently checked by:
1. breadth-first search;
2. union--find.

For every connected graph, all-pairs shortest-path distances are independently computed by:
1. breadth-first search from every source;
2. Floyd--Warshall.

The resulting distance matrices must agree exactly. Degree is read directly from adjacency, and eccentricity is the exact row maximum of the distance matrix.

The replay verifies:
- connected labeled counts \(1,1,4,38,728,26704\);
- degree-maximizer-set versus center-set disagreement counts \(0,0,0,0,400,18480\);
- distinct unique leader counts \(0,0,0,0,0,720\);
- exactly two six-vertex conflict isomorphism classes;
- orbit size \(360\) for each class;
- representative edge sets \(\{02,04,05,12,13\}\) and \(\{04,05,12,13,14,23\}\);
- degree vectors \((3,2,2,1,1,1)\) and \((2,3,2,2,2,1)\);
- eccentricity vectors \((3,3,2,4,4,4)\) and \((3,3,4,4,2,4)\);
- farness vectors \((8,10,8,14,12,12)\) and \((10,8,11,11,8,14)\);
- the closeness tie between the competing maximum-degree and center vertices in both classes.

Run:

`python3 verify_degree_center_boundary.py`

The first output line must be:

`VERIFY_OK`

The exhaustive classification stops at six vertices.
