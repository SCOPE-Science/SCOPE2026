---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For n>=3, q>=0 set N=2^n,H=2^(n+q). Inclusion-exclusion gives 120[S(N+H,5)-S(N,5)] = 5^N(5^H-1)+10*3^N(3^H-1)-10*2^N(2^H-1)-5*4^N(4^H-1). Lifting-the-exponent makes four term valuations n+q+2,n+q+3,N+1,2N. When q<N-n-1 or q>N-n-1 the uniquely smallest term gives respectively n+q-1 or N-2 after dividing by 120. At the unique tie q=N-n-1, normalized 5^(2^s) congruence (5^(2^s)-1)/2^(s+2)=3 mod 4 gives four residues 3,2,1,0 modulo four, hence one extra factor and N-1. D is strictly positive because m is larger and S(m,5) increases for m>=5. Independent modular exponentiation and small direct Stirling recurrence checks corroborated transition and high-shift plateau without assuming the printed formula; analytical valuation comparisons cover unbounded n,q.

## originality

PASS

Theorem 1.3 in Zhao–Hong–Zhao (2012 preprint, 2014 journal) prints an unrestricted formula n+v2(a-b)-1 at k=5. Specializing to a=1+2^q,b=1 yields a contradiction for (n,q)=(4,12): published printed expression gives 15 but exact valuation is 14. The submitted statement does not rediscover that expression; it gives the sharp range of validity, a one-value resonance spike, and full uniform plateau. The later Zhao et al. paper treats other regimes/columns; no dominating three-case fifth-column result was found. Possible errata or unindexed corrections are explicitly retained.

## value

PASS

A concrete universal quantifier defect in a published Stirling valuation formula has a natural mathematical repair: the exact fifth-column law uniformly in the shift exponent, including its linear regime, exceptional cancellation and plateau. This complete two-parameter arithmetic classification is more valuable than merely exhibiting one counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
