# Scientific review: profile-sensitive two-circle Gaussian Jensen covariance

## Correctness — PASS

The statement fixes the polynomial ensemble, its variance profile and the order of limits. Formula (5) is exact: a Laguerre-series identity for the logarithm of correlated circular complex Gaussians reduces angular covariance to one dilogarithm integral. Uniform coefficient variation yields the required \(O((1+|x|)^{-2})\) majorant after microscopic angular scaling, justifying compact-uniform convergence. Strict convexity of \(\log\Phi_w\) holds because every exponential tilt of a strictly positive profile has positive variance. The large-separation coefficient follows from both endpoint Laplace asymptotics, a uniformly valid small-argument dilogarithm expansion, and Fourier Plancherel. The reversal formula follows by change of variables. A standalone numerical checker passed 34 corroborative assertions; it is not an infinite proof.

## Originality — PASS (self-review)

Kiro–Nishry's full accessible article (Sections 1, 3 and Appendix) supplies a general Gaussian zero-fluctuation setting and an earlier dilogarithm formula. Buckley–Nishry's inspected full text concerns hyperbolic Gaussian analytic-function zeros and limiting laws. These do not give the present two-radius circular Jensen-mean covariance for arbitrary strictly positive profiles or its strict fixed-midpoint monotonicity and sharp endpoint/bulk separation constant. An earlier unweighted one-circle Gaussian Mahler variance is a specialization, not coverage of the two-variable result. Targeted searches for concentric-circle logarithmic covariance, finite Gaussian Kac profiles, and Jensen potential aliases did not identify a decisive covering result. The novelty conclusion has an explicit residual risk: broader general-purpose Gaussian log-field theorems or alternate Jensen covariance literature might encode an equivalent formula without the inspected wording. No claim of independently certified historical priority is made.

## Value — PASS

The variance of one circular logarithmic mean cannot determine covariance of two means at distinct radii. The new two-radius kernel resolves the natural \(1/n\) radial observation window for Gaussian polynomial logarithmic potentials; strict decorrelation at fixed logarithmic midpoint quantifies how measurements separate, and the sharp coefficient identifies sensitivity to both endpoint coefficient variances and their bulk squared mass. The result applies to an entire open class of positive smooth variance profiles, not an arbitrary numerical slice, and exposes a concrete exponential law unavailable from a single-radius variance asymptotic.

## Boundaries and priority risk

The profile remains strictly positive and \(C^1\); endpoint-vanishing weights and non-Gaussian coefficients are not included. The large-distance asymptotic concerns the already obtained limiting kernel. There is no central limit, zero-count covariance, or independence conclusion. Mathematical priority is not independently established and potential reformulation through general Gaussian potential covariances remains a risk.

Self-review: passed. Independent audit: not yet performed.
