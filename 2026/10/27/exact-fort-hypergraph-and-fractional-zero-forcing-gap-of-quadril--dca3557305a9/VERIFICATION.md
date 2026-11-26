---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With neither hub in a fort, internal pages are all-or-none, and an exterior hub excludes exactly one full page, so the minimal forts are pairs of full pages. With only u present, each b_i must be in the fort (otherwise either b_i or a_i has exactly one inside neighbor); {u,b_1,…,b_r} is itself a fort and minimal. The other hub is symmetric. With both hubs present, each page needs an internal vertex and one suffices. A uniform internal-side choice contains a one-hub fort; every mixed choice is minimal, since a subset retaining both hubs still needs every selected internal vertex, and subsets with fewer hubs cannot contain a one-hub or full-pair fort. This yields 2^r+binom(r,2). A forcing set must hit every fort; conversely if forcing stops early its nonempty white remainder is a fort. The two-page forts allow at most one empty page. A set smaller than r cannot then include a hub; if it hits r−1 pages with singletons, a uniform-side choice misses a one-hub fort and a mixed choice misses the opposite mixed fort. At size r, precisely the double-page plus omitted-page pattern without hubs and the one-hub pattern with at least one internal vertex on that hub's side can hit all forts. Their counts r(r−1)2^(r−2) and 2r(2^(r−1)−1) give the claimed sum. The disjoint one-hub forts give the fractional lower bound 2; summing all full-page-pair inequalities gives r/2. Internal weights 1/4 and hub weights max(0,1−r/4) attain both bounds in the appropriate regimes and meet every mixed constraint. The ratio is 1 at r=2, 3/2 at r=3, and 2 at r≥4. Internally disjoint length-three u–v paths with the edge uv give planarity and bipartiteness, and deletion of any one vertex leaves a connected graph. Separate direct enumeration at r=2,3 gave 5 and 11 minimal forts and 6 and 30 minimum forcing sets, matching also the claimed families.

## originality

PASS

The inspected work already establishes the fort-transversal/fractional framework and an additive Cartesian-product lower bound for ordinary zero forcing, and the scalar Z(B_r)=r is not a separate novelty claim. The complete ordinary minimal-fort hypergraph, all labeled minimum ordinary forcing sets, and the exact fractional value with an attained factor two are distinct in the inspected evidence. Same-book paired domination and skew zero forcing use different constraints, and similar exact fort results on trees do not specialize to these books.

## value

PASS

The complete obstruction hypergraph reveals why one-per-page ordinary choices fail without a hub, and directly yields a labeled optimum census and an exact LP comparison. In particular, the family attains a factor of two on explicit planar, bipartite, two-vertex-connected graphs, not merely approaching it on trees, while retaining a tractable full description of the obstructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
