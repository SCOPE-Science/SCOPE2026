# One strict covariance switch across positive coupon frequencies in fixed-size group drawings

## Finding
Fix integers \(n\ge2\), \(1\le s<n\), and \(t\ge2\). In each of \(t\) independent rounds sample a uniform \(s\)-element subset from \(n\) different coupons. Write \(U\) for the number of coupons never encountered and \(M_r\) for those encountered in exactly \(r\) rounds, where \(1\le r\le t\). With \(p=s/n\) and \(q=(n-s)/n\), the covariance is
\[
\operatorname{Cov}(U,M_r)=n^2q^t\binom tr p^r q^{t-r}(R_r-1),\qquad
R_r=\left(\frac n{n-1}\right)^{t-1}\left(\frac{n-s-1}{n-s}\right)^{t-r}.
\]
The power with exponent zero is \(1\), even when its base vanishes.

There is an integer \(j\in\{2,\ldots,t\}\) such that \(\operatorname{Cov}(U,M_r)<0\) for every \(1\le r<j\) and \(\operatorname{Cov}(U,M_r)>0\) for every \(j\le r\le t\). No positive multiplicity has zero covariance. For \(s=n-1\), the transition is \(j=t\); for \(s\le n-2\) it is
\[
j=\left\lceil t-\frac{(t-1)\log(n/(n-1))}{\log((n-s)/(n-s-1))}\right\rceil.
\]
For fixed \(n,t,r<t\) the sign is nonincreasing as the packet size \(s\) grows. There are genuine packet-width sign reversals: at \((n,t,r)=(6,5,2)\) the exact covariances for \(s=1\) and \(s=2\) are respectively \(120475/839808>0\) and \(-160256/820125<0\). If \(n\to\infty\), \(s/n\to\rho\in(0,1)\), and \(t=t_n\to\infty\), then \(j/t\to\rho\).

## Assumptions and scope
The model uses independent rounds but samples without replacement *within* each round. The population size \(n\), packet size \(s\), round count \(t\), and positive multiplicity \(r\) are integers satisfying \(n\ge2\), \(1\le s<n\), \(t\ge2\), and \(1\le r\le t\). The zero-frequency class is counted separately as \(U=M_0\); the strict one-switch theorem concerns only positive multiplicities. The endpoint \(s=n-1\) is included. The final asymptotic requires a nondegenerate limiting packet fraction and diverging round count, without any prescribed relation between their growth rates.

## Proof
For an individual coupon, its across-round occurrence indicators are independent Bernoulli variables with parameter \(p\). Therefore
\[
\mathbb EU=nq^t,\qquad \mathbb EM_r=n\binom tr p^rq^{t-r}.
\]
For distinct coupons \(i\) and \(k\), conditioning on coupon \(i\) being absent in every round leaves an independent uniform \(s\)-subset drawn from the other \(n-1\) coupons in each round. Thus coupon \(k\) then appears in exactly \(r\) rounds with probability
\[
\binom tr\left(\frac s{n-1}\right)^r\left(\frac{n-s-1}{n-1}\right)^{t-r}.
\]
A coupon cannot simultaneously have zero and positive frequency. By summing over the \(n(n-1)\) ordered distinct pairs,
\[
\mathbb E[UM_r]=n(n-1)q^t\binom tr\left(\frac s{n-1}\right)^r\left(\frac{n-s-1}{n-1}\right)^{t-r}.
\]
Subtracting the product of the two displayed means yields the asserted covariance, including the edge case \(s=n-1\) with the zero-exponent convention. All factors outside \(R_r-1\) are strictly positive.

