# A universal rank threshold for Greenwood dependence among uniform spacings

## Finding
Let \(m\ge2\) be an integer. For a uniformly random vector \(X=(X_1,\ldots,X_m)\) on the unit simplex, write \(X_{[1]}>\cdots>X_{[m]}\) for its decreasingly ranked coordinates, and \(Q=\sum_iX_i^2\) for Greenwood's squared-spacing statistic. Define the harmonic tails
\[
T_{m,k}=\sum_{j=k}^m\frac1j,\qquad U_{m,k}=\sum_{j=k}^m\frac1{j^2},\qquad 1\le k\le m.
\]
Then the exact joint-statistic covariance is
\[
\boxed{\operatorname{Cov}(X_{[k]},Q)=\frac{T_{m,k}^{2}+U_{m,k}-2T_{m,k}}{m(m+1)(m+2)}.}
\]
For every \(m\ge2\), ranks with positive covariance form a nonempty initial interval, those with negative covariance form a nonempty terminal interval, and there is at most one zero-covariance rank between them. With \(r_m\) denoting the last positive rank,
\[
\boxed{\lim_{m\to\infty}\frac{r_m}{m}=e^{-2}.}
\]
Thus the largest approximately \(13.53\%\) of ranks are positively associated with overall quadratic concentration; the rest are negatively associated, apart from a possible boundary tie. This assertion concerns rankwise covariance, not independence or monotone regression.

## Assumptions and scope
The vector is exactly uniform Dirichlet, \(X\sim\operatorname{Dirichlet}(1,\ldots,1)\), equivalently the \(m\) spacings cut out by \(m-1\) independent uniform points in \([0,1]\). Ties between coordinates have probability zero. Rank one means the *largest* spacing. The result applies to all integers \(m\ge2\) and all integer ranks \(1\le k\le m\). The limiting fraction takes \(m\to\infty\) under this symmetric null model; no alternative data-generating distribution is asserted.

## Proof
**Ranked-gap coordinates.** On the ordered simplex, set \(x_{m+1}=0\) and \(Y_j=j(x_j-x_{j+1})\) for \(1\le j\le m\). These coordinates are nonnegative, sum to one, and invert to \(x_k=\sum_{j=k}^mY_j/j\). Sorting a uniform-simplex point multiplies its constant density by \(m!\); the gap transformation has constant nonzero Jacobian and maps onto the full simplex. Consequently \(Y\sim\operatorname{Dirichlet}(1,\ldots,1)\).

**Quadratic form and Dirichlet moments.** The squared-spacing statistic becomes
\[
Q=\sum_{a,b=1}^{m}\frac{Y_aY_b}{\max(a,b)}.
\]
Let \(A_{ab}=1/\max(a,b)\), \(R_j=\sum_bA_{jb}=1+H_m-H_j\), and \(S=\sum_{a,b}A_{ab}=2m-H_m\). Also \(\operatorname{tr}A=H_m\), hence \(S+\operatorname{tr}A=2m\). Here \(H_n=\sum_{i=1}^n 1/i\), with \(H_0=0\).

For uniform Dirichlet \(Y\), the exact moment identity
\[
\mathbb E\!\left[\prod_iY_i^{a_i}\right]=\frac{\prod_i a_i!}{m(m+1)\cdots(m+d-1)},\qquad d=\sum_i a_i,
\]
for nonnegative integer exponents implies
\[
\mathbb E Q=\frac{2}{m+1},\qquad
\mathbb E(Y_jQ)=\frac{S+2R_j+\operatorname{tr}A+2A_{jj}}{m(m+1)(m+2)}.
\]
Since \(\mathbb EY_j=1/m\) and \(R_j+A_{jj}-2=H_m-H_{j-1}-1\), subtraction gives
\[
\operatorname{Cov}(Y_j,Q)=\frac{2(T_{m,j}-1)}{m(m+1)(m+2)}.
\]
Linearity and the inverse ranked-gap transformation yield
\[
\operatorname{Cov}(X_{[k]},Q)=\frac{2}{m(m+1)(m+2)}\sum_{j=k}^m\frac{T_{m,j}-1}{j}.
\]
Finally, pairing the off-diagonal terms in the square of \(T_{m,k}\) gives
\[
2\sum_{j=k}^m\frac{T_{m,j}-1}{j}=T_{m,k}^{2}+U_{m,k}-2T_{m,k},
\]
which proves the exact formula.

