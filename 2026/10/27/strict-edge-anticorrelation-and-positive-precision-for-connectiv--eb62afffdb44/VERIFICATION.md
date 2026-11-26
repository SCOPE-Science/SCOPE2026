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

In odds t=p/(1−p), impose nonempty columns and apply partition Möbius inversion to the three left vertices. The column sums divided by t are f=x²+x+1, g=x+2 and h=3 for the three partition types, x=1+t. Marking one or two edges yields the stated E and three C values: in the disjoint case the three two-block partitions contribute x²+2x=xg, while for the same-left pair their contribution is 1+2x². To check the decisive factorization, expand P C_dis−E² in powers of F=f^k, G=g^k, H=h^k with k=n−2. The F², H² and GH coefficients vanish, and those of FG, FH and G² are −t²xg(2x+1), 2t²(2x+1)² and −t²g². With u=h/g and v=g/f, 0<v<u<1 follows from 3f−g²=t(2x+1). At k=0 the bracket has value −2t²(x+1). For k≥1, geometric summation and B(1−u)>C(1−v) keep it below that same negative bound. C_row=C_dis−t²g^k, and the two Bernoulli lower bounds at f/g and h/g give C_col≤C_row for k≥1. For n=2 the separate column numerator is −2t⁴(x+1). Full and single-edge-deleted graphs all have positive conditional probability because every edge lies on a 4-cycle; comparing their indicator vectors excludes any nonzero zero-variance linear combination. The inverse is entrywise positive by the convergent nonnegative-matrix geometric series, whose terms of orders zero and one already give strict positivity on and off the diagonal respectively. Consequently the linear partial correlations have the stated sign. Independent bit-set connectivity enumeration at p=1/4 for n=2,3,4 confirms all nine covariance signs, e.g. unnormalized n=2 differences (−378,−1521,−378); replay with node /workspace/review-evidence/bounded-checks.js. The analytic inequalities, not these checks, cover real p and unbounded n.

## originality

PASS

Pass is for the common-odds all-parameter family, not for the unit-odds case or for a new principle about inverses. Cao–Fu Theorem 1.2 is exact coverage at p=1/2, even for arbitrary complete bipartite dimensions, and Erickson supplies the n=3 Rayleigh comparison. The date shared with Cao–Fu does not establish priority in either direction. The direct comparison of their proof, the cographic result and the broader weighted complete-graph work did not yield coverage of K_{3,n}, n≥4, at arbitrary common non-unit odds. That weighted extension is substantive and survives discounting the known slices; positive precision is a consequence of the strict covariance sign and full support dimension here.

## value

PASS

The weighted reliability dependence question is natural for all retention probabilities, not just uniform subgraph sampling. Exact signs on a genuine infinite bipartite family give a test case for more general dependence theory, and the result predicts signs of linear relationships even after regressing on every other indicator. The latter is a useful consequence, not a second independent novelty claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
