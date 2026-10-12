# Self-review

## Correctness
**PASS.** For an \(n\)-point equal-weight empirical loss law, the integrated quantile contains fewer than two tail masses exactly when \(n(1-\alpha)<2\). If it contains less than one mass, VaR and Expected Shortfall both equal the maximum. If it contains between one and two masses, Expected Shortfall is a strictly increasing affine function of the second-largest loss when the maximum is fixed, so reversal is impossible. At the first integer with at least two tail masses, the displayed equal-mean, equal-maximum vectors give the exact opposite ranking. The standalone verifier returns `VERIFY_OK`.

Risk: the integer boundary is quantile-convention sensitive; the claim therefore fixes the generalized-inverse convention explicitly.

## Originality
**PASS.** Acerbi and Tasche supply the generalized-inverse formulas, empirical-order-statistic interpretation, and the qualitative reason VaR and Expected Shortfall differ. Those definitions do not themselves state the constrained ordering theorem with equal mean and equal maximum loss. Targeted published-result and scholarly searches did not locate the sharp threshold \(\lceil2/(1-\alpha)\rceil\), the \(40\)-scenario and \(80\)-scenario benchmarks, or the matched witness.

Risk: the theorem is an elementary but nontrivial extremal consequence of classical definitions; an unindexed note or implementation test may contain an equivalent observation. Search failure is not a proof of historical uniqueness.

## Value
**PASS.** VaR and Expected Shortfall are canonical competing tail-risk summaries. Matching both expected loss and worst-case loss removes two obvious reasons for their rankings to differ. The theorem identifies exactly how much empirical tail resolution is still required before the measures can disagree, giving the concrete thresholds \(40\) scenarios at \(95\%\) confidence and \(80\) at \(97.5\%\). This isolates a practically interpretable order-statistic mechanism rather than a generic VaR-versus-ES counterexample.

Self-review: passed. Independent audit: not yet performed.
