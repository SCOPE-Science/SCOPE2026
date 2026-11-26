# Independent mathematical audit

## correctness

PASS

The distribution depends only on ranks. Each count is at least one (the global extremum) and at most two (one per row), with mean 2n/(n+1) by the uniform rank in the n+1-cell row/column union. For the mixed moment I checked the three ordered max/min pair types and their multiplicities 2n(n-1), 2n, 2n(n-1). In the disjoint case the two crossed cells force x>y, not merely separate row constraints. For the row-shared integral, writing d=x-y reduces the inner integral to d(1-d)+(1-d)^3/6. For the column-shared and disjoint cases, integrate their polynomials over the full square and subtract the opposite triangle in variables x and 1-y. The opposite-triangle Dirichlet integrals are respectively q_n and 2q_n/(n-1)^2. This recovers the stated integrals and the covariance after subtracting the product of means. The marginals and mixed moment determine all four probabilities. Strict positivity reduces to the stated central-binomial inequality: binom(2n,n) >= binom(2n,2) >= (n+1)(n+2)/2, which is strictly larger than the required right-hand side for n>=2. Stirling's estimate makes the q_n correction exponentially small and division by p_n(1-p_n) gives the correlation coefficient and asymptotic. As a separate bounded check, python3 /workspace/checks/dual_extrema.py exhausts ranks modulo simultaneous column permutations for n=2,3,4,5 (12, 120, 1680, 30240 equally weighted representatives). The exact tables agree, including the zero off-diagonal entries at n=2. The replay does not imply the unchecked infinite cases; the integral proof does.

## originality

PASS

Only the paired, same-array max–min law is credited: the marginals are prior. The strongest inspected broader local-extrema results and exact Resultary entries do not supply this mixed moment or the bivariate law. The closest univariate prior was accessible at abstract level only; possible uninspected coverage remains a limitation, not a priority claim.

## value

PASS

Two rows are the smallest nontrivial family with variable counts of both local optima, while the column size is unbounded. The natural comparison is between opposite equilibria of the same payoff matrix, not independent matrices; even the sign and size of the correlation are not determined by the extremum marginals. The mixed moment resolves that issue for every n and classifies the entire joint law, giving a quantitative dependence scale and a useful finite-size benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
