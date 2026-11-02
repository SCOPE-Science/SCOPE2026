# Scientific review

## Correctness — PASS

The statement is for the stationary, two-coordinate partial-reset diffusion with fixed \(r>0\) and \(\gamma\to\infty\). The generator applied to \(x^2+\gamma q^2\) is strictly dissipative outside a compact set. Exact second-order stationarity equations provide uniform moments. An exact compensated-Poisson martingale identity averages out the fast coordinate with an \(L^2\) remainder, giving a stationary Ornstein--Uhlenbeck limit for the bath. The uniqueness of the frozen-bath reset diffusion's invariant measure identifies the joint stationary weak limit. The three empirical-average regimes follow from this limit, an exact bath increment estimate, and a positive, integrable stationary autocovariance. All three ranges of \(T_\gamma/\gamma\) are quantified. The standard-library program `CHECK.py` verifies 282 exact-rational and numerical assertions; finite tests do not replace the convergence proof.

## Originality — PASS, qualified

Santra and Das (arXiv:2603.17027v1, March 17, 2026) give the model and its stationary moment equations and propose the frozen-bath tracer marginal by time-scale separation. The marginal mixture formula and stationary second-moment equations are explicitly credited, not presented as new. Previously available two-time covariance calculations for this partially reset model already imply its integrated autocovariance; that algebra is used only as supporting verification here. The assessed claim instead proves joint stationary weak convergence and a three-regime **distributional** Gaussian law for empirical position averages, neither of which follows from the one- or two-time moment formulas. Biswas et al. (arXiv:2412.09260) analyze correlation functions under complete memory renewal; their different resetting map is not the present conditional frozen-bath system. Maes and Thiery (arXiv:1705.07670) reset bath particles rather than the observed probe. Search-based noncoverage is not treated as proof of novelty. Publication-priority risk remains for general stochastic averaging and unseen related specialized work.

## Value — PASS

A time-scale-separation approximation for a memory-preserving reset experiment becomes a mathematically justified joint invariant-law limit, with a direct experimentally relevant consequence: long single-trajectory averages can remain randomly offset in the regime \(1\ll T_\gamma\ll\gamma\). The explicit crossover function \(\Phi\) quantifies when the observation window begins to resolve bath relaxation and the offset disappears. This is distinct from a mere stationary-variance computation and gives a natural, physically motivated three-regime classification.

## Limitations and closest literature

Only the single harmonic auxiliary bath, independent white noises, Poisson probe-only resets and stationary initial law are treated. No uniform spatial-tail convergence, nonlinear bath theorem or unqualified claim of first publication is asserted. The 2026 primary paper's complete arXiv HTML was inspected; the separately hosted journal full text could not be fetched and remains a residual comparison risk. The most relevant accessible earlier reset-correlation paper employs complete memory resetting. All claimed Gaussian limits are proven weak limits; no unrelated functional central limit theorem or independent assessment is claimed.

Self-review: passed. Independent audit: not yet performed.
