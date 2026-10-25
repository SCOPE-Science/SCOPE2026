# Independent mathematical audit

## correctness

PASS

For k=2,3,4 fixed cells, multinomial masses relative to independent Pois(lambda_n) satisfy an O(1/n) correction A_k(total;lambda_n); the stated truncation s<=L log n and exponential tails justify exchange with polynomially bounded |count differences| moments. Adjacent edge variance/covariance tends to 2lambda-m^2 and h-m^2; disjoint edge covariances multiply by n and tend to -c^2/lambda via the global total constraint. Correct disjoint pair multiplicity yields the displayed V, which independent finite-Poisson truncation recomputed at loads .005,.02,.1,.3,1,3,10,70. The Hoeffding projection g=m+H(A)+H(B)+K(A,B) decomposes V as Var(K)+4[Var(H)-Cov(H,A)^2/lambda] and shows strict positivity because |a-b| is not separable (mixed 0/1 cross-difference -2). Sparse and Gaussian-dense expansions were independently checked for scaling, with the analytic Poisson series and Gaussian kernel providing nonfinite justification.

## originality

PASS

Banić–Elezović Part 2 (arXiv:2610.17046v1, 12 Oct 2026) is a HIGHLY relevant primary paper on EXACTLY the same statistic and variance. Its abstract, Introduction §1 and Synthesis §§7-8 explicitly restrict all asymptotics to FIXED n as N→infty; their Var(D)/N=alpha(n)-beta(n)/N+gamma(n)/N^2+o(N^-2) is not uniform when n,N grow proportionally (authors say accurate for N≫n). Their exact decomposition is acknowledged prior coverage of the general covariance partition; it does not itself give a proved uniform finite-load Poisson coefficient, cancellation of lambda-linear terms, or lambda endpoints. The previous Part1 gives expectations; Comb Test gives finite null law by dynamic programming. The precise new proportional-load regime has genuinely different limits, though any unindexed extension by these authors is a priority risk.

## value

PASS

A sharp analytic variance coefficient under the natural growing-bin proportional-occupancy regime changes how one calibrates total variation of fixed-sample histograms; the non-negligible negative conditioning correction and complete sparse/dense crossover supply useful probability and statistical information not captured by fixed-bin N→infty asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
