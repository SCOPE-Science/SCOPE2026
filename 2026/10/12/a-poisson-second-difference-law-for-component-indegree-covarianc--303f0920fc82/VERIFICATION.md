---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For uniform independent images T:[n]->[n], the components equal the count of directed cycles. Conditioning on each prescribed length-k cycle, k vertices receive one cycle edge and the other n-k outgoing images stay i.i.d.; this yields conditional PGF n(1+k(z-1)/n)(1+(z-1)/n)^(n-k), and the exact finite Q_n sum in RESULT.md. Expanding 1+kw/n-(1+w/n)^k=-C(k,2)w^2/n^2+O(k^3/n^3) and bounding a_{n,k}<exp[-k(k-1)/(2n)] gives uniform compact convergence Q_n->-(1/2)(z-1)^2exp(z-1). Cauchy coefficient extraction yields e^-1(-r^2+3r-1)/(2r!), positive only r=1,2 for fixed r. Separately enumerated ALL n^n self maps for n=2,3,4,5 using undirected component union-find and indegree counts; exact rational coefficients match the derived finite formula; Q(1)=Q'(1)=0.

## originality

PASS

Compared exact joint covariance polynomial and fixed-r limiting coefficient signs with full Hansen–Jaworski 2006/2008 paper and general random-mapping marginal enumeration. Their component-count distributions and conditioned indegree marginal methods are broader machinery, but inspected theorems do not state the entire component–indegree covariance profile or its Poisson second-difference limit. A previously known indegree-zero special case is not counted separately as novel. Flajolet–Odlyzko general framework may implicitly yield the result; its full text was not available and is residual risk.

## value

PASS

Full degree-generating covariance simultaneously resolves the sign and magnitude for every fixed in-degree class, beyond isolated component moments; useful structural dependence statistic in random functional digraphs. Analytic asymptotic proof, not finite census, establishes infinite claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
