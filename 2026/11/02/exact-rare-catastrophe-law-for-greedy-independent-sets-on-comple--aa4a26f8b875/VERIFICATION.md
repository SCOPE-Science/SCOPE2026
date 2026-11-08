---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For H d-regular balanced bipartite, C4-free, n≥d+2, the input G is its K_{n,n} CROSS-EDGE complement, not graph complement. Any mixed independent set corresponds to complete bipartite incidence in H, hence one side singleton (C4-free), and maximality forces a centered star of size d+1; other maximal sets are U,V size n. Conditional on first accepted u in U, the next feasible vertex is one of n+d−1: probability d/(n+d−1) of opposite-class star; d(d−1) same-class choices share unique neighbor v, which beats n−d outside U vertices with probability 1/(n−d+1). Sum p=dn/((n+d−1)(n−d+1)). Per-atom probability p/(2n) for d≥2; for d=1 each matching pair has 1/n². Counting neighbors without 4-cycles gives n≥1+d(d−1), so d=O(sqrt n), p~d/n and Var(X)~dn uniformly. Projective-plane incidence H attains limiting n^(3/2) variance coefficient one along prime-power orders. Independent exhaustive 8! order calculation for H=C8, n=4,d=2 yielded p=8/15 and each of 8 star atoms 1/15; n=3,d=1 yielded each of 3 matched-pair atoms 1/9.

## originality

PASS

Best-of-knowledge originality of the specific final claim, excluding established background components; real Resultary searches and relevant primary-source statements did not show a dominating equivalent, with explicit primary access and unindexed-source residual risks. A chain-graph exact law only covers nested neighborhoods. Even H=C8 gives nonnested cross-neighborhoods, defeating specialization, and complete multipartite exact laws lack partial deletion patterns.

## value

PASS

Exact complete probability distribution of random-order greedy MIS for a natural dense class with sparse incidence deletions, including uniformity of each rare small atom, all moments and a sharp variance-order envelope attained by projective-plane incidences. These are meaningful probabilistic graph invariants beyond density/concentration estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
