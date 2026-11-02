# Scientific review of the conditional leaf--distance theorem

## Correctness

**PASS.** Conditioning on the ordered marked path gives a uniform rooted forest, and the directed matrix-tree determinant proves its multivariate child-count enumerator. A uniform root draw plus independent uniform parent draws yields the exact occupancy mixture; the leaf criterion distinguishes the marked path's interior from its two endpoints. This establishes all conditional binomial moments for nonpath cases and treats the path boundary separately. Exact algebra gives the difference with numerator \(2(n-1)-\ell(\ell+1)^2\), which strictly decreases through zero, so the global maximizer and all ties follow. The distance-two/three stochastic incomparability has explicit opposed witnesses. An executable checker passes 20,000 exact assertions, including exhaustive Prüfer enumeration through eight vertices. The unbounded claims rely on the written proof, not enumeration.

## Originality

**PASS, with historical-priority risk.** Pitman's 1998 Theorem 1 already establishes the general forest child-count generating polynomial, and Section 5.7 concerns marked paths. The conditional occupancy law is acknowledged as a specialization of that established input, not an independently novel enumeration. The assessed contribution is the sharp all-distance optimization of the *total* leaf statistic: a unique cubic cutoff, its \(n^{1/3}\) scale and infinite arithmetic tie family, plus the opposed expectation/upper-tail order between distances two and three. Neither these comparisons nor the stochastic-incomparability family was located in the primary source material or in the targeted published finding searches. The closest earlier work on endpoint degree versus marked distance does not imply the behavior of total leaf count without an additional analysis of all off-path vertices and path endpoints. An overlooked exact specialization in older labeled-tree literature remains possible.

## Mathematical value

**PASS.** The number of leaves and the distance between two distinguished vertices are intrinsic statistics of the same classical model. A monotone conditional response would be plausible from endpoint-degree results; instead the response switches direction at a nontrivial cubic threshold, much smaller than the usual square-root distance scale. The exact infinitely recurring tie cases and the non-stochastic-order witness distinguish the claim from a routine single expectation calculation.

## Closest literature and limitations

- Pitman (1998), Technical Report 498, Theorem 1 and Section 5.7: exact forest enumerator and marked-path framework; these are foundational prior coverage.
- Meir and Moon (1970), *The distance between points in random trees*: the marked-distance marginal problem, not a conditional total-leaf optimization in the material available for comparison.
- Aldous (1990), *The random walk construction of uniform spanning trees and uniform labelled trees*: classical leaf and distance asymptotics; full text not available in this check.

Results are for uniform labeled trees and fixed marked vertices. No independent priority adjudication or independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
