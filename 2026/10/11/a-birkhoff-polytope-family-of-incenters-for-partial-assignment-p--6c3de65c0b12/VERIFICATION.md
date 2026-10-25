---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For N>=3 and integers 2<=k<N, the known exact facet description in H_k is nonnegative coordinates, row<=1 and column<=1. Orthogonal projections of coordinate and row/column normals onto the total-zero tangent space have norms q=sqrt(1-N^{-2}) and h=sqrt(N-1). A ball of radius r in H_k is contained iff C_ij>=qr and all row/column sums<=1-hr. Summation gives r<=k/(N sqrt(N^2-1)) and r<=(N-k)/(N sqrt(N-1)); uniform C0=kJ/N^2 attains the min. Equality of bounds occurs at k=N+1-sqrt(N+1). Below or at equality, the coordinate lower bounds sum to total k and force unique C0. Above it, both margin upper bounds sum to total k and force all margins k/N; subtracting sJ, s=(N-k)sqrt(N+1)/N^2, leaves lambda B_N with lambda=[k-(N-k)sqrt(N+1)]/N>0. This proves full center face, dimension (N-1)^2, N! vertices and precise facet contacts. Integer equality iff N=h^2-1,k=h(h-1),h>=2. All k-assignment vertices have squared norm k and uniform barycenter C0; averaging squared distances gives k-k^2/N^2+||Z-C0||^2, forcing unique circumcenter and contact with every vertex. Independent LP checks 45 (N,k) cases through N=11 and enumeration of all vertices in six small cases matched; this finite evidence corroborates but does not replace the all-parameter proof.

## originality

PASS

Best-of-knowledge original exact Euclidean radius and all-incenter phase classification for the canonical fixed-k complete-bipartite matching slice. Primary same-object full texts establish the H-representation and combinatorics but not the metric result; the closest published metric polytope results have nonisometric affine hulls or different objects/optimizations. All four structured comparisons and genuine primary full-text inspections are recorded. The identical Resultary hit is the same research record, not independent earlier coverage.

## value

PASS

The fixed-k nonattacking-rook polytope is a natural polytope in assignment optimization and combinatorial convexity. The Frobenius largest-ball radius measures simultaneous robustness of entry positivity and row/column capacity constraints. Beyond a computable number, this establishes a sharp rank transition from a singleton center to a full (N-1)^2-dimensional Birkhoff-polytope family, classified through vertices, coordinate tangencies and the rare integer critical ranks. The outer sphere remains uniquely centered and contacts all combinatorial vertices. This is a motivated complete geometric classification rather than an arbitrary finite slice, numerical table, or restatement of the standard Chebyshev LP. The proof is elementary given known facets, but the structural optimizer-face classification is not a textbook numerical plug-in.

The dated certificate retains the supplied scientific assessment, sources and limitations.
