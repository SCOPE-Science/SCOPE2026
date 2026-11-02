# Scientific self-review

## Correctness — PASS

The claim is quantified for a unit-interval diffusion, and nondimensionalization restores general interval length and diffusivity. The local-time normalization gives \(\mathbb E L_d=d\) and the exact second moment \(2\int_0^d(d-s)H_s(0,0)\,ds\). The Neumann heat-kernel bound yields \(\mathbb E L_d^2\le3d^{3/2}\); Cauchy–Schwarz then gives the lower pulse-removal envelope \(kd/(1+3k\sqrt d)\), while a reflection-principle hit bound supplies the upper envelope. Uniformly positive Neumann heat kernels during every gap sandwich each conditional removal probability between constants times the isolated-pulse probability. Elementary infinite-product analysis then proves the necessary-and-sufficient survival series, not merely a sufficient condition. The independent half-line Robin boundary calculation gives the short-pulse crossover; a right-endpoint excursion requires an exponentially unlikely round-trip. The standalone verifier reproduces 254 finite numerical/algebraic checks but is not the source of the infinite-horizon proof.

## Originality — PASS, qualified

Grebenkov and Ye (arXiv:2610.23017, publicly posted 2026-10-16) provide the weighted boundary-local-time formulation, discuss piecewise-constant reactivities, and analyze smooth time dependence through adiabatic approximations. Their finite-integrated-reactivity implication is not the equivalence for shrinking finite-rate pulses: these regimes need not have small reaction rate, and pulse width separately caps exposure. Grebenkov (arXiv:1909.07677) studies local-time distribution and constant reactivity; Bressloff (arXiv:2205.13985) studies *randomly* switching reactive states. Guillaume (doi:10.3390/appliedmath4030058) studies a finite-time intermittent *perfect* barrier; only its abstract could be inspected. Comparison against retrieved research records identified no statement whose hypotheses entail the sharp pulse series. This is a best-knowledge comparison, not a uniqueness proof. Residual risk: a general parabolic potential/capacity or dynamically gated reaction theorem not located in accessible sources might already imply the result.

## Value — PASS

The problem of whether a bounded-volume diffusing reactant eventually reacts on a temporally gated surface is physically natural. The sharp series gives a constructive design rule and a non-adiabatic phase diagram, exposing a qualitative failure of an extrapolation from integrated reactivity: even \(\sum\kappa_n\delta_n=\infty\) may leave permanent survivors. Conversely, a finite total reactive open time may nevertheless suffice for almost-sure eventual capture. The exact limiting crossover separates reaction-limited exposure \(\kappa\delta\) from the diffusion-limited cap \(\sqrt{D\delta}\) without assuming slow parameter changes.

## Limits and priority risk

The statement does not cover arbitrarily close pulses, nonlinear boundary mechanisms, unbounded domains or higher-dimensional geometries. The motivation's full accessible primary text has been assessed, but a complete priority guarantee over every earlier result is impossible; an inaccessible relevant abstract and general heat-equation literature remain residual risks. Numerical tests do not establish the theorem and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
