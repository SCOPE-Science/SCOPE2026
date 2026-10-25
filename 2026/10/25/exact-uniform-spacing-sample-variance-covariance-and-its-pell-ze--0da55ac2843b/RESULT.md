# Exact uniform-spacing/sample-variance covariance and its Pell-zero ranks

## Finding
For every integer \(n\ge2\), let \(U_1,\ldots,U_n\) be independent uniform observations on \((0,1)\). Write \(U_{(0)}=0<U_{(1)}<\cdots<U_{(n)}<U_{(n+1)}=1\), and define all \(n+1\) spacings \(G_{n,r}=U_{(r+1)}-U_{(r)}\), \(0\le r\le n\). Let \(S_n^2=(n-1)^{-1}\sum_{i=1}^n(U_i-\overline U)^2\) be the unbiased sample variance. The entire mixed covariance profile is
\[
\operatorname{Cov}(G_{n,r},S_n^2)=
\frac{6r(n-r)-n(n-1)}{6n(n-1)(n+1)(n+3)}
\qquad(0\le r\le n).
\]
Thus the two endpoint gaps have strictly negative covariance for every \(n\ge2\), whereas central gaps have positive covariance. For \(2\le n\le5\), all internal gaps have positive covariance; for \(n=6\), the two nearest-end internal gaps have zero covariance; for \(n\ge7\), the nearest-end internal gaps have negative covariance. The exact finite-sample sign at every index is the sign of \(6r(n-r)-n(n-1)\).

There are infinitely many exact zero-covariance internal gaps, with **all** zero pairs classified as follows. Let integers \(x_k,y_k\) be defined by
\[
x_k+y_k\sqrt3=(2+\sqrt3)^k,\qquad k=2,3,\ldots.
\]
Then \(\operatorname{Cov}(G_{n,r},S_n^2)=0\) if and only if
\[
n=x_k-1,\qquad r=\frac{x_k-1\pm y_k}{2}
\]
for some integer \(k\ge2\). The first zero pairs are \((n,r)=(6,1),(6,5),(25,5),(25,20),(96,20),(96,76)\). This is a statement about uncorrelatedness, not independence.

If \(r_n/n\to u\in[0,1]\), then
\[
n^2\operatorname{Cov}(G_{n,r_n},S_n^2)
\longrightarrow u(1-u)-\frac16.
\]
Consequently the asymptotic sign boundary occurs at the two fractions \(\tfrac12(1\pm1/\sqrt3)\), approximately \(0.211325\) and \(0.788675\).

## Assumptions and scope
The observations are independent and exactly uniform on \((0,1)\); ties occur with probability zero. The sample size satisfies \(n\ge2\). Both boundary gaps between the observation range and the endpoints of \([0,1]\) are included, so the total number of gaps is \(n+1\). The standard divisor \(n-1\) is used for sample variance; for variance computed with divisor \(n\), multiply every displayed covariance by \((n-1)/n\). All formulas are exact in the stated finite domain.

## Proof
Set \(M=n+1\). The vector \((G_{n,0},\ldots,G_{n,n})\) is Dirichlet with all \(M\) parameters equal to one. For \(1\le a<b\le n\), let \(D_{a,b}=U_{(b)}-U_{(a)}=\sum_{t=a}^{b-1}G_{n,t}\), let \(\ell=b-a\), and write \(I_{a,b,r}=\mathbf 1\{a\le r<b\}\). The Dirichlet moment formula \(\mathbb E\prod_jG_{n,j}^{e_j}=\prod_j e_j!/[M(M+1)\cdots(M+\sum_j e_j-1)]\) gives
\[
\mathbb E D_{a,b}^2=\frac{\ell(\ell+1)}{M(M+1)},\quad
\mathbb E[G_{n,r}D_{a,b}^2]=
\frac{(\ell+1)(\ell+2I_{a,b,r})}{M(M+1)(M+2)}.
\]
(The second expectation uses \(I=0\) for both boundary gaps.) Subtracting \(\mathbb EG_{n,r}\,\mathbb ED_{a,b}^2\), with \(\mathbb EG_{n,r}=1/M\), yields
\[
\operatorname{Cov}(G_{n,r},D_{a,b}^2)
=\frac{2(\ell+1)}{M(M+1)(M+2)}
\left(I_{a,b,r}-\frac\ell M\right).
\]
For the unbiased variance, the pairwise-difference identity gives
\[
S_n^2=\frac{1}{n(n-1)}\sum_{1\le a<b\le n}D_{a,b}^2.
\]
Two elementary finite sums, valid for every \(0\le r\le n\), are
\[
\sum_{a\le r<b}(b-a+1)=\frac{r(n-r)(n+2)}2,
\qquad
\sum_{a<b}(b-a)(b-a+1)
=\frac{n(n-1)(n+1)(n+2)}{12}.
\]
Here all pair indices have \(1\le a<b\le n\); the first sum is empty at \(r=0,n\). Inserting these into the covariance sum proves
\[
\operatorname{Cov}(G_{n,r},S_n^2)
=\frac{6r(n-r)-n(n-1)}{6n(n-1)(n+1)(n+3)}.
\]
This also shows \(\sum_{r=0}^n\operatorname{Cov}(G_{n,r},S_n^2)=0\), consistent with \(\sum_{r=0}^nG_{n,r}=1\).

