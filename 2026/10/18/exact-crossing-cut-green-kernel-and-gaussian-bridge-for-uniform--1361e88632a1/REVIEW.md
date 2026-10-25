# Independent mathematical audit

## correctness

PASS

Uniform ordered perfect matching: each prescribed edge probability 1/(M-1), pair of disjoint edges probability 1/((M-1)(M-3)); X_k internal edges gives H_k=k-2X_k. For u=min(k,l), v=max(k,l), exact covariance 2u(u-1)(M-v)(M-v-1)/((M-3)(M-1)^2). The scan transition P(close|H_k=h)=h/(M-k) yields Y_{k+1}=((M-k-2)/(M-k))Y_k+innovation, and uncorrelated innovation variances produce positive determinant and tridiagonal inverse at all even M>=4. Martingale rescaling by (M-k)(M-k-1) has predictable variance 2t^2/(1-t)^2 and bounded jumps on compact subintervals; reversal plus Doob near endpoints yields the C[0,1] Gaussian bridge. The Brownian Green kernel double integral is 1/45. Independently enumerated all (M-1)!! matchings at M=4,6,8,10,12 and verified all exact means, covariances, tridiagonal inverses and determinants with Fraction arithmetic. Finite enumeration verifies only these sizes, not the martingale FCLT.

## originality

PASS

Best-of-knowledge new technical specialization assessed after four statement/implication comparisons, primary-source reading and Resultary search. Published general background and covered special consequences are credited; no dominating prior theorem for the final stated result was found in material actually inspected.

## value

PASS

Exact nonscalar finite covariance inverse and determinant for a natural matching scan, plus its nontrivial continuous Gaussian-bridge limit and exact integrated span variance, give reusable stochastic-process invariants; these are not a renaming of a one-chord degree statistic. Conditional independence is not asserted for the discrete non-Gaussian profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
