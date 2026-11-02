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

The exact finite calculation can be reproduced with Python 3 (standard library only):

```
python3 verify_coloring_recursive.py
python3 verify_coloring_independent.py
```

The first program performs recursive proper-colouring enumeration on the explicitly specified eleven-vertex graph, constructs legal moves from neighbourhood constraints, computes all components and their signed-winding labels, and checks the metric from all \(56\) automorphism-orbit representatives.

The second program independently enumerates the \(240\) outer-pentagon colour words, all apex colours, and independent permitted shadow colours. It constructs every edge by grouping colourings that agree on ten coordinates, determines components via disjoint-set union, and obtains eccentricities by independently canonicalizing palette and dihedral symmetries.

Both programs were executed successfully from the final packaged paths. They agree on \(12{,}480\) states, \(45{,}240\) edges, two connected components of \(6{,}240\) vertices, two classes of the signed invariant, and component radius \(15\) and diameter \(17\). Their exhaustive enumeration is a finite certificate for this graph alone. These checks do not establish an infinite-family theorem or independent external review.
