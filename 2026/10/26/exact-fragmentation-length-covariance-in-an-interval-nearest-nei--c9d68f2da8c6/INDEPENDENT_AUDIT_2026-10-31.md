# Independent mathematical audit

## correctness

PASS

For n i.i.d. uniform sample points, the undirected distinct-edge nearest-neighbor graph is a chain of adjacent order statistics with an interior gap deleted exactly when it is a strict local maximum. Thus C_n=1+sum_{i=2}^{n-2} A_i, L_n=(W-sum A_i E_i)/S using independent exponential spacings with S their full n+1 sum and W internal sum. Conditioning on relative order, C is independent of W; independence from S of normalized proportions transfers Cov(C,L)=-Cov(C,B)/(n+1). Exact exponential rank probabilities give site covariance 11/27, nearest neighboring peak covariance -11/54 and distance-two covariance 139/5400; all farther disjoint triples are independent. Summing ordered covariances gives 0 for n<=3, -11/135 at n=4, -(139n+405)/(2700(n+1)) for n>=5. First moments n/3 and (7n+15)/(18(n+1)) follow directly. The source correctly distinguishes n=4 from n>=5 and undirected distinct edges from directed multiplicity. Independent rational rank-averaging on n=2..8 (seven cases) reproduced covariance, and the 5-order-statistic combinatorial count was inspected. Infinite n follows from finite-range local-dependence moment summation, not numerical extrapolation.

## originality

PASS

Best-of-knowledge mathematical comparison of the same object, definitions, parameter quantifiers, and implication strength. Foundation and partial coverage are credited explicitly; neither failed searches nor inaccessible full literature alone are represented as novelty proof. The different counting convention matters mathematically: local-max deletion turns undirected edges into a different observable, while C_n is an additional random variable. The source computes five-local-variable mixed moments 413/1800 and 139/5400 that are needed beyond the cited separate observables.

## value

PASS

A canonical stochastic-geometric network statistic is the dependence of fragmentation (component count) on total length of distinct nearest-neighbor edges. The exact finite-n covariance is strictly negative for all n>=4 yet converges to a nonzero constant rather than vanishing; this provides an interpretable, invariant coupling for one-dimensional random geometric graphs distinct from known separate LLNs/variances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
