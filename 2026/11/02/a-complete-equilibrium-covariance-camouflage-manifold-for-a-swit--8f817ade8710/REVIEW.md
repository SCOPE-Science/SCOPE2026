# Scientific review: equilibrium-covariance camouflage

## Correctness — PASS

The strictly stationary model is well posed because both stiffnesses are positive. The vector generator recurrence yields the exact second and fourth moments. The covariance solves a two-dimensional matrix evolution; its initial right derivative is fixed by the stationary quadratic balance. The characteristic polynomial and variance yield a completely factorized if-and-only-if condition, and positivity of switching rates exhausts the parameter domain. ODE uniqueness establishes the covariance at every lag, not merely at a sampled set. The fourth cumulant is a strictly positive rational expression throughout the open parameter domain. Exact symbolic and rational replay of `verify.py` passed 229 checks. The proof of global positivity and uniqueness is analytic; finite tests serve only as reproducibility checks.

## Originality — PASS, qualified

The physical model and stationary Gaussian-mixture law were established by Biroli et al. (arXiv:2312.02570). General Markov-modulated OU autocovariance and moment machinery were established by Huang et al. (arXiv:1412.7952); the forward formulae themselves are not claimed as new. Zhang and Wang (DOI:10.1080/03610918.2015.1132321) study stationary marginals; Frydel (arXiv:2407.12213) considers on/off trap fluctuations. Inspected materials did not yield the exact two-parameter, positive-stiffness covariance-camouflage classification or the restricted fourth-cumulant formula. The main possible prior implication is an unrecognized specialized corollary of the Huang et al. forward matrix formula, which could weaken independent originality. Biroli et al.'s separately mentioned supplementary material was not independently examined. Neither a negative search nor the partition of a database proves worldwide novelty; independent publication-priority review remains unperformed.

## Mathematical value — PASS

The exact classification resolves a natural inverse question in switching confinement: whether complete stationary temporal covariance can rule out a hidden switching potential. It cannot, even when the competing equilibrium OU diffusivity is fixed. The result is not an arbitrary numerical coincidence: every effective rate admits a two-dimensional continuum of counterexamples, with the complete positive-rate locus and a strictly positive measurable fourth-order obstruction. It distinguishes temporal second-order identifiability from one-time spatial distributional information. The result does not establish performance from finite noisy data, nor extend to non-Markov environments.

Self-review: passed. Independent audit: not yet performed.