The denominator is positive. The numerator is a concave quadratic in \(r\), with real zeros
\[
\rho_{\pm}(n)=\frac12\left(n\pm\sqrt{\frac{n(n+2)}3}\right).
\]
It is positive exactly at integer indices strictly between the real zeros and negative at indices outside their closed interval. At an integer zero, set \(m=|n-2r|\). Then the zero condition is equivalent to \((n+1)^2-3m^2=1\), with \(n+1>0\) and \(m\ge1\). Every positive integer solution \((x,m)\) to \(x^2-3m^2=1\) is given by \(x+m\sqrt3=(2+\sqrt3)^k\), \(k\ge1\): if \(m>1\), then \((x',m')=(2x-3m,2m-x)\) is another nonnegative solution with \(0\le m'<m\), because \(\sqrt3m<x<2m\); the recursion terminates at \((2,1)\) and its inverse is multiplication by \(2+\sqrt3\). The \(k=1\) solution gives \(n=1\), excluded by the sample-variance definition; for \(k\ge2\), parity of \(n\) and \(m\) agrees, and \(0<m<n\), so both \(r=(n\pm m)/2\) are admissible integers. This establishes necessity and sufficiency of the complete Pell classification.

For \(r_n/n\to u\), divide numerator and denominator of the exact formula by \(n^2\) and \(n^4\), respectively, proving the asymptotic limit and its two transition fractions. All edge/boundary classifications follow directly from the finite numerator, including the small-size exceptions stated above.

## Verification
The standalone standard-library script `verify.py` independently expands sample variance into squared sums of Dirichlet coordinates and evaluates degree-two and degree-three monomials by factorial multiplicities, without using the proof's conditional overlap formula. It checks all \(n=2,\ldots,18\) and every gap rank including boundary gaps, the zero-sum constraint, finite signs, Pell recurrence through twelve powers, and exact zero ranks exhaustively for \(2\le n\le2000\). Executing `python verify.py` produces `PASS: 2402 exact-arithmetic checks including full-gap direct moments, symmetry, and Pell zero ranks`. These finite checks support, but do not replace, the all-size analytic proof and Pell descent.

## Relationship to prior work
Royen [1, Section 4, Theorem 3] obtains the *marginal distribution* of sample variance from uniform observations, and [2] extends this distributional treatment to bounded continuous parents. Neither inspected full text gives the mixed rank-by-rank covariance with order-statistic gaps; a marginal distribution alone does not determine a joint mixed moment. Kochar [3] and the review [4, Section 5] establish stochastic comparisons of spacing vectors and sample variance across *different parent distributions*, not the within-sample rank-sign profile or its Pell-zero classification. Yao et al. [5] establish dependence-order properties of the spacing vector; their abstract does not state a covariance with sample variance, and the full paper was not accessible for comparison. The underlying Dirichlet factorial-moment identity and Pell equation are classical, and are not presented as discoveries. The proposed contribution is their specific exact joint covariance, complete sign diagram, and arithmetic classification of zero ranks.

## Limitations
This is an exact uniform-parent result and is not asserted for nonuniform observations. Zero covariance does not imply independence. The central-limit sign formula is a statement about covariance and does not establish a limiting joint distribution. Historical-priority uncertainty remains, especially concerning unavailable full text of [5] and other possible equivalent moment expansions; absence from targeted searches does not prove uniqueness. No independent external audit has been performed.

## References
1. T. Royen, *On the Laplace transform of some quadratic forms and the exact distribution of the sample variance from a gamma or uniform parent distribution*, arXiv:0710.5749, first posted 2007-10-30. https://arxiv.org/abs/0710.5749
2. T. Royen, *The exact distribution of the sample variance from bounded continuous random variables*, arXiv:0810.1572, first posted 2008-10-09. https://arxiv.org/abs/0810.1572
3. S. C. Kochar, *On stochastic orderings between distributions and their sample spacings*, Statistics & Probability Letters **42** (1999), 345–352, doi:10.1016/S0167-7152(98)00224-7.
4. S. Kochar, *Stochastic Comparisons of Order Statistics and Spacings: A Review*, ISRN Probability and Statistics (2012), Article 839473, doi:10.5402/2012/839473.
5. J. Yao, M. Burkschat, H. Chen, T. Hu, *Dependence Structure of Spacings of Order Statistics*, Communications in Statistics—Theory and Methods **37** (2008), 2390–2403, doi:10.1080/03610920801894887.
