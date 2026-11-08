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

The exact Stirling partition expansion [Adelberg--Lengyel equations (5.2),(5.4)] has unique 2-adically lowest term corresponding to u_1=r=n-k: v2(i+1)<i for i>1. With q=2^h, k=bq+a, B=q-a, T=(c-b-1)q, Kummer yields constant t_b=v2 binom(2c-b-1,c) for T<=d<=r. For d<T, v2 Lambda <=(r+d)/2 implies r-v2 Lambda >=(B+1)/2 > t_b under B>=2t_b, so no cancellation of the leading term. Legendre gives v2 S(cq,k)=s2(a)+s2(b)-s2(c)+t_b. Counting excluded block endpoints and B<2t_b gives E(c) independent of h. The positive index k=cq works; k=0 has undefined ordinary valuation. Independently computed 1881 sufficient-range exact recurrences of 2052 finite examples, and inspected packaged verify.py partition check and modular range; no finite-to-infinite inference.

## originality

PASS

The published Adelberg--Lengyel 2021 Theorem 3.1 covers an initial block half subject to scale assumptions, whereas its Conjecture 3.1 requests density one for n=c2^h. The new strict valuation estimate supplies a uniform O_c(1) exception bound, stronger than the published half-block theorem and directly proves the positive-index conjecture. A full-text reading of the original theorem and conjecture plus Resultary/targeted literature searches found no directly dominating statement. This is best-of-knowledge, not priority certification.

## value

PASS

Resolves a specifically stated arithmetic conjecture and supplies an explicit uniform finite exception envelope rather than an asymptotic existence argument; the stronger bound and all-height scope would be independently useful for dyadic Stirling valuation research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
