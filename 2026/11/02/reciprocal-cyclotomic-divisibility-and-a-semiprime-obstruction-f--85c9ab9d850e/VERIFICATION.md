---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

A minimal nontrivial reciprocal-divisibility solution must have 1<a<b. Setting c=(a^2-a+1)/b gives 1<=c<a, bc==1 mod a, and from a|F(b) one gets a|c^2 F(b)==F(c) mod a; also c|F(a). Thus (c,a) is a strictly smaller solution unless c=1, which forces a|F(1)=1, a contradiction. Separately S(n)=n^-1 sum_{d|n}d phi(d), multiplicative numerator on prime powers (p^{2e+1}+1)/(p+1)==1 mod p, excluding p and p^2. For pq, S(pq)=F(p)F(q)/(pq) and integrality would imply the forbidden reciprocal pair. All cases Omega<=2 exhausted. Independent finite tests to a,b<=300 and n<=500 corroborate, not replace descent.

## originality

PASS

Qualified PASS: the closest 2026 De Koninck–Letendre paper treats the identical gcd-reciprocal sum and its semiprime reciprocal polynomial relation, including a bound on solutions (Proposition 1); the reviewed special assertion is *no* nontrivial positive reciprocal divisibility pairs at all, rather than an upper bound on count and a global O(X^{2/3+epsilon}) sparsity result. The full primary HTML mathematical comparison did not identify the universal descent obstruction. Classical Vieta-jumping-type descent gives residual priority risk.

## value

PASS

PASS: excluding every prime, prime square and squarefree semiprime is a natural sharp initial factor-count obstruction for the integrality problem; a clean universal cyclotomic two-cycle rigidity lemma is independently useful. No claim about Omega>=3 or existence there.

The dated certificate retains the supplied scientific assessment, sources and limitations.
