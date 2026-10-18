# Scientific review: cubic-chirped Gaussian ambiguity moments

## Correctness — PASS

The complex Gaussian integral is legitimate for every real delay and chirp because the quadratic coefficient has positive real part. Multiplication of the two shifted Gaussian signals gives the cubic finite-difference identity, and completion of the square gives the exact nonvanishing ambiguity formula. Direct Doppler integration yields the stated positive moment integral. The Tricomi integral representation, the hyperbolic substitution for the modified Bessel function, and the two dominated-convergence cases give the exact all-exponent moment classification. The critical \(p=4\) result uses a bona fide \(K_0\) logarithmic asymptotic, not an extrapolation of the adjacent power laws.

The packaged checker independently integrates the original complex ambiguity definition at four sample points, compares 21 moment quadratures to the Tricomi expression, and verifies normalization and the critical Bessel identity. Checks passed. Limitations: these finite checks are corroborative only, and fixed \(p\) is essential in the asymptotic quantifier.

## Originality — PASS, with bounded publication-priority risk

The complete all-\(p\) moment law for this normalized Gaussian-envelope cubic chirp, and particularly the \(p=4\) transition with its explicit constants, is the compared claim. Known Gaussian-integral algebra, Moyal normalization and Lieb's universal Gaussian extremal inequality are prior contributions, not originality claims. Jung's full 2006 treatment of ambiguity \(p\)-norm inequalities does not specify a cubic-phase Gaussian moment law. Jaming's full 2006 ambiguity-zero study gives bounds for zero-free neighborhoods, not this globally zero-free family or its moment asymptotics. Wang, Wang and Li's full 2013 cubic-chirp model addresses radar parameter estimation rather than Gaussian-envelope ambiguity moments. Recorded searches found no direct equivalent result. The 1990 Lieb paper was located but its full text could not be obtained; only its abstract and Jung's faithful full-text quotation of the relevant inequality could be compared. An older optics or radar source may remain unindexed; priority has not been independently certified.

Other related mathematical results concern Haar-pulse ambiguity folds, two-Hermite Wigner nodal geometry, Gaussian-cat Wigner-negative volume, and B-spline Cauchy-transform zeros. Their objects and conclusions do not imply these cubic-chirp ambiguity moment asymptotics. Scientific comparisons and residual publication-priority risks are detailed in `AUDIT.json`.

## Mathematical value — PASS

The result determines an entire continuum of natural ambiguity-function moment invariants instead of a selected numerical sample. The change from \(c^{1-p/2}\) to the critical \((\log c)/c\) law and then to \(c^{-1}\) is an exact structural transition governed by the integrability boundary of a limiting delay profile, and yields explicit rates missing from a universal norm bound. It also distinguishes global zero-freeness from time-frequency moment concentration: every ambiguity point remains nonzero while all moments of order above two vanish in the large-chirp limit and the Moyal moment stays fixed. These effects are meaningful for ambiguity localization and Rényi-type concentration measures, without claiming an external application theorem.

## Remaining limitations

The scope excludes time-limited signals, general amplitude envelopes, higher-degree phases, arbitrary cross-ambiguities and double limits in which the exponent varies with the chirp. No independent literature-priority determination or mathematical audit is represented by this review.

Self-review: passed. Independent audit: not yet performed.
