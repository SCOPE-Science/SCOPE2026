# Self-review

## Correctness
PASS. The proof reconstructs the stochastic model from competing exponential hazards and uses exact moments. The first-failure time and failure label factorize, the surviving component's residual lifetime is independent by lack of memory, and the covariance/variance formulas follow directly. Rewriting the rate ratio through \(s=r+r^{-1}\ge2\) proves the sharp extrema without numerical optimization. The equal-rate Pearson formula exactly reproduces Proposition 4.2 of Li and Li.

## Originality
PASS. The closest source, Li and Li (2026), proves heterogeneous exponential TP2, computes Pearson correlation only for equal component rates, and separately prints a heterogeneous Kendall formula. The present Pearson formula covers all positive rate pairs. The source's Kendall formula also makes its prose claim of a minimum at equal rates algebraically impossible; the correct extremum is a unique maximum. Bassan and Spizzichino (1999) was read in full and treats the common-rate Ross model and dependence orderings, not this heterogeneous Pearson result. Focused database searches did not reveal a covering statement.

Residual risk: specialized or nonindexed reliability literature may contain an equivalent moment calculation under different notation.

## Value
PASS. The result directly completes a dependence quantity that the recent source computes only in its symmetric specialization, supplies the sharp heterogeneous range and equality case, and corrects the direction of the source's Kendall interpretation. It also separates a rate-sum invariant covariance from heterogeneity-driven marginal variance inflation, which explains why dependence weakens as component rates separate.

## Closest literature and limitations
The primary comparison is Li and Li, DOI 10.1017/S0269964825100168. The historical comparison is Bassan and Spizzichino, DOI 10.1239/aap/1029955261. The theorem is restricted to two exponential components with a common decelerating factor; it does not extend automatically to general baselines, unequal deceleration, more components, or all concordance measures.

Self-review: passed. Independent audit: not yet performed.
