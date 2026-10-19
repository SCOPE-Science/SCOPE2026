# Universal signedness law and clipping bias for Gaussian Hutch# Frobenius estimation

## Finding
Let \(A\) be a nonzero real \(m\times n\) matrix and let \(r\geq1\) be an integer. Take independent matrices \(\Omega\in\mathbb R^{n\times r}\) and \(\Psi\in\mathbb R^{m\times r}\) with independent standard normal entries. For the nonadaptive Hutch# squared-Frobenius estimator
\[
H_r(A)=\frac{\|A\Omega\|_F^2}{r}+\frac{\|\Psi^{\mathsf T}A\|_F^2}{r}-\frac{\|\Psi^{\mathsf T}A\Omega\|_F^2}{r^2},\qquad F(A)=\|A\|_F^2>0,
\]
there is a **universal signed limit at diverging effective rank**. Let \(A_j\) be any sequence of nonzero real rectangular matrices (with no restriction on changing dimensions) such that
\[
R_j:=\frac{F(A_j)^2}{\operatorname{tr}((A_j^{\mathsf T}A_j)^2)}\longrightarrow\infty.
\]
For every fixed positive integer \(r\), using fresh independent sketches for each \(j\),
\[
\frac{H_r(A_j)}{F(A_j)}\ \xrightarrow[]{\mathrm{law}}\ 2-\frac{\chi^2_{r^2}}{r^2}.
\]
In particular, letting \(Q(k,x)=\Pr\{\chi^2_{2k}>2x\}\) denote the regularized upper gamma tail,
\[
\lim_{j\to\infty}\Pr\{H_r(A_j)<0\}
=q_r:=\Pr\{\chi^2_{r^2}>2r^2\}=Q(r^2/2,r^2)>0.
\]
The nonnegative clipping \(H_r^+(A)=\max\{0,H_r(A)\}\) has a nonzero **relative upward bias**, whose exact limiting value is
\[
\lim_{j\to\infty}\frac{\mathbb E H_r^+(A_j)-F(A_j)}{F(A_j)}
=\delta_r:=\Pr\{\chi^2_{r^2+2}>2r^2\}-2\Pr\{\chi^2_{r^2}>2r^2\}>0.
\]
For instance, \(q_1=0.157299207050\ldots\) and \(\delta_1=0.257808290370\ldots\). As \(r\to\infty\),
\[
q_r\sim\frac{1}{\sqrt\pi\,r}\exp\!\left[-\frac{1-\log2}{2}r^2\right].
\]
At the opposite spectral extreme, for **every nonzero rank-one** real \(A\), the normalized estimator is exactly
\[
\frac{H_r(A)}{F(A)}=U_r+V_r-U_rV_r,
\quad U_r,V_r\overset{\mathrm{iid}}\sim\chi_r^2/r,
\]
so its negative probability \(p_r\) is the explicit one-dimensional integral
\[
p_r=\int_1^\infty f_r(u)\,\Pr\!\left\{V_r>1+\frac{1}{u-1}\right\}\,du,
\]
where \(f_r\) is the density of \(\chi_r^2/r\), and has the **different** sharp rare-event behavior
\[
p_r\sim\frac12\sqrt{\frac{2}{3\pi r}}\exp[-(1-\log2)r].
\]
Thus a nonnegative target can yield a negative result at any fixed sketch budget, even when the spectrum becomes arbitrarily flat; clipping to enforce nonnegativity changes the estimator's mean by an explicitly nonvanishing amount.

## Assumptions and scope
All matrices are real and finite-dimensional; the Gaussian entries in the two sketches are independent of each other. The sketch count \(r\) is fixed while \(j\to\infty\) in the effective-rank limit. No distribution is assumed for the deterministic matrices \(A_j\). The rank-one formula holds at every finite \(r\). The \(r\to\infty\) tail statements are taken **after** their respective fixed-matrix-rank or high-effective-rank limits; they do not assert a joint \(j,r\to\infty\) limit. In the high-effective-rank conclusion, each \(A_j\) can be tall, wide, square, dense, sparse, or ill-conditioned, subject only to \(R_j\to\infty\).

