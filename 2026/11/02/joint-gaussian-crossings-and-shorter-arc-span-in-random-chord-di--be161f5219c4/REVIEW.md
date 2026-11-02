# Scientific review

## Correctness — PASS

The uniform matching representation, chord-length definition and all indices agree. Exact finite-size moments follow from one- and two-edge inclusion probabilities. The crossing-count projection is an order-two iid U-statistic; the shorter-arc sum's potential empirical-rank first-order influence cancels because the shortest-arc score is symmetric under arc complementation. The resulting double-degenerate rank-correction kernel has \(O(n^2)\) second moment; its cusp error is \(o_p(n^{3/2})\). Hence a classical iid bivariate CLT supplies the nondegenerate covariance matrix. The supplied finite checker passed 13,895 exact assertions; this independently checks finite formulas but is not substituted for the limit proof.

## Originality — PASS (qualified)

Acan [arXiv:1501.01489v1] already defines the total shorter-arc length and derives conditional crossing-degree information; Paguyo [arXiv:2104.01134] recovers a **univariate** crossing-count CLT and its exact variance. Neither inspected relevant full-text section states a joint CLT for this crossing/span pair or its sharply nonzero asymptotic correlation. Prior separate findings on higher crossing-clique/span covariance and crossings/nestings joint fluctuation neither logically imply this limit nor its variance fraction; their components are not claimed new. The large classical chord-diagram literature leaves residual risk of an unlocated equivalent multivariate corollary. No independent historical-priority assessment has taken place.

## Value — PASS

The theorem identifies a natural, highly predictive geometric quantity for a global graph statistic, quantifies its asymptotic explanatory power exactly at \(15/16\), and isolates a reverse-influence cancellation needed to couple geometrical ranks with an iid chord model. The result is a nondegenerate two-dimensional limit, not a routine restatement of the crossing marginal limit or an isolated finite calculation.

Self-review: passed. Independent audit: not yet performed.
