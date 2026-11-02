# Tail-covariance majorization gives uniform stochastic improvement in one-probe Gaussian range finding

## Finding

For each integer \(m\ge2\), \(a>b>0\), and positive semidefinite \(m\)-by-\(m\) matrix \(C\) with \(\operatorname{tr}C=m\), consider a single Gaussian test vector with covariance \(\operatorname{diag}(1,C)\) and the ordinary rank-one randomized range approximation of \(A=\operatorname{diag}(a,b,\ldots,b)\). The complete distribution of the squared Frobenius residual depends on \(C\) only through its eigenvalues \(\mathbf t=(t_1,\ldots,t_m)\).

**Sharp spectral-majorization law.** If \(\mathbf t\) majorizes \(\mathbf s\), then the squared residual with spectrum \(\mathbf t\) is first-order stochastically **no larger** than the one with spectrum \(\mathbf s\). If these vectors are not permutations, the improvement is strict at **every** threshold strictly between \(mb^2\) and \(mb^2+a^2-b^2\). Among all covariance matrices of trace \(m\), the unique optimal spectrum for every such error probability is \((m,0,\ldots,0)\), and the unique worst spectrum is \((1,\ldots,1)\). Thus every increasing error criterion that is nonconstant on the attainable error support, and every interior quantile, is improved by concentrating tail covariance eigenvalues, while preserving the leading-probe variance and total tail variance.

In particular, for a correlation matrix \(C\), every marginal probe-coordinate variance remains exactly one. Within this family, the global optimum is attained precisely by \(C=\mathbf v\mathbf v^\top\) for sign vectors \(\mathbf v\in\{-1,+1\}^m\), and the unique worst covariance is \(C=I_m\). In dimension three, \(C_\rho=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\) gives strict improvement at every nontrivial threshold whenever \(|\rho|\) increases. Dimension three is the minimum size in which this fixed-marginal dependence choice exists.

## Assumptions and scope

Fix an integer \(m\ge2\), real singular values \(a>b>0\), and a real symmetric positive semidefinite \(C\) with \(\operatorname{tr}C=m\). Let \(X\sim N(0,1)\) and \(Y\sim N(0,C)\) be independent. Set \(\omega=(X,Y)\), \(A=\operatorname{diag}(a,bI_m)\), and \(q=A\omega/\|A\omega\|_2\), well defined almost surely. The rank-one range approximation is \(qq^\top A\), and the nonnegative random variable is
\[
L(C)=\|A-qq^\top A\|_F^2.
\]
Let \(\mathbf t\) contain the eigenvalues of \(C\), sorted nonincreasingly and repeated by multiplicity. For nonnegative vectors with equal sum, \(\mathbf t\succeq\mathbf s\) denotes majorization: \(\sum_{j=1}^k t_j\ge\sum_{j=1}^k s_j\) for every \(1\le k<m\). The claim is for exact arithmetic and one Gaussian test column without oversampling.

## Proof

**Step 1: exact residual and Gaussian spectral reduction.** Since \(q\) is a unit vector,
\[
L(C)=\|A\|_F^2-\|q^\top A\|_2^2
=mb^2+(a^2-b^2)\frac{b^2\|Y\|_2^2}{a^2X^2+b^2\|Y\|_2^2}.
\]
Orthogonally diagonalizing \(C\) gives \(T_{\mathbf t}=\|Y\|_2^2\overset{d}=\sum_{j=1}^m t_jZ_j^2\), with independent \(Z_j\sim N(0,1)\), also independent of \(X\). Because \(\sum t_j=m>0\), both \(X^2\) and \(T_{\mathbf t}\) are strictly positive almost surely. Consequently, \(mb^2<L(C)<mb^2+a^2-b^2\) almost surely.

**Step 2: exact CDF as a strictly convex Gaussian survival average.** Let the threshold \(e\) satisfy \(mb^2<e<mb^2+a^2-b^2\), and define
\[
h=\frac{e-mb^2}{a^2-b^2}\in(0,1),\qquad
k=\frac{a^2}{b^2}\frac{h}{1-h}>0.
\]
Rearranging Step 1 gives \(L(C)\le e\) exactly when \(T_{\mathbf t}\le kX^2\). Hence
\[
F_{\mathbf t}(e)=\mathbb P(L(C)\le e)
=\mathbb E\left[S\left(\frac{T_{\mathbf t}}{k}\right)\right],\qquad
S(u)=\mathbb P(\chi_1^2\ge u)=2[1-\Phi(\sqrt{u})].
\]
For every \(u>0\), direct differentiation gives
\[
S''(u)=\frac{e^{-u/2}(1+u)}{2\sqrt{2\pi}\,u^{3/2}}>0.
\]
Thus the random variable inside the expectation is a strictly convex function of the linear form \(\mathbf t\mapsto\sum_j t_jZ_j^2\). For distinct nonnegative weight vectors \(\mathbf t,\mathbf s\), the equality \(\sum_j t_j Z_j^2=\sum_j s_j Z_j^2\) has probability zero (because a nontrivial linear combination of the independent continuous random variables \(Z_j^2\) is zero with probability zero). Strict Jensen therefore shows that \(\mathbf t\mapsto F_{\mathbf t}(e)\) is strictly convex along any distinct pair of weight vectors. Its permutation invariance follows from exchangeability of the \(Z_j^2\). A strictly convex symmetric function is strictly Schur-convex modulo permutations (represent the more balanced vector as a nontrivial convex combination of permutations of the more concentrated one). This establishes the stated strict all-threshold stochastic ordering.

