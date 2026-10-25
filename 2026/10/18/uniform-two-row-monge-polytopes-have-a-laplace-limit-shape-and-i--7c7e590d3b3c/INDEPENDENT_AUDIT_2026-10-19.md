# Independent mathematical audit

## correctness

PASS

Normalize 2n iid Exp(1) coordinates by their sum to obtain the intrinsic-uniform simplex; column differences are iid continuous Laplace and sorting full pairs enforces the Monge order, with equal n! arrangement probabilities. The bijection U=W+D_+, V=W+(-D)_+ has Jacobian one and factorization Exp(2) for W independent of Laplace D. Sorting preserves original gamma row sums, giving Beta(n,n) exactly. Empirical-L1 quantile convergence for Laplace D and uniform marked LLN for W give full cumulative A,B limits, with A(1/2)=1/8, B(1/2)=3/8. The exact joint CDF of largest D and negative smallest D tends to product independent Gumbels; denominator S/(2n)=1+O_P(n^-1/2) does not change centered extremes. Independent finite sampling for n=100,2000 corroborated cumulative curves only; infinite a.s. and weak limits follow analytically.

## originality

PASS

Erickson–Kretschmann gives the same body and its 1/n! relative volume; conditioning/sorting provides the law but its explicit Laplace-W independence, whole cumulative mass shape and joint extremes are not stated by that cited theorem. The noisy Monge estimation literature concerns a different probability model.

## value

PASS

Provides a complete natural intrinsic-uniform random-point model for a standard Monge polytope and identifies deterministic row asymmetry and asymptotically independent edge extremes; this answers distributional questions not captured by volume or polytope face counts. Exact sampler is useful for geometric sampling and simulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
