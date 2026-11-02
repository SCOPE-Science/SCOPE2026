# Scientific review: Reentrant stationary-support topology in Haar-basis zeroth-order descent

## Correctness — PASS

For \(d\ge2\), expanding the actual orthogonal forward differences yields the exact affine recursion with uniform-sphere innovations. The proof reconstructs the stationary series and Wasserstein contraction, then applies the complete polygon inequality and connectedness to determine its entire compact support, rather than guessing from sampled trajectories. Its second moment and absolute-continuity boundary are independently established. The accompanying verifier passed 780 exact-rational support/moment tests, 750 finite-difference identity checks and five separate stationary simulations. The general argument is analytic; finite checks are corroborative.

## Originality — PASS, qualified

Kozak et al. (arXiv:2107.03941, Sections 2, 3 and 9.1) introduce the orthogonal finite-difference setup and study convergence, but their inspected full text does not classify constant-step invariant support. Rando et al. (arXiv:2206.05124, Algorithm 1, Assumptions 2–3, Appendix D.4) treat the same structured estimator in a stochastic setting and focus on convergence estimates, not the exact reentrant topological support thresholds. Searches of equivalent sphere-innovation random recursions and accessible published mathematical records found no direct full-algorithm statement. Classical geometric random-series or affine-recursion results could cover the support geometry in an alternate language; the claim does not assert novelty of polygon closure or contractive random-series theory. Priority therefore remains qualified.

## Value — PASS

This is a full-dimensional exact stationary benchmark with a sharp algorithmically meaningful distinction: in some stable stepsize regimes the method *cannot* visit a central neighborhood of its minimizer in stationarity, whereas in others its support includes the minimizer. The sphere at the center rate and the fixed outer radius as the mean-square error vanishes distinguish support geometry from usual optimization error estimates. The result does not generalize to arbitrary objectives, sampling mechanisms or finite-sample confidence guarantees.

## Closest literature and limitations

- Kozak, Molinari, Rosasco, Tenorio and Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941.
- Rando, Molinari, Villa and Rosasco, *Stochastic Zeroth order Descent with Structured Directions*, arXiv:2206.05124.
- Banakh, Bartoszewicz, Filipczak and Szymonik, *Topological and measure properties of some self-similar sets*, arXiv:1403.0098 (abstract-level comparison only, not a full-text noncoverage assertion).

The restrictions are integer dimension at least two, full i.i.d. Haar bases, centered isotropic quadratic, noiseless forward differences and strictly stable constant steps. A complete priority search over geometric random-series literature and independent scientific audit are outstanding.

Self-review: passed. Independent audit: not yet performed.
