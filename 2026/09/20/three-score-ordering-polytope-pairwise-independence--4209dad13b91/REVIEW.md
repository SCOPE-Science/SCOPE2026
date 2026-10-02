# Independent audit review — 2026-10-01

## Final claim

For three pairwise-independent real observations with one common atomless marginal law, the six labeled strict-order probabilities are exactly \((a,b,c,b,c,a)\) with \(0\le a,b,c\le1/4\) and \(a+b+c=1/2\), every such point is attainable, and the resulting maximum-rank and two-calibration-score rank envelopes are sharp.

## Correctness — PASS

Conditioning on one coordinate leaves each of the other two with the common marginal by pairwise independence; conditional Fréchet bounds integrate to \(1/4\le q_i\le1/2\). Pairwise comparison probabilities and total mass force reversal symmetry. The torus construction \((U,V,(U+V)\bmod1)\) realizes a vertex with exact pairwise-product marginals; coordinate permutations give all three vertices, and mixing them preserves the identical pairwise-product marginals, so the full triangle is attained. The inspected rational-arithmetic artifact is consistent with these identities but is not needed for the proof.

## Originality — PASS

The closest inspected primary literature treats symmetric order statistics—distributions of the sorted values and their joint reliability functions—under \(k\)-independence. The 2025 full text frames its optimization entirely through \(X_{j:n}\) and count vectors and does not encode which named observation occupies each rank. Published SCOPE searches found related pairwise-independence extremal problems but no theorem that implies this complete six-pattern labeled-order polytope.

## Value — PASS

The complete labeled-rank identification region is a natural finite extremal problem under a standard limited-independence assumption, and its exact conformal/rank calibration consequence quantifies a concrete inferential failure mode. It is not merely a recomputation of sorted-order-statistic bounds.

## Source inspections

- **Tight Bounds for Joint Distribution Functions of Order Statistics Under k-Independence** (https://doi.org/10.3390/e27121250): NOT_COVERING_LABEL_SENSITIVE_CLAIM. The paper optimizes symmetric functions of sorted order statistics; it does not state the six probabilities for named labels occupying ranks.
- **Bounding Moments of an Order Statistic When Each K-Tuple is Independent** (DOI 10.1007/978-94-011-5532-8_34): INACCESSIBLE_PLAUSIBLE_SOURCE. The available description concerns moments/distributions of order statistics, not labeled permutation patterns; full theorem text remains a terminology risk.

## Residual risks

- Kemperman (1997), Okolewski (2017), or older copula/order-pattern literature could contain an equivalent label-sensitive formulation under different terminology; their unavailable portions were not treated as proof of noncoverage.