## Proof
**1. Reduction to singular directions.** Orthogonal invariance of the independent Gaussian sketches allows reduction to the nonzero singular values \(\sigma_{j,i}\) of \(A_j\). Define \(F_j=\sum_i\sigma_{j,i}^2\) and \(S_j=\sum_i\sigma_{j,i}^4\), so the hypothesis is \(S_j/F_j^2\to0\). Let \(X_i=(X_{ia})_{a=1}^r\) and \(Y_i=(Y_{ib})_{b=1}^r\) be independent standard Gaussian vectors for each singular direction. Then
\[
\frac{H_r(A_j)}{F_j}
=\frac{\sum_i\sigma_{j,i}^2\|X_i\|^2}{rF_j}
+\frac{\sum_i\sigma_{j,i}^2\|Y_i\|^2}{rF_j}
-\frac{1}{r^2}\sum_{a,b=1}^r\left(\frac{\sum_i\sigma_{j,i}X_{ia}Y_{ib}}{\sqrt{F_j}}\right)^2.
\]

**2. Gaussian-chaos central limit theorem.** Each of the first two sums has mean one and variance \(2S_j/(rF_j^2)\to0\). The vector of \(r^2\) cross-products in parentheses is a sum of independent centered \(r^2\)-vectors with covariance exactly \(I_{r^2}\). Its sum of fourth moments is bounded by a constant depending only on the fixed \(r\), times \(S_j/F_j^2\to0\). The multivariate Lyapunov (hence Lindeberg) central limit theorem gives convergence to \(N(0,I_{r^2})\). Continuous mapping and Slutsky yield the claimed \(2-\chi^2_{r^2}/r^2\) law. Its distribution is continuous at zero, so the negative-event probabilities converge to \(q_r\).

**3. Clipping bias.** The Gaussian fourth-moment identity gives the exact finite-matrix variance
\[
\operatorname{Var}(H_r(A)/F(A))=\frac{2}{r^2}\left(1+\frac{\operatorname{tr}((A^{\mathsf T}A)^2)}{F(A)^2}\right)\le\frac4{r^2};
\quad\mathbb E[H_r(A)/F(A)]=1.
\]
The centered identity follows directly by conditioning on either sketch and applying \(\operatorname{Var}(g^{\mathsf T}Bg)=2\operatorname{tr}(B^2)\), followed by one Wishart fourth-moment contraction; it also appears in Chen--Halikias--Musco--Persson (2026). Uniform boundedness of second moments makes the negative-part functions uniformly integrable. Since \(H_r^+=H_r+(-H_r)_+\), the clipping-bias limit equals \(\mathbb E[(Z/r^2-2)_+]\) with \(Z\sim\chi^2_{r^2}\). The chi-square density relation \(z f_k(z)=k f_{k+2}(z)\) proves the stated exact gamma-tail difference. Its strict positivity follows from the positive probability of \(Z>2r^2\).

