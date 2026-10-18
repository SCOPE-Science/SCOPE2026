# Independent mathematical audit

## correctness

PASS

The fixed-size channel K=k has maximal-correlation square k(n-m)/(m(n-k)) by Chang-Chen Theorem 1.6. Since K is visible from S and independent of uniform T, the squared conditional-expectation norm of any centered unit-variance f(T) averages over k. A single normalized coordinate indicator is extremal simultaneously for every k, so this average is exact, not just an upper bound. h(k)=k/(n-k) convex and h(k)<=k/(n-m) give the stated p(n-m)/(n-mp) and p bounds, including p=0,1. With m/n->a in (0,1), bounded convergence yields p(1-a)/(1-ap). Theorem 1.5 yields marked correlation max(R(S,T),max r_j); conditional Bernoulli retention bounds r_j by sqrt(p) and constant coefficients attain equality. Independent singular-value norms of full finite joint tables matched for (n,m,p)=(4,2,.3),(5,3,.7),(6,1,.4),(6,4,.2).

## originality

PASS

PASS best-of-knowledge: source Theorem 1.6 is for a fixed deterministic nested k, not observed binomial K; the nontrivial equality for the mixture uses common first-order extremizer, rather than averaging maxima without justification. Source Theorem 1.5 gives general marked-subvector reduction but not R(S,T) for dependent Bernoulli nesting. Its generality alone does not calculate the formula. Earlier Csaki-Fischer hypergeometric spectrum underlies the k-fixed case. The marked sqrt(p) consequence follows readily from source 1.5 once the mixture bound is known; novelty is chiefly the exact random-size subset formula and its matched equality.

## value

PASS

Exact maximal-correlation coefficient is a natural strong-dependence invariant for a canonical uniform-sampling/erasure channel; mixture operator norms cannot generally be obtained by naively averaging fixed-size norms. A compact explicit law and marked consequence are useful benchmarks for stochastic dependence and randomized data release, beyond renaming a fixed-size expression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
