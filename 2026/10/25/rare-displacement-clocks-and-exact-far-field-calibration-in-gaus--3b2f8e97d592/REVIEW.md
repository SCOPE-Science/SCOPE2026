# Scientific review: rare-displacement clocks in Gaussian renewal-competition walks

## Correctness — PASS
The renewal-cycle occupation argument yields the geometric count and independent equilibrium event age. Conditioning a Gaussian sum on its nonzero terminal position yields exact weights proportional to \(n^{-1/2}\exp(-an-r^2/(2n))\). Poisson summation proves the prefactor and exponentially suppressed complex modes, and its first two derivatives give the conditional mean and variance with exact constant corrections. A random-index conditional CLT and negligible equilibrium age establish the bivariate count/physical-age limit. Exponential-clock specializations satisfy the stated formulas. The accompanying executable passed 186 deterministic comparisons; finite checks supplement, not replace, these proofs.

## Originality — PASS with residual risks
The originating work (Li–Zhang–Liu, arXiv:2609.09738v1, §§2.5, 3.2) already provides the stationary position characteristic function and a Gaussian diffusion-tail approximation. Colantoni–Pagnini (arXiv:2507.07590v1) develop general reset CTRW counting machinery, while Asmussen–Hashorva–Laub–Taimre (arXiv:1712.04070v1) examine tails of related random sums. Classical Cramér–Lundberg asymptotics anticipate a geometric-sum exponential tail. Accordingly, neither the marginal geometric law nor the general exponential-tail mechanism is claimed new. The narrow assessed claim combines an exact physical reset-age transform, exponentially accurate conditional far-field jump-count moments, bivariate conditional Gaussian physical-age fluctuations, and the finite-rate calibration of this model. Text inspected for the three arXiv papers did not explicitly supply this combined claim. An unlocated broader renewal/conditional large-deviation theorem may imply some or all of it; priority needs external review.

## Value — PASS
The far-field position marginal alone does not tell how many movement events generated an excursion or how old the excursion is. The theorem reconstructs both observables, quantifies their shared fluctuations, and shows an exponentially material mismatch between finite-rate Gaussian jumps and their diffusion approximation. This is a motivated physical observability and model-calibration gap, not a bare Gaussian-sum formula.

## Limitations and verification
The law is conditional on an exact nonzero spatial displacement, not a first passage or exceedance. Temporal increments are independently resampled at every event, the jump lengths are independent Gaussian variables, and the bivariate age limit assumes finite second moments. The proof and `checks/verify.py` allow reproduction. No independent audit or priority certification has occurred.

Self-review: passed. Independent audit: not yet performed.