**Finite-rank sign structure.** Write \(W_{m,k}=T_{m,k}^2+U_{m,k}-2T_{m,k}\). For the largest rank, \(W_{m,1}>0\): \(W_{1,1}=0\) and, as \(m\) increases by one, the value \(H_m^2+H_m^{(2)}-2H_m\) increases by \(2(H_m-1)/(m+1)+2/(m+1)^2>0\). At the smallest rank, \(W_{m,m}=2/m^2-2/m<0\).
Moreover,
\[
W_{m,k}-W_{m,k+1}=\frac{2(T_{m,k}-1)}{k},\qquad 1\le k<m.
\]
The tail \(T_{m,k}\) strictly decreases with rank. Thus \(W_{m,k}\) first decreases and then increases (possibly with one flat step). Because its initial value is positive and its terminal value remains negative, its sign switches exactly once from positive to negative, allowing at most a single zero-rank at the boundary. In particular, no later return to nonnegative covariance is possible.

**Asymptotic threshold.** If \(k_m=\lceil\theta m\rceil\) for fixed \(0<\theta<1\), the integral comparison for harmonic tails gives \(T_{m,k_m}\to\log(1/\theta)\), while \(0\le U_{m,k_m}\le1/(k_m-1)\to0\). Therefore
\[
W_{m,k_m}\longrightarrow\log(1/\theta)\bigl(\log(1/\theta)-2\bigr).
\]
Its sign is positive for \(\theta<e^{-2}\) and negative for \(\theta>e^{-2}\). Combining this with the finite one-crossing property sandwiches \(r_m/m\) between any fixed parameters on opposite sides of \(e^{-2}\), proving the limit.

## Verification
Run \(\texttt{python3 verification.py}\) with Python 3's standard library. The script performs exact rational integration of degree-three uniform-Dirichlet monomials independently of the displayed harmonic simplification for every rank and \(2\le m\le9\); tests the sign ordering by exact arithmetic through \(m=350\); and prints numerical large-dimension threshold comparisons. The recorded execution passed 71,058 assertions. Computation is **not** used as a proof for arbitrary \(m\); the preceding algebra and harmonic-tail argument supply that proof.

## Relationship to prior work
Pyke (1965) surveys spacing theory. Rao and Sobel (1980), especially Section 3, derive marginal and joint laws of ordered uniform spacings and sums of extreme spacings; those distributions do not state the cross-covariance with the quadratic statistic or the rankwise sign threshold. Royen (2010, arXiv:1008.4059v1) provides exact distributional representations and quantiles for the *marginal* squared-spacing statistic \(Q\), but not the covariance by ordered rank. The classical moment formula for the Dirichlet distribution supplies the third-degree integration engine. The new point here is the exact rankwise mixed covariance and its universal \(e^{-2}\) sign boundary. This is not a claim that the underlying coordinate or moment identities themselves are new.

## Limitations
The statement holds only for uniform Dirichlet spacings, not arbitrary Dirichlet parameters or nonuniform spacings. Covariance sign does not imply stochastic ordering or independence. The possible finite zero-covariance boundary rank is not classified arithmetically. Existing general Dirichlet integration formulas could contain equivalent unlocated presentations of this mixed moment; historical priority has not been independently certified. No independent audit has been performed.

## References
- R. Pyke, *Spacings*, Journal of the Royal Statistical Society Series B 27 (1965), 395–436. DOI: 10.1111/j.2517-6161.1965.tb00602.x.
- J. S. Rao and M. Sobel, *Incomplete Dirichlet integrals with applications to ordered uniform spacings*, Journal of Multivariate Analysis 10 (1980), 603–610. DOI: 10.1016/0047-259X(80)90073-1.
- T. Royen, *The distribution of the square sum of Dirichlet random variables and a table with quantiles of Greenwood's statistic*, arXiv:1008.4059v1, made public August 24, 2010. https://arxiv.org/abs/1008.4059.
