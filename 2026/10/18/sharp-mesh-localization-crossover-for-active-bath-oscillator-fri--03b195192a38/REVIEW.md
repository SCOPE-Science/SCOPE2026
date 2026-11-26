# Independent mathematical audit

## correctness

PASS

Checked the stated second-order normalization against Beyen–Maes–Santra Eqs. 2 and 19–22 and App. C: the two-sided alias sum has prefactor n/2 for the friction eigenvalue and 1/2 for the variance intensity of the 1/n-normalized modes. The Bessel coefficients are positive for p>0; A and B converge and are strictly positive for k≠0, so the unique positive root and its signs follow. For the limits, after rescaling the Bessel integral by sqrt(p), the rescaled density converges in L1 to the standard normal using a Gaussian majorant on the whole rescaled integration interval. Its characteristic function limit is uniform on compact mode scales. The contour-shift bound can use s=j/(2p) for j≤p and s=1/2 for j≥p, giving exp(−c min(j²/p,j)); in u=j/sqrt(p) the squared ratios are bounded by an integrable envelope exp(−2c min(u²,|u|)), adequate for uniform shifted-grid tails. In the coarse regime this gives nA/sqrt(p)→sqrt(pi); n²B converges by the summable denominator bound to pi² csc²(pi x). This yields the claimed p^(1/4)sqrt(n) constant and, for fixed n,k, the leading negative friction and finite normalized noise. In the critical regime the same envelope dominates the discrete m-tail since n/sqrt(p) stays bounded away from zero, giving A→Theta and pB→Psi/rho². For the theta profile alone, Gaussian Riemann summation and denominator domination give its small-rho endpoint; the nearest aliases dominate both sums at large rho, including the double minimum at x=1/2. No uniform microscopic expansion or boundary-mode claim is needed. The finite verify.py was inspected, not rerun; it tests dimensionless friction aliasing and finite approximations, not the noise normalization or infinite limits.

## originality

PASS

Credit is confined to the sharp joint mesh/localization asymptotics at interior fractional mode, including the crossover profile and the point-kernel consequences of the coarse regime. The input Fourier coefficients and finite alias sums are published, and the individual finite zero is an algebraic consequence, not a separate originality claim.

## value

PASS

The theorem resolves a natural competition between the lattice and a shrinking interaction width, with an explicit change in threshold scale and computable mode dependence. Even at fixed chain size it distinguishes the divergent negative second-order friction from bounded normalized noise. This quantifies the reduced model but does not establish full-system instability or any uniform validity or failure of the weak-coupling remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
