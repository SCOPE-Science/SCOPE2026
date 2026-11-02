---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The identity Cov(T,D_r)=n*q_n(r)*(f_n(r)-mu_n) follows by conditioning on the degree of a labelled vertex. Conditional on r neighbours, the remaining n-1-r edges are uniform among the B=binom(n-1,2) nonincident pairs; triangles through the vertex contribute binom(r,2)*(n-1-r)/B and triangles avoiding it contribute binom(n-1,3)*(n-1-r)_3/(B)_3. Subtracting classical mu=binom(n,3)*(n-1)_3/(binom(n,2))_3 gives a cubic g_n(r), with q_n(r)>0 for every allowed degree. I independently recomputed the exact six pivot rational expressions at 0,1,3,4,n-3,n-2 and the coefficient certificates under n=t+14: pivots alternate +,-,-,+,+,- and each shifted positivity numerator has positive coefficients. Three disjoint real intervals each contain a root, exhausting a nonzero cubic; the signs at all integer degrees follow. At n=13 the n-2 numerator is negative, causing positive covariance. A fresh independent exact symbolic/rational checker corroborated identities and complete profiles through n=150. The arbitrary-n theorem is the polynomial root/positivity proof, not the finite loop.

## originality

PASS

Best-of-knowledge PASS for the exact triple-switch sign classification, not the underlying hypergeometric conditioning or triangle expectation. The existing G(n,m) deviation and degree-sequence papers concern different observables/invariants in material actually inspected. Full potentially relevant Goldschmidt–Griffiths–Scott text was not accessible and could theoretically contain an equivalent exact covariance; risk explicitly retained.

## value

PASS

A sharp full degree-frequency covariance phase diagram for sparse fixed-edge random graphs has mathematical content beyond the routine first-moment calculation: fixing the total edge count introduces competing edge depletion and yields three rigorously located, nonobvious sign reversals. The n=14 onset and n=13 obstruction give a natural finite threshold, potentially useful in joint subgraph-degree fluctuation analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
