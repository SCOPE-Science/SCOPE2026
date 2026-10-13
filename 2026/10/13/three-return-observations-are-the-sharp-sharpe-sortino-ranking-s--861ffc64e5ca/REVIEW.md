# Self-review

## Correctness
**PASS.** A two-observation admissible sample must be \((-a,b)\) with \(b>a>0\). Sharpe equals \((b/a-1)/(b/a+1)\) and lower-partial-moment Sortino equals \((b/a-1)/\sqrt2\), so both rankings are strictly increasing in the same scalar and cannot reverse. The exact three-observation witness has common mean \(3\), Sharpe squares \(27/56<27/38\), and Sortino squares \(27>27/4\). Padding by the common mean preserves the ordering for every larger sample size. The packaged exact-rational verifier returns `VERIFY_OK`.

Risk: the proof is tied to equally weighted observations and a common target; changing those assumptions changes the finite-domain question.

## Originality
**PASS.** Prior literature already establishes the concepts and, more strongly, that Sharpe and Sortino can produce opposite rankings outside distributional regimes where they are monotone transforms. That existence claim is not new. The accepted claim is the sharp empirical-support boundary: two observations force agreement, three suffice, with an exact equal-mean witness and a persistent padding family. Searches by metric names, opposite-ranking language, support-size language, three-outcome language, and the exact witness did not locate this boundary.

Risk: the boundary follows from elementary algebra once the two formulas are juxtaposed, so an unindexed exercise, code test, or practitioner example could contain an equivalent three-observation construction.

## Value
**PASS.** Sharpe and Sortino are standard competing portfolio-performance summaries whose key distinction is whether upside variability is penalized. The smallest empirical support on which that modeling choice can change a portfolio ranking is therefore a natural interpretive boundary. The equal-mean witness isolates the mechanism cleanly: a smaller loss improves Sortino while a more dispersed upside worsens Sharpe. Robustness to common downside-denominator conventions and persistence at every larger sample size make the result more than an isolated numerical example.

Self-review: passed. Independent audit: not yet performed.
