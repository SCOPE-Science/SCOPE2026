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

For each fixed symbol order, the centered row-pair weights y_ab=w_ab−n/2 are skew-symmetric with row sums zero: across columns, each rank of the first row appears once. Writing T=Σ_{a≠b} y_ab², the row-order mean is n(n−1)/2. For n≥3 the sum of y_ab y_bc over distinct triples is T, because the unrestricted product sums vanish and the omitted a=c terms sum to −T. Disjoint row edges have zero covariance by reversal, giving conditional variance (n+1)T/[n(n−1)]. For a relative derangement with h two-cycles there are h opposite edge pairs with covariance −1/4 and n−2h directed two-step pairs with covariance −1/12; disjoint comparison edges are independent. Thus the symbol-averaged squared weight is (n−2h)/12 and the sum of h over ordered row pairs is 2I(L). The conditional mean is constant, giving the stated formula. At n=2 every comparison count is one and the variance is zero. Equality at general n forces all relative row permutations to be involutions; after making one row the identity, the rows are commuting involutions generating a faithful transitive abelian group, hence a regular elementary abelian 2-group. Conversely its table has all relative derangements made of two-cycles. Column permutations leave the score invariant and each isotopic square has the same number of preimages by the stabilizer formula. A fresh bounded direct enumeration, summing the score and its square over every row/symbol relabelling pair with exact integer arithmetic, gave (I,mean,variance)=(1,1,0),(0,3,1),(4,6,10/9) for cyclic orders 2,3,4 and (12,6,0) for the elementary abelian order-four table. This corroborates the symbolic proof; the broader frozen verification runs were not independently replayed.

## originality

PASS

The supported distinct claim is the arbitrary-fixed-square second moment under independent uniform row and symbol action and its collapse to the single statistic I(L). The ascent statistic, symbol-comparison representation and cyclic row-order special problem are prior. Neither the mean alone nor the extremal-intercalate classification alone is credited as a new result.

## value

PASS

This quantifies how the natural ascent statistic varies within a fixed isotopy orbit, making a statistic of all randomized adjacent-row comparisons exactly recoverable from a local subsquare count. The collapse is specific and informative: for example, at order four the cyclic and elementary-abelian tables have different variances, the latter zero. The contribution is the general identity, not exhaustive small cases or an already known extremal classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
