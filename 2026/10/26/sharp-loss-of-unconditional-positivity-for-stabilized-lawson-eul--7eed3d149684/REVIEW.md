# Scientific review

## Correctness — PASS

The final statement is the complete all-step nonnegativity classification for the stated symmetric three-node path, together with the precise off-diagonal crossing and its logarithmic equal-weight limit. The update is derived directly from the source's stabilized Lawson–Euler formula. The spectral decomposition of the three-node generator gives the semigroup derivatives. When edge rates agree, all off-diagonals are positive and the middle diagonal gives the exact \(2/(3e)\) threshold, while the endpoint diagonals cannot set a larger threshold. With unequal rates, the slow spectral contribution to the larger edge's transition derivative is negative, its fast contribution is positive, and they cross once. The limit near equal rates follows from their explicit coefficients. The supplied numerical checker is supplementary, not a substitute for these arguments. No unstated numerical-precision claim is made.

## Originality — PASS, qualified by coverage risk

The closest primary source is Caliari, Cassini, Einkemmer and Ostermann, arXiv:2303.15861, Section 2 and appendix, which supplies the actual stabilized Lawson–Euler method and unconditional negative-real-axis scalar spectral stability for \(\alpha\geq1/(2e)\). It does **not** give the Markov-entrywise positivity criterion for weighted paths. Hu and Shu, arXiv:1807.03728, construct a different positivity-preserving exponential Runge–Kutta method under different subflow/coefficient assumptions. Jones, Epstein and García-Mochón, DOI:10.1177/0272989X17696997, derive ordinary Markov transition probabilities but not this numerical update's all-step classification. published-finding corpus comparisons to exact positivity thresholds for Padé, Crank–Nicolson and SSP-SDIRK methods concern different stability functions and do not imply the present identity, rate-rigidity, or logarithmic delayed crossing. Uncatalogued equivalent findings about monotonic Markov transition probabilities remain possible.

## Value — PASS

The claim isolates a mathematically relevant difference between a diffusion solver's norm/spectral stability and its nonnegative mass transport: strict modal contraction can coexist with negative transition coefficients at arbitrarily large steps. The all-step positivity property survives only at exact conductance balance, and its sharp stabilization requirement is determined exactly. The logarithmic divergence of the first affected edge's sign-change time quantifies why finite-step testing may misleadingly appear robust to small heterogeneity. These are structural, reproducible thresholds of a published integrator, not an arbitrary parameter slice or a small numerical improvement.

## Limitations and residual risks

Only symmetric three-node paths and their exact-arithmetic stabilized Lawson–Euler step are classified. The computed sign crossing need not be the first failure of full-matrix positivity. No nonlinear reaction, multidimensional grid, general graph, or floating-point guarantee follows. The self-review is not a third-party novelty certificate. The closest-paper sections and relevant comparative primary literature were inspected, but unindexed equivalent results cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
