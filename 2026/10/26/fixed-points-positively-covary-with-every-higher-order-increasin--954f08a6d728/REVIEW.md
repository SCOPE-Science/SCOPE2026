# Independent mathematical audit

## correctness

PASS

For each k-subset of positions, probability that associated values increase is 1/k!, giving E Z=binom(n,k)/k!. Size-biasing by Z picks independent uniform k-subsets I and V and forces i_j -> v_j. Expected fixed points in forced positions is sum_{j,x}p_{j,x}², and in remaining positions (n-k)/n (zero when k=n), so Cov(F,Z)=E Z sum_j(sum_x p_{j,x}²−1/n). Each rank distribution has squared L2 mass >=1/n; the first rank has support n-k+1, giving strict lower bound (k-1)/(n(n-k+1)), all 3<=k<=n. For fixed k, rescale discrete order-statistic mass to beta-density f_j, sum exact beta integrals via central-binomial convolution to coefficient (4^(k-1)/(2k-1)! - k/(k!)²)n^(k-1)+O_k(n^(k-2)), with k3 coefficient 1/20. Independent full permutation enumeration for n3..7, k3..n validates exact formulas in 15 cases. Does not claim k growing asymptotics or positive association.

## originality

PASS

Qualified: Pinsky’s original increasing-subsequence-biased permutation measure is prior, as is the k=2 inversion connection. The cross moment with fixed-point count for all k>=3, strict positivity, explicit lower bound and fixed-k constant were not identified in inspected relevant primary or indexed sources.

## value

PASS

Gives a closed and strictly positive mixed covariance between two central permutation statistics for every 3<=k<=n, an explicit positive lower bound and the exact fixed-k asymptotic scale. It is a natural new quantitative connection between cycle structure and pattern counts, beyond marginal moment computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
