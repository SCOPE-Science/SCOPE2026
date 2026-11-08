# Independent mathematical audit

## correctness

PASS

For partial-injection ranks i,j with disjoint im(alpha) and dom(beta), independent choices yield Z_{n;i,j}=n! binom(n,i)binom(n,j)/(n-i-j)!, for i+j<=n. Summing via Vandermonde gives P(S=s) proportional to binom(2n,n-s)/s!. Ratios to binom(2n,n) are bounded by 1 and converge to 1 at fixed s; dominated convergence proves Poi(1) in total variation. Conditional I given S=s is hypergeometric (2n,n,n-s) with exact mean (n-s)/2 and variance (n-s)(n+s)/(4(2n-1)); Stirling/local CLT yields (I-J)/sqrt(n)->N(0,1/2). Domination by 1/s! in the vacancy mixture yields asymptotic independence. Independent literal composition enumeration verified every rank cell for n=1,2,3 and scalar totals 3,21,229.

## originality

PASS

PASS best-of-knowledge for the two-statistic conditional joint law; scalar sequence and leading total asymptotics explicitly known and excluded from novelty.

## value

PASS

Zero products are intrinsic annihilation relations in finite inverse monoids. The known total count omits the ranks of the factors. The joint law gives a natural full asymptotic profile on different scales: tight Poisson unused vertices and an independent sqrt(n) Gaussian rank imbalance, sharply contrasting with unconditional near-full ranks. This exact asymptotic classification is potentially useful for random product or zero-divisor graph studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
