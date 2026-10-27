# The one-crossing ranked-spacing covariance profile and its universal \(e^{-2}\) threshold

## Finding
Let \(m\ge2\). Form the \(m\) successive spacings from \(m-1\) independent uniform points on \([0,1]\), and rank them as \(U_{[1]}>\cdots>U_{[m]}\) (ties have probability zero). Write \(Q_m=\sum_{i=1}^{m}U_i^2\), and \(H_r=\sum_{i=1}^{r}i^{-1}\), with \(H_0=0\). For every integer \(1\le k\le m\),

\[
\operatorname{Cov}(U_{[k]},Q_m)=\frac{2}{m(m+1)(m+2)}\sum_{j=k}^{m}\frac{H_m-H_{j-1}-1}{j}.
\]

As the rank increases, these covariances have one and only one transition from positive to negative, permitting a single zero at the transition rank; in particular the largest-gap covariance is strictly positive and the smallest-gap covariance strictly negative. If \(r_m\) is the last strictly positive rank, then
\[
\lim_{m\to\infty}\frac{r_m}{m}=e^{-2}.
\]
For every fixed \(\alpha\in(0,1)\) and integer sequence \(k_m/m\to\alpha\),
\[
\lim_{m\to\infty}m^3\operatorname{Cov}(U_{[k_m]},Q_m)
=\log(1/\alpha)\bigl[\log(1/\alpha)-2\bigr].
\]
Thus the asymptotic share of gap ranks positively associated with quadratic concentration is approximately \(13.53\%\), with the remainder negatively associated. The sum of all rank covariances is exactly zero.

## Assumptions and scope
All assertions concern the continuous uniform-spacing law, equivalently \(U\sim\operatorname{Dirichlet}(1,\ldots,1)\), in every integer dimension \(m\ge2\). The quadratic concentration \(Q_m\), also used as a Moran-type spacing statistic or Simpson concentration, is the unnormalized sum of squared lengths; the lengths sum to one. Rank \(k=1\) refers to the largest spacing. The sign transition need not coincide with a zero at an integer rank. No statement is made for general nonuniform spacing laws, nonsymmetric Dirichlet laws or arbitrary concentration functionals.

## Proof
**Step 1 (uniform Dirichlet increments).** Put \(U_{[m+1]}=0\), and set \(Y_j=j(U_{[j]}-U_{[j+1]})\) for \(1\le j\le m\). The ordered region of the original simplex has constant density \(m!\) times the ordinary simplex density. Its linear triangular transform into \(Y\) has determinant \(1/m!\) in simplex coordinates, so \(Y\sim\operatorname{Dirichlet}(1,\ldots,1)\). Consequently
\[
U_{[k]}=\sum_{j=k}^{m}\frac{Y_j}{j},\qquad
Q_m=\sum_{j=1}^{m}\sum_{\ell=1}^{m}\frac{Y_jY_\ell}{\max(j,\ell)}.
\]
Both equalities also follow by telescoping; the second uses the identity \(\sum_{i\le\min(j,\ell)}(j\ell)^{-1}=1/\max(j,\ell)\).

**Step 2 (mixed third moment).** Define \(B_{j\ell}=1/\max(j,\ell)\). Direct summation gives
\[
\sum_{\ell=1}^m B_{j\ell}=1+H_m-H_j,\qquad \operatorname{tr}B=H_m,\qquad\sum_{j,\ell=1}^{m}B_{j\ell}=2m-H_m.
\]
For any real vector \(a\), put \(A=\sum_j a_j\) and \(T=\sum_j a_jY_j\). The uniform Dirichlet moments of orders one, two and three are respectively
\[
\mathbb E Y_i=\frac1m,\quad \mathbb E(Y_iY_j)=\frac{1+\delta_{ij}}{m(m+1)},\quad
\mathbb E(Y_iY_jY_\ell)=\frac{1+\delta_{ij}+\delta_{i\ell}+\delta_{j\ell}+2\delta_{ij}\delta_{i\ell}}{m(m+1)(m+2)}.
\]
These formulas give \(\mathbb EQ_m=2/(m+1)\) and
\[
\mathbb E(TQ_m)=\frac{2mA+2\sum_j a_j\bigl(\sum_\ell B_{j\ell}+B_{jj}\bigr)}{m(m+1)(m+2)}.
\]
Subtracting \(\mathbb ET\,\mathbb EQ_m=2A/[m(m+1)]\), we find
\[
\operatorname{Cov}(T,Q_m)=\frac{2}{m(m+1)(m+2)}\sum_{j=1}^m a_j(H_m-H_{j-1}-1).
\]
Choose \(a_j=\mathbf1\{j\ge k\}/j\) to obtain the claimed exact formula.

