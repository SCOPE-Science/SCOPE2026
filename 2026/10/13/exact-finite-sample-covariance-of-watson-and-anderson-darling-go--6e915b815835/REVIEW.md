# Scientific review

## Correctness — PASS

The transformed empirical process has the exact canonical kernel representation. The Watson kernel has the constant diagonal \(1/12\), so mixed covariances retain only matched off-diagonal unordered pairs; the exact cross-kernel integral is \(1/72\). Those statements yield \((n-1)/(36n)\) for all sample sizes. The Watson variance uses an exact \(1/720\) pair-kernel integral, and the Anderson–Darling variance uses explicit beta-logarithm and triangular bridge integrals. The independent coefficient checker and directly computed sorted-sample simulations support, but do not replace, these proofs. The one-observation correlation is correctly left undefined.

## Originality — PASS, with residual risk

Stephens (1974) analyzes component decompositions, marginal moments and asymptotic power, not this finite-sample cross-covariance; Hwang–Kuriki (2024) derive distinct generalized processes and marginal spectra, not the mixed statistic. A 2010 composite-null paper is not directly covering. Even exact covariances pairing each statistic with Cramér–von Mises would not determine their mutual covariance: it is an independent off-diagonal entry of the joint covariance matrix. Search results and source reading identified no equivalent mixed-moment formula. Durbin–Knott (1972) remains a material but not decisive access risk because its full original report could not be inspected here; unindexed older finite-statistic calculations could also overlap.

## Value — PASS

Watson and Anderson–Darling are standard, scientifically distinct integral diagnostics: mean-centering removes an empirical location-on-the-circle mode, while inverse binomial-variance weighting emphasizes tail departures. Exact finite-null dependence matters when both diagnostics are read jointly. The theorem gives more than separately known marginal moments: a positive dependence at all nondegenerate sample sizes, an explicit strict monotonicity law, and a nonzero limiting correlation. The proof identifies the nontrivial mechanism—complete cancellation of a diagonal mixed contribution—without asserting an unproved combined-test threshold.

## Limitations

A known continuous null is essential; estimated nuisance parameters, two-sample tests, joint tail probabilities, and historical uniqueness are not established. The inaccessible Durbin–Knott article and potentially unindexed historical derivations are acknowledged rather than treated as negative novelty evidence.

Self-review: passed. Independent audit: not yet performed.
