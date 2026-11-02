# Review: singleton success-run likelihood ratios

## Correctness

**PASS.** The one-run lengths are uniformly composed conditional on their number, because every length composition has exactly the same count of compatible zero placements. Counting unit parts gives the displayed conditional law. On each common support, the explicit ratio of adjacent rows increases strictly in the singleton count; moving support endpoints and transitivity give all TP2 minors, including boundary zeros. The Vandermonde factorial-moment calculation gives the exact positive covariance. A standalone verifier passed 2,304,064 exact finite assertions. All-parameter correctness comes from the written combinatorial identities, not an experimental extrapolation.

## Originality

**PASS with historical-priority risk.** Classical fixed-weight one-run counts (Stevens, Mood, Schuster, as recorded by Balado–Silvestre, Section 4.2, Eq. (201)) and integer-composition counts are prior foundations. The inspected 2026 broad enumeration, 2011 composition article and 2012 restricted-composition analysis did not state the conditional singleton-count likelihood-ratio chain or TP2 conclusion. Closest publicly indexed work treats adjacent run-transition correlations, run-count balancing, and maxima of compositions rather than these conditional singleton statistics. The 2004 Markov run-count paper and some earlier joint run-length literature were not fully accessible; possible implicit prior coverage is a residual risk. No priority is asserted for the binomial formulas alone.

## Mathematical value

**PASS.** The Wald–Wolfowitz fixed-content setting makes run count a standard randomization statistic, while singleton successes distinguish fragmentation into isolated events. The theorem compares their entire conditional distributions in likelihood-ratio order, rather than just an expectation or a chosen threshold. This gives an exact positive-dependence structure and a finite-sample covariance identity without an asymptotic approximation. The subject is intrinsic to run-based inference, and the inequality is uniform over all feasible sample sizes and content counts.

## Verification boundaries

The computational checker covers exactly the finite ranges described in the result; it is not a proof for unbounded parameters. The proof establishes only order two of total positivity, and only for uniform fixed-content binary words. Full historical priority is unresolved; in particular, inaccessible older multivariate run-length treatments might include an equivalent formulation.

Self-review: passed. Independent audit: not yet performed.
