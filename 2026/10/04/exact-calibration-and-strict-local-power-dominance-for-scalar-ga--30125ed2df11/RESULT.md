# Exact calibration and strict local-power dominance for scalar Gaussian two-way cross-fitting
## Finding
Consider the balanced two-way cross-fitted one-sample mean statistic introduced by Kim and Ramdas. Let \(m\ge2\), let \(X_1,\ldots,X_{2m}\) be iid \(N(\mu,1)\), and split the observations into two halves of size \(m\). Write \(\bar X_j\) and \(s_j\) for the mean and the usual unbiased sample standard deviation in half \(j\), and define
\[
t_j=\frac{\sqrt m\,\bar X_j}{s_j},\qquad j=1,2.
\]
For the scalar version of the published two-way cross-fitted statistic, under \(\mu=0\),
\[
T_m^{\mathrm{cross}}\overset d=\sqrt{\frac{m}{m-1}}\,S\bigl(|t_1|+|t_2|\bigr),
\]
where \(t_1,t_2\) are independent Student random variables with \(m-1\) degrees of freedom and \(S\) is an independent Rademacher sign. Therefore for every \(0<\alpha<1/2\), an exact one-sided finite-sample level-\(\alpha\) cutoff is
\[
c_{m,\alpha}=\sqrt{\frac{m}{m-1}}\,q_{1-2\alpha}\bigl(|t_{m-1}^{(1)}|+|t_{m-1}^{(2)}|\bigr),
\]
where \(q_p(Y)\) is the \(p\)-quantile of the continuous law of \(Y\).

Moreover, under local alternatives \(\mu_m=h/\sqrt m\) with fixed \(h\ne0\), the exactly calibrated cross-fitted test has asymptotic power strictly larger than the source paper's corresponding single-split test at the same asymptotic level \(\alpha\). The limiting cross-fit cutoff is
\[
c_\alpha=\sqrt2\,u_\alpha,\qquad
u_\alpha:=\Phi^{-1}\!\left(\frac{1+\sqrt{1-2\alpha}}2\right).
\]
Then
\[
\pi_C(h;\alpha)
=\int_{|u|>u_\alpha}\phi(u-\sqrt2h)\{2\Phi(|u|)-1\}\,du
>\pi_S(h;\alpha)
\]
for every \(h\ne0\), where
\[
\pi_S(h;\alpha)
=\Phi(h)\Phi(h-z_{1-\alpha})+\Phi(-h)\Phi(-h-z_{1-\alpha}).
\]
At \(h=0\), both limits equal \(\alpha\).

For example, at \(\alpha=0.05\), \(u_\alpha=1.948821862507\ldots\) and \(c_\alpha=2.756050308607\ldots\). At \(h=1\), the limiting powers are \(0.291558566988\ldots\) for the two-way cross-fit and \(0.218986550651\ldots\) for the single split.

## Assumptions and scope
The result is for one-dimensional Gaussian observations with known unit population variance, although the statistic itself studentizes each half. The total sample size is \(2m\), each half has size \(m\ge2\), and the split is balanced. The one-sided significance level satisfies \(0<\alpha<1/2\). The exact null statement is finite-sample. The power comparison is asymptotic along \(\mu_m=h/\sqrt m\) for fixed nonzero \(h\).

The result concerns the particular two-way cross-fitted statistic displayed in Appendix A of Kim and Ramdas. It does not claim that arbitrary averages over many random splits admit this calibration, that post-data choice among split aggregators is valid, or that the cross-fitted statistic remains dimension-agnostic when dimension grows.

## Proof
For scalars, the first term of the published statistic is
\[
\frac{\sqrt m\,\bar X_1\bar X_2}
{\sqrt{m^{-1}\sum_{i\in I_1}\{\bar X_2(X_i-\bar X_1)\}^2}}
=\operatorname{sgn}(\bar X_2)\sqrt{\frac m{m-1}}\,t_1.
\]
The second term is the same expression with the halves exchanged. Thus, almost surely,
\[
T_m^{\mathrm{cross}}
=\sqrt{\frac m{m-1}}
\left\{\operatorname{sgn}(t_2)t_1+\operatorname{sgn}(t_1)t_2\right\}
=\sqrt{\frac m{m-1}}\operatorname{sgn}(t_1t_2)(|t_1|+|t_2|).
\]
Under \(\mu=0\), each \(t_j\) has a Student law with \(m-1\) degrees of freedom. For a symmetric continuous Student law, sign and magnitude are independent; independence of the two halves then makes \(S=\operatorname{sgn}(t_1t_2)\) an independent fair sign. This proves the exact null representation. Since \(|t_1|+|t_2|\) has a continuous law, for \(c\ge0\),
\[
\Pr_0(T_m^{\mathrm{cross}}>c)
=\frac12\Pr\!\left(|t_1|+|t_2|>c\sqrt{\frac{m-1}{m}}\right),
\]
which yields the exact cutoff formula.

