# Self-review

## Correctness — PASS

The exact stationary generator establishes the two needed moments and the zero mean. The two-time covariance conditions on the absence of any reset and integrates to the Green–Kubo coefficient; the independent complete-cycle regenerative reward calculation matches that coefficient symbolically. The extrema theorem follows from two exact derivative factorizations and a Descartes sign-count argument, not from numerical root plots. The reset variance is finite and positive, all rate parameters are strictly positive, and the zero-reset limit is treated separately. A standalone symbolic/rational/high-precision checker was run successfully. Numerical calculations do not establish novelty, and the proof does not claim properties for finite observation durations.

## Originality — PASS (self-review, residual priority risk)

The motivating paper arXiv:2310.04840v1 covers the same model and its single-time moments, notably stationary variance/kurtosis. Its Eqs. (36)–(44) and discussed figure concern moment dependence on resetting laws, not the Green–Kubo integral of temporal covariance or the two-extremum time-average variance classification. arXiv:2306.09453v1 studies a harmonic active particle driven by *resetting noise* while retaining the continuous particle position; this does not imply the theorem for resets of both position and sign. Published research and semantic record searches did not identify an equivalent sharp phase threshold or implication from stronger coverage. Search failure alone is not a proof of priority; a previously unlocated semigroup/renewal specialization remains possible. The one-time moment identities and renewal tools are acknowledged prior ingredients, and independent priority evaluation is outstanding.

## Scientific value — PASS

The Green–Kubo coefficient controls the leading uncertainty of empirical time averages in active-matter measurement. Its resetting-rate optimum need not follow the one-time stationary-variance optimum. A complete, sharp two-extremum/no-two-extremum phase classification and an exact rational example in which uncertainty crosses its no-reset baseline provide a motivated dynamical reliability boundary, not an arbitrary narrow invariant. The result supplies a reproducible stationary-noise benchmark for active transport subject to intervention.

## Closest literature and limits

Olsen (2023), arXiv:2310.04840v1 (self-review, one-time moments), and Guéneau–Majumdar–Schehr (2023), arXiv:2306.09453v1 (different reset rule), are the closest primary sources examined. The claim uses noninteracting, harmonic, independent-Poisson, full-reset dynamics; no general interacting-particle or finite-time claim follows.

Self-review: passed. Independent audit: not yet performed.
