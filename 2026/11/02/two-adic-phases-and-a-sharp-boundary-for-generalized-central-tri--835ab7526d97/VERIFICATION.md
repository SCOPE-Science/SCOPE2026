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

Expand T_n(b,c)=sum_k binom(n,2k)binom(2k,k)b^(n-2k)c^k. For C=v2(c)>=2B=2v2(b), normalization by b^n yields odd 2-adic unit because every central binomial factor for k>=1 is even, giving nB. For C<=2B-2, write n=2m+e and reverse index j=m-k. Divide by D=(2m+1)^e binom(2m,m)b^e c^m; the j-th normalized term is ((m)_j)^2(b^2/c)^j/(2j+e)!. Legendre gives valuation >=j(2B-C-2)+s2(j)>=1, so D is the unique odd-leading normalized term and v2(T_n)=mC+eB+s2(m). For j>=2 the falling factorial has an even factor and the term vanishes modulo four; j=1 yields m²b²/(2c) modulo four for both parity cases. At critical C=2B-1, T2=2^(2B)(u²+v), odd v can force any additional valuation r>=1 or zero; no (n,B,C)-only formula. For coprime b,c the even-b phase yields the binomial histogram across dyadic blocks and odd b gives all odd coefficients. Independently computed 2400 direct multinomial sample indices and checked these valuations/unit cases; full domain follows from symbolic term bounds.

## originality

PASS

Published primary results on the same subject and Resultary related findings were compared at the level of claimed mathematical implication; strongest already-covered components are credited and excluded from the novelty claim. The remaining specific classification appears new in actually inspected material, subject to listed source-access and indexing risks.

## value

PASS

The natural two-parameter generalized trinomial diagonal gains a complete noncritical 2-adic valuation phase diagram, a first normalized-unit correction and an explicit sharp obstruction at the remaining valuation boundary. The exact primitive-coefficient frequency census adds arithmetic information beyond classical parity, while explicitly excluding Legendre-polynomial subclasses already covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
