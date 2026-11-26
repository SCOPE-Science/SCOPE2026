# Independent mathematical audit

## correctness

PASS

For R=sqrt(a), all integer maximizers have bounded x=(n-a)/R: for each Poisson integrand the ratio of successive terms is t/(n+1), which forces monotonicity outside the extreme endpoints of the two intervals. The radial Gaussian diagonalization has the given t=pi r^2 normalization. Stirling expansion gives the displayed cubic correction Q and a uniform O(R^-2) remainder after normalization by sqrt(2 pi) R/w; averaging over the symmetric fixed widths leaves the order-R^-1 term unchanged. For d<1 the strict quadratic maximum and the Lipschitz first correction, comparing to the integer nearest a, bound |x| by O(R^-1). For d>1 the two nondegenerate maxima solve x=d tanh(dx); their height difference from the odd correction is positive in favor of the lower index, since H_d(x_d)/F_d(x_d)=x_d(x_d^2-d^2-3)/6<0. Local optimization and lattice rounding affect that comparison only at O(R^-2). For d=1 the quartic loss and linear term bound maximizing |x| by O(R^-1/3), and the rescaled polynomial -y^4/6-4y/3 has unique maximizer -2^(1/3). The rescaled lattice mesh tends to zero. This proves the law for all maximizers, not finite-index uniqueness.

## originality

PASS

Supported distinction: the fixed-area-width law, including its bounded subcritical drift and explicit fixed-width thresholds and peaks. The negative cubic-root coefficient and lower-branch selection as phenomena are already explicitly established in the closely related October 18 record and must not be credited here as new phenomena.

## value

PASS

Fixed area is a natural localization constraint and makes the normalized annuli shrink, with peak eigenvalues on a different scale from the earlier macroscopic-width theorem. Knowing the preferred Hermite degree and resolving its quartic-critical scale and the leading-order tie gives information the leading Gaussian limit cannot supply. The contribution is the fixed-area classification, not discovery of the universal coefficient in all settings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
