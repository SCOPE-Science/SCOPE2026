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

The theorem is proved by classifying induced subgraphs according to the two selected bipartition sizes and the number of selected deleted-matching edges. A graph with at least three vertices in each part contains a six-vertex subgraph with at least six edges; the same is true with two vertices on one side and four on the other. The only nonstar forests therefore have selected part sizes \((2,2)\), \((2,3)\), or \((3,2)\) with the requisite missing edges. Explicit disjoint case counts give the stated bivariate polynomial.

The self-contained `verify.py` uses the Python standard library. It enumerates all vertex subsets for each \(2\le p,q\le7\) and \(0\le t\le\min\{p,q\}\) independently of the symbolic case counting, recording both forest membership and the number of connected components. It separately counts induced \(P_4\) and \(P_5\) vertex subsets. Replay with `python3 verify.py` produced:

```text
VERIFY_OK parameter_triples=163 subsets=413040 path_type_checks=326 crown_balance_tests=5 max_vertices=14
```

No enumeration beyond these parameter ranges was performed, and the finite tests are not a substitute for the proof. No independent audit has been performed.