**Step 3: exact extremizers, correlation matrices and quantiles.** For any nonnegative \(\mathbf t\) with sum \(m\),
\[
(m,0,\ldots,0)\succeq\mathbf t\succeq(1,\ldots,1).
\]
Strictness in Step 2 forces the unique extremal spectra, and strictly ordered continuous CDFs give strictly ordered interior quantiles and strictly ordered means. If additionally \(C\) has unit diagonal, its rank-one positive semidefinite representation is \(C=\mathbf v\mathbf v^\top\), where the diagonal constraint forces \(|v_i|=1\); the identity is the only matrix with eigenvalues all equal to one. For \(m=2\), the eigenvalues of \(C_\rho\) are \(1+|\rho|\) and \(1-|\rho|\), giving strict monotonicity in \(|\rho|\).

**Step 4: exact extreme CDFs and mean.** At the most concentrated spectrum, \(T=mZ^2\), and the standard Cauchy ratio \(X/Z\) yields
\[
F_{\rm rank\,one}(e)=\frac2\pi\arctan\sqrt{\frac{k}{m}}.
\]
At the isotropic spectrum, \(T\sim\chi_m^2\), so the beta ratio \(T/(T+X^2)\) gives
\[
F_{\rm iso}(e)=I_{k/(k+1)}\left(\frac m2,\frac12\right),
\]
where \(I_z(p,q)\) is the regularized incomplete beta function. Polar integration for two independent standard normal variables gives the optimal expected residual
\[
\mathbb E L_{\rm rank\,one}
=mb^2+(a^2-b^2)\frac{b\sqrt m}{a+b\sqrt m}.
\]
For \(m=2\), \(a=3\), \(b=1\), and \(e=2.8\), one has \(k=1\), and hence
\[
F_{\rm iso}(e)=1-1/\sqrt2\approx0.2928932188,
\quad F_{\rm rank\,one}(e)=\frac2\pi\arctan(1/\sqrt2)\approx0.3918265520.
\]
The corresponding mean squared errors are approximately \(4.9168888812\) and \(4.5630179281\), respectively.

## Verification

The standalone file `VERIFY.py` checks the direct matrix residual identity on 540 Gaussian draws across multiple dimensions and singular-value pairs, the all-threshold endpoint laws, strict monotonicity along 31 numerical thresholds and 11 correlation values, the optimal mean against numerical quadrature, and the derivative sign. On replay with the recorded dependencies it passes **1,264** deterministic algebraic/numerical assertions. These finite checks are corroboration; the all-dimension and all-threshold assertions follow from Steps 1–4, not sampling.

## Relationship to prior work

Scotto Di Perrotolo, Diouane, Gürol, and Vasseur (arXiv:2405.04811, first public May 8, 2024) derive Gaussian covariance-aware Frobenius error bounds for randomized low-rank approximation, but their relevant theorem and Section 3.1.2 do not give the full single-column error law or strict majorization ordering of tail covariance eigenvalues. Boullé and Townsend (arXiv:2105.13052, May 27, 2021) establish a generalized covariance-aware randomized SVD with Theorem 2 assuming at least four oversampling columns, outside the present one-column setting. Classical majorization inequalities for convex expectations under exchangeable summands (Marshall–Proschan) supply the abstract ordering mechanism used in Step 2; the mathematical addition here is its exact covariance-to-error representation, all-threshold rank-one range-finder classification, and fixed-marginal optimal covariance design.

Bock, Diaconis, Huffer, and Perlman (1987) and Diaconis–Perlman (1988) analyze tails of weighted gamma sums, which can cross when weights change. Their accessible abstracts do not resolve the additional independent chi-square denominator in this projection-error problem; whether an equivalent statement is implicit in their full texts remains an originality risk. Originality is assessed relative to the material actually read, not certified as exhaustive.

## Limitations

The result requires a single probe, an independently sampled leading coordinate, a strictly separated leading singular value, and an isotropic equal-singular-value tail. It does not establish a comparable ordering for multiple probes, non-Gaussian vectors, arbitrary trailing singular spectra, floating-point arithmetic, or other loss norms. Rank-one tail covariance is degenerate as a Gaussian distribution but remains valid for the ordinary range approximation because the leading variance is positive. No independent scientific audit or publication-priority certification has been performed.

## References

1. A. Scotto Di Perrotolo, Y. Diouane, S. Gürol, X. Vasseur, *A general error analysis for randomized low-rank approximation with application to data assimilation*, 2024, https://arxiv.org/abs/2405.04811.
2. N. Boullé, A. Townsend, *A generalization of the randomized singular value decomposition*, 2021, https://arxiv.org/abs/2105.13052.
3. M. E. Bock, P. Diaconis, F. W. Huffer, M. D. Perlman, *Inequalities for linear combinations of gamma random variables*, 1987, https://doi.org/10.2307/3315257.
4. P. Diaconis, M. D. Perlman, *Bounds for tail probabilities of weighted sums of independent gamma random variables*, Stanford University technical report, 1988, https://purl.stanford.edu/jh932cq9916.
5. A. W. Marshall, F. Proschan, *An inequality for convex functions involving majorization*, J. Math. Anal. Appl. 12 (1965), 87–90 (cited in Bock et al.).
