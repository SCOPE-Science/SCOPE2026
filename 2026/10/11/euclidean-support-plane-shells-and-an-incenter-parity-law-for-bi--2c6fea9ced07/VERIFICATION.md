---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Centered roots from two perfect matchings are complementary (k-1)-simplices, with only their individual zero-sum relations, so free-sum facets omit one from each; count k² and intrinsic dim 2k-2. Solving exact facet normal equations gives x_h=-d+k1_{1<=((h-i) mod k)<=d} and y_h=x_h-1+k1_{h=i}; ||n_ij||²=k[k-1+2d(k-1-d)] and support value 1. Maximizing d(k-1-d) gives stated radius for both parities and k or 2k contacts. Cyclic center-averaging proves optimality; zero-sum contacting normals force active equalities at any optimum. For odd k, their span rank k-1; for even k the differences of adjacent contacting offset normals span ker(x-y), rank 2k-2, proving unique center. Independently reconstructed exact normals, Gram norms and rank for k=2..7; finite checks only diagnostics.

## originality

PASS

Best-of-knowledge mathematical comparison of the complete statement and stronger potential prior claims: None implies contact facet counts or affine dimension of optimal-center locus under the specified orthonormal metric.

## value

PASS

Exhaustive facet metric shells plus contact multiplicities and exact dimension of all inball centers for a natural bipartite-cycle root-polytope family; the odd/even change in uniqueness is a substantive geometric rigidity invariant, not merely a facet count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
