---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The white-profile argument proves that any zero forcing set leaves at most two whites. Two whites in one part cannot force, and two whites in distinct singleton parts also cannot force; every other cross-part pair is forced in two steps. This gives the exact minimum sets, excludes larger inclusion-minimal sets, and yields the star-center irrelevance criterion. Fresh exhaustive simulation through order nine reproduced the full classification for all 87 multipartite isomorphism types tested. The repaired RESULT preserves this proof and changes the literature interpretation to acknowledge and correct the prior Proposition 3.2.

## originality

PASS

Grood et al. already state that every complete multipartite graph with at least two parts is well-forced, so that headline is prior-covered. However, their Proposition 3.2 proof asserts that any set omitting two vertices from different parts is zero forcing; this is false when both omitted parts are singletons. The repaired result explicitly acknowledges that prior theorem, corrects the singleton boundary, gives the exact minimal-set classification for every part profile, and derives the exact irrelevant-vertex classification. Those refinements are not supplied by the inspected prior sources.

## value

PASS

Correcting the boundary of a published family-level proposition and giving the exact minimal-set and irrelevant-vertex structure is mathematically useful: the singleton distinction changes which subsets are zero forcing, and the vertex classification answers a named structural question introduced in the same literature. The repaired presentation no longer claims novelty for the already-known well-forced conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
