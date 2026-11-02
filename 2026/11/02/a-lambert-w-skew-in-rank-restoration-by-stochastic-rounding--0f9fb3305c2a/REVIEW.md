# Scientific review

## Correctness

**PASS.** The claim is supported by (i) exact two-column inclusion–exclusion, explicitly including the all-zero-column cases; (ii) a complete classification of maximal-origin-hyperplane intersections with the Boolean cube; (iii) finite hyperplane inclusion–exclusion with a uniform exponentially smaller remainder and its first two derivatives; (iv) localization and strict convexity of the finite-width optimizer; and (v) a controlled Lambert-W inversion. The verifier performs exact rational tests on small instances. No numerical experiment is treated as a general proof.

## Originality

**PASS, with priority risk.** The closest motivating numerical-analysis source studies implicit singular-value regularization and the same two-column midpoint construction but does not determine the varying-fraction optimizer. Established square-matrix singularity results already identify zero and duplicate columns as important mechanisms; that general idea is acknowledged and not presented as new. The assessed new statement is the global fixed-width optimizer, its precise Lambert-W shift, and its nonvanishing failure-probability improvement. The accessible published-results search did not surface an implication covering this result. An older fixed-width fair-sign result is contextually relevant but its technical full text was not accessible for complete examination.

## Value

**PASS.** For stochastic-nearness rounding, midpoint input maximizes entrywise randomization, yet the exact chance of rank restoration is minimized at a non-midpoint fraction. The theorem resolves this tension for all fixed column counts and supplies a sharp rare-failure reduction, with an exact two-column finite-sample benchmark. The exact probability is a natural reliability metric when formerly identical columns are independently quantized. No claim is made about general matrix inputs, downstream conditioning, or changing rounding probabilities in a biased way.

## Limitations

The result is specific to a constant rank-one input, independent one-bit rounding and fixed column width. The asymptotic expansion does not cover growing column width. The claim is a rank-restoration probability classification, not a guarantee on the magnitude of the smallest positive singular value. Publication-priority assessment is provisional, and an independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
