---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The n−1 simple-root edge differences are a basis of the intrinsic Euclidean hyperplane sum x_i=0. Their ± convex hull is a crosspolytope with facet dual normals x^ε satisfying consecutive coordinate gaps ε_i. The zero-sum variance identity gives ||x^ε||²=(1/n)sum_{p<q}(sum_{k=p}^{q−1}ε_k)² ≤ n(n²−1)/12, with equality only the two constant sign patterns for n≥3 (and the two choices for n=2). Opposite tight facets bound every ball globally, so r=√[12/(n(n²−1))]; centers are exactly the stated hyperplane section and slack halfspaces, with relative dimension n−2, including zero-dimensional n=2. Opposite vertices of norm √2 force unique circumsphere center zero. Independently enumerated all sign vectors in small dimensions, confirming exactly two tight normals; proof itself is all n.

## originality

PASS

D’Alì–Juhnke-Kubitzke–Köhne–Venturello analyze graph symmetric-edge polytope face enumerations, gamma vectors and triangulations; Delucchi–Hoessly identify the same path body as a tree-metric fundamental polytope and study combinatorial face structure. Neither inspected relevant primary material gives the exact Euclidean distance-to-facet formula plus complete affine incenter locus. Indexed star/cycle/bipartite-root/polytope radii are different graph families and not stronger path formulas.

## value

PASS

Canonical A-type root-space realization differs metrically from an abstract crosspolytope. The exact n^(-3/2) inradius, two-facet tangency, and unexpected n−2 dimensional incenter family are natural geometric invariants useful in root-polytopal metric comparisons, not a mere face-count recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
