# Exact positive dependence and slow decorrelation of the largest uniform spacing and Greenwood's statistic

## Finding
Let \(n\ge2\), let \(U_1,\ldots,U_{n-1}\) be independent uniform random variables on \([0,1]\), and let \(G_1,\ldots,G_n\) be the consecutive spacings, including both boundary gaps. Put
\[
M_n=\max_{1\le i\le n}G_i,\qquad Q_n=\sum_{i=1}^{n}G_i^2,
\qquad H_n=\sum_{j=1}^{n}\frac1j,\quad H_n^{(2)}=\sum_{j=1}^{n}\frac1{j^2}.
\]
The finite-sample mixed moment and covariance are exactly
\[
\mathbb E[M_nQ_n]=\frac{2(n+1)H_n+H_n^2+H_n^{(2)}}{n(n+1)(n+2)},
\qquad
\operatorname{Cov}(M_n,Q_n)=\frac{H_n^2+H_n^{(2)}-2H_n}{n(n+1)(n+2)}>0.
\]
The variances and Pearson correlation are
\[
\operatorname{Var}(M_n)=\frac{nH_n^{(2)}-H_n^2}{n^2(n+1)},\qquad
\operatorname{Var}(Q_n)=\frac{4(n-1)}{(n+1)^2(n+2)(n+3)},
\]
\[
\operatorname{Corr}(M_n,Q_n)=
\frac{(H_n^2+H_n^{(2)}-2H_n)\sqrt{(n+1)(n+3)/(n+2)}}{2\sqrt{(nH_n^{(2)}-H_n^2)(n-1)}}.
\]
Consequently,
\[
\operatorname{Cov}(M_n,Q_n)\sim\frac{(\log n)^2}{n^3},\qquad
\operatorname{Corr}(M_n,Q_n)\sim\frac{\sqrt6}{2\pi}\frac{(\log n)^2}{\sqrt n}\longrightarrow0.
\]
The two diagnostics have strictly positive correlation at every finite sample size, yet their linear correlation vanishes asymptotically at an explicit, slow rate. The same formulas apply to the rotation-invariant longest-gap and squared-gap-sum statistics formed by \(n\) independent uniform points on a circle.

## Assumptions and scope
The interior sample is continuous and uniform; there are exactly \(n\) spacings, and their sum is one. Equivalently \((G_1,\ldots,G_n)\sim\operatorname{Dirichlet}(1,\ldots,1)\), with density \((n-1)!\) on its \((n-1)\)-dimensional simplex. We use the unscaled Greenwood statistic \(Q_n\); alternative conventions multiply it by a known deterministic factor. The result is for every integer \(n\ge2\). At \(n=1\), both statistics are constant, so correlation is undefined.

## Proof
For distinct selected coordinates \(G_1,\ldots,G_j\) and \(0\le t\le1/j\), the simplex-volume identity gives
\[
\Pr(G_1>t,\ldots,G_j>t)=(1-jt)^{n-1}.
\]
Conditionally on this event, after subtracting \(t\) from these \(j\) coordinates and dividing all residual coordinates by \(1-jt\), the residual vector is again uniform Dirichlet. Since \(\mathbb E\sum_iG_i^2=2/(n+1)\) and \(\mathbb E G_i=1/n\), the conditional quadratic sum is
\[
\mathbb E[Q_n\mid G_1>t,\ldots,G_j>t]
=jt^2+\frac{2jt(1-jt)}n+\frac{2(1-jt)^2}{n+1}.
\]
By inclusion-exclusion for \(\{M_n>t\}\), and the tail-integral identity \(\mathbb E[M_nQ_n]=\int_0^1\mathbb E[Q_n\mathbf1_{\{M_n>t\}}]\,dt\),
\[
\mathbb E[M_nQ_n]
=\sum_{j=1}^n(-1)^{j-1}\binom nj\int_0^{1/j}(1-jt)^{n-1}
\left[jt^2+\frac{2jt(1-jt)}n+\frac{2(1-jt)^2}{n+1}\right]dt.
\]
The three beta integrals sum to
\[
\frac{2}{n(n+2)j}+\frac{2}{n(n+1)(n+2)j^2}.
\]
The finite alternating-binomial identities
\[
\sum_{j=1}^n(-1)^{j-1}\binom nj\frac1j=H_n,\qquad
\sum_{j=1}^n(-1)^{j-1}\binom nj\frac1{j^2}=\frac{H_n^2+H_n^{(2)}}2
\]
then give the stated mixed moment. For completeness, the first identity follows by integrating \([1-(1-x)^n]/x\) on \((0,1)\). Writing the second sum as \(B_n\), the binomial recursion gives \(B_n-B_{n-1}=H_n/n\) (equivalently integrate \(-(1-x)^{n-1}\log x\)), and summing yields \(B_n=\sum_{k=1}^nH_k/k=(H_n^2+H_n^{(2)})/2\).

