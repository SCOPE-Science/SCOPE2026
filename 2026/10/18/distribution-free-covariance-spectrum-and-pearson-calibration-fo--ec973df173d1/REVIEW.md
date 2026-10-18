# Scientific review

## Correctness (C) — PASS

The claim fixes positive \(p\), arbitrary finite \(q\ge2\) and \(L\ge2\). The two-coordinate weighted Hoeffding decomposition is unique by conditional expectation; the centered pair-score sum separates into independent single-coordinate terms and orthogonal degenerate interactions, giving the exact variance identity (1). The polarization of that identity determines all four orthogonal invariant subspaces and their eigenvalues. Direct overlap counting gives equation (2). The exact Pearson mean follows by trace, and a bounded one-dependent multivariate CLT gives the specified **singular** Gaussian limit and weighted chi-square law. No finite computational checks are used to infer the infinite assertion. A standard-library verifier independently checks exact covariance entries and all modes; 1988 assertions passed. No boundary probability of zero, estimated probabilities, or growing alphabet is included.

## Originality (O) — PASS on inspected comparisons, with documented uncertainty

The 2020 full text of Karmakar–Wu concerns general dependent-series Gaussian approximation; it does not evaluate this model's nontrivial persistent boundary eigenspace or explicit Pearson limit. The 2022 full text of Carugno–Vivo–Coghi derives the finite-time moment-generating function for a much broader class of Markov pair-occupation measures. That formula **does implicitly determine** the covariance matrix after differentiation. The present statement is limited to the probability-invariant closed spectral decomposition and resulting calibration; these require additional orthogonal decomposition not stated as a formula there. The broader-generating-function relationship is acknowledged and no novelty is claimed for the mere existence of pair moments. Targeted prior-record searches returned only different overlap and categorical-occupancy results, not the four-mode spectrum. Residual risk: historical treatments of Markov flux may already make this spectral specialization; this review does not establish global priority.

## Value (V) — PASS

Overlapping bigrams are natural empirical transition statistics and not independent multinomial cells. The exact four-level spectrum cleanly isolates \(q-1\) endpoint-gradient directions with bounded variance from symmetric and interaction directions with linear variance. Because the eigenvalues are probability-invariant after Pearson weighting for any strictly positive categorical law, the theorem yields an exact universal trace and a concrete corrected large-sample null law for an ungrouped Pearson goodness-of-fit statistic. The difference between \(\chi^2_{q^2-1}\) and \(\chi^2_{(q-1)^2}+2\chi^2_{q-1}\) is substantive, not a routine numerical increment.

The cited papers are Karmakar and Wu (arXiv:2001.10164v1) and Carugno, Vivo and Coghi (arXiv:2201.00582v1). Independent historical-priority review and independent theorem audit are outstanding.

Self-review: passed. Independent audit: not yet performed.
