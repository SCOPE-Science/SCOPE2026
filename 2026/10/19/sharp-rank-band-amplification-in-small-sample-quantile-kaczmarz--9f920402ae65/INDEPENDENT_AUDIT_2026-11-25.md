# Independent mathematical audit

## correctness

PASS

For rank i, count subsets containing i with p−1 lower and k−p higher ranks. On adjacent positive weights, the ratio is above 1 iff (p−1)(m−i)>i(k−p); the two sides cross at most once, so the c largest weights can be chosen consecutively, including plateaux or zero tails. For m=k³ a collision in k independent lattice uniforms has probability at most k(k−1)/(2m). Conditioning on no collision gives the desired sample, while the binomial tail for the independent lower median gives CDF limit Φ(2z) for √k(J/m−1/2). Uniform CDF convergence bounds every half-open band of scaled width c√k/m by the corresponding normal mass up to o(1). Centered bands attain the limit, including zero width by continuity and diverging width by tightness. In the construction, every absolute residual is i/(m+1), the good rows have two linearly independent representatives, and the unit-row projection has squared error 1−r_i² for a good row and (1+r_i)² for a bad row. The selected r_i tends to 1/2 and the bad-row premium tends uniformly on the central band to 3/2, giving the stated expectation and the strict increase threshold Φ⁻¹(7/12).

## originality

PASS

The established distinct claim is the sharp contamination envelope and its realization as an expected-error obstruction for the particular small-sample rank-selected update. The algorithm itself, order-statistic law and Gaussian median limit are not new. The strongest inspected related result on hypergeometric median corruption does not imply the rank-band profile and its realization.

## value

PASS

The exact scale c/m≈k⁻¹ᐟ² separates negligible from potentially dominant corrupt-row selection for a published algorithmic choice. The row-normalized witness translates rank bias into a quantitative expected-error increase, even for a vanishing corruption fraction; this is a useful one-step obstruction to a uniform contraction guarantee, not just a restatement of the median CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
