# Independent mathematical audit

## correctness

PASS

For uniform π∈S_n, the unordered prefix set S_i of i values is independent of their relative ranks, including the event R_i that position i is the prefix maximum. If j<i, conditional on R_i, π_j is uniform among S_i except its maximum, which necessarily exceeds j, so conditional P(E_j)= [i(n−j)/n−1]/(i−1). Multiplying its difference from (n−j)/n by P(R_i)=1/i gives Cov(R_i,E_j)=−j/[ni(i−1)]. On j=i, P(max S_i≤i)=1/C(n,i), giving diagonal 1/n−1/[iC(n,i)]; for j>i, π_j is independent of the earlier relative prefix rank, so covariance zero; R1 is constant. Summation yields row 1/(2n)−1/[iC(n,i)] (i≥2); it is positive at interior i=2..n−1 for n≥4 and negative final. Summing rows yields Cov(R,X)=(n−1)/(2n)−(1/n)Σ_{k=1}^{n−1}1/C(n−1,k). The binomial reciprocal bound for n≥5 proves strictly positive, while n=2,3,4 give −1/4,−1/6,−1/24; expansion yields 1/2−3/(2n)+O(n^(−2)). Standard independent record ranks and Eulerian X variance yield Corr∼sqrt(3)/sqrt(n log n). Independent literal enumeration of every π for n=2..7 reproduced every matrix entry and global totals −1/4,−1/6,−1/24,1/15,3/20,89/420. Finite checks corroborate an all-n conditional-subset proof.

## originality

PASS

Ehrenborg--Steingrímsson provide prescribed excedance-set enumeration; Gnedin provides the initial-rank record representation; Brändén--Claesson express both kinds of statistics through mesh-pattern expansions. These are substantial antecedents, but none of their materially inspected theorems supplies the evaluated n×n mixed covariance kernel and the sharp aggregate sign transition n=5. General bivariate Stirling/Eulerian or mesh-pattern generating functions could encode it implicitly; the judgment is best-of-knowledge and qualified. Resultary nearest records concern fixed-point/descent dependence and inversion precision, not the same event pair.

## value

PASS

Position-resolved cross-covariance is a natural joint statistic of two canonical permutation observables, not determined by either marginal distribution. Its entire upper-zero/lower-negative/same-position-positive pattern, exact row sums and sharp sign reversal of the aggregate covariance at n=5 provide an all-n structural dependence classification. The positive finite covariance limit but vanishing correlation quantifies an instructive asymptotic contrast. This is a complete exact fact rather than a tiny-instance recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
