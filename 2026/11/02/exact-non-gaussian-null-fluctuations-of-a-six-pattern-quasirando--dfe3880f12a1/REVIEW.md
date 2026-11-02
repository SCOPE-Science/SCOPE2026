# Review of the six-pattern null fluctuation theorem

## Correctness

**PASS.** The object is the precisely defined weighted sum of normalized three- and four-point pattern densities for a uniformly random permutation of length at least four. The first conditional projections are exact multiples of the same centered polynomial product, with opposite coefficients; the weighted combination therefore cancels pointwise. The explicitly defined canonical second kernel has squared \(L^2\) norm \(121/3600\), obtained by rational polynomial integration on the four coordinate-order chambers. Standard fixed-order Hoeffding decomposition and the canonical second-order U-statistic limit then prove the spectral limit and asymptotic variance \(121/1800\). The packaged checker reproduces the rational identities, including exhaustive sizes four through seven. A computation does not, by itself, establish the infinite-sample theorem; that step relies on the stated analytic decomposition and spectral limit.

## Originality

**PASS, subject to historical-priority risk.** The 2023 six-pattern quasirandomness paper establishes a universal extremal inequality and suggests independence testing, but the inspected text does not give the statistic's sampling null limit or its exact variance coefficient. The 2018 general random-permutation-pattern theory supplies the Hoeffding/spectral methodology but predates this combination and does not calculate its cancellation or numerical coefficient. Searches for equivalent formulations, broader implications, and exact tabulations did not identify a directly covering result. An unlocated stronger specialized result is possible and remains a risk; no uniqueness or exhaustive-literature claim is made.

## Value

**PASS.** The exact fluctuation scale, non-Gaussian character, and leading variance are directly relevant to calibration of the six-pattern independence diagnostic proposed by the source article. The derivation isolates a structural Legendre-product cancellation across pattern orders, which explains why an ordinary normal approximation at \(\sqrt n\) scale fails. The claim does not assert fully tabulated critical values or quantitative rates.

## Closest literature and remaining limitations

The closest sources are Crudele–Dukes–Noel (arXiv:2303.04776, first posted 2023-03-08), Even-Zohar (arXiv:1811.07883), and the joint-pattern asymptotics of Janson–Nakamura–Zeilberger. All identify useful context; the exact coefficient and mixed-order degenerate null law were not found therein. The eigenvalue list is implicit, and there is no independent reproduction of the full proof beyond the packaged exact algebraic checks.

Self-review: passed. Independent audit: not yet performed.
