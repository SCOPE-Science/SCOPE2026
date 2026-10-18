---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For n product of prime powers the bi-unitary condition removes only the middle divisor p^{a/2} for even exponent a, so F(p^a)=Σ_{j=0}^a p^{-2j}-1_{2|a}p^{-a}. Its local closure contains 1 and C_p=(1-p^-2)^-1. For primes p>=5, independently verified 10 finite rational witness products; for p>=41, fifth Ramanujan prime R5=41 gives five primes p<q<2p, forcing ∏_{q>p}C_q>C_p. Thus the binary-series interval lemma applied to log C_p fills [1,T=π²/9] by finite-support approximations. The eight independent scale factors from p=2 and3 are {1,17/16,9/8,153/128,5/4,4/3,45/32,3/2}; their maximum adjacent ratio is 16/15<T, so scaled intervals overlap and fill [1,(3/2)T]=[1,π²/6]. The universal divisor bound gives the other inclusion. Independent direct bi-unitary divisor enumeration for n<=256 and exact rational witness checks corroborated steps, but cannot replace Ramanujan or the series lemma.

## originality

PASS

Tóth 2009 studies bi-unitary Euler/gcd-sum analogues and asymptotic sums, not the reciprocal-square value-set topology. Defant explicitly treats unitary divisor sums, with different local factors 1+p^{-2a} and a disconnected reciprocal-square range. Sanna treats ordinary divisor sums, where the reciprocal-square range has three components. Neither theorem covers bi-unitary middle-divisor deletion or its extra 17/16 factor and interval bridging. Targeted Resultary and literature searches found no exact covering bi-unitary closure theorem; the possibility of an unindexed one remains.

## value

PASS

This determines a natural complete range-closure invariant at the first integer exponent beyond absolute harmonic convergence. It explains a sharp qualitative difference among ordinary, unitary and bi-unitary divisor systems at the same exponent, using the unusual exponent-two 17/16 multiplier to eliminate gaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
