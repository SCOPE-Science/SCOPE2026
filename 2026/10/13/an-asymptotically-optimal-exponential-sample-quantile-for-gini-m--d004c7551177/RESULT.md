# An asymptotically optimal exponential-sample quantile for Gini mean-difference correlation

## Finding

Let \(X_1,\ldots,X_n\) be independent and identically distributed exponential observations with common rate \(\lambda>0\), where \(n\ge2\). Write \(X_{(1)}\le\cdots\le X_{(n)}\), and define the **unnormalized sample Gini mean difference**
\[
G_n=\binom n2^{-1}\sum_{1\le i<j\le n}|X_i-X_j|.
\]
For all integers \(1\le k\le n\), put
\[
B_{n,k}=n(H_n-H_{n-k})-k,\qquad
V_{n,k}=H_n^{(2)}-H_{n-k}^{(2)},
\]
where \(H_j=\sum_{r=1}^j1/r\), \(H_j^{(2)}=\sum_{r=1}^j1/r^2\), and \(H_0=H_0^{(2)}=0\). Then
\[
\operatorname{Cov}(G_n,X_{(k)})=
\frac{2B_{n,k}}{n(n-1)\lambda^2},\quad
\operatorname{Var}(G_n)=\frac{2(2n-1)}{3n(n-1)\lambda^2},\quad
\operatorname{Var}(X_{(k)})=\frac{V_{n,k}}{\lambda^2},
\]
and hence
\[
\operatorname{Corr}(G_n,X_{(k)})=
\sqrt{\frac{6}{n(n-1)(2n-1)}}\,
\frac{B_{n,k}}{\sqrt{V_{n,k}}}.
\tag{1}
\]
It vanishes for \(k=1\) and is positive for every \(2\le k\le n\). Whenever \(k/n\to p\in(0,1)\), the correlation converges to
\[
\rho(p)=\sqrt3[-p-\log(1-p)]\sqrt{\frac{1-p}{p}}.
\tag{2}
\]
There is a **unique maximizer** \(p_*\in(0,1)\) of this limiting correlation; it is the unique interior solution to
\[
-\log(1-p_*)=p_*+2p_*^2,
\qquad p_*=0.930056414449\ldots.
\tag{3}
\]
Its value is
\[
\rho(p_*)=2\sqrt3\,p_*^{3/2}\sqrt{1-p_*}
=0.821728798370\ldots.
\tag{4}
\]
For **every choice** of finite-sample maximizer \(k_n\in\arg\max_{1\le k\le n}\operatorname{Corr}(G_n,X_{(k)})\),
\[
\frac{k_n}{n}\longrightarrow p_*,\qquad
\max_{1\le k\le n}\operatorname{Corr}(G_n,X_{(k)})
\longrightarrow\rho(p_*).
\tag{5}
\]
Thus asymptotically the empirical quantile with rank near \(93.006\%\) has the strongest **Pearson correlation** with the sample Gini mean difference among individual sample order statistics.

## Assumptions and scope

The observations are independent and have the same continuous exponential distribution; their common rate \(\lambda\) is arbitrary and cancels from the correlations. No censoring, weighting, truncation, fitting of model parameters, or additional normalization by the sample mean is applied. The sample Gini **mean difference**, which has the units of the observations, differs from the usual dimensionless sample Gini **coefficient**. Each rank \(k\) is an integer from \(1\) through \(n\). Statements (2)–(5) concern a proportionally growing rank and a finite-sample rank maximizer, not equality of the finite maximizer with a rounded constant for every \(n\).

## Proof

Define \(X_{(0)}=0\) and the ordered gaps \(Y_j=X_{(j)}-X_{(j-1)}\) for \(1\le j\le n\). The exponential lack-of-memory property, equivalently the order-statistic spacing density, gives mutually independent \(Y_j\) of rates \(\lambda(n-j+1)\). In particular \(\operatorname{Var}(Y_j)=\lambda^{-2}(n-j+1)^{-2}\). Rewriting every absolute difference as a sum of these gaps gives exactly
\[
X_{(k)}=\sum_{j=1}^kY_j,\qquad
G_n=\frac{2}{n(n-1)}\sum_{j=2}^n(j-1)(n-j+1)Y_j.
\tag{6}
\]
Indeed the gap \(Y_j\) appears in precisely \((j-1)(n-j+1)\) unordered differences. Independence in (6) yields
\[
\operatorname{Cov}(G_n,X_{(k)})
=\frac{2}{n(n-1)\lambda^2}\sum_{j=2}^k\frac{j-1}{n-j+1}.
\]
Since \((j-1)/(n-j+1)=n/(n-j+1)-1\), the sum is \(B_{n,k}\), including its zero value for \(k=1\). The other variance is \(\lambda^{-2}V_{n,k}\), while
\[
\operatorname{Var}(G_n)=\frac{4}{n^2(n-1)^2\lambda^2}\sum_{j=1}^{n-1}j^2
=\frac{2(2n-1)}{3n(n-1)\lambda^2}.
\]
This proves (1) exactly for every admitted integer and every positive rate.

