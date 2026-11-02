---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

P_n is precisely the intrinsic-Euclidean zero-sum l1 section with positive and negative masses at most one. A sign sector with k positive coordinates has coarea weight sqrt(n)/[(n-1)(k-1)!(n-k-1)!], and conditional radial parameter s has density (n-1)s^(n-2); the two simplicial direction distributions are independent uniform Dirichlet. Hence E[s²]=(n-1)/(n+1), conditional E||X||²=2(n-1)/(n+1)[1/(k+1)+1/(n-k+1)], and weighted Vandermonde gives trace 4(n-1)(2n-1)/(n(n+1)²). Permutation symmetry fixes the full covariance scalar; multiplying the sector counts gives Vol=sqrt(n) C(2n-2,n-1)/(n-1)!. Substitution into the dimension-matched cross-polytope constant yields the claimed exact rational power R_n^(2(n-1)). Exact n=2 equality, n=3,4 deficits and gamma-logconvexity lower bound C(2d,d)>=4^d/sqrt(pi(d+1/2)) together with the decreasing tail factor prove strict R<1 for n>=5; Stirling gives (3/2-log pi)/2. Independently recomputed all rational weighted moments and ratio signs n=2..31. Finite tests are not used to prove n unbounded. Caveat: the root polytope notation is full type-A, not positive root.

## originality

PASS

Qualified PASS after comparing same body under complete-graph symmetric edge polytope, full type-A root polytope, and the central l1 section. D’Alì–Delucchi–Michałek identify the body and investigate Ehrhart, facets, graph structure; Chen–Davis–Korchevskaia establish facet graph correspondence; Kipp characterizes local isotropic maximizers and crosspolytope benchmark. None of their inspected results gives uniform volume second moments for this complete-graph family and its strict all-dimensional ratio.

## value

PASS

The full complete-graph root polytope is a standard combinatorial/convex-geometric family, and its intrinsic uniform-volume covariance and isotropic constant are natural affine invariants not determined by Ehrhart counts. An exact covariance plus dimensionwise strict comparison to cross-polytopes and sharp first-order isotropic deficit constitute a useful continuous-measure classification in all dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
