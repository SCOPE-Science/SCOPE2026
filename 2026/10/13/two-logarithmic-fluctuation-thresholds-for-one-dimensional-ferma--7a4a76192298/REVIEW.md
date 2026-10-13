# Scientific review: Two logarithmic fluctuation thresholds for one-dimensional Fermat distances

## Correctness — PASS

The exact first and second moments follow from the Dirichlet \((1,\ldots,1)\) spacing law. Uniform gamma-ratio expansions for \(\alpha=O(\log N)\) and Stirling's formula yield the squared coefficient-of-variation crossover, including the \(\tfrac12\log\log N\) correction. The Rényi exponential-spacing representation reduces normalized distances to normalized sums of independent exponential powers. The two fixed-ratio regimes follow from second moments or explicitly truncated first and second moments. At the logarithmic boundary, two cutoffs separated by \(O(\log\log N)\), a gamma central limit theorem, and a maximal-exponential bound yield the profile \(\Phi(-s)\). The upper-tail events remain negligible in probability but can dominate second moments, explaining the apparently conflicting limits. Exact identities were separately checked in 597 finite symbolic/numeric cases by the included verifier. That finite checking is not an infinite-parameter proof. The source model requires independent uniform points on \([0,1]\); the exponent grows only in the specified regimes.

## Originality — PASS, with bibliographic uncertainty

The closest directly inspected work is Chazal, Ferraris, Groisman, Jonckheere, Pascal and Sapienza, arXiv:2311.18663, Proposition 4.1 and its appendix. It supplies Dirichlet moments and asymptotics for each **fixed** exponent, while the present conclusion requires a joint growing-exponent limit and proves the \(\sqrt{\log N}\) critical profile and the mismatch between variance and convergence-in-probability thresholds. Aly (2020), DOI 10.2174/1876527002010010001, studies weighted uniform-spacings sums under fixed power \(r>0\); its examined theorem statements do not claim the growing-power phase portrait. Searches using Fermat distance, uniform spacings, Dirichlet power sums, Rényi entropy, exponential-power sums, and their logarithmic-parameter equivalents located no covering result. No complete priority claim is warranted: older spacing literature or general triangular-array theorems may contain an equivalent formulation. The source paper's exact moments alone do not state or prove the probability-convergence crossover.

## Value — PASS

The sample-size-dependent exponent choice is the precise parameter/noise trade-off motivating the source paper. The results identify both a variance-based threshold near \((\log N+\tfrac12\log\log N)/\log4\) and a different typical-sample threshold near \(\log N\). In the intervening natural range, relative variance diverges even though the normalized statistic approaches one in probability; at the latter boundary the exact normal-CDF crossover describes how the limiting typical level collapses. This warns against using the coefficient of variation alone to predict typical distance instability, and is not an arbitrary parameter slice. It does not provide higher-dimensional, nonuniform, or quantitative-rate extensions.

## Closest literature and residual risks

- Chazal et al., arXiv:2311.18663, Section 4.1 and Appendix A: full text examined for the exact statistic, fixed-power estimates and available proofs.
- Aly, DOI 10.2174/1876527002010010001: published open-access full text consulted for the fixed-power definition and theorem statements; not a comprehensive review of all its cited older spacing papers.
- Relevant earlier uniform-spacing and exponential-power sum literature may have an equivalent triangular-array statement under different terminology. No independent priority audit has been performed.

Self-review: passed. Independent audit: not yet performed.