For a sequence \(k/n\to p\in(0,1)\), harmonic-sum comparison or uniform Riemann sums on compact subintervals of \((0,1)\) show
\[
\frac{B_{n,k}}n\to-p-\log(1-p),\qquad
nV_{n,k}\to\frac{p}{1-p}.
\]
Since \(\sqrt{6/[n(n-1)(2n-1)]}\sim\sqrt3/n^{3/2}\), equation (2) follows. Write \(g(p)=-p-\log(1-p)>0\). By differentiation, the sign of \(\rho'(p)\) agrees with that of \(2p^2-g(p)\). Furthermore
\[
\frac{g(p)}{p^2}=\sum_{r=2}^{\infty}\frac{p^{r-2}}r
\]
is strictly increasing from \(1/2\) to infinity as \(p\) ranges from zero to one. Therefore \(g(p)=2p^2\) has exactly one interior root. The derivative is positive before it, negative after it, and \(\rho(p)\to0\) at both endpoints. This proves (3)–(4) and unique global optimality.

It remains to justify optimizing over **all ranks**, rather than exchanging a pointwise limit with a maximum. Set \(a_n=\sqrt{6/[n(n-1)(2n-1)]}=O(n^{-3/2})\). For \(1\le k\le n/2\),
\[
0\le B_{n,k}\le\frac{k^2}{n},\qquad V_{n,k}\ge\frac{k}{n^2},
\]
and thus equation (1) bounds the correlation by \(O((k/n)^{3/2})\), uniformly in this range. In the other tail put \(h=n-k+1\le n/2\); harmonic-integral comparisons give
\[
B_{n,k}\le n[1+\log(n/h)],\qquad
V_{n,k}\ge\frac1{2h},
\]
so the correlation is bounded uniformly by
\[
O\left(\sqrt{\frac hn}\,[1+\log(n/h)]\right).
\]
Both bounds tend to zero on sequences of ranks with \(k/n\to0\) or \(k/n\to1\), respectively. Since the interior maximum in (2) is strictly positive, global maximizing ranks cannot accumulate at either endpoint. On every closed interior rank-proportion interval the harmonic approximations are uniform, so any subsequential limit of \(k_n/n\) must maximize \(\rho\). Uniqueness forces the limit \(p_*\) and proves both assertions (5).

## Verification

The standalone standard-library Python file `verify_order_gini.py` checks (1) via a second representation: an explicit covariance matrix for the original order statistics, combined with the linear-order-statistic representation of the pairwise Gini mean difference. Exact rational comparisons cover all \(1\le k\le n\) for \(2\le n\le45\), totaling 1,034 covariance cells and the corresponding variance identities. Additional checks evaluate the pairwise-difference and gap forms on actual simulated samples, compare theory and independently generated empirical correlations, examine sample maximizing ranks through \(n=1000\), and numerically bracket (3). Run `python3 verify_order_gini.py` in a Python 3 installation; it requires only the standard library. The analytic argument establishes all infinite-parameter and asymptotic statements; computational tests alone do not do so.

## Relationship to prior work

Vellaisamy and Zeleke [1] give the exponential order-statistic spacing law and its marginal order-statistic consequences, but their inspected work concerns transforms, the Basel problem and combinatorial identities, not the mixed Gini/order-statistic correlation or its maximizing rank. Hosking's L-moment framework [2] identifies the Gini mean difference as a standard linear-order-statistic scale statistic and provides a broad setting in which mixed moments might be recovered by combining known order-statistic covariances; his complete paper was not accessible for a decisive all-results comparison. Gail and Gastwirth [3] study the **scale-free normalized Gini coefficient** as a goodness-of-fit statistic, rather than the unnormalized Gini mean difference used here. Pushkarna, Saran and Tiwari [4] derive population inequality indices for Marshall–Olkin exponentials and recurrence relations for censored order-statistic moments; their inspected full paper has neither the sample Gini mean-difference covariance curve nor its optimizing quantile. The 2026 study [5] treats marginal inequality-index estimation rather than this joint rank optimization. The exact covariance is elementary given the classical spacings; the asserted distinction is the explicit finite rank profile and the sharp, all-ranks limiting optimization in (3)–(5).

## Limitations

No independent mathematical audit or historical-priority certification has been performed. Historical joint L-statistic/order-statistic treatments could contain equivalent formulas or imply this quantile optimizer indirectly, particularly [2] and [3], for which full texts were inaccessible. The result applies only to independent common-rate exponential samples and the unnormalized Gini mean difference. It does not identify a uniquely maximizing finite rank for all sample sizes, guarantee optimality under another dependence criterion, imply optimal prediction beyond Pearson correlation, or address the ordinary normalized Gini coefficient.

## References

[1] P. Vellaisamy and A. Zeleke, *Exponential Order Statistics, the Basel problem and Combinatorial Identities*, arXiv:1604.02644, first submitted 10 April 2016; later published as *Exponential order statistics and some combinatorial identities*, DOI: 10.1080/03610926.2018.1508710. https://arxiv.org/abs/1604.02644

[2] J. R. M. Hosking, *L-Moments: Analysis and Estimation of Distributions Using Linear Combinations of Order Statistics*, Journal of the Royal Statistical Society B **52** (1990), 105–124. https://doi.org/10.1111/j.2517-6161.1990.tb01775.x

[3] M. H. Gail and J. L. Gastwirth, *A Scale-Free Goodness-Of-Fit Test for the Exponential Distribution Based on the Gini Statistic*, Journal of the Royal Statistical Society B **40** (1978), 350–357. https://doi.org/10.1111/j.2517-6161.1978.tb01048.x

[4] N. Pushkarna, J. Saran and R. Tiwari, *Bonferroni and Gini Indices and Recurrence Relations for Moments of Progressive Type-II Right Censored Order Statistics from Marshall-Olkin Exponential Distribution*, Journal of Statistical Theory and Applications **12** (2013), 306–320. https://doi.org/10.2991/jsta.2013.12.3.7

[5] R. Vila and H. Saulo, *Bias analysis of a linear order-statistic inequality index estimator: Unbiasedness under gamma populations*, arXiv:2602.14861. https://arxiv.org/abs/2602.14861