The same tail integration without \(Q_n\) gives \(\mathbb E M_n=H_n/n\) and \(\mathbb E M_n^2=(H_n^2+H_n^{(2)})/[n(n+1)]\). Standard Dirichlet monomial integration gives
\[
\mathbb E Q_n=\frac2{n+1},\quad
\mathbb E Q_n^2=\frac{4(n+5)}{(n+1)(n+2)(n+3)},
\]
using \(\mathbb E G_i^4=24/[n(n+1)(n+2)(n+3)]\) and \(\mathbb E G_i^2G_j^2=4/[n(n+1)(n+2)(n+3)]\) for distinct \(i,j\). Subtraction gives the covariance and variance expressions. Strict positivity is immediate from
\[
H_n^2+H_n^{(2)}-2H_n=(H_n-1)^2+(H_n^{(2)}-1)>0\quad(n\ge2).
\]
Finally \(H_n=\log n+\gamma+o(1)\) and \(H_n^{(2)}\to\pi^2/6\) give both asymptotics directly. Rotation invariance of the symmetric pair \((M_n,Q_n)\) supplies the circular interpretation.

## Verification
The standalone script `verify.py` performs exact-fraction checks at every \(2\le n\le80\): the binomial integrals, the harmonic formula, all variance formulas and an independently derived exponential-order-statistic covariance agree. It also directly integrates the polynomial density over the ordered simplex for \(n=2,3\), obtaining \(\mathbb E[M_2Q_2]=25/48\) and \(\mathbb E[M_3Q_3]=349/1080\). For \(n=2\), the covariance equals \(1/48\) and the correlation equals \(\sqrt{15}/4\). These finite checks are corroboration; the proof above establishes the all-\(n\) theorem.

## Relationship to prior work
Shtembari and Caldwell (2020) derive distributions for sums of smallest or largest ordered uniform spacings, including the largest gap. Singh and Misra (2021) analyze overlapping-spacing statistics and their asymptotic testing properties, including the Greenwood statistic. Eller and Shtembari (2021) compare classical spacings tests, discussing both the Greenwood statistic and tests based on largest spacings. Those marginal, summed-order-statistic, and asymptotic testing results do not state the finite-sample mixed moment between the largest spacing and the quadratic sum. The novelty claimed here is this specific mixed dependence law and its explicit asymptotic correlation, not the standard Dirichlet representation, marginal moment identities, or existing testing theory. A separately published exact covariance of the *unnormalized exponential-sample range and sample variance* concerns different statistics: normalization by the random exponential sum prevents that covariance alone from implying the present result.

## Limitations
The formula covers uniform spacings only, not nonuniform or overlapping-order spacings, and it determines mixed second-order dependence rather than a complete joint distribution. Vanishing Pearson correlation does not assert independence. Priority remains provisional because some older general spacing literature and a Greenwood-statistic paper with only partial accessible text could contain related formulas. Independent validation has not been performed.

## References
Shtembari, L. and Caldwell, A., *On the sum of ordered spacings* (2020), arXiv:2008.02048, first posted 2020-08-05, https://arxiv.org/abs/2008.02048.

Singh, R. and Misra, N., *U-statistic based on overlapping sample spacings* (2021), arXiv:2110.10737, first posted 2021-10-20, https://arxiv.org/abs/2110.10737.

Eller, P. and Shtembari, L., *A goodness-of-fit test based on a recursive product of spacings* (2021), arXiv:2111.02252, first posted 2021-11-03, https://arxiv.org/abs/2111.02252.

Arendarczyk, M., Kozubowski, T. J. and Panorska, A. K., *The Greenwood statistic, stochastic dominance, clustering and heavy tails* (2022), DOI:10.1111/sjos.12520, first online 2021-02-17, https://doi.org/10.1111/sjos.12520 (partially accessible for priority comparison).