Suppose \(s\le n-2\). Then \(R_r>0\) and
\[
\frac{R_{r+1}}{R_r}=\frac{n-s}{n-s-1}>1.
\]
At the left end \(R_1=\bigl(n(n-s-1)/((n-1)(n-s))\bigr)^{t-1}<1\), while \(R_t=(n/(n-1))^{t-1}>1\). Hence the sign crosses once. It never vanishes: an equality \(R_r=1\) with \(r<t\) would imply equality of two reduced positive rational powers
\[
\left(\frac n{n-1}\right)^{t-1}=\left(\frac{n-s}{n-s-1}\right)^{t-r}.
\]
Reduced fractions have equal positive numerators if and only if the numerators match; here this would force \(n^{t-1}=(n-s)^{t-r}\), impossible because \(n>n-s\) and \(t-1\ge t-r\ge1\). Solving \(R_r>1\) for real \(r\) yields exactly the stated ceiling formula. If \(s=n-1\), then \(R_r=0\) for \(r<t\) and \(R_t>1\), so the conclusion remains valid.

For fixed \(n,t,r<t\), the positive factor \(\bigl((n-s-1)/(n-s)\bigr)^{t-r}\) is strictly decreasing in \(s\in\{1,\ldots,n-1\}\). Therefore the sign of \(R_r-1\) can only change from positive to negative as packet size increases. Direct substitution with \((n,t,r)=(6,5,2)\) gives the stated opposite-signed exact values.

For \(s/n\to\rho\in(0,1)\), expand the two logarithms as \(\log(n/(n-1))=1/n+O(n^{-2})\) and \(\log((n-s)/(n-s-1))=1/(n-s)+O(n^{-2})\), uniformly when \(s/n\) stays in a compact subset of \((0,1)\). Their ratio tends to \(1-\rho\). Since the ceiling incurs at most one additive unit, division by \(t\to\infty\) gives \(j/t\to\rho\).

## Verification
An independent enumeration of all sequences of \(t\) uniform \(s\)-subsets for \(58\) feasible triples \((n,s,t)\) inspected \(259368\) ordered packet sequences and checked \(169\) exact-rational covariance equalities. Additional exact-rational evaluations over \(2\le n<35\), all \(1\le s<n\), and \(2\le t<25\) checked strict sign transitions. The two packet-width reversal values were checked as exact fractions. Run \`python3 checker.py\` in a directory containing the supplied checker file. Finite checks are corroboration; the above argument proves every admissible instance.

## Relationship to prior work
Mahmoud and Smythe (2012), Proposition 1 and Section 10, already supply an exact, general covariance formula for all coupon-type counts in a broad random group-size model, including deterministic packet sizes under their modeling assumptions. Their paper explicitly displays a special exact \((0,1)\) covariance; its general covariance may be specialized to recover the finite second moments above. The new point claimed here is **the complete strict one-switch sign structure for all positive frequencies, the absence of arithmetic ties, monotonicity across packet size, and a concrete width-driven sign reversal**, which are not explicitly identified by the prior matrix formula. Betken and Thäle (2022) study normal and Poisson approximation for the unseen count using the same fixed-packet sampling model; their conditional one-coupon observation agrees with our conditioning proof. Schilling and Henze (2021) prove Poisson laws for low-frequency coupon counts but not the finite all-frequency covariance sign classification. A published result on iid one-coupon-at-a-time uniform occupancy exhibits an analogous covariance sign switch; it does not cover the dependent within-packet sampling mechanism.

## Limitations
This result gives pairwise covariance signs, not independence, stochastic ordering or a multivariate limit theorem. The asymptotic transition law assumes \(s/n\to\rho\in(0,1)\); it does not cover vanishing or nearly unit packet fractions. Its elementary finite covariance expression is not claimed to precede or replace Mahmoud and Smythe's general exact formula. The classification has not undergone independent validation. The historical possibility that the complete sign classification was previously extracted from the general covariance formula remains a priority risk.

## References
1. H. M. Mahmoud and R. T. Smythe, *On the joint behavior of types of coupons in generalized coupon collection*, Advances in Applied Probability **44** (2012), 429–451, doi:10.1239/aap/1339878719, particularly Proposition 1 and Section 10.
2. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485v1 (first posted 2022-02-15), later Journal of Applied Probability **60** (2023), 1352–1366, doi:10.1017/jpr.2023.6.
3. J. Schilling and N. Henze, *Two Poisson limit theorems for the coupon collector's problem with group drawings*, Journal of Applied Probability **58** (2021), 966–977, doi:10.1017/jpr.2021.15.
