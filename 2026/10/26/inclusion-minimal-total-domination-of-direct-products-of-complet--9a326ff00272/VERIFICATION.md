---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Identify cells with incidence edges in K_{p,q}. A selected set totally dominates iff no row+column pair covers all selected edges, including checks at selected cells. If a matching of size three occurs, those three edges dominate and all larger selected sets are nonminimal; any two-edge subset fails via a mixed cover. Otherwise Konig matching-cover duality supplies a vertex cover of size at most two, which may be neither a single vertex nor a mixed row/column pair, so must consist of two rows or two columns. Exactly two distinct edges per supported row/column are necessary and sufficient for inclusion minimality. Inclusion-exclusion subtracts full 2x2 intersections from the two four-cell families, giving 6*C(p,3)*C(q,3) z^3 plus [C(p,2)C(q,2)^2 + C(q,2)C(p,2)^2 - C(p,2)C(q,2)] z^4 (p>=3), or C(q,2)^2 z^4 (p=2). Direct open-neighborhood exhaustive checks over 2x2,2x3,2x5,3x3,3x4,4x4 gave exactly predicted coefficients (e.g. 3x3 {3:6,4:45}, 4x4 {3:96,4:396}). The 2x2 disconnected boundary gives one four-cell minimal set.

## originality

PASS

PASS, qualified: Henning–Kazemi 2012 establishes the *minimum* k-tuple total domination of direct complete-graph products; Kazemi 2018 Proposition 7 establishes upper 2k+2 for K_n x K_2 and explicitly asks Question 1 for general factors. The present k=1 all-factor upper value and complete inclusion-minimal polynomial answer a nontrivial special case, while k>1 remains open. Iswadi 2011 studies metric-locating-total domination, a stronger and different property. Bahadir et al. study general well-totally-dominated graphs, not this full labeled polynomial. No earlier source located enumerating all minimal open total dominating sets in the exact product family.

## value

PASS

PASS: An explicit open question concerning the upper k-tuple parameter is resolved at its natural k=1 boundary, and the full inclusion-minimal size distribution is much stronger than the known minimum domination parameter. The classification and well-totally-dominated criterion are mathematically motivated complete results for a standard categorical graph product.

The dated certificate retains the supplied scientific assessment, sources and limitations.
