# Research review: temporal energy anticorrelation under collective renewal resetting

## Correctness — PASS

The exact conditional-Gaussian reduction gives cross-particle squared-position covariance equal to four times squared diffusion strength multiplied by stationary renewal-age covariance. The phase-age process is a piecewise-deterministic Markov process with a finite cyclic Erlang stage chain; the explicit gamma-distributed stationary conditional ages produce the stated initial moments. The finite linear generator gives all four positive-shape closed forms, and the nonzero residue of the dominant complex eigenpair rigorously forces infinitely many negative and positive lag intervals at all integer shapes at least five. The boundary case four retains a dominant strictly positive nonoscillatory mode. The independent direct-renewal sampling and 124 comparisons are supporting tests, not proofs of the infinite-lag assertion.

## Originality — PASS, with residual risk

De Mauro et al., arXiv:2509.06658v1 (2025), provide the common renewal reset model and same-time Brownian-gas correlations, not a stationary, unequal-time covariance of the squared positions of distinct particles. Eule and Metzger, arXiv:1510.07876 (2015), provide renewal-reset mixtures and Gamma-family one-time distributions. Stojkoski et al., arXiv:2107.11686 (2021), provide single-particle temporal correlations with Poisson resetting; Bengtsson, arXiv:2205.06103 (2022), provides binary alternating-renewal switch correlations. General stationary age/residual-life moment and correlation research addresses same-time ages and remaining lifetimes, rather than lagged shared-clock cross-particle energy. The assessed claim is the exact spectral five-stage threshold, not the renewal representation or phase-type formalism. A broad, implicit theorem about all phase-type age covariances might cover this specialization and remains a genuine residual literature risk; absence of search hits is not proof of novelty.

## Value — PASS

The 2025 collective-reset Brownian gas makes equal-time particle correlations a natural measurement, but their temporal sign is not settled by equal-time results. The theorem determines whether temporal energy anticorrelation can arise solely from increased clock regularity, supplies the first integer stage for which it must occur, and identifies a nonzero leading oscillatory mode. It is a structural and physically motivated boundary rather than an arbitrary parameter slice. Negative correlations decay at long lag, and detectability has not been established.

## Scope of review

Scientific claims are proved under the idealized free-particle assumptions in the accompanying RESULT.md and reproduced at finite lags using verify.py. The proof is not an independent certification, and general renewal-spectral literature could contain a stronger preexisting theorem. All numerical tests are finite.

Self-review: passed. Independent audit: not yet performed.
