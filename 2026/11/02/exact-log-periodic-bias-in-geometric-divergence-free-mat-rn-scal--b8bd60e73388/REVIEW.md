# Scientific review: exact log-periodic bias in geometric divergence-free Matérn scale mixtures

## Correctness — PASS

The claim concerns exactly the stationary Matérn-derived divergence-free *finite* covariance family and the separate, increment-only bilateral limit. Differentiation of \(\phi(t)\) reproduces the trace formula and derivative. The derivative establishes nonnegative increments and both tail majorants. Geometric tail summation gives the explicit finite-grid bound. In the Mellin strip \(0<\Re s<2\), integration by parts gives the Gamma transform without a missing boundary term. Periodization on \(\log q\) gives the stated Fourier coefficients. Gamma's zero-free property rules out every harmonic vanishing. Vertical-line Stirling estimates prove the needed absolute convergence, first-harmonic dominance, and exact minimax constant. The embedded numerical verifier passed 100 illustrative checks; these tests are not the infinite proof.

## Originality — PASS, with historical priority risks

The 2026 Matérn compression source fixes the kernel and physical-scale weights but does not calculate the bilateral geometric-grid Fourier coefficient or sharp best-power-law bias. The earlier 2026 operator-learning source also uses geometric length modes and evaluates empirical structure functions, not this explicit analytic law. Sornette's 1998 review already develops discrete-scale invariance, Poisson summation, Mellin transforms, Gamma coefficients, and turbulence log-periodicity; none of those *methods or qualitative consequences* is claimed as original. The distinction is the explicitly evaluated, provably nonzero harmonic spectrum for this particular divergence-free kernel, its sharp small-grid **minimax** prefactor, and the finite-grid approximation certificate. Owhadi's 2023 multiscale Gaussian hydrodynamics work is substantively related, and a general spectral mixture result could imply this specialization; the full 2023 body was not materially inspected. The accessible comparison therefore supports originality but is not a proof of historical uniqueness.

## Mathematical value — PASS

The \(8/3\) weight is chosen to mimic a \(2/3\) covariance-increment law. The finding quantifies an inherent error introduced *by discretizing the physical length scale geometrically*, even before any velocity coefficients are fitted or compressed. It gives the first-harmonic bias amplitude for any scale spacing, a sharp small-spacing design law, and a directly computable finite-length cutoff budget. That distinguishes two concrete sources of scaling deviation, geometric phase and missing extreme scales. It does not claim empirical turbulent exponents, physical cascade phenomena, interpolation convergence, or error in a complete compression algorithm.

## Limits

The bilateral increment object is not a stationary finite-variance covariance. The Matérn-based formula is specific to spatial dimensions two and three and to exact geometric scale spacing. The classical 1998 general Mellin/Poisson formalism reduces methodological novelty, and a stronger earlier Gaussian-scale-mixture theorem may subsume the statement. Finite-precision checks cannot establish the infinite assertions; the written proof must be used for those.

Self-review: passed. Independent audit: not yet performed.
