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

For n>=3, B=2^n, A=7B, m=A+1 and S=<A2^i+1>, the residues mod m are represented by w(t)=At+m*lambda(t) for 0<=t<=A, where lambda minimizes number of Mersenne coins (2^j-1). Nonnegative combination normalization plus lambda(t)<=t handles all multiples of m. The Apéry gap p(t)=w(t)-m is pseudo-Frobenius if each nonwrapping added coin c_j satisfies lambda(t+c_j)<=lambda(t); wrapping additions are automatically in S. Binary digit sum gives exact lambda(B-d)=d, lambda(A-d)=d (5<=d<=n+2), lambda(t1)=lambda(t2)=n+2 with t1=4B-n-2, t2=6B-n-2. Constructive coin decompositions bound all suffix values after t1 by n+2. Also lambda(A)=4,lambda(A-1)=5 and small suffix upper bounds, proving all displayed indices. Distinct residues give exactly n+2 explicit PF elements and type>=n+2, not exact type. Independent Dijkstra/coin checks verified n=3,4,5,6 and all proposed gaps, not an all-n proof.

## originality

PASS

Earlier Proth Frobenius, genus and special k=2^r+1 pseudo-Frobenius analyses do not establish these k=7 negative-offset gaps. The exact infinite family is a qualified best-of-knowledge new inclusion, not a complete type classification; the later journal text remains a possible coverage risk.

## value

PASS

The first three-one-bit Proth generator family is a natural instance where the Apéry order can be attacked by binary expansions. A growing n+2 explicit lower bound and two separated gap branches plus a top cluster give structural type information not mechanically determined from Frobenius or genus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
