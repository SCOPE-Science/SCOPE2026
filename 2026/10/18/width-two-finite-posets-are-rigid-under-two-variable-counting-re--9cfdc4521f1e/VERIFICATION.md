---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Every equitable class in any finite strict poset is an antichain, since a minimal element of the induced order has zero internal predecessors. Thus the target and any matching competitor have only singletons and doubletons. In the target, two doubletons must have a cross-comparison by width. If both directions occurred, regularity would force indegree and outdegree one on the full bipartite four-cycle, impossible. The profile therefore gives either a directed matching or a complete order between each pair, in the competitor as well. Any two successive directed relations between doubletons compose to a nonempty relation, hence the quotient order is total. A matching from i to k forces both legs through every intermediary j to be matchings, since a complete leg composes with a regular nonempty leg to a complete comparison. Transitivity also forces the long matching to equal the composition. Consequently each interval spanned by a matching edge is a matching clique, and one may choose labels along consecutive matched pairs so that every longer matching is label-preserving. This gives reconstruction even if the competing strict poset has no width promise. It also yields a perfect elimination order and shows that the only flips are independent simultaneous flips on connected matching components, so that stable classes are precisely orbits. To make the logical bound explicit, use one-variable colour definitions of quantifier rank ≤t for t≤|P|−1, include the rank-≤t+1 coverage conjunct that each vertex has some listed colour, and enforce class sizes and interclass counts up to rank t+2. Coverage rules out extra, unlisted colours. Initial named unary colours cost rank zero and are preserved. The empty matching graph and n=1 both satisfy the formulas. The three checkers and verification record were inspected statically, not replayed; the finite counts are not premises of the proof.

## originality

PASS

The strongest indexed overlap gives relative counting-logic identification and orbit recovery for forest orders. This class intersects but does not contain width-two posets, and the report does not give the width-two matching rigidity, chordality or flip group. The general C² literature treats identification among arbitrary relational structures, which fails for some frozen targets and so cannot simply be applied. The supported distinction is the all-size width-two reconstruction under the strict-poset promise coupled with the explicit automorphism structure, not the general connection between refinement and C².

## value

PASS

The result identifies a natural bounded-width family from a weak invariant even against unbounded-width strict-poset competitors, and identifies precisely which automorphisms remain after refinement. The transitivity-induced composition rule explains why matching ambiguities that obstruct unrestricted identification disappear. It yields a full reconstruction and elementary abelian symmetry group, not merely a fixed-size collision count or an invocation of generic C² machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
