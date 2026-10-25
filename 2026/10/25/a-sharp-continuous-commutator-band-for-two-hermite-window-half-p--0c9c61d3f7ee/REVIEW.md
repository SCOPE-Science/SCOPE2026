# Scientific review: sharp Hermite-window half-plane commutator band

## Correctness — PASS

The result is on an explicitly defined vector-valued Hilbert space, with both the STFT convention and normalized windows fixed. The proof first derives the two-window isometry by Plancherel and window orthogonality, rather than assuming an abstract matrix representation. Fiber compression is exact for the half-plane multiplier. Three elementary Gaussian antiderivatives produce an explicit real-symmetric matrix, whose commutator has the claimed universal skew matrix and Gaussian scalar profile. Multiplication-operator spectral theory proves the full essential spectral interval, multiplicity, absence of eigenvectors, absolute continuity, and noncompactness. The derivative of the scalar profile proves the unique optimal separation. The self-contained checker completed 714 finite consistency tests. Numerical checks are supporting evidence and do not establish the infinite-dimensional assertions.

## Originality — PASS (best knowledge, residual risk noted)

Jaming–Speckbacher (arXiv:1906.02964, Sections 1–2 and 4) investigates Hermite-window concentration and sampling but does not give the joint two-window half-plane commutator spectrum. Keller–Luef (arXiv:1905.07741 / JFAA 2021, Sections 5.2–5.3) establishes semiclassical compositions for smooth single Hermite windows, not the exact fixed-scale discontinuous pair. Arroyo Neri et al. (DOI:10.1155/2021/9919243, Section 3) provides a broad prior horizontal Hermite-fiber representation, which this work explicitly acknowledges. That representation does not state the optimized paired-threshold norm, its spectral band, absolute-continuity multiplicity, or norm nonattainment. Those exact quantitative conclusions require evaluating the specialized Gaussian Gram matrix and optimizing its commutator.

Semantic searches of published mathematical records found a fixed-half-line Hermite spectral-gap result and unrelated commutator bounds, but no result with this exact two-threshold statement. Remaining risk: the new theorem is a quantitatively evaluated special case of the published matrix framework, and an older source could already perform the same elementary specialization. Priority is not independently certified.

## Mathematical value — PASS

The result exactly quantifies the noncommutativity of two naturally nested time-frequency concentration measurements in the first nontrivial two-window Hermite packet. It is not just a numerical finite-matrix optimization: it classifies the complete infinite-dimensional continuous spectrum, its multiplicity, and noncompactness while giving an explicit global geometric optimum. The analytic one-window setting has scalar horizontal fibers and zero commutators; simultaneous Hermite modes introduce a universal nonzero obstruction. The sharp constant supplies a reproducible benchmark for multiwindow localization and reveals the contrast between maximizing the *operator* norm over thresholds and failure of norm attainment for any individual input signal.

## Scientific limits

The window scale is fixed, and no result is asserted for other Hermite orders, nonparallel half-planes, or arbitrary masks. The general matrix representation is prior work. The originality review is best knowledge rather than an exhaustive independent priority search.

Self-review: passed. Independent audit: not yet performed.
