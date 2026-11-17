---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: Exact hypergeometric indicator decomposition yields P=n*C(n²-n,k-1)/C(n²,k) and J=[C((n-1)²,k-1)+(n-1)² C((n-1)²,k-2)]/C(n²,k), then Cov=n²(J-P²). Factorial cancellation gives the stated product for J/P². Uniform expansion at k=cn with c bounded positive yields log(J/P²)=-(c-2)²/(2n²)+a(c)/n³+O(n^-4) where a(2)=2/3. Thus Cov→-c²(c-2)² exp(-2c)/2; in k=2n+x sqrt n+o(sqrt n), nCov→e^-4(8/3-2x²), with boundary signs deliberately unspecified. Independently computed exact binomial moments for n=10,30,100,200 at k=2n; nCov≈0.0561333,0.0513003,0.0495763,0.0492085 approaching 8 e^-4/3≈0.048841.

## originality

PASS

PASS best-of-knowledge: McKay–Skerman arXiv:1302.2446 treats general bipartite degree sequences with an acceptability hypothesis whose density condition fails for k=Theta(n). Their theorem does not determine the signed degree-one cross-part covariance or its fine critical-window correction. Prior Resultary exact covariance results count isolated (degree-zero) vertices, a different indicator with negative covariance, not the present degree-one sign reversal. Palka 1984 paper is a plausible historical source but only bibliographic material was accessible; Oxford authenticated source attempt returned vpn_disconnected, explicitly retained as priority risk rather than automatic O failure.

## value

PASS

PASS: This exact natural joint degree-count statistic of fixed-edge bipartite graphs has a surprising sign reversal in a sharply specified sqrt(n) window around mean degree 2, invisible in the ordinary fixed-c limit. It resolves a meaningful dependence threshold distinct from marginal degree distributions or isolated-vertex covariances and gives a directly reusable asymptotic quantitative fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