**Step 3 (single transition).** Let \(w_j=H_m-H_{j-1}-1\), strictly decreasing in \(j\), and \(S_k=\sum_{j=k}^{m}w_j/j\). The top-rank tail is
\[
S_1=\tfrac12\bigl(H_m^2+H_m^{(2)}\bigr)-H_m>0,\qquad H_m^{(2)}=\sum_{j=1}^{m}j^{-2},
\]
where positivity for \(m\ge2\) follows from \(S_1=1/4\) at \(m=2\), together with the strictly positive increment \(S_1(m+1)-S_1(m)=(H_m-1)/(m+1)+1/(m+1)^2\). Conversely \(S_m=(1/m-1)/m<0\). Since \(w_j\) decreases and has one change from positive to nonpositive, \(S_{k+1}=S_k-w_k/k\) strictly decreases for ranks before that change and thereafter is nondecreasing, while remaining strictly negative once its summands are nonpositive. Hence the sequence \(S_k\) goes from strictly positive to strictly negative exactly once, possibly taking value zero at one integer rank. The identity \(\sum_{k=1}^{m}S_k=\sum_{j=1}^{m}w_j=0\) proves exact covariance cancellation, consistent with \(\sum_kU_{[k]}=1\).

**Step 4 (limit at proportional ranks).** Let \(k_m/m\to\alpha\in(0,1)\). Uniformly for \(j\ge k_m\), harmonic comparison yields \(H_m-H_{j-1}=\log(m/j)+O_{\alpha}(m^{-1})\). Thus the sums are Riemann sums:
\[
S_{k_m}\longrightarrow\int_{\alpha}^{1}\frac{\log(1/x)-1}{x}\,dx
=\tfrac12\log^2(1/\alpha)-\log(1/\alpha).
\]
Combining with the exact denominator gives the claimed scaled limit. Its sign is positive for \(\alpha<e^{-2}\) and negative for \(\alpha>e^{-2}\); the finite single-transition property sandwiches \(r_m/m\) between any such two proportions and proves its limit.

## Verification
The complete stand-alone `verify.py` uses Python's exact rational arithmetic and an independent monomial-moment summation over all ordered triples of Dirichlet coordinates. It checks all ranks for \(2\le m\le12\), first moments, quadratic means, the covariance formula, cancellation, boundary signs and single-transition ordering. It also performs bounded floating-point asymptotic sanity checks (not used to prove the limit). Execute `python3 verify.py`. The current package execution passed 279 assertions. The infinite-rank limit and all-dimension statements are proved above, not inferred from the finite checks.

## Relationship to prior work
Moran's classical sum-of-squared uniform-spacings statistic motivates \(Q_m\). Bairamov, Berred and Stepanov (published online 10 April 2008) study distributions, means and asymptotics of ordered uniform spacings; their article explicitly cites Moran's quadratic statistic and gives ranked marginal formulas. The inspected Sections 2–5 do not state a mixed ordered-rank/total-quadratic covariance law or a signed rank threshold. The present theorem combines these established objects in a new mixed-moment comparison. Classical joint spacing representations could imply the formula upon specialization and moment summation, so priority remains subject to independent historical review. The same covariance law does not follow merely from separate marginal expectations, an entropy-versus-concentration covariance, or exceedance-count comparisons.

## Limitations
The proof is specific to the uniform simplex and quadratic concentration. At a finite dimension, an exact-zero rank is not excluded. The result is a covariance statement, not stochastic monotonicity or an independence criterion. No independent scientific or historical-priority audit has been performed.

## References
1. I. Bairamov, A. Berred and A. Stepanov, *Limit results for ordered uniform spacings*, Statistical Papers 51 (2010), 227–240; first published online 10 April 2008. DOI: 10.1007/s00362-008-0134-3. https://www.researchgate.net/publication/225529699_Limit_results_for_ordered_uniform_spacings
2. P. A. P. Moran, *The random division of an interval*, Journal of the Royal Statistical Society Series B 9 (1947), 92–98 (background quadratic statistic; bibliographic reference confirmed from source 1, full original not inspected).
3. R. Pyke, *Spacings*, Journal of the Royal Statistical Society Series B 27 (1965), 395–449 (classical general theory; bibliographic reference confirmed from source 1, full original not inspected).
