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

The q-round EF invariant is a partial bijection of the underlying points, preserving every chosen two-set. Before round j, at most 2(j-1) points on either side are assigned; if both root orders are at least 2q, the bijection can extend to the at most two new points, irrespective of Spoiler's side. Equality and intersection, hence the partial graph isomorphism, are preserved. For the path-forest lemma, in a path on s selected vertices each representing edge after the first meets its predecessor in one endpoint and is disjoint from all earlier edges other than that predecessor; it adds exactly one point. Distinct components use disjoint points, yielding the stated minimum, realized by disjoint root paths. An independent short check of the full lower bound is to take n=2k and use exactly one adjacency plus k-1 isolated selected vertices; the adjacent pair uses exactly three points and the isolates 2(k-1) fresh points, for minimum root order 2k+1. For n=2k+1, use k+1 pairwise disjoint two-sets, needing 2k+2 points. Both witnesses are existential of rank k+1, including n=2,3. They hold in every larger order and fail at n. Thus the formula separates exactly the claimed pairs and establishes the existential collapse, the least distinguishing rank, and the 2q-1 class count (empty singleton list at q=1). Bounded checks of these two pattern types for q=2,3,4,5 give respective first root orders 3,5,7,9 and 4,6,8,10. The frozen checker and its recorded q<=4 output were inspected, not executed or treated as an EF proof.

## originality

PASS

The exact all-rank partition and matching existential cutoffs are supported as distinct from the compared earlier literature. A same-date balanced Johnson result gives the q=3 partition on restriction, with the singleton T_2 added as explicitly noted there; that is material overlap, with no order inferred. A later-dated Resultary record gives the same rank theorem on n,m>=3 and a stronger unrestricted-depth variable-width theorem; its existential forest witnesses cover the same separations. Its exact implication is recorded, not dismissed as mere analogy. It is not evidence establishing earlier publication of the theorem. The judgment concerns the all-rank finding, not ownership of the generic EF technique, fixed-rank subcases, or newness of the claim relative to literature published after the frozen work.

## value

PASS

Triangular graphs are a canonical line-graph/Johnson family with unnamed underlying points. The result gives the full budget needed to detect root order in pure graph logic, not just eventual indistinguishability or isolated finite values. The fact that pure existential patterns attain the same sharp cutoffs despite the availability of alternation is useful to anyone analyzing the logical profile of this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
