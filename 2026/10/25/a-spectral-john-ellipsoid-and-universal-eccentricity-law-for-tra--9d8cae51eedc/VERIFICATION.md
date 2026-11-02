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

The bipartite stable-set inequalities are all facet-defining by total unimodularity and degree>=3. The scalar trace root is unique by spectral monotonicity with 0 and 2d eigenvalues and Jensen/chord bounds. Vertex/edge transitivity makes two facet-support norms constant; the root forces every slack equal to its corresponding ellipsoid radius. Explicit positive weights 2/(r+2) per coordinate and 2r/[d(r+2)] per edge satisfy the exact John centroid/covariance identities, proving global maximality and uniqueness. The H spectrum and second trace moment tr[(H/d-I)^2]/N=1/d yield the strict semiaxis bracket and universal large-degree limit. Newly constructed 3-cube verifies Q_ii=a², each edge norm=b² and John matrix equality to 3.6e-15; finite check is corroboration only.

## originality

PASS

Best-of-knowledge: two full closest John-ellipsoid primary results use related transitive incidence spectra but different ambient polytopes/facets; neither established the vertex-space all-contact theorem and universal eccentricity limit.

## value

PASS

The explicit metric maximum-volume inscribed ellipsoid on stable-set polytopes of a natural infinite symmetry family is not just an optimized example. A universal signless-Laplacian prescription, exact all-facet contacts, and an unusual graph-independent high-degree limiting eccentricity reveal structural geometry with plausible use for further graph-polytope metric questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
