# Independent mathematical audit

## correctness

PASS

Regeneration at the common reset justifies the stationary generator identities. Reflection makes the covariance diagonal and the horizontal mean real. For Z=X+iY the isotropic translational quadratic variation cancels in Z^2; the equations for E[exp(i Theta)], E[exp(2i Theta)], E[Z], E[Z exp(i Theta)] and E[Z^2] close with rates r+d, r+4d, r+k, r+k+d and r+2k respectively. Centering subtracts (E[Z])^2, essential for the crossings. Clearing the positive denominators gives P=2(r+k)^2(r+d)^2-r(r+2k)(r+k+d)(r+4d). Its signs have two changes for every k,d>0 including k=d with the zero cubic term removed, while P(0)>0, P(d)=-d^2(2d^2+9dk+2k^2)<0 and P ultimately positive. Thus the two bracketed roots are simple and exhaustive. At D=0 the transverse variance is strictly positive by the displayed moment formulas and the longitudinal variance is bounded below by the variance of its conditional mean given reset age: the latter mean is continuous, vanishes at age zero, and is positive for every positive age. Nonzero horizontal mean rules out rotational invariance about the trap origin, not merely unequal eigenvalues. With b=k/d and x=r/d the four limits follow by sign bracketing near the simple roots of the appropriate rescaled polynomials: 2-4y-2y^2 and x^2(x-2)(x+1) for b small, 2-4x and y^3-4y for b large. The bracket at x=1 identifies the branches at each scale. An independent bounded symbolic check confirmed the quartic, the sign identity at d, the four scaled limits and the free factorization. The supplied verification.py was inspected but not executed. At k=0 the exponential reset age still gives finite stationary moments and the remaining crossing is 2d.

## originality

PASS

Pass for the global finite-confinement classification, including the paired confinement scalings. The same-model moments, centered scalar anisotropy obtained by subtracting them, and the free-particle crossing are not independently original. The primary trapped-model paper's reentrance concerns kurtosis; its equations supply the inputs but no theorem on the number, simplicity, location and singular behavior of the positive centered covariance crossings. Literature and catalogue comparisons are bounded.

## value

PASS

The exact number and direction of sign reversals are qualitative predictions for an entire continuum of stable traps, not a fixed-parameter moment recomputation. The singular limits explain how the transition missing in the free model is lost and how the two confinement scales separate in a strong trap. These predictions use centered rather than raw moments and identify experimentally meaningful reset-rate regimes independent of isotropic translational noise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
