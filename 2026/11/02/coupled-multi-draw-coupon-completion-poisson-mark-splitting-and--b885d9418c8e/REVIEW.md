# Self-review

## Correctness: PASS

The all-offered and one-choice processes share a single sequence of uniformly sampled fixed-size groups. The unselected total is a pure-death chain with exact death probability \(1-\binom{n-u}{d}/\binom nd\); its geometric holding-time decomposition and central-window exponential approximation yield the required Poisson factorial moments. Conditioning on a specified never-offered subset produces an exact tagged formula, and inclusion-exclusion identifies the two independent Poisson marks. A sparse-event continuous-time coupling proves the joint completion law and the exact finishing-round tie limit. The package verifier independently represents labeled states and aggregated count states and reproduces 1,351 exact/numerical assertions. Finite checks are not substituted for the limit proof; fixed \(d\) and fixed critical-window arguments are essential.

## Originality: PASS (qualified)

The closest primary work, Doumas–Spektor (arXiv:2607.01463), gives each policy's marginal Gumbel limit and expectation, **not** their dependence under identical offered groups. Neither its shift by \(C_d\) nor a difference of independent marginal Gumbels implies the paired law: the two completion times share unoffered extreme coupons. Xu–Tang derives one-choice mean behavior, and grouped coupon limit literature concerns offered sets rather than the two-policy coupling. Targeted mathematical-record searches and accessible earlier claims did not disclose the independent two-mark splitting, the joint CDF or its logistic delay and exact-tie limit. Residual historical-priority risk remains for unindexed marked-coupon processes and inaccessible complete older source text; novelty is not independently certified.

## Mathematical value: PASS

Two natural policies use precisely the same groups and have marginal Gumbels differing by a constant. Their **joint** law determines the likely extra time actually incurred in the same experiment, including a nonzero probability of finishing together despite the more restrictive one-choice rule. The exact tie probability \(e^{-dC_d}\) and continuous positive-delay law expose concrete dependence information inaccessible from the known separate marginals. This is a motivated comparative question, not a substitution into the marginal formulas.

## Closest sources and limits

The primary source is Doumas and Spektor, arXiv:2607.01463, first posted July 1, 2026. Additional comparisons include Xu–Tang (2011), Mahmoud–Smythe on generalized coupon-type counts, and Schilling–Henze and Betken–Thäle on group-draw Poisson limits. Theorem assumptions require fixed offered group size, independent rounds, uniform subsets and the specified least-collected selection rule; no growing-group rate or independent priority confirmation is claimed.

Self-review: passed. Independent audit: not yet performed.
