# Scientific review of the micropaint-island limit

## Correctness — PASS

For fixed positive propulsion speed, orientation flip rate and spatial window, the paired-tumble skeleton reaches every positive level almost surely. Strong Markov and the bounded two-state first-passage equation identify the spatial color-chain rates. Independent exponential sojourns then give a coupled marked Poisson limit, with terminal-window truncation controlled. A separate tilted-generator calculation verifies the finite-window Laplace representation and all-moment limit. `checker.py` passed 202 analytic/numerical assertions and two Monte Carlo comparisons using 50,000 samples, as supplementary checks.

## Originality — PASS, qualified best-knowledge

Sezik and collaborators (arXiv:2603.24277) establish the paint observable, one-point first-arrival laws, long-time expected color fractions and heuristic microscopic island widths. D'Auria and collaborators (arXiv:1006.2965) provide the broader established Markov-additive spatial ladder theory; the finite-parameter two-state generator is therefore not asserted as novel. The assessed addition is the jointly marked Poisson limit for microscopic counter-color intervals under vanishing diffusivity, along with their amplified compound-Poisson area and nonzero empty-window probability. The accessible relevant statements do not explicitly give this limit, but it is a possible short specialization of generic ladder theory; priority remains qualified. The 2026 Latouche ladder-process chapter (DOI:10.1007/978-3-031-98576-8_2) was available as an abstract only, leaving a material full-text comparison risk.

## Value — PASS

The physically motivated question is not merely the fraction of space painted in a minority orientation, but whether rare opposing patches persist, how often they appear, and how large they are. The result answers all three: finite-rate Poisson starts, exponential diffusivity-scaled lengths, and a complete non-Gaussian compound-Poisson integrated coverage law. The nonzero limiting occurrence probability despite vanishing area gives a meaningful singular boundary behavior beyond the previously reported expected-volume and width scales.

## Scientific limitations

The claim concerns a single noninteracting one-dimensional particle, the positive spatial ray, initial rightward orientation, fixed positive propulsion and flip rate, a fixed spatial observation window, and completion of first arrivals over unbounded physical time. It does not apply to actual finite-time paint fields, two-sided joint correlations, feedback from deposited paint or simultaneous window growth. General ladder-process theory is a relevant prior framework and independent mathematical and publication-priority audits remain unperformed.

Self-review: passed. Independent audit: not yet performed.
