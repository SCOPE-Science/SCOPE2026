# Scientific review

## Correctness — PASS

The proof constructs a joint law at every attainable conditioned run count using two nested sets of internal cuts. Even-to-odd transition weights are the exact ratios of uniform-composition counts; odd-to-even steps split the color with fewer runs. Uniform-subset insertion proves the marginals, and a single positive split proves majorization. The generating-function calculation gives the exact quadratic conditional expectations. Exhaustive independent enumeration and an exact rational transition-kernel check both passed for all \(1\le a,b\le7\). The infinite-family proof is the combinatorial argument, not the finite enumeration.

## Originality — PASS under examined sources

The closest accessible papers treat the joint run-count distribution, marginal or joint longest-run distributions, and general run-length order statistics. Kazemi–Jafari (2014) gives the fixed-content composition counts but not the ordered coupling. Wentzel-Larsen–Anhøj (2019) provides joint crossing/longest-run computations but not a simultaneous refinement for every conditioned count. Kong's accessible ordered-run article describes exact marginal formulas without this order comparison. Full texts of Lou (1996) and Kong (2006) remained inaccessible; the assessed originality is a reasoned literature comparison, not a guarantee of historical priority.

## Mathematical value — PASS

A single coupling compares all conditional run-length vectors rather than one statistic or fixed finite range. It proves simultaneously the joint monotonicity of the two color-specific longest runs, majorization for every Schur-convex dispersion measure, and sharp strict decrease of the quadratic run-concentration statistic. The latter has explicit rational calibration formulas. This directly connects the classical runs-count and longest-run diagnostics under the fixed-margin two-sample randomness null.

## Limitations

The result applies only to uniform fixed-content binary words; it does not order the positions of runs or arbitrary prefix-sensitive test statistics. Inaccessible literature leaves a residual priority risk. Computational checks cover finite parameters only.

Self-review: passed. Independent audit: not yet performed.
