---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The exact difference-body identity D=Delta(n,k)-Delta(n,k)={z:sum z_i=0, ||z||_infty<=1, ||z||_1<=2m} follows in both directions: any vertex difference has signed mass <=min(k,n-k), while for an admissible z the intervals max(0,-z_i)<=y_i<=min(1,1-z_i) have endpoint sums t and n-t and admit sum y_i=k. On the intrinsic zero-sum Euclidean subspace, centered-ball inclusion in D is equivalent to two sharp support constraints. Projection e_i-1/n has norm sqrt((n-1)/n); the maximizing L1 norm of a unit zero-sum vector is 2 sqrt(floor(n^2/4)/n), with equality exactly on balanced two-valued sign blocks. Hence width min(sqrt(n/(n-1)),m sqrt(n/floor(n^2/4))) and the exact union of active equality normals. The tie condition m^2(n-1)=floor(n^2/4) reduces for odd n to n=4m^2-1, and for even n>=4 has no solution. This checks all n>=3 and 1<=k<=n-1, including the n=3,k=1 coincident-family boundary. An independently coded SciPy convex-hull facet reconstruction of D for eight (n,k) cases n=3..6 gives maximum absolute error 2.22e-16 in predicted intrinsic width, but the finite test cannot prove the all-n identity.

## originality

PASS

No stronger published theorem identified that determines the same difference-body inradius and its entire two-normal-family phase classification for all proper hypersimplices. The rank-one standard regular-simplex width is acknowledged prior knowledge; the original hypersimplex inradius and matroid-base-polytope rank-radii concern different convex bodies. This is best-of-knowledge, not absolute priority.

## value

PASS

Hypersimplices are canonical uniform-matroid base polytopes; intrinsic Euclidean minimum support width and all extremizing normals are natural dimension- and rank-sensitive invariants. The two competing norm barriers, exact difference body and arithmetic two-orbit transition (n=4m^2-1, first genuinely distinct tie (15,2)) are a complete structural classification beyond an arbitrary finite table or trivial simplex restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
