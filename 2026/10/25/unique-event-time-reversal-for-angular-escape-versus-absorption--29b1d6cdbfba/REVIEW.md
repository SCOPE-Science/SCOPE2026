# Review: angular termination-time crossover

## Correctness — PASS

The model is exactly the angular bound-state diffusion on \((-\pi/2,\pi/2)\) with generator \(D\partial_\theta^2\) and independent Poisson killing. The Dirichlet backward transform \(F\) and its derivative yield the two conditional means. Their difference has the same sign as an explicit \(H(z,u)\) for all \(\kappa,D>0\) and all interior starts. The derivative factorization \(Q(w)\), with \(Q\) strictly decreasing, forces a unique minimum and therefore a unique interior sign crossing. Analytic expansions establish the exact small-rate threshold, its first correction, and the strong-rate boundary-layer constant. Independently derived exit-time moments corroborate the leading small-rate threshold. The included finite numerical checks passed, but are not used as the proof.

## Originality — PASS, with residual risk

Bressloff (arXiv:2302.09105), sections 3.2–3.3, derives the **two conditional mean times separately** and plots them; those formulas imply our starting point, so they are not claimed as new. The examined portions do not give the all-rate one-crossing theorem, \(1/\sqrt5\) low-reactivity limit, second-order coefficient, or \(w_*\) high-reactivity layer. Bressloff (arXiv:2302.13986) concerns sticky Brownian occupation time rather than the same angular conditioning. Bressloff–Kim (2019) treats velocity-jump search and conditional passage times, not the specified one-dimensional angular diffusion with competing exponential killing. Semantic database searches did not identify a stronger result covering the sign theorem; these searches alone cannot establish uniqueness. A generically phrased, unindexed theorem for exponentially killed Brownian exit times remains a genuine originality risk.

## Value — PASS

The first-terminal-event conditional times quantify a practical distinction in reversible wall attachment: whether a particle that escapes tends to depart sooner or later than a particle that is killed. The result resolves this ordering **for every initial orientation and every reaction/diffusion ratio**, with exactly one crossover rather than relying on plotted curves. The two endpoint laws identify a physically meaningful coefficient-of-variation threshold at weak reactivity and a shrinking boundary layer at strong reactivity. This structural classification is not a normalization check or just another formula for an already-known MFPT.

## Scope and limits

The result concerns a single wall-binding episode; source-level bulk-return and whole-channel MFPT questions remain separate. Nonexponential killing and angular drift are not covered. Independent audit and validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
