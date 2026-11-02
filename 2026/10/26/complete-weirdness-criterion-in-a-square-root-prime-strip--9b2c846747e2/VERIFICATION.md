---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For n=2^k p q, M=2^(k+1)-1, x=p-M>0 even, abundance a=M(p+1)-xq and a<Mp<pq. Distinct proper divisors below a reduce semiperfectness to a=r+sp+tq (0<=r,s,t<=M). When weird and a>=q, both terminal residues t=0 and t=1 exceed M; their differences give nonzero delta with |delta|<=x-2, then a≡-x(delta+1) mod p. Since (x-1)^2<=M forces p>x(x-1), no possible positive, -1, or <=-2 delta can yield an admissible forbidden short residue. Thus a<q; the t=0 residue alone yields precisely M(p+1)/(x+1)<q<Mp/x and 1<=[x(q+1)]_p<=x-1. The converse is exact. The derived abundance bound is strict. Fresh independent proper-divisor coefficient enumeration agreed for 6,867 positive-abundance prime pairs through k=7, including 2^3*19*61 with a=56; finite tests do not prove all k.

## originality

PASS

Iannucci 2015 already developed the general semiperfectness subset-sum obstruction and a finite k<=14 census, and conjectured the one-third-scale abundance bound. A published all-prime three-quarter bound is weaker; it does not imply the conjectured bound in this square-root strip or the exact one-residue iff criterion. A genuinely new short-gap two-residue exclusion is required. Unknown historically equivalent formulations remain possible.

## value

PASS

The square-root prime strip is a natural uniform arithmetic regime where the general long subset-sum test collapses to a single congruence and two sharp interval bounds; the result proves the stronger conjectured abundance bound on this entire (unbounded-k) regime. It does not assume infinitely many prime pairs in the strip.

The dated certificate retains the supplied scientific assessment, sources and limitations.
