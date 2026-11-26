# Independent mathematical audit

## correctness

PASS

At a stationary observation under a Poisson process, the backward age is Exp(r), independent of the standardized Brownian increments. With S=sqrt(2DT), E[S^2]=2D/r and (E[S])^2=(2D/r)pi/4. Since the signed min has the opposite conditional mean to the max, the normalized covariance is g_N-(1-pi/4)a_N^2 where a_N is the standard-normal max mean and g_N is the standard-normal max/min covariance. Distinct coordinates have conditional cross moment zero and hence zero covariance, not independence. Gaussian integration by parts for the max mean gives the displayed integral; normalizing phi^2 gives a variance-1/2 Gaussian and the N=4 orthant probability with correlation 1/3. In the joint moment over x<y, writing y phi(y)=-phi'(y) first gives (N-2) times the integral with phi(y)^2 and the CDF difference to power N-3 for N>=3. The x integration then gives -phi(y) for N=3 and minus the integral of phi(x)^2 below y for N=4. Thus the products are respectively 0, -sqrt(3)/pi, -3/pi. N=3 is positive by 9pi>16sqrt(3); N=4 is negative using arcsin(1/3)<pi/8 and 225/256<3/pi. For all N the Gaussian interpolation derivative is the inner product of max and min gradients, an indicator sum for coincidence of their arg-indices; differentiation and smoothing are justified by bounded gradients and Gaussian integrability. Conditional on a proposed coincident pair, the other N-1 pairs are independent, and positive Gaussian correlation bounds each mixed-tail probability by its marginal product. Applying the same opposite-monotonicity inequality to the proposed pair leaves a bound of 1/N^2 (each CDF power has mean 1/N). Summing and integrating proves 0<=g_N<=1/N. With a_N nondecreasing, a_4>1, and 1-pi/4>1/5, every N>=5 is strictly negative. Standard Gaussian tail estimates give a_N~sqrt(2 log N); the centered Gaussian max has variance at most 1 by Gaussian Poincare. Consequently the reset variances have leading term (4D/r)(1-pi/4)log N, the covariance the negative of that, and the correlation tends to -1. Independent replay: python3 /workspace/reproductions/brownian_edges.py uses nested adaptive quadrature on cutoffs 8 and 10, not the frozen grid; it found normalized covariances 0.250000000000, 0.011171104578, -0.122711037218, -0.216030789774, -0.398084893281 at N=2,3,4,5,8. This checks the formulas/signs at those points only; the covariance bound is needed analytically for all N.

## originality

PASS

The supported distinct finding is the strict all-population sign classification, especially negativity for every N>=4, with a uniform Gaussian order-covariance estimate. Credit the prior stationary Gaussian age mixture, leading conditional extreme scaling and marginal order laws. The leading signed-edge covariance and correlation are natural consequences of that scaling plus moment control, not a separate novelty justification. The close Nov. 22 Resultary finding has equivalent small-N signs and a stronger asymptotic for the opposite convention, but expressly leaves the uniform finite-N sign assertion open. The result is not a restatement of an independently reset gas's extrema.

## value

PASS

The cutoff answers a motivated joint fluctuation question in the established solvable reset gas. It pinpoints when common-age variability overtakes the positive conditional Gaussian extreme dependence, though single labelled coordinates are uncorrelated. The uniform bound converts competing effects into a finite cutoff valid at all larger populations and independent of D,r, rather than merely a handful of checked signs or a rephrasing of a marginal extreme law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
