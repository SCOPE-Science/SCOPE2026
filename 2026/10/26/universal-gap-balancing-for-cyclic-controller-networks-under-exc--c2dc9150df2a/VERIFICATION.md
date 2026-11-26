---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Exchangeability conditional on r gives the uniform r-subset law. For an undeleted noncontroller in the interior of a gap, both disjoint paths to its neighboring controllers must be blocked for it to be unserved; inclusion–exclusion gives the four stated binomials. Independently, count a maximal unserved surviving run of length ell by its two deleted end vertices, ell surviving interior vertices and r-2 unrestricted deletions outside: for a gap d there are d-ell positions, so F(d)=sum_{ell=1}^{d-1}(d-ell)*ell*binom(n-ell-2,r-2). This directly gives the asserted second difference and agrees with F=0 for r=0,1. It also yields the two-deletion specialization. A transfer from a to b with a>=b+2 sums the second differences at d=b+1,...,a-1. These d are <=n-k, so the second differences are strictly positive for 2<=r<k, or for r=2 regardless of k. Convexity survives nonnegative mixing and strictness survives positive mass at r=2. Under independent deletion, the vertex and disjoint blocking paths factor, and mixing the binomial second differences gives d*p^2*(1-p)^d. Cases k=n and r=n have the asserted counts. Independently enumerated component checks through n=5 agreed, with 227 placement/formula comparisons and 1,040 placement–failure pairs across 47 parameter cases.

## originality

PASS

The supported distinct claim is the exact separable fixed-cardinality outage law and its all-cardinality convexity, yielding one balanced placement optimal for every exogenous exchangeable deletion law. The shared component-protection payoff and a strategic two-controller antipodal observation are not credited as new. The closest examined indexed results involve loss of source status on a cycle that remains intact; even their multigap conditions optimize a different quantity. The general controller game does not supply this conditional law or the transfer inequality.

## value

PASS

For a natural component-survival objective the result gives exact finite-n expected losses even with correlated failures, and a common optimizer without needing the cardinality distribution. The explicit loss kernel, convexity coefficient and strictness distinguish genuine robustness of the placement from an intuition about separation; they are useful even when individual scenario distributions differ substantially.

The dated certificate retains the supplied scientific assessment, sources and limitations.
