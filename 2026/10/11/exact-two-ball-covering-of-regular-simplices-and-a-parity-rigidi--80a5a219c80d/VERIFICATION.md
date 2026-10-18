---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The barycentric variance identity gives r_q^2=s^2(q-1)/(2q) and forces a unique centroid when a ball contains q vertices. Pigeonhole forces a k-vertex ball in any two-ball cover, hence radius >=r_k. The hyperplane sum_A lambda_i=1/2 cuts the entire simplex into two convex cells whose vertices are selected original vertices and cross-edge midpoints. Those midpoints have squared distance s^2/4 to both complementary face centroids, no larger than r_k^2 and r_l^2, so convexity covers the entire body rather than only its vertices. In odd dimensions both balls must contain disjoint k-vertex groups at exact radius and their centers are unique; in even dimensions the radius slack r_k-r_(k-1)>0 gives a ball of second-center perturbations. Valid for all integer d>=3; no total optimizer classification for even d.

## originality

PASS

Claim-specific equivalence, implication, stronger-theorem and table checks were performed with actual Resultary/public primary searches. The novel remainder identified is not directly covered by inspected named theorems. This is a best-of-knowledge priority assessment, not exhaustive proof that no older equivalent exists.

## value

PASS

A two-ball covering of an entire convex body cannot generally be inferred from its optimal vertex clustering. Establishing exact all-dimensional covering and full odd-dimensional optimizer count plus an even-dimensional rigidity-to-continuum transition resolves a natural convex covering/facility-location invariant beyond routine face circumradius substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
