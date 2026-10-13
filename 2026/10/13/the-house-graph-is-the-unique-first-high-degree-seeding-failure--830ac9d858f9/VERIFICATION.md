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
The embedded `verify_strict_majority_high_degree_boundary.py` performs an exact finite replay using only the Python standard library.

For every labeled simple graph on \(2\) through \(5\) vertices, connectivity is checked independently by breadth-first search and by transitive closure.

For every connected graph and every two-vertex seed set, the strict-majority closure is computed independently by:
1. synchronous round-by-round activation;
2. an incremental queue algorithm that maintains active-neighbor counts.

The two methods agree throughout.

The replay verifies:
- connected labeled graph counts \(1,4,38,728\);
- counts \(1,0,18,290\) with an unambiguous high-degree pair;
- suboptimal high-degree-pair counts \(0,0,0,60\);
- at five vertices, \(230\) cases with heuristic/optimal spread \((5,5)\) and \(60\) with \((3,5)\);
- exactly seven five-vertex isomorphism classes with an unambiguous high-degree pair;
- exactly one failing isomorphism class;
- the representative house edges \(\{01,03,04,12,14,23\}\);
- degree vector \((3,3,2,2,2)\) and threshold vector \((2,2,2,2,2)\);
- high-degree pair \(\{0,1\}\) with closure \(\{0,1,4\}\);
- optimal spread \(5\), attained by exactly \(\{0,2\},\{1,3\},\{2,4\},\{3,4\}\);
- house orbit size \(60\) and automorphism-group order \(2\).

Run:

`python3 verify_strict_majority_high_degree_boundary.py`

The first output line must be:

`VERIFY_OK`

The exhaustive classification stops at five vertices.