For the local-power limit, under \(\mu_m=h/\sqrt m\), the two half-sample Student statistics converge jointly to independent
\[
A=Z_1+h,\qquad B=Z_2+h,
\]
with \(Z_1,Z_2\) iid \(N(0,1)\). Therefore
\[
T_m^{\mathrm{cross}}\Longrightarrow L_h
:=\operatorname{sgn}(AB)(|A|+|B|).
\]
Set
\[
U=\frac{A+B}{\sqrt2},\qquad V=\frac{A-B}{\sqrt2}.
\]
Then \(U\sim N(\sqrt2h,1)\), \(V\sim N(0,1)\), and they are independent. Also
\[
AB=\frac{U^2-V^2}{2},\qquad
|A|+|B|=\sqrt2\max\{|U|,|V|\}.
\]
Under the null, exchangeability of \(|U|\) and \(|V|\) gives
\[
\Pr(L_0>\sqrt2u)
=\frac12\left[1-\{2\Phi(u)-1\}^2\right].
\]
Solving this probability equal to \(\alpha\) gives \(u=u_\alpha\) and hence \(c_\alpha=\sqrt2u_\alpha\). Under the local alternative, rejection is exactly the limiting event
\[
|U|>u_\alpha,\qquad |V|<|U|,
\]
which gives the displayed integral for \(\pi_C\).

It remains to compare with one split. Let \(z=z_{1-\alpha}\). Conditional on \(|U|=r\), the single-split limiting rejection probability is
\[
g_S(r)=
\begin{cases}
0,&r\le z/\sqrt2,\\
\Phi(r)-\Phi(\sqrt2z-r),&r>z/\sqrt2,
\end{cases}
\]
whereas the cross-fit conditional rejection probability is
\[
g_C(r)=\mathbf 1\{r>u_\alpha\}\{2\Phi(r)-1\}.
\]
Let \(d(r)=g_C(r)-g_S(r)\). The equation defining \(u_\alpha\) implies the upper normal-tail probability at \(u_\alpha\) is strictly below \(\alpha\), so \(u_\alpha>z\). Hence \(d(r)<0\) for \(z/\sqrt2<r\le u_\alpha\), while for \(r>u_\alpha\),
\[
d(r)=\Phi(r)-\Phi(r-\sqrt2z)>0.
\]
Both tests have null level \(\alpha\), so \(\int_0^\infty d(r)2\phi(r)\,dr=0\).

Under the local alternative, the density of \(|U|\) relative to its null folded-normal density is
\[
w_h(r)=e^{-h^2}\cosh(\sqrt2hr),\qquad r\ge0,
\]
which is strictly increasing in \(r\) whenever \(h\ne0\). Therefore, writing \(r_0=u_\alpha\),
\[
\pi_C(h;\alpha)-\pi_S(h;\alpha)
=\int_0^\infty d(r)\{w_h(r)-w_h(r_0)\}2\phi(r)\,dr>0.
\]
The integrand is nonnegative everywhere and strictly positive on sets of positive measure on both sides of \(r_0\). This proves strict local-power dominance.

## Verification
The accompanying `verify.py` independently checks the scalar algebraic reduction on deterministic nondegenerate half-samples, recomputes the limiting \(5\%\) cutoff from the closed form, numerically verifies the null-size identity, checks the one-crossing sign pattern of \(d(r)\), and evaluates the two limiting power formulas at several nonzero local signals. Its successful output is `VERIFY_OK`.

The computational checks support the displayed constants and algebra but are not used as substitutes for the finite-sample distributional proof or the all-\(h\ne0\) monotone-likelihood-ratio argument.

## Relationship to prior work
Kim and Ramdas define this exact two-way cross-fitted statistic in Appendix A and prove its fixed-dimensional limiting null distribution. They emphasize that the sum is not Gaussian, describe calibration as challenging, and state that they do not know in general whether many split-based tests can be calibrated with provably higher power than a single split. In a separate appendix they derive the scalar Gaussian local-power formula for their single-split test. Those ingredients motivate the present question, but the source does not give the scalar finite-sample Student representation, its exact cutoff, the closed limiting cutoff, or the strict cross-fit versus single-split local-power comparison proved here.

Guo and Shah subsequently develop rank-transformed subsampling for aggregating many randomized split statistics. Their paper explicitly revisits the Kim--Ramdas mean example, notes that the simple cross-fitted statistic has a nonnormal limit, and proves power properties for a different rank-transformed aggregation procedure. It does not analyze the exact two-way cross-fitted statistic above or imply the finite-sample Student law and single-crossing dominance theorem stated here.

## Limitations
The strict power theorem is local-asymptotic and Gaussian. It does not compare finite-sample powers, does not extend automatically to unknown non-Gaussian laws, unequal split sizes, dimensions above one, or aggregations over more than the two complementary directions. The exact cutoff is expressed through a quantile of a sum of two independent absolute Student variables; outside special cases that quantile generally requires numerical evaluation.

The literature search found no equivalent statement, but absence from the searched sources is not a proof of historical novelty. A residual risk remains that the same scalar distributional identity or the one-crossing power argument appears in older work under different terminology for symmetrized split-sample Student statistics.

## References
1. I. Kim and A. Ramdas, “Dimension-agnostic inference using cross U-statistics,” arXiv:2011.05068, first posted 10 November 2020; Bernoulli 30(1), 683–711 (2024), DOI 10.3150/23-BEJ1613.
2. F. R. Guo and R. D. Shah, “Rank-transformed subsampling: inference for multiple data splitting and exchangeable p-values,” arXiv:2301.02739, first posted 6 January 2023; Journal of the Royal Statistical Society Series B 87(1), 256–286 (2025), DOI 10.1093/jrsssb/qkae091.
