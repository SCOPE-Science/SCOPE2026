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

Using D(n)/n=sum_{p|n} e_p/p, prime powers imply a=p-1. For p<q, a q+b p=(p-1)(q-1), equivalent (a+1)q+(b+1)p=pq+1. For p=2, parity forces a+1 odd>=3 and hence (a+1)q>2q+1 impossible. For odd p, B=b+1>=2 forces 2<=A=a+1<=p-1, uniquely A=q^{-1}(mod p), so q not congruent1 mod p. Conversely for odd p<q with q not congruent1, u inverse in 2..p-1 and k=(u q-1)/p with 1<=k<q; B=q-k cannot equal1 since q(p-u)=p-1 impossible. Thus a=u-1,b=q-1-k uniquely positive. Squarefree a=b=1 forces (p-2)(q-2)=3, giving n=15. Fixed odd p the p-2 allowable nonzero residue classes give asymptotic (p-2)/(p-1)Li(Q) by PNT in AP. Independently enumerated all 2<=p<q<100 primes and positive a<p,b<q; 249 admissible prime supports matched exactly, only squarefree (3,5). The unbounded claim rests on modular proof and PNT in AP.

## originality

PASS

Structured searches compared exact claims and implications; see named checks and inspection evidence. Best-of-knowledge only; residual literature-priority risks remain.

## value

PASS

This is a complete unbounded arithmetic coincidence classification for every integer with at most two distinct prime factors, including uniqueness for each admissible prime support, a sharp squarefree exception and positive-density support family. It addresses a natural equality between standard multiplicative arithmetic functions; despite elementary algebra, the support stratification is not an arbitrary numerical table or literal substitution into a listed prior theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
