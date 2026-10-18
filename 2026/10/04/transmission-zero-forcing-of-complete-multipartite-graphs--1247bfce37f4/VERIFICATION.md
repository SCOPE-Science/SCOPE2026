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

For noncomplete K_{n1,...,nr}, ordinary zero forcing requires at least N-2 seeds: with >=3 white vertices a first force either cannot occur or leaves >=2 whites of one part, after which no force is possible. A minimum complement must consist of vertices in distinct parts. For omitted x in part i,y in j, synchronous round-one weights are (nj-1)alpha and (ni-1)alpha; the only possible second round adds (N-nj-1)alpha+(nj-1)alpha^2 to y after x fills. Thus the size-N-2 criterion is beta<=max_{s>=2} min((s-1)alpha,(N-s-1)alpha+(s-1)alpha^2); N-1 succeeds iff beta<=Delta alpha. All-singletons K_N has N-1/N transition at (N-1)alpha. This is a symbolic proof for positive alpha,beta<=1, not an inference from finite tests; independent exact-rational direct subset testing of 592 small graph/parameter instances agreed. Boundaries beta=equality are included by >= threshold condition.

## originality

PASS

The exact three-phase arbitrary multipartite classification is not implied by the initiating paper's two-part subfamilies or its maximum-degree top phase, and the third-part second-round interaction is genuine. Resultary also indexes a simultaneous narrower r>=3 statement (record 2), which is equivalent on the new domain; originality of this broader canonical version is accordingly best-of-knowledge/priority-sensitive and NOT a claim that the two records are independent discoveries.

## value

PASS

All complete multipartite graphs form a natural basic test family for a newly defined weighted one-shot propagation invariant. Classifying the entire N-2/N-1/N phase diagram in terms of exact part sizes (including r=2 and complete degeneracies) is a reusable structural classification, not a tiny finite computation. Its value is the family theorem; the simultaneous narrower record should not be counted a second independent contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
