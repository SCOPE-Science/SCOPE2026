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

All geodesics in a clique with length-one pendant leaves have length <=3. A triple of selected edges is on a geodesic exactly when it comprises two pendant edges at distinct hubs i,j and the clique edge ij. Active pendant hubs P therefore uniquely partition all EGP sets, with nonempty leaf-edge factors ((1+x)^b_i-1) and free clique edges outside choose(P,2). Inclusion maximality forces every active pendant edge and permissible clique edge, giving one facet for each nonempty P and 2^n-1 facets. The max formula follows by optimizing sum b_i - choose(s,2); singleton, pair, triple facet comparisons force nonpurity for all n>=3 and b_i>=1. One-leaf facet sizes give all n-3 consecutive missing sizes. Independent BFS shortest paths/direct subset enumeration yielded 45/7 sets/facets for b=(1,1,1), 79/7 for b=(1,2,1), 915/15 for b=(2,1,1,1); all maxima and formulas matched.

## originality

PASS

Previously known scalar gp_e of some pendant cliques is explicitly excluded from priority. A full two-variable all-subset polynomial, complete distinct facet census, heterogeneous positive leaf multiplicities, universal nonpurity and arbitrary gap lengths are mathematically stronger and not implied by the full-text 2024 scalar maximum theorem. 2026 corona paper remains a named high-priority full-text risk.

## value

PASS

The full two-weight polynomial and entire facet census of a natural heterogeneous leaf-bundled clique graph are useful beyond scalar edge-general-position number; the universal nonpurity and unbounded facet-size gaps give a structural boundary for related simplicial complexes. This is a complete family classification rather than an arbitrary tiny computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
