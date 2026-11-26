# Independent mathematical audit

## correctness

PASS

The two proximals give 10(x−z̄)/11 and (y_i+x_new)/2, and the dual extrapolation is the updated sum plus twice the selected increment. Basis evaluation reproduces the exact Lyapunov slacks. Independent determinant expansion gives the stated positive leading minors for P and H(1/100), with H(0)=I. The affine slack is positive on the closed interval, uniformly by bounding it below by the smaller endpoint minimum eigenvalue. Conditional on the current state the new subset is independent, so the expected quadratic energy contracts uniformly, and norm equivalence controls all four coordinates. The repeated full-batch update on (x,y_1+y_2,z̄) has eigenvalues −2,0,15/22, and the legitimate start has first-coordinate coefficients −25/59 and 16/177 on the two surviving eigenmodes. For k>=1 the latter contributes at most (25/118)2^k in magnitude, so the event of probability q^k proves the reported lower bound. At q=1/4 it is strictly positive, not an exponential lower bound; above it the lower bound grows. The unique saddle is zero from the linear saddle equations.

## originality

PASS

Strong prior conceptual coverage exists for dependence-induced stability changes, including the very same selection law for DIANA. The supported distinct claim is the exact SPDHG instance and its opposed mean-square bounds at fixed blocks, marginals and step sizes, not the general phenomenon or the certificate methods. Bounded statement-level comparisons did not yield an earlier theorem implying this instance.

## value

PASS

At identical work in expectation, blockwise marginals, objective and extrapolated SPDHG steps, serial-like laws give uniform geometric mean-square contraction while independent inclusion is already insufficient and stronger batching drives exponential second-moment growth. This is a practical caution about substituting a batching law without joint analysis, with exact positive and negative certificates rather than a qualitative warning. Its relevance is outside existing sufficient step bounds, not a refutation of those bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
