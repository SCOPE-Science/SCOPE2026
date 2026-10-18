# Independent mathematical audit

## correctness

PASS

For uniform partitions of [n], n>=1, and 1<=r<=n, marking an r-block gives a bijection between weighted pairs (partition,marked block) and (chosen r-subset,partition of complement). Thus E[X_{n,r}f(K_n)] = C(n,r)B_{n-r}/B_n * E f(1+K_{n-r}); f=1 and f(k)=k yield E X=C(n,r)B_{n-r}/B_n and Cov(K_n,X_{n,r})=EX*(1+q_{n-r}-q_n), using E K_m=q_m-1 including m=0. Bell numbers are moments of Poisson(1) (Dobinski), so strict Cauchy-Schwarz B_m^2<B_{m-1}B_{m+1} for m>=1 makes q_m strictly increase; c_n(r) strictly decreases, and at r=n equals 2-q_n<0 for n>=2 (n=1 has c=0). This supplies a unique nonpositive-first threshold t_n and strictly negative entries above it. With alpha_n e^{alpha_n}=n+1, the Bell-ratio asymptotic q_m=m/alpha_m+O(1/alpha_m) has error o(1) for m near n; derivative F'(x)=1/(1+alpha_x)+1/[alpha_x(x+1)(1+alpha_x)] and r=O(alpha_n) imply q_n-q_{n-r}=r/(alpha_n+1)+o(1) uniformly in that window. Monotonicity extends boundary signs beyond the window, t_n/(alpha_n+1)->1. Independently checked exact Bell thresholds n=2,3,5,10,20 and growth of q_m using integer recurrence. Read checker source: RGS finite enumeration n<=9 and exact Bell ratios through n=300 corroborate, do not replace the asymptotic proof. Boundary cases n=1 and r=n accounted for.

## originality

PASS

Best-of-knowledge PASS for the combined exact size-biased Palm identity, explicit mixed covariance, unique sign switch and sharp Lambert-W location. Classical Bell generating-function machinery implies computability of mixed moments, but neither inspected Chern theorem nor its singleton examples themselves states the sign-transition theorem.

## value

PASS

A complete qualitative phase diagram for a natural dependence statistic: counts of small blocks correlate positively with total block count, while counts of larger blocks correlate negatively. The unique exact finite threshold and its Lambert-W asymptotic resolve a meaningful probabilistic boundary, beyond the familiar separate means and elementary block marking. The Palm identity is useful for arbitrary observables f, not just covariance; neither random-partition normality nor a first moment alone reveals a sign change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
