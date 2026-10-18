---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For any finite connected n-vertex G (n>=2), the private leaf v-prime forces selecting at least one of {v,v-prime} for each v; a semipaired dominating set must have even size, yielding 2ceil(n/2) lower bound. In a tree T, repeatedly remove and pair either two leaf siblings at distance two or the unique terminal leaf and its adjacent support vertex at distance one, maintaining a tree; induction yields a matching saturating all or all but one vertex in T². A spanning tree of G transfers these distance<=2 pairs to G. Choose V(G) for even n or V(G) union unmatched leaf for odd n. Independent enumeration checked the exact minimum for all 771 labeled connected G of n=2..5.

## originality

PASS

The general exact semipaired leaf-corona invariant is not a published semitotal-corona formula: semitotal domination requires local partners but no global even pairing. The tree-square matching lemma is a known combinatorial phenomenon and is used as an ingredient rather than claimed as exclusive novelty.

## value

PASS

A uniform sharp parity-dependent semipaired domination formula over every connected base graph is an exact classification of a natural graph product, with a constructive certificate and a meaningful distinction from semitotal domination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
