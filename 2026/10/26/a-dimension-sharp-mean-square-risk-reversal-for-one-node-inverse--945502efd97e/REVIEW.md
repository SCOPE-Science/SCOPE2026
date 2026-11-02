# Independent mathematical audit

## correctness

PASS

Independently reduced the actual final theorem for real uniform spherical v and A=I-(1-eta)uu^T to W=(u^Tv)^2~Beta(1/2,(n-1)/2), with mean 1/n and variance 2(n-1)/(n^2(n+2)). The endpoint interpolant is unbiased with exact risk delta^2 Var(W)/eta^2; the one-node Lanczos estimator is 1/(1-delta W). Verified the absolutely convergent power-series coefficient formula and d_{j+1}-d_j recurrence by new exact Fraction calculations for n=2,3,4,5,8,20 and j<=12; direct beta quadrature confirms the unique n=3 crossover eta approximately 0.0503804097941. The symbolic recurrence makes d_j<0 for all j>=3,n>=4 (n=4 increment remains negative). At n=3 the increment first negative and then positive, coefficient sequence crosses sign once and the normalized power series is strictly increasing, proving uniqueness beyond numerical work. The n=2 exact ratio is >1. Dominated convergence of eta G to 0 gives the sharp singular-limit ratio (n+2)/(2(n-1)). Finite checks verify finite formulas, not unbounded coefficient signs, for which the printed proof is used.

## originality

PASS

Best-of-knowledge originality of the precise final mathematical claim, not novelty of standard premises or algorithms: The generic stochastic spectral-measure and Gauss-quadrature formulations are equivalent for a one-step Lanczos rule, but earlier papers do not give this specific MSE comparator or its n=3 crossing. Checked relevant primary statements and Resultary semantic results. Failed searches alone are not novelty proof; risks explicitly retained.

## value

PASS

The exact one-probe MSE ordering is nontrivial: a biased nonlinear Gaussian quadrature estimator defeats an unbiased spectral-endpoint interpolant uniformly for n>=4, with a sharp opposite order in dimension two and a one-threshold transition in dimension three. This offers an exact risk benchmark for inverse-trace spectral quadrature beyond generic high-probability approximation bounds. The benchmark is limited to two spectral levels and assumes exact endpoints for the interpolant; it is not a practical advantage for known traces or arbitrary spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
