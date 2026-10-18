# Independent mathematical audit

## correctness

PASS

For the exact rational C_alpha, direct differentiation gives grounded margins and mixed density N_alpha/[(1-alpha)(1-alpha uv)^3]. For alpha=-t<0, N=(1+tu)(1+tv)+t[(1+tuv)^3-(1-u)(1-v)]>0. For 0<=alpha<=1/2, N is bounded below by a separately affine polynomial whose four corners are nonnegative. For 1/2<alpha<1 the density at (0,1) is negative; alpha=1 is undefined and alpha>1 has an interior pole. This proves the iff admissible interval alpha<=1/2, including alpha=1/2. On alpha=-t, the Spearman loss L=12t/(1+t)*integral(w/(1+tuv)) has derivative 12(A-t^2 B)/(1+t)^2. H=t^2B/A is strictly increasing because H'/H=2/t-2E_B[q/(1+tq)]+2E_A[q/(1+tq)]>0; H(2)<1 by strictly negative covariance of q with (1+2q)^-2. Since L tends to zero at t=0 and infinity, there is exactly one maximum at t*>2, and each intermediate negative Spearman value has exactly two negative parameters. Uniform convergence to independence follows from the pointwise <=1/(1+t) estimate. Independent symbolic identities and Gaussian quadrature yield t*=2.33900178182 and rho=-0.15564754516; numerical digits do not prove uniqueness.

## originality

PASS

The 2026 originating paper chooses [-2,1/2] and explicitly says the lower cutoff preserves uniqueness of dependence/concordance values. Its Appendix A obtains alpha<=1/2 as a necessary upper bound and numerically verifies the selected finite interval; it does not establish copula validity for all negative alpha, the unique negative Spearman fold below -2, or exact two-to-one rank-correlation calibration. The new maximum-domain classification and fold survive statement-level comparison, not merely parameter-name mismatch.

## value

PASS

Correct identification of the maximal valid parameter domain is required before estimating or calibrating this explicitly proposed bivariate family. Locating a unique Spearman fold quantifies a structural identifiability defect: two distinct copulas have the same negative Spearman rank correlation, and very negative parameters approach independence. The numerical enhancement of the most negative correlation over alpha=-2 is small (~7.2e-4) and is not the sole significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
