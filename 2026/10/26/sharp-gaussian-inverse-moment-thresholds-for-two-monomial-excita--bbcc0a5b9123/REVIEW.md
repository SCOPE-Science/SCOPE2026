# Independent mathematical audit

## correctness

PASS

For fixed m,d≥2, write the iid real Gaussian vector as Rω, with R and uniform ω independent. The row Gram determinant is R^(2d+2)F_d(ω)², where F_d is the orthogonal residual of ω^d along ω. Its spherical zeros have finite support/sign patterns: at each zero every nonzero entry satisfies ω_i^(d−1)=a≠0. On the tangent space the derivative of the residual is diagonal with (d−1)a on the support and −a off support (da vanishes tangentially). It is injective into the tangent space; hence the small sublevel neighborhoods have volume comparable to s^(m−1), with exact negative-moment cutoff m−1, and full rank holds almost surely. The largest singular value lies between R and sqrt(R²+R^(2d)); for R≥1 it is also at least m^((1−d)/2)R^d by the second row norm. Therefore S is comparable to R^d F_d for R≤1, and to R F_d for R≥1, while κ is comparable to R^(1−d)/F_d and R^(d−1)/F_d in the two regimes. The χ_m radial density at zero gives the strict integrability thresholds, with divergence at equality and harmless Gaussian tails at infinity. For fixed F_d>0, S/(R^d F_d)→1 as R→0; for R≥1 a sublevel event requires t/F_d≥1/sqrt(2). This and the χ_m small-radius bound dominate the scaled conditional probability by a constant times F_d^(−m/d), integrable off (2,2). The limit via the Gaussian polar density gives the stated unnormalized surface-measure integral. At (2,2) the angular function is |cosθ sinθ(sinθ−cosθ)|; the four coordinate-axis slopes are 1 and the two diagonal slopes are 1/sqrt(2). Its angular cdf is therefore a s+o(s) with a=(4+2sqrt(2))/π. On sqrt(t/η)≤R≤δ the cdf in the conditional radial integral is squeezed by the angular cdf at t/R² and sqrt(1+δ²)t/R²; the radial density is R e^(−R²/2). For fixed small η and δ the omitted low and high radii contribute O(t) (at high radii use the linear angular upper bound); on the annulus the integral of t/R is asymptotic to (t/2)log(1/t). Letting δ,η go to zero fixes the coefficient a/2. Thus the Gaussian setting, exceptional endpoint, pseudoinverse statement and all strict thresholds agree with the frozen claim.

## originality

PASS

The strongest indexed overlap is two-row Gaussian Hankel conditioning, with a different random matrix and a different small-ball mechanism. The inspected primary works on nonlinear excitation, Vandermonde conditioning and general singular-value bounds do not give the two-monomial Gaussian cutoff or the two-regime exact hard-edge law. This is a bounded statement-level comparison, not historical priority.

## value

PASS

An order-one two-monomial excitation block is the simplest setting where almost-sure identifiability can coexist with infinite expected worst-direction noise amplification. The exact sample threshold m>d makes that distinction operational, and the differing condition-number threshold identifies when nearly collinear directions rather than small sample radius control moments. The sharp logarithmic transition and its coefficient resolve the genuine tie case, rather than extrapolating from generic bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
