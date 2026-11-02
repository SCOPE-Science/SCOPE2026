# Self-review

## Correctness (PASS)

The setting is finite and completely specified: positive stationary law, stochastic baseline, conditional-expectation Gibbs kernel and weighted Hilbert-space adjoints. The proof carefully separates normality of the baseline from that of the compression. The singular-value compression bound is valid for any orthogonal projection; noncommutative Schatten Hölder controls powers of a nonnormal compression. Squared singular-value losses sum to the exact projection residual, and convexity gives the sharp dimension factor. The time-two defect is an exact trace/commutator identity; the normal case follows from the spectral theorem. Ergodicity of the normal baseline implies a strict operator contraction on mean-zero functions, proving ergodicity of the compressed chain. Sharpness is an explicit lazy-refresh chain and one-cell partition, not extrapolated from finite testing. The standalone checker passed 5,602 exact-rational assertions, including normal nonreversible examples and nonnormal second-step checks. Finite tests do not prove the infinite quantification across sizes/times.

## Originality (PASS, provisional)

The nearest full primary text, Choi–Wang (2026), §4 Theorem 4.1 and Corollaries 4.2–4.4, proves the all-time comparison when the baseline is reversible and treats both centered operators as self-adjoint. No normal nonreversible all-time result or explicit all-time normality-defect gap is stated there. The 2025 Choi–Wang group-averaging paper and Choi–Hird–Wang projection article concern related but different averaged-kernel comparisons. Related records on binary conditional-expectation chains and reversible autocovariances are not implication-wise covering; the former concerns \(L^p\) time-reversal of chains of projections, not Gibbs compression of a normal baseline. An existing finite three-state nilpotent nonnormal example has distinct assumptions and cannot cover a theorem for normal baselines; the latter family cannot have nonzero nilpotent centered operators. Standard Schatten Hölder and singular-value compression are credited; the substantive combination is the quantitative sharp Markov comparison and its commutator defect. A historical matrix-inequality or unindexed sampling literature corollary remains possible, and priority is not independently certified.

## Mathematical value (PASS)

Gibbs block averaging is a natural practical operation for simplifying transition kernels. The result extends a recent reversible-only finite-time guarantee to genuinely directed normal chains without any commutation requirement on the partition, and shows why simply inheriting normality of the averaged chain is invalid. It does more than relabel a hypothesis: a new quantitative deficit bridges arbitrary and normal baselines; its time-two obstruction is a computable commutator, while its dimension coefficient is globally best possible. It provides both a strict all-time guarantee and a sufficient near-normal condition, though only for squared weighted Frobenius error and transition counts.

## Closest literature and risks

* Choi–Wang (2026), arXiv:2610.39239v1, full public HTML §4: reversible-only singular-power theorem and strictness; directly compared.
* Choi–Wang (2025), arXiv:2509.02996, full public HTML §§3–5: related group averaging and other mixing metrics; no identified domination.
* Choi–Hird–Wang (2025), doi:10.1002/rsa.70016, full public text §§2–3: permutation-based projection construction, not the present theorem.
* Recent two-block and spectral-partition papers were available mainly through abstracts; broader literature and textbook-derived priority remain risks. These sources are not asserted wholly noncovering when their full material was inaccessible.

Self-review: passed. Independent audit: not yet performed.