**4. Large sketch tail for the flat-spectrum law.** Write \(k=r^2\). The density of \(Z/k\), \(Z\sim\chi^2_k\), has asymptotic form
\[
f_k(u)=\sqrt{\frac{k}{4\pi}}\,u^{-1}\exp[-kI(u)]\,(1+O(k^{-1})),\qquad I(u)=\frac{u-1-\log u}{2},
\]
uniformly on compact subsets of \((0,\infty)\). Because \(I\) strictly increases on \([2,\infty)\) with \(I'(2)=1/4\), the one-sided endpoint Laplace method gives
\[
\Pr\{Z>2k\}=\frac{e^{-kI(2)}}{\sqrt{\pi k}}(1+o(1)),
\]
which yields the displayed \(q_r\) asymptotic.

**5. Rank-one law and sharp boundary saddle.** For rank-one \(A=\sigma uv^{\mathsf T}\) with unit \(u,v\), let \(U_r=\|v^{\mathsf T}\Omega\|^2/r\) and \(V_r=\|\Psi^{\mathsf T}u\|^2/r\). They are independent normalized chi-squares and the three sketch terms reduce to \(U_r,V_r,U_rV_r\). Negativity is equivalent to \((U_r-1)(V_r-1)>1\). The case \(U_r,V_r<1\) cannot satisfy this strict inequality, leaving precisely the integral over \(u>1\) written above. For \(v(u)=1+(u-1)^{-1}\), the gamma density and tail estimates uniform near \(u=2\) give the integrand asymptotic
\[
\frac{u-1}{2\pi u}\exp[-rJ(u)],\qquad J(u)=I(u)+I(v(u)).
\]
Writing \(u=1+t\) with \(t>0\), direct differentiation gives
\[
\frac{dJ(1+t)}{dt}=\frac{t^3-1}{2t^2(t+1)}.
\]
Therefore the unique global minimum is \(u=2\), where \(J(2)=1-\log2\), \(J''(2)=3/4\), and the prefactor is \(1/(4\pi)\). The ordinary interior Laplace formula supplies \(p_r\sim(4\pi)^{-1}\sqrt{8\pi/(3r)}e^{-r(1-\log2)}\), exactly the stated constant. Contributions outside a compact neighborhood of \(u=2\) are exponentially smaller because the action rises strictly on each side and diverges at both boundaries.

## Verification
The companion `verify.py` checks the centered-Wishart algebraic identity for several shapes and independent Gaussian draws; evaluates the exact gamma-tail and clipping-bias constants; numerically integrates the rank-one formula and checks its sharp saddle approximation; and compares large-effective-rank predictions against 48,000 independently sampled Gaussian sketch pairs for nonconstant, slowly varying singular values. Run with `python verify.py` using NumPy and SciPy. These simulations are reproducibility diagnostics, not substitutes for the Lyapunov, uniform-integrability, or Laplace arguments proving the general and infinite-limit claims.

## Relationship to prior work
Chen, Halikias, Musco, and Persson (2026) introduce Hutch#, prove unbiasedness and its exact variance, and optimize a weighted interpolation with a Gaussian trace estimator. Their full accessible primary text analyzes relative-error guarantees and numerical root-mean-square errors, but does not derive the signed high-effective-rank limit, the universal negative-value probability, the positive-part clipping bias, or the different rank-one negative tail. The variance identity used in Step 3 is credited to that paper and is **not** an originality claim. Meyer et al. (2021) analyze the distinct projection-based Hutch++ trace estimator, whose positive-semidefinite application has a nonnegative representation; its guarantees do not give signedness laws for Hutch#. The ordinary multivariate CLT and gamma asymptotics are tools, not newly claimed results. The contribution here is their precise interaction with the nonadaptive two-sided Gaussian estimator and the two spectral endpoint regimes.

## Limitations
This characterizes the unweighted original real-Gaussian Hutch# estimator. It does not claim an identical limit for Rademacher probes, complex Gaussian sketches, weighted Hutch#, Hutch++ or Hutch-flat, nor an asymptotic law under joint growth of sketch count and effective rank. The high-effective-rank theorem is asymptotic and supplies no finite-effective-rank total-variation guarantee. Any source-equivalent result in unindexed literature would affect originality, and no independent audit has been performed.

## References
1. T. Chen, D. Halikias, C. Musco, D. Persson, *Hutch#: Optimal non-adaptive Frobenius norm estimation*, arXiv:2609.28472, first posted 2026-09-23, https://arxiv.org/abs/2609.28472.
2. R. A. Meyer, C. Musco, C. Musco, D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, arXiv:2010.09649 (2020), https://arxiv.org/abs/2010.09649.
3. D. Persson, A. Cortinovis, D. Kressner, *Improved Variants of the Hutch++ Algorithm for Trace Estimation*, SIAM J. Matrix Anal. Appl. 43 (2022), https://doi.org/10.1137/21M1447623.
