# Independent mathematical audit

## correctness

PASS

Squaring the exponential in the Rayleigh–normal convolution gives exp(−x²/2) times the integral of r times a normal kernel with center ηx and scale s; this yields the stated density, including the normalization and the η=0 case. With t=η/s and g(z)=φ(z)+zΦ(z), the derivative in t of the noncommon part tΦ(tx)/g(tx) of the x-score is φ(z)[(1+z²)Φ(z)+zφ(z)]/g(z)². Integrating (u+z)² against φ(u) on u>−z gives exactly the bracket, strictly positive even for negative z. At η=1 the ratio vanishes for x≤0 and its positive-half-line log derivative is φ(t_a x)/(x g(t_a x)). Independently, one integration by parts in the mixture CDF gives F_η(x)=Φ(x/s)−η exp(−x²/2)Φ(ηx/s) for η<1. On differentiating, the terms containing derivatives of the Φ factors cancel since φ(x/s)=exp(−x²/2)φ(ηx/s); the remaining derivative is strictly negative at each finite x. The mixture converges almost surely to R in this representation, whose CDF is continuous (including at zero); an interior strict gap persists to the endpoint by monotonicity. The ordered quantiles couple the variables so that the transport cost equals the mean difference, which is also a lower bound for every coupling. The Rayleigh mean sqrt(π/2) gives the exact W1 metric and hence the constant-speed path. I inspected but did not run the included finite quadratures; none is needed for the assertion on the continuum.

## originality

PASS

The density, its interpolation between endpoint laws, and those endpoint laws are established prior content. The supported distinct content is global parameter likelihood-ratio ordering with the stated endpoint qualification, the signed CDF derivative and strict order, and the resulting exact W1 geometry for the fixed family. This is a bounded comparison, not a priority guarantee.

## value

PASS

The family is fixed by Palm peak-height calibration, not an arbitrary Gaussian mixture. The result orders all finite height thresholds as curvature correlation changes, with the stronger likelihood-ratio comparison on the full interior support. The exact W1 formula supplies a uniform sharp sensitivity measure for these fixed marginals. None of this asserts a comparison for finite meshes or a coupling of the underlying Gaussian processes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
