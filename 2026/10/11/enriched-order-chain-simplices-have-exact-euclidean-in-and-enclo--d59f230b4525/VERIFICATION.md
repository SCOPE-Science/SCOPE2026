---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Verified from the primary signed-filter definition that the chain hull has exactly n+1 affinely independent u,v_k vertices. Reconstructed every facet a_k,b from vertices, norms N_{n-k}, and positive dependency b+sum 2^(k-1)a_k=0; for any inball (c,r), summing facet-clearance inequalities proves r<=2^n/(N_{n-1}+sum 2^(k-1)N_{n-k}). The facet-equality linear system attains that bound uniquely, yielding the asserted incenter coordinates. Bisector equations give q_j=1/2-2^-j; all vertices lie at squared distance n/4+4/3-2^-n-4^-n/3. q is in ordinary chain order polytope, hence in their enriched hull, so convex contact weights and parallel-axis identity prove the unique minimum enclosing sphere. Checked n=1 endpoint and asymptotic n->infinity. Independently recovered facets via matrix inversion, solved Chebyshev LP and exact circumcenters and nonnegative barycentric contact weights for n=1..10; finite checks only corroborate universal proof. Source verify.py uses floating-point inradius checks (contrary to prose claim of exact symbolic checks), but the analytic derivation does not rely on those tests.

## originality

PASS

Best-of-knowledge independent comparison of complete statements and implications: primary full-text sources establish enriched-polytope definitions, facets and transfer but not chain-specific metric radii; generic signed and marked poset radius theorems apply to different canonical objects and do not imply the asserted paired radii. Exact Resultary hit is mirror of audited claim, excluded from independent priority. Historical generic-simplex reduction remains a stated risk.

## value

PASS

The chain gives a canonical, geometrically natural family of all-dimensional reflexive simplices, and the inball and minimum enclosing ball are natural metric invariants rather than arbitrary finite slices. The explicit pair of centers/radii and sharp aspect ratio n^(3/2)/(2sqrt(3)) distinguish the enriched-order realization from its Ehrhart-equivalent enriched-chain crosspolytope partner (ratio sqrt(n)); these are not furnished by the known Ehrhart/transfer results, and a researcher comparing geometry of enriched poset polytopes could need these exact values. Elementary linear algebra after specialization is transparently acknowledged; no general arbitrary-poset radii claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
