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

Inclusion-exclusion k! S(n,k)=sum_{j<=k}(-1)^(k-j)binom(k,j)j^n proves uniform coefficientwise period lambda(p^a) from n>=a because nonunits vanish and units obey Carmichael. CRT gives R=max a and L=lcm lambda. For an eventual period T, triangular coefficient identities at 1<=k<=p-1 force j^T=1 mod p^a for all j=1..p-1. At odd p, they give p-1|T; at least one small representative has v_p(j^(p-1)-1)=1 via root factorization and sum j=p(p-1)/2 nonzero mod p^2, so LTE forces p^(a-1)|T. At 2^a, coefficient k=3 yields order of 3 equal lambda(2^a). At n=a-1 coefficient k=p has remaining contribution -p^(a-1) for every eventual T, blocking earlier starts; for a=1 constant term of G_0 distinguishes. Independently computed exact Stirling coefficients verified asserted lambda/R values for every modulus 2..50; finite checks do not establish arbitrary m.

## originality

PASS

All-modulus exact least *coefficientwise* index period and least preperiod is a tighter classification than known eventual periodicity or selected scalar evaluations; qualified against a very relevant inaccessible 2026 Stirling-transform source.

## value

PASS

The ordered-Bell polynomials are a classical central combinatorial family, and least eventual coefficientwise period plus least starting index are natural exact modular invariants not determined merely by existence of periodicity. The all-modulus minimality classification and explicit witnesses can be reused by modular Stirling-transform studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
