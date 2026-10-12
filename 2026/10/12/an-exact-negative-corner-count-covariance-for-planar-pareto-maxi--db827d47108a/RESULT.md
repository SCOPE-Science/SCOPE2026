# An exact negative corner-count covariance for planar Pareto maxima

## Finding

Let \(M_n\) be the number of upper-right Pareto maxima in an independent planar sample of size \(n\), and let \(K_n\) count points simultaneously exceeding fixed coordinate thresholds. The dependence has a universal negative sign despite complete independence of \(M_n\) from the two individual coordinate-threshold counts.

For \(n\ge2\), let \(p=\Pr(X>s)\), \(q=\Pr(Y>t)\), both strictly between zero and one. Put \(A_n=\#\{j:X_j>s\}\). Then for every integer \(0\le a\le n\),
\[
\operatorname{Cov}(M_n,K_n\mid A_n=a)
=-a(1-q)\sum_{i=a+1}^{n}\frac{1-(1-q)^{i-1}}{i(i-1)}. \tag{1}
\]
Here an empty sum gives zero, including when \(a=0\). The sign is strictly negative for \(1\le a<n\) and zero for \(a\in\{0,n\}\). Since \(M_n\) is independent of \(A_n\), averaging (1) over \(A_n\sim\operatorname{Bin}(n,p)\) gives
\[
\operatorname{Cov}(M_n,K_n)
=-(1-q)\sum_{a=1}^{n-1}\binom na p^a(1-p)^{n-a}a
\sum_{i=a+1}^{n}\frac{1-(1-q)^{i-1}}{i(i-1)}<0. \tag{2}
\]
For fixed \(0<p,q<1\),
\[
\lim_{n\to\infty}\operatorname{Cov}(M_n,K_n)=-(1-p)(1-q), \tag{3}
\]
and for every \(n\ge2\) the following explicit exponential error bound holds:
\[
0<\operatorname{Cov}(M_n,K_n)+(1-p)(1-q)
\le (1-q)\big((1-p)^n+(1-pq)^n\big). \tag{4}
\]
Equations (1)–(4) constitute one finite-sample and asymptotic covariance law, rather than separate discoveries.

## Assumptions and scope

For each integer \(n\ge2\), observe iid pairs \((X_j,Y_j)\), \(1\le j\le n\). Within each pair, the coordinates are independent and have arbitrary continuous marginal distributions. A point is Pareto maximal when no other sampled point is at least as large in both coordinates; ties occur with probability zero. The thresholds \(s,t\) are deterministic, with exceedance probabilities \(p,q\in(0,1)\) independent of \(n\). The northeast count is \(K_n=\#\{j:X_j>s,\ Y_j>t\}\). Let \(B_n=\#\{j:Y_j>t\}\). Coordinatewise probability-integral transforms show that the law depends on the marginals only through \(p,q\).

## Proof

**Record representation.** Sort the sample by decreasing first coordinate and call the correspondingly ordered second coordinates \(Z_1,\ldots,Z_n\). By independent continuous marginals, the \(Z_i\) remain iid, independent of the sorted first-coordinate values. Write \(R_i=\mathbf1\{Z_i>\max_{j<i}Z_j\}\), with \(R_1=1\). Then \(M_n=\sum_{i=1}^{n}R_i\), \(\Pr(R_i=1)=1/i\), and conditional on \(A_n=a\), \(K_n=\sum_{j=1}^{a}\mathbf1\{Z_j>t\}\). The relative-rank permutation of the second-coordinate sample is independent of its unordered values and of all sorted first-coordinate values. It follows that \(M_n\) is independent of the pair \((A_n,B_n)\), even though it need not be independent of \(K_n\).

**The only nonzero mixed terms.** For each \(i\le a\), the event \(R_i=1\) depends on the relative ranks within the first \(a\) second-coordinate values, so it is independent of their symmetric count \(K_n\). Thus \(\operatorname{Cov}(R_i,K_n\mid A_n=a)=0\) for \(i\le a\). Suppose \(i>a\) and \(j\le a\). Conditional on \(R_i=1\), the identity of the maximum among the first \(i\) observations is fixed to be position \(i\), while their unordered multiset remains unaltered. Consequently
\[
\Pr(Z_j>t\mid R_i=1)
=\frac{iq-[1-(1-q)^i]}{i-1}.
\]
Combining this with \(\Pr(R_i=1)=1/i\) gives
\[
\operatorname{Cov}\big(R_i,\mathbf1\{Z_j>t\}\big)
=-\frac{(1-q)[1-(1-q)^{i-1}]}{i(i-1)}. \tag{5}
\]
The \(Z_i\) sequence is independent of \(A_n\), so conditioning on \(A_n=a\) does not alter (5). Summation over all \(i>a\) and \(j\le a\) proves (1). For \(1\le a<n\) every summand is positive inside the leading negative sign. If \(a=0\), the quadrant count vanishes. If \(a=n\), the quadrant count equals \(B_n\), independent of \(M_n\). The conditional regression mean \(\mathbb E[M_n\mid A_n]\) is the constant harmonic number \(H_n\); the law of total covariance now proves (2).

**Limit and nonasymptotic error.** For integers \(1\le a\le n\), use the exact telescoping identity
\[
 a\sum_{i=a+1}^{n}\frac1{i(i-1)}=1-\frac an.
\]
Writing \(r=1-q\), equation (1) becomes
\[
\operatorname{Cov}(M_n,K_n\mid A_n=a)
=-r(1-a/n)+ra\sum_{i=a+1}^{n}\frac{r^{i-1}}{i(i-1)}. \tag{6}
\]
The residual is nonnegative and at most \(r^{a+1}(1-a/n)\) for \(a\ge1\). For \(a=0\), the actual conditional covariance is zero rather than the first term of (6). Therefore, upon averaging (6) for \(a\ge1\),
\[
0<\operatorname{Cov}(M_n,K_n)+r(1-p)
\le r\Pr(A_n=0)+r\mathbb E[r^{A_n}].
\]
Since \(\Pr(A_n=0)=(1-p)^n\) and \(\mathbb E[r^{A_n}]=(1-pq)^n\), this is (4); the strict inequality follows from the positive event \(A_n=0\). Both bases are strictly smaller than one, so (3) follows.

## Verification

A standalone standard-library script `check_pareto_records.py` verifies the mixed-moment identity by exhaustive enumeration of all \(n!\) relative-rank permutations for each \(2\le n\le7\). In particular it checks every threshold-rank pair \((a,b)\) and compares the covariance to an independent fixed-count hypergeometric formula, giving 199 exact-rational cells. It then checks the binomial-mixture reduction for three rational threshold probabilities, and separately checks sign and bound (4) on a nine-point rational parameter grid for every \(2\le n\le34\). Sample checks yield covariance \(-1/16\) for \(n=2,p=q=1/2\), and \(-15/128\) for \(n=3,p=q=1/2\). Execute `python3 check_pareto_records.py` with Python 3; no third-party packages are required. The infinite-domain theorem is proved above, not by these finite checks.

## Relationship to prior work

Bentley, Kung, Schkolnick and Thompson (1978) analyze the expected number of maximal vectors using random relative orderings, providing a record-permutation foundation. Bai, Hwang, Liang and Tsai (2001) analyze marginal distributions and limit theorems for planar maximal-point counts. Barbour and Xia (2001) provide closely related probabilistic approximation results. These sources frame the maximal-point statistic but the inspected available results do not directly state the covariance between that statistic and a count in a prescribed northeast rectangle, nor its exact conditional sign and limiting constant. The new covariance law is not a claim of new marginal record distributions or of independence of the quadrant count. An uninspected historical joint-process identity could imply the same result.

## Limitations

The coordinate-independence assumption is essential to the iid record-order reduction. No claim is made for dependent coordinates, tied marginal distributions, thresholds with \(p\) or \(q\) varying with sample size, or dimensions above two. The inequalities concern covariance, not stochastic domination or causal effect. Exact historical priority has not been independently certified; broader multivariate record processes may yield related specializations. Verification by finite enumeration does not establish the universal statements independently of the analytic proof.

## References

1. J. L. Bentley, H. T. Kung, M. Schkolnick, and C. D. Thompson. *On the Average Number of Maxima in a Set of Vectors and Applications*. Journal of the ACM 25(4), 536–543 (1978). DOI 10.1145/322092.322095. https://doi.org/10.1145/322092.322095
2. Z.-D. Bai, H.-K. Hwang, W.-Q. Liang, and T.-H. Tsai. *Limit Theorems for the Number of Maxima in Random Samples from Planar Regions*. Electronic Journal of Probability 6, paper 3 (2001); public journal date January 22, 2001. Primary MSC 60D05. DOI 10.1214/EJP.v6-76. https://doi.org/10.1214/EJP.v6-76
3. A. D. Barbour and A. Xia. *The Number of Two-Dimensional Maxima*. Advances in Applied Probability 33, 727–750 (2001). DOI 10.1239/aap/1011994025. https://doi.org/10.1239/aap/1011994025
