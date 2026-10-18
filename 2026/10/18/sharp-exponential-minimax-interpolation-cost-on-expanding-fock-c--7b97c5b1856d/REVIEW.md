# Self-review

## Correctness — PASS

The exact normalized Gram computation is carried out with the data inner product factor \(1/N\); hence its nonzero eigenvalues are precisely the Poisson residue probabilities rather than \(N\) times those probabilities. Each equals a strictly positive series, so the sampling map is onto. The explicit Fourier-mode interpolants meet the data and attain squared norm \(1/p_{N,m}\). Stirling bounds together with geometric Poisson-tail estimates give lower and upper bounds of order \(N^{-1/2}e^{-NM}\) for the minimum residue probability, with potential zero-index masses handled separately. Strict convexity identifies the maximum of the rate-minimization envelope and proves unique worst-harmonic localization except at the stated boundary cases. The \(\rho\to\infty\) expansion follows from the logarithmic identric-mean integral. Remaining limitation: constants depend on fixed \(\rho\); no uniform critical-window estimate is claimed.

## Originality — PASS, subject to historical priority risk

Horoshko and collaborators (arXiv:1602.07852, equation (9)) already provide the exact circular coherent-state Gram/Fourier/Poisson identity. Alpay, De Martino and Diki (arXiv:2604.22165v2) develop complex RKHS representer theory and Fock-space interpolation, but the inspected Fock applications do not classify the least singular value of expanding regular-polygon sampling. Seip's density theorems address infinite sampling/interpolation sets. Closest published research entries concern concentric Szegő-orbit conditioning, equispaced Bergman pole Hessians, and critical Gaussian Gabor biorthogonals; their operator/invariant/scaling hypotheses do not imply the present statement. The assessed contribution is specifically the sharp \(\sqrt N\) order, optimized identric-mean exponential rate, critical transition and worst-mode localization. A related *Optimal circular states* (2024) paper was accessible only through an abstract/first-page preview, leaving a disclosed residual priority risk.

## Mathematical value — PASS

The worst-case norm of an RKHS interpolation right inverse quantifies stability of all data at once. In the double-scaling regime of \(N\) points and squared radius \(\rho N\), exact cyclic diagonalization alone leaves a nontrivial discrete minimax problem involving infinitely many Poisson aliases. Its solution yields a nontrivial universal threshold \(e^{-1}\), a complete harmonic-location phase diagram, an exact exponential condition rate, and the sharp polynomial growth order. This is a motivated quantitative interpolation theorem, not merely a recomputation of the known Gram eigenvalues.

## Scientific limits and closest sources

The full 2016 circular-state article and the full 2026 complex-RKHS article were inspected; the 2024 related circular-state paper could not be read in full. Finite checker diagnostics supplement, not establish, infinite-dimensional proofs. No independent verification is asserted.

Self-review: passed. Independent audit: not yet performed.
