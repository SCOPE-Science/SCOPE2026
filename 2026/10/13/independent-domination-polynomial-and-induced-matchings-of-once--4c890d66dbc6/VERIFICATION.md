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

A maximal independent set D of S(G) intersects the original vertices in U; for W=V\U each inserted edge vertex z_uv must be selected exactly when both endpoints lie in W. Such D is automatically independent and all z_uv are dominated; original excluded w is dominated iff it has a neighbor in W. This establishes the full W-bijection and exponent n-|W|+|E(G[W])|. In every nonempty admissible W, each tree component contributes +1 to |W|-|E|, each cyclic component <=0, and one edge in every component yields an induced matching, so |W|-|E|<=im(G). The endpoints of a maximum induced matching attain equality. Any extra unicyclic component at equality would provide an extra disjoint induced-matching edge, so the minimum coefficient consists exactly of im(G) nontrivial tree components. Forest DP states A(excluded), B(included supported by child), C(included awaiting parent) have the correct edge and vertex weights; the root uses A+B. Independently enumerate all 76 labeled graphs of order <=4 by brute maximal independent sets and compare exact polynomial/induced matching boundary.

## originality

PASS

Best-of-knowledge: older independent-domination-polynomial papers derive general generating identities; subdivision-domination studies generally analyze selected families. A 2019 paper gives some family-specific values including a ladder formula contradicted at L_3 by a concrete four-vertex independent dominating set (the printed value is six), so that formula cannot imply the all-graph bijection. No inspected primary treatment supplies the general no-isolates W correspondence, induced-matching minimum identity, and all-coefficient forest recursion together.

## value

PASS

The universal bijection is a substantial reusable structural description of all maximal independent sets of fully subdivided finite graphs; the induced matching endpoint connects separate natural graph invariants and the exact polynomial-time forest DP enables all-coefficient computations. It also resolves/diagnoses misleading special-case formulas, not merely a small-instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
