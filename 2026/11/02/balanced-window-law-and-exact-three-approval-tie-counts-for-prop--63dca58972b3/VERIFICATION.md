---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Let n>=3 cyclic labeled voters/candidates, each voter approves d consecutive positions, k selected, 0<=k<=n, and f has positive strictly decreasing increments through d. Each selected candidate appears in exactly d windows, so sum_i b_i=dk. Discrete concavity gives universal upper bound (n-r)f(q)+rf(q+1) at q=floor(dk/n), r=dk-nq, with equality exactly if every window count is q or q+1. The periodic mechanical-word choice x_j=floor((j+1)k/n)-floor(jk/n) gives a feasible k-subset whose every d-window sum is balanced, establishing the biconditional and independence from f including PAV. At d=3 sparse minority t=min(k,n-k), 3t<=n, spacing >=2 of the majority between minority bits gives n/(n-2t)*binom(n-2t,t). In the central case the absence of 000 and 111 forces every cyclic run length 1 or 2, and summing pairs of binomial run choices with weight n/a gives the stated exact count. Complement and k=0,n cases are covered. An independent Python exact mask enumeration at n=12,k=6 counts 174 winning committees; the script supplied covers n<=12 all d and n<=18 for d=3. This is corroboration, not proof for all n.

## originality

PASS

Qualified PASS for a complete all-optimum committee description for a natural uniform cyclic voter profile, independent of strictly concave Thiele weights, and an all-n exact d=3 labeled tie-count formula. Janeczko–Faliszewski 2023 prove general tie-counting complexity, and Ai 2026 general PAV optimal-set complexity; Avramidis et al and Lassota–Sornat study algorithms on structured interval profiles rather than a closed exact cyclic symmetric winner-set distribution. Jensen smoothing, mechanical balanced words and circular run counting are classical proof ingredients; a prior application to this exact voting profile could render the result covered, and searches cannot guarantee priority.

## value

PASS

Tie-breaking uncertainty matters in multiwinner voting. A canonical regular circular profile can have many maximizing committees, and the theorem determines all optimizers, common score, an exact labeled count for d=3 and an exponential family of ties; the n=12,k=6 count 174 gives a concrete nontrivial example. It is a natural whole family, not an arbitrary one-off census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
