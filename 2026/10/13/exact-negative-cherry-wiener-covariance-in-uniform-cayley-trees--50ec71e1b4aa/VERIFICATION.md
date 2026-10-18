---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

A prescribed pair of leaves adjacent to a chosen center corresponds bijectively to any Cayley tree on r=n−2 remaining labels, with probability r^{r−2}/n^{n−2}; the conditional reduced tree is uniform. Exactly W_n=W_r+2Σ_x d(c,x)+2r+2; exchangeability gives EΣ_xd=2μ_r/r. Count all n binom(n−1,2) cherry indicators to derive mixed moment. The path between two labeled vertices has tail Pr(D_m≥k)=∏_{j=2}^k(1−j/m), from fixed-path forest-extension Laplacian, so μ_m exact. Q_n=2(n−1)−3d_{n−2}−binom(n,2)(d_n−d_{n−2}). For n≥627, K=floor(sqrt(n−2))≥25 and telescoping products give d_n−d_{n−2}>(4/n), forcing Q_n<−3d_{n−2}<0. Independent Fraction arithmetic checked every 4≤n≤626, while independent BFS over ALL 18,247 Prüfer-labelled trees for n=3..7 reproduced the covariance (n4 −9/16, n5 −696/625, n6 −440/243). Gaussian-product/Riemann sums give Δ_n∼√(π/2)/√n and EC_n∼e^−2 n/2, hence stated asymptotic. Certificates finite only for explicitly complete 4..626 interval; analytic tail handles infinitely many.

## originality

PASS

Best-of-knowledge novelty assessment compares identical mathematical statements and implications, not titles or a lack of search hits. Neither a cherry marginal nor Janson’s Wiener–internal-path joint moments determines their exact covariance. Comparison risks remain explicitly recorded; noncoverage is not asserted from abstracts of unread whole papers.

## value

PASS

Relates a canonical local symmetry-bearing motif (pair of sibling leaves) to a canonical global metric index on all uniform labelled trees, with exact finite covariance, strict universal sign and nontrivial n^{5/2} asymptotic constant. The cross-statistic dependence is not determined by either separately-known marginal; meaningful structural probability theorem, not a routine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
