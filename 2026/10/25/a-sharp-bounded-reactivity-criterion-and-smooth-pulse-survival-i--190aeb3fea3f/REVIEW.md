# Scientific review

## Correctness — PASS

The reflected process is explicitly fixed to generator \(\partial_{xx}\) with uniform invariant measure and boundary-layer local-time normalization. The Neumann heat kernel makes the exact weighted local-time covariance a positive convolution kernel. Its integral over the real line is \(2/3\) via the Basel sum. Young's inequality yields the stated sharp variance bound; constant reactivity saturates the coefficient asymptotically. Under uniformly bounded nonnegative reactivity, variance divided by squared total exposure tends to zero, and a quadratic-exposure subsequence plus Borel--Cantelli establishes the full almost-sure law. For the smooth pulse construction, stationary uniform initialization and the folded-Brownian reflection estimate make the boundary-hitting event probabilities summable, forcing only finitely many nonzero pulse contributions almost surely. A finite-time survival bound follows from Chebyshev. The standalone program passed 19 finite assertion groups; the proof, not the numerics, establishes the infinite statements.

## Originality — PASS, with residual priority risk

The starting framework and its finite-total-reactivity survival implication are already present in Grebenkov and Ye, arXiv:2610.23017v1. Classical boundary-local-time spectral methods and earlier local-time distribution theory also predate this result. The assessed contribution is the if-and-only-if classification for *arbitrary bounded measurable* temporal reactivities, the sharp stationary weighted-local-time variance constant, and the explicit smooth unbounded pulse counterexample with a finite almost-sure but infinite-mean integrated hazard. This is not a rephrasing of the source's adiabatic power-law examples. Semantic literature and local claim searches did not identify a prior statement proving the same combined sharp boundary; this is evidence, not a proof of uniqueness. A general weighted additive-functional theorem or another publication may implicitly subsume pieces of it.

## Value — PASS

A surface with infinite nominal integrated chemical activity need not react with every confined particle if its activity is concentrated into sufficiently short, intense bursts. Conversely, any bounded activation schedule with divergent integrated activity forces eventual reaction even without monotonicity or periodicity. The exact variance coefficient and explicit survival bound quantify reliability of exposure-based reasoning. The nonuniform-integrability phenomenon, finite accumulated hazard almost surely despite infinite expected hazard, distinguishes temporal chemical forcing from stationary average-rate intuition.

## Closest literature and scope limits

Grebenkov and Ye (2026) give the reaction-clock formalism and adiabatic regimes; Grebenkov (2019, 2007) supplies the established local-time spectral background; Ye and Grebenkov (2025) treats correlations for related first-reaction observables rather than the present global-in-time temporal-pulse comparison. The result is restricted to a stationary particle in a unit interval, with a fixed endpoint target and deterministic reactivity. Independence and priority review have not been undertaken.

Self-review: passed. Independent audit: not yet performed.
