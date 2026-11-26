# Independent mathematical audit

## correctness

PASS

The repaired claim is about moments of physical position at fixed initial phase, with raw position measured from the center of the initial cell. The positive normalized affine phase density rho(Ly)=(1+eta(1−2y))/L has flux v/L=a rho(L)−b rho(0). A positive Robin killed heat kernel on the compact interval gives a fixed-time minorization for the phase process, hence the required convergence. With regulator normalization dU=sqrt(2D)dW+dK^0−dK^L between jumps, the corresponding jump intensities are b dK^0/D and a dK^L/D. For psi'=Q(b+Delta u/L)/D, Q=2DL/H=L+psi(0)−psi(L), the jumps of LN+psi(U) are ±Q and the local-time drifts cancel at both ends; D psi''=v. The resulting martingale yields E X_t=vt+c(u0)+o(1) with c=x0+(psi−u)(u0)−E_rho(psi−u). The midpoint constant is −L² Delta(6D+LS)/(12H²). Applying Itô to functions with equal endpoint values and independently chosen endpoint derivatives gives E K^i/t→D rho(i); the continuous and jump brackets then give D_var=D int(psi')² rho + Q²[a rho(L)+b rho(0)]/2. Bounded phase error affects the variance by o(t). Exact integration gives the stated D_var, and the coefficient of 2t in the raw second moment is D_var+v c. The primary derivation starts at the cell center x0=0 and computes the raw second moment (Appendix D), so the proper comparison is D_raw^mid−D_printed=−DL² Delta²/(3H²), not the centered difference. At D=L=1, a=3/2, b=1/2, centered and printed values are 15/32 but raw is 43/96. The new exact replay ran successfully; it verifies the algebra, not the infinite-time stochastic argument. The source checker was read but not run. The one-way renewal calculation is an additional centered-limit check only.

## originality

PASS

The repair explicitly credits the earlier propagator, drift and its counting-tilted characteristic denominator, and drops the broad SCGF/LDP claim. The exact phase-dependent mean offset, the corrected raw coefficient at the same center start, and the quantitative separation from the centered coefficient are distinct from the inspected prior Eq. (26) and its derivation. No matching exact correction was identified in the screened primary and catalogue material. This credits the exact same-model prior work and claims no priority for the reflected-process, corrector or martingale methods.

## value

PASS

This distinguishes two experimentally and mathematically different coefficients in the same biased transport model, recovers the initial-condition correction that couples to drift at order t, and gives a true same-convention correction to a printed formula. In particular there is a strictly positive-rate example where the printed and centered values agree but the raw prediction remains wrong; merely comparing the centered coefficient to the printed number misses it. The exact coefficients are useful for fitting raw and centered moments without forcing them to have the same subleading slope, and provide independent transport benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
