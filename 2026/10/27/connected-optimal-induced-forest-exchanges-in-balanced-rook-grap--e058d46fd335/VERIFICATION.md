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

# Verification instructions

Using Python 3.9 or later, execute `python3 rook_forest_verify.py` in a directory containing the standalone checker. No additional packages, web services, or other files are required. A successful run terminates with `VERIFY_OK`.

The checker reconstructs rook adjacency from cell indices and tests all induced vertex subsets at \(n=2,3,4\); it separately enumerates all Hamilton paths of \(K_{n,n}\) at \(n=2,3,4,5\) as pairs of permutations. From edge sets, it tests every possible one-edge deletion and every absent edge insertion against the complete set of Hamilton paths. This independently generates exchange adjacencies and evaluates connected components, degrees and triangles. It compares an unrelated reversal implementation for small parameters.

The expected output is:

```text
ROOK_INDEPENDENT_OK n=2 max_forest=3 maximizing_subsets=4
ROOK_INDEPENDENT_OK n=3 max_forest=5 maximizing_subsets=36
ROOK_INDEPENDENT_OK n=4 max_forest=7 maximizing_subsets=576
GRAPH_OK n=2 vertices=4 degree=3 edges=6 triangles=4 connected=1
GRAPH_OK n=3 vertices=36 degree=7 edges=126 triangles=156 connected=1
GRAPH_OK n=4 vertices=576 degree=11 edges=3168 triangles=5184 connected=1
GRAPH_OK n=5 vertices=14400 degree=15 edges=108000 triangles=216000 connected=1
VERIFY_OK
```

These are exhaustive finite computations at the displayed parameters only. The universal conclusions follow from the symbolic proof. Independent mathematical audit has not been performed. Literature access limitations are disclosed in the review.
