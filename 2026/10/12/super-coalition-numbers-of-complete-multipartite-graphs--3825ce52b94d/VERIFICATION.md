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
The symbolic proof establishes the theorem for arbitrary connected complete multipartite graphs. The critical checks are: (1) the direct witness definition is equivalent to the stated complement criterion; (2) every coalition partner union leaves at most two vertices, so more than four blocks are impossible; (3) a four-block partner graph either contains a two-edge matching, forcing the \(K_{2,2}\) exception, or is a star, forcing three distinct non-singleton partite classes; and (4) both cases have explicit constructions.

`verify.py` independently implements the graph, the literal super-domination predicate, and exhaustive set-partition enumeration. It checks every connected complete-multipartite part profile of order \(2\) through \(8\), every vertex subset for the complement criterion, and three explicit universal-vertex examples. The finite census is not used to justify the infinite statement.
