# Independent mathematical audit

## correctness

PASS

A common exponential stationary reset age gives conditionally independent centered Gaussian modes with bounded variances, hence zero ordinary cross covariance and finite moments. Coupling at the first subsequent common reset proves uniqueness. Independently, the stationary generator on x_i² gives M_i=2D_i/(r+2γ_i). Its equation on x_i²x_j², i≠j, gives (r+2γ_i+2γ_j)E[X_i²X_j²]=2D_iM_j+2D_jM_i; on x_i⁴ it gives (r+4γ_i)E[X_i⁴]=12D_iM_i. Subtracting the Gaussian baseline and using the factor three on the diagonal yields F_ij=r/(r+2γ_i+2γ_j) for all i,j. Then b_i=(F_ii^−1−1)/2 is positive exactly when 0<F_ii<1; the other entries are forced by the harmonic-mean relation. Conversely any fixed r>0, γ_i=rb_i/2 and D_i=M_i(r+2γ_i)/2 give a realization with every positive target M_i, so the absolute clock rate is unidentifiable from these statistics. Cauchy's minors have the claimed signs in increasing order; duplicate rows give the upper rank bound and one representative per rate gives the matching lower bound. Independent clocks keep the marginals but give zero off-diagonal power covariance. A real orthonormal nonzero Fourier basis on the circle gives precisely the required independent drivers and positive rates; the arbitrary inverse criterion is for OU modes, not for arbitrary spectra on a fixed circle. The finite archived checks were inspected but not run or used as the universal proof.

## originality

PASS

Credit the explicit complete realization and rate-identification result for arbitrary finite lists of positive, independently driven OU modes, with a clock-coordination test within the stated models. The forward renewal law already contains the joint moments; the off-diagonal elimination, Cauchy minor signs and rank calculation are elementary consequences once the kernel is extracted, not separately new mathematical principles. The strongest explicit catalog match for the forward kernel and strict total positivity is later and restricted to periodic EW, so it is equivalent on a substantial subcase but does not establish earlier coverage of the full inverse result.

## value

PASS

The utility is a complete feasible-data test, not an isolated forward moment calculation. Given measured second moments and normalized fourth-cumulant data, the criterion can reject this common-clock model, reconstruct all damping-to-reset ratios within it, and detect rate degeneracy. The independent-clock contrast isolates a measurable effect absent from one-mode laws and ordinary cross covariance. It does not identify global Poisson resetting uniquely among unrelated stochastic models or recover absolute rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
