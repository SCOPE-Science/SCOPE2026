# Scientific review: weak-resetting rare-displacement law

## Correctness — PASS

The modeled process, stationary construction, and parameter domains are explicit. Synchronous coupling gives uniqueness, and the convergent two-sided stochastic integral gives existence. The stationary characteristic-function identity yields the previously known Laplace-product representation. The new logarithmic moment-generating function is a monotone Riemann sum with a bounded error. Interior derivatives converge; exponential tilting concentrates at every finite prescribed rate-space point, and Chernoff bounds give exponential tightness and the closed-set upper bound. The proof does not assume endpoint lower semicontinuity of a limiting moment-generating function that diverges at finite epsilon. Series expansions give the rate's strict Gaussian comparison and its two limiting regimes. The standalone checker passed 79 finite comparisons; no finite computation is substituted for the large-deviation proof.

## Originality — PASS, with residual priority risk

Pierce (arXiv:2204.07215) and Tal-Friedman–Roichman–Reuveni (arXiv:2205.03363) establish the model, stationary products, low moments, and Gaussian weak-contraction limit. Biroli–Feld–Hartmann–Majumdar–Schehr (arXiv:2406.08387) establish fixed-contraction stationary densities and pointwise exponential tails for both signs of rescaling. Their inspected treatments do not formulate or evaluate the joint weak-contraction/rare-displacement large-deviation rate or the finite-parameter pressure bound. Meylahn–Sabhapandit–Touchette concerns long-time additive-functionals rather than the stationary distribution in this parameter limit. The full exact product and generic large-deviation machinery are explicitly credited, not asserted to be newly discovered. The new target is a nontrivial double-scale asymptotic and its sharp rate geometry, not another way of naming the known product. A broad weighted-Laplace perpetuity theorem could imply this special case; an independent literature priority audit has not been performed.

## Scientific value — PASS

The source papers motivate transition to Gaussian-looking stationary laws as resets become weak, while also identifying fixed-parameter exponential far tails. The new result resolves the precise regime between these descriptions, with a universal, strictly sub-Gaussian rare-event cost, a dilogarithmic rate, and explicit finite-parameter control of the pressure. It quantifies rare stationary excursions of order \(1/\varepsilon\), compared with Gaussian central fluctuations of order \(1/\sqrt\varepsilon\), in a physically established resetting model. This is a motivated asymptotic observable; neither a relabeled normalization nor a recomputation of a previously tabulated constant.

## Closest sources and scientific limits

- Pierce, arXiv:2204.07215, April 14, 2022: stationary advection-diffusion with proportional resets and weak-resetting Gaussian limit.
- Tal-Friedman et al., arXiv:2205.03363, May 6, 2022: exact product, independent-Laplace decomposition and central Gaussian limit.
- Biroli et al., arXiv:2406.08387, June 12, 2024: exact stationary law, fixed-parameter Gaussian core/exponential far tails, first-passage analysis.
- Meylahn et al., Phys. Rev. E 92 (2015): long-time additive-observable large deviations under resetting; not the joint stationary rescaling regime.

The result concerns one-dimensional stationary Brownian motion, fixed positive diffusion and reset rates, and deterministic multiplicative Poisson resets. It does not give finite-epsilon rare-event prefactors, path-space rates, or uniform probability asymptotics outside fixed rate-space thresholds.

Self-review: passed. Independent audit: not yet performed.
