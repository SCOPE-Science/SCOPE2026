# Mathematical review

## Correctness: PASS
The exact Rayleigh form on polynomial Krylov vectors is a signed spectral moment sum with a single negative rank-one term. The positive-band Gram is strictly positive definite for \(\ell\le q\) by Vandermonde rank. The rank-one inertia criterion gives an exact event, not merely a bound. Chi-square concentration and highest-degree asymptotics yield the three critical regimes, while a degree-\(q\) annihilating polynomial gives certain detection in \(q+1\) Krylov vectors. Normalization cancels in the sign test. The boundary is negligible because the negative-band Gaussian squared weight has a continuous law. Finite simulations verify representative cases but do not prove universal statements.

## Originality: PASS, with historical-priority risk
The 2026 modified Newton–Lanczos paper analyzes modified algorithms and stopping decisions, not an exact distributional sign test for an unmodified Krylov Ritz compression of a single negative spike against fixed positive bands. The full 1999 CWI probabilistic Lanczos paper provides one-sided spectrum bounds derived from Chebyshev, Lanczos and Ritz polynomials; these bounds do not state the exact random Gram downdate event and \(n^{1/(2\ell-1)}\) hierarchy. The accessible 1992 and 1994 abstracts discuss general extreme-eigenvalue approximation bounds, not this specialized distributional phase transition. The 1992 full text was not accessible using authorized channels, and unindexed specialized literature remains a priority risk. Related mathematical-record searches found nearby spectral and Lanczos findings, but no one that implies the stated exact probability law.

## Value: PASS
The object is an early-terminated Krylov negative-curvature diagnostic for indefinite Hessians in Newton-type optimization. A one-dimensional negative eigenspace can be missed by short random-start Lanczos probes even though the Hessian is indefinite. The result supplies quantitative finite-sample error probabilities, explicit transition constants, and an iteration-versus-spike phase hierarchy, terminating at the number of distinct positive spectral levels plus one. This identifies precisely when a small number of Hessian-vector products is probabilistically trustworthy on a natural spectral benchmark, not simply a textbook property of a rank-one matrix.

## Limitations
The model assumes fixed finitely many positive spectral bands, one negative eigenvalue, standard Gaussian initialization, real arithmetic and exact Lanczos. No general spectral-distribution, finite precision, or modified-Newton convergence claim is proved. Independent priority verification remains open.

Self-review: passed. Independent audit: not yet performed.
