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

Distinct subset binary weights yield exactly C(n,k) ambient fixed coordinate hyperplanes. For each k-subset I, replacing two of its indices constructs a tangent point e_J with |I intersect J|=k-2, so coordinate functional p_I annihilates the entire affine tangent span (which requires intersection >=k-1). All ambient fixed hyperplanes are thus in the invariant projective dual. C*-Euler localization on its projective, potentially singular, variety gives chi=C(n,k). Compact-support additivity gives complement chi=0. k=1,n-1 correctly excluded. This all-n proof does not rely on finite checks.

## originality

PASS

Best-of-knowledge original Euler-characteristic identity for the full projective dual, not merely for Gr(k,n). Classical Grassmannian chi and torus Euler localization are prior ingredients, but do not by themselves say every coordinate hyperplane belongs to the dual. Full primary texts inspected cover topology of dual complements and singular/normality geometry, not this fixed-point count. The method is short, so an unindexed folklore observation remains a material priority risk.

## value

PASS

Determines a global topological invariant of generally highly singular projective duals uniformly in k,n, including Pfaffian degeneracy cases, via a non-obvious complete fixed-point inclusion. It yields a zero Euler characteristic for the complement. This is mathematically motivated by contrasting complicated singular geometry with ambient chi; it does not claim deeper Betti or Hodge data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
