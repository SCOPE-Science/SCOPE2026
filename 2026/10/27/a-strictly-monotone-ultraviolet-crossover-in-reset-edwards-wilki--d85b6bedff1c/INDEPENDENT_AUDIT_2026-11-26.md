# Independent mathematical audit

## correctness

PASS

At a stationary observation time S=r times the reset age is unit exponential, and the conditional centered Gaussian has variance (D/(πνΛ))h(S/x). The exponential Laplace transform gives the stated mean and frequency-pair covariance, hence the exact standardized fourth moment. For h(z)=sqrt(πz)erf(sqrt(z))+exp(-z)-1, its elasticity decreases strictly: the logarithmic derivative of the ratio A/B in the proof is the difference of the negative means of two tilted laws and is negative by their strictly increasing density ratio. Thus for x₂>x₁, h(S/x₂)/h(S/x₁) is strictly increasing in S. Weighting the exponential law by h(S/x₁)^2 instead of h(S/x₁) strictly increases the expectation of the squared ratio; Jensen then gives strict monotonicity. For the small-x endpoint the difference between h(z) and sqrt(πz)-1 lies in [0,exp(-z)] by the Gaussian tail bound; changing variables S=xz shows its contributions to both raw profile moments are O(x). For the large-x endpoint the exponential moments and the integral Taylor remainder give E[h]=1/x-1/(3x²)+O(x⁻³), E[h²]=2/x²-2/x³+O(x⁻⁴). Both expansions match, and dominated continuity gives the stated open range. Identification uses standardized excess kurtosis, not the unnormalized fourth moment without knowledge of D. The independent age-space quadrature /workspace/review_checks/check_3.py corroborates both asymptotic regimes; it is not the proof of monotonicity.

## originality

PASS

Pass for strict increase and the endpoint corrections of the finite hard-band crossover, not for the reset-age mixture or continuum leading endpoint. Neither the continuum EW law nor the closely related pinned or periodic results inspected covers this theorem.

## value

PASS

The exact hard-band monotonicity resolves identifiability of a physically meaningful cutoff from a dimensionless one-point statistic in the ideal model. The endpoint corrections quantify weakening sensitivity in both limits. This is not automatic for Gaussian modes under common resets, and goes beyond evaluating the already-known continuum limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
