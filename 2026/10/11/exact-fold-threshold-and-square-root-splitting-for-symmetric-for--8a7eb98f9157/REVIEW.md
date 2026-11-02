# Independent mathematical audit

## correctness

PASS

Independently reconstructed the construction x*(t) by exponentiating the sign-specific linear equations. Strict decrease of h on [0,L] and antisymmetry imply 0<c*<H, positive first-half and negative second-half crossing, x*(0)=x*(L)=x*(2L)=0, and transverse velocities H-c*>0 and -(H+c*)<0. The Poincaré map is increasing and convex by scalar comparison; at infinity displacement tends to +∞ on both tails. At c=c*, the crossing residence-time derivative Q=1/(H-c*)+exp(bL)/(H+c*) gives P_uu=2bQ>0 and parameter derivative P_c=-2(1-exp(-bL))/b<0. This establishes isolated fold and, by strict monotone parameter response and convexity, exactly 0/1/2 fixed points. Reversal x(t)→-x(-t) yields initial values ±u and reciprocal multipliers. Taylor gives u~sqrt(2(1-exp(-bL))/(b² Q))sqrt(c-c*), multiplier expansions 1±2bQKsqrt(c-c*). Checked the trigonometric integration and B<A/3 derivative condition. Independent solve_ivp+root finding used three choices (A,B,b) and deltas 1e-3,1e-4; P(0,c*) residual <=6e-13, symmetric roots and predicted sqrt coefficient approached correctly. Numerical tests are corroborating, not infinite proof. Verified all seven actual Git blob identities and source tree SHA.

## originality

PASS

A fresh comparison of the actual mathematical implications finds no covering independent theorem. Gasull–Zhao (2023) gives global two-cycle upper bound, convexity and perturbative fold configurations, but not the exact half-wave bias functional or its explicit fold and Floquet constants. Bravo–Fernández–Ojeda (2024) restricts the coefficients to first trigonometric polynomials and develops half-map bounds, not a formula for arbitrary C^3 monotone even half-wave profiles. The older Carmona et al. cosine-reduced equation could cover the pure harmonic specialization, not the asserted arbitrary mixed-waveform class; its inaccessible text remains a priority risk. The indexed self-match was excluded as independent evidence.

## value

PASS

The scalar b|x| forced oscillator is a natural exactly analyzable piecewise-linear periodic model. Determining the exact parameter at which periodic states first appear and their sharp local separation and reciprocal stability for an infinite-dimensional family of monotone symmetric forcing profiles answers more than the known universal two-cycle bound. The weighted Laplace functional distinguishes waveform shape; a mixed first/third-harmonic example shows this is not merely the classical single-sinusoid calculation. The full waveform-dependent theorem and natural bifurcation profile have plausible further use in nonlinear-oscillator comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
