# Independent mathematical audit

## correctness

PASS

Orthogonal invariance makes the sketched columns independent N(0,I_s) and scaled N(0,epsilon^2 I_s). The 2-by-2 Gram smallest-eigenvector projector gives exact H(a/(epsilon^2 c),t) with independent beta-prime a/c and squared direction cosine Beta(1/2,(s-1)/2). For s=3, the Wishart determinant exponent (s-3)/2 vanishes; integrating ordered eigenvalues gives orientation density (cos^2theta+epsilon^-2 sin^2theta)^-2, so tangent-integral quotient is epsilon^2/(1+epsilon^2). For s=2, beta-prime ratio density (1+r)^-2 and H(x,t)=t^2/x+O(x^-2) yield exactly epsilon^2 log(1/epsilon)+O(epsilon^2). For fixed s>=3, exclusion of ratio r<2epsilon^2 costs O(epsilon^s) and dominated convergence supplies E[t^2/r]=1/(s-2). Independent 500,000-sample Gaussian Gram eigendecompositions at epsilon=.08 produced measured mean squared errors s=2:.0175163, s=3:.0063331, s=4:.0033404, s=6:.0016328; exact s=3 theoretical .0063593. Checks are finite and not proofs of limits.

## originality

PASS

Park-Nakatsukasa (2023) studies precisely trailing right singular-vector sketch accuracy but its primary Theorem 3.1 and Corollary 3.1 are multiplicative perturbation/high-probability bounds requiring sketch dimension multiple of column count; neither states an exact s=3 expected squared-angle identity or s=2 borderline logarithmic mean. Takemura-Sheena (2002/2005) studies weak eigenvector limits as the entire covariance spectrum becomes infinitely dispersed, not convergence of squared-angle expectations at the nonuniform-integrability s=2 boundary. Thus the finite Wishart mean and sharp row threshold are not direct corollaries of the cited bounds or weak convergence.

## value

PASS

The smallest allowed full-column-rank sketch undergoes a genuine integrability transition when a single additional Gaussian row is added. The exact finite-epsilon three-row law and s=2 logarithmic penalty give quantitative benchmarks for nullspace and total-least-squares sketch dimension, avoiding misleading extrapolation from weak limiting eigenvector laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
