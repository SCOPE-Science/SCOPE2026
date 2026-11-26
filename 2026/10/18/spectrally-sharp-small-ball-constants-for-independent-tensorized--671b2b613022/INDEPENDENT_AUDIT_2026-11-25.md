# Independent mathematical audit

## correctness

PASS

Rechecked the repaired claim. After SVD the independent scalars are sums of s_k G_k H_k. Conditioning on the G_k gives variance sum s_k²G_k²>0 almost surely and characteristic function product (1+s_k²t²)^(-1/2). For rank at least two this is integrable and gives the stated positive continuous origin density. The joint density is a product, and the Euclidean ball scales by (sqrt(ell)*F/tau)^ell; tail integration then proves the stated moment iff, including divergence at equality. For normalized weights w_k=s_k²/F² the Fourier integral for F f_M(0) is minimized pointwise at equal w_k by strict concavity of log(1+w_k t²); equality of the integral forces the flat spectrum. The beta integral gives the gamma ratio. A second check uses the conditional normal density: F f_M(0)=(2π)^(-1/2) E[(sum w_k G_k²)^(-1/2)], finite for rank≥2 by the bound using min(w_k)*chi-square_r. Strict Jensen gives the dense comparison since this variance is nonconstant with mean one. At flat rank the variance is chi-square_r/r and the negative half moment gives the same gamma ratio and limit. At r=ell=2 the scalar law for M=I_2 is Laplace and the leading constants are π and 1. The rank-one comparison has normalized density (log(1/|x|)+O(1))/π, and coordinatewise 1+|log|y_j|| bound after rescaling to a unit ball gives the product logarithm and exact coefficient. The fixed independent separable-residual normalization cancels the scalar L² factor.

## originality

PASS

The repaired distinct scope is the exact fixed-spectrum, rank-at-least-two leading law for independent bilinear observations, its sharp spectrum-constrained comparison and its moment implications. The sources checked provide scalar rate bounds, crossed-block results, or the already credited rank-one radial argument. None of those statements or proofs supplies the rank-at-least-two origin-density coefficient and spectral extremum for this statistic. No separate originality is assigned to rank one or to the qualitative disappearance of the logarithm.

## value

PASS

The leading coefficient of this validation failure probability is a natural quantity not determined by rank-only bounds. The sharp spectrum-constrained optimum and its strict dense-probe gap at each finite rank quantify the cost of tensorization even when the logarithmic loss is absent. The law also yields exact probe-count thresholds for finite inverse moments. The repair preserves those conclusions and does not claim convergence of an approximation fitted on the probes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
