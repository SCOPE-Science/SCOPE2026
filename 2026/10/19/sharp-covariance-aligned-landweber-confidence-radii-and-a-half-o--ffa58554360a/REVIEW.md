# Independent mathematical audit

## correctness

PASS

Sum the iteration from zero: x_K=(I−G^K)x†+(I−G^K)B^(-1)Aᵀε. The error is a deterministic source bias plus a Gaussian with covariance σ²B^(-1)(I−G^K)^2. Strict full rank and step bound make that covariance positive definite. After whitening, the deterministic mean is Γ_K^(-1/2)G^KB^νw and the covariance is identity. Its maximum norm equals M times the operator norm of this commuting spectral product, attained at a maximizing eigendirection. The resulting squared length is χ²_n with noncentrality equal to the squared mean norm. A coupling of the Poisson counts in the chi-square mixture gives strict decrease of coverage at each positive finite radius as noncentrality increases; the continuous strictly positive density then makes the proposed quantile necessary as well as sufficient. In the stated two-mode family the small-mode ratio is asymptotic to (2/K)t^(ν−1/2) and the unit-mode ratio is 1/(2^K−1). At equality of the exponents 2/K is larger. For diverging noncentrality the norm differs from the mean norm by at most the standard-normal norm, giving r_*∼Δ_K at a fixed probability level; continuity handles finite limits. Separately the exact Euclidean bias supremum tends to M2^(−K), while the collapsing covariance eigenvalue is asymptotic to σ²K²t/4. Dividing these separately optimized quantities explains the contrasting t^(−1/2) inflation.

## originality

PASS

The fixed-shape Gaussian calibration uses a classical noncentral law, and the nearest same-model primary source gives the exact Gaussian error, an ordinary Euclidean source-bias bound, and a sufficient covariance ellipsoid. The supported distinction is the exact aligned source-ball maximum together with the sharp half-order boundary and a separation example that exposes even the exact Euclidean-bias-based norm inflation. The inspected results do not state or supply that spectral boundary and separation solely by applying their sufficient bounds.

## value

PASS

The exact radius is an implementable replacement for an existing conservative bound in the specified family. The two-mode construction is directly motivated by the competing extremes of the published normwise bound: it demonstrates a smoothness threshold and divergence of that bound when the exact radius can stay bounded, and quantifies the divergence rates when both grow. This shows that loss of alignment, not merely a loose Euclidean bias estimate, can dominate the discrepancy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
