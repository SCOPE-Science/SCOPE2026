---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For any finite simple connected cactus order>=3, every connected dominating set includes every cut vertex (otherwise two components of G-v cannot both be dominated from a connected selected set). Noncut vertices are leaves or each belong to exactly one cycle. For a cycle block, omitting >2 consecutive free vertices leaves an undominated middle vertex; omitting two disjoint runs splits selected vertices, with no bypass in the block-cut tree. Thus each cycle permits omission of zero/one/two adjacent free vertices, independent across cycles and leaves; this bijection gives x^a(1+x)^ell product over cycles of (x^q+q x^(q-1)+t x^(q-2)); q=0 and q=1 cases interpreted without negative powers, K1 and K2 separate. The discriminant q²-4t is >=0 for q=2 (t<=1), q=3 with articulation (t<=2), q>=4 (t<=q), and is negative exactly for the isolated triangle (q=t=3). Hence all nontriangle cactus roots real nonpositive and coefficient log-concavity/unimodality. Fresh independent subset enumeration for many connected tree/cactus samples confirms full polynomial and triangle exception, not infinite substitute.

## originality

PASS

Prior special-case connected-domination polynomials for paths, cycles, corona, friendship and wheel coalescences are credited. General block-cut combinatorics suggests a factorization but there is no stated full arbitrary-cactus connected-domination polynomial and unique-real-root-exception classification in the inspected published works. The recent Shao-Zhao root-closure paper proves substitution for lexicographic products and density of complex connected-domination roots; its accessible abstract does not decide the cactus-real-rooted locus. Full text was inaccessible, so an equivalent statement inside it remains explicit originality risk.

## value

PASS

Arbitrary cacti are a natural broad graph class; an exact block-factor bijection with sharp classification of nonreal-root exceptions immediately yields all coefficients, connected-domination number, real-rootedness and log-concavity. This is an all-order structural theorem beyond calculating a handful of cycle or friendship graph examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
