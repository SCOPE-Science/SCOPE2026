# Independent mathematical audit

## correctness

PASS

The exact one-step density and both asymptotic laws hold for fixed d and beta, averaged over the query and cuts. On each child branch the inverse map from retained fraction and new normalized position to cut and old normalized position has absolute determinant u; the joint density 2u leaves the new normalized query uniform independently of the path history. The increments of the log sides are thus Exp(2) times a uniformly chosen coordinate vector, and their sum is Gamma(N, rate 2). For the differences against the last coordinate, the covariance is (I+11^T)/(2d), with determinant d/(2d)^(d-1), and the covariance with the total is zero. This proves the ordinary joint CLT with independent Gaussian blocks. For the local limit, the direction vectors span: a convolution contains an absolutely continuous component, the characteristic function has modulus strictly below one away from zero, and at large frequency at least one of the directional projections grows proportionally to the frequency norm, so the modulus is bounded away from one there as well. The fixed-range window in difference coordinates is Jordan measurable and splits into d pieces of volume (log beta)^(d-1) according to its minimum. The local Gaussian density at zero then gives the displayed constant. For the conditional CLT the joint directions (1,v_j) span d dimensions, and the centered total has one-step variance 1/4. Summing the uniform fixed-window local limit over O(sqrt N) unit intervals in the total coordinate gives a Riemann sum of the standard normal density, times the same shape constant; the uniform o(N^(-d/2)) errors sum to o(N^(-(d-1)/2)). Rounding the two endpoints costs only two fixed windows. Dividing by the sharp rarity probability establishes the conditional limit. An independent d=2 check is Fourier inversion of (1+t^2/4)^(-N), which gives f_N(0)=Gamma(N-1/2)/(sqrt(pi) Gamma(N)) and rarity equivalent 2 log(beta)/sqrt(pi N). Read RESULT.md lines 23–65, VERIFICATION.md and verify.py; the packaged script was inspected, not run, and its recorded finite checks prove none of the limits. One nonessential scope sentence about zero-probability ties needs a qualification: for d>=3 there is positive probability of two unsplit directions at every finite depth. Ties are null conditional on all directions having been selected and disappear eventually almost surely; the omitted-coordinate probability decays exponentially, and no tie convention or tie exclusion is needed for the Finding.

## originality

PASS

The supported distinction is the exact bounded-aspect-ratio probability and prefactor, and the Gaussian log-volume law conditional on that rare event, for an independent uniform tag in the uniform-cut model. Do not credit the elementary size-bias identity, ordinary Gaussian limit machinery, or qualitative shape failure as novel on their own. No checked statement or direct specialization establishes the sharp local and conditional conclusions together or separately for this model.

## value

PASS

The typical query cell is the volume-weighted object relevant to random partition regression. An exact probability and prefactor for acceptable aspect ratio yield more than a coarse elongation bound, and the conditional limit shows that choosing the geometrically rare regular cells does not change the leading log-volume fluctuations. Both results concern all fixed dimensions and fixed admissible thresholds, not a selected finite numerical configuration. They do not extend here to fixed queries, growing dimension, or whole-tree counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
