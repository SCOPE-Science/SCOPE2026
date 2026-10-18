# Exact two-probe diagonal risk and a Gaussian moment phase for leave-one-out XDiag

## Finding

Consider the literal leave-one-out XDiag coordinate-quotient formula (defined below). There are two exact, complementary phenomena.

**Sign probes, two samples.** For every integer \(n\ge2\), every nonzero real diagonal positive-semidefinite matrix \(A=\operatorname{diag}(a_1,\ldots,a_n)\), and two independent uniform Rademacher probes, the two leave-one-out component estimators agree *on every outcome*. Nevertheless, writing \(T=\sum_i a_i^2\) and \(\widehat d\) for their average, the covariance and exact mean-square diagonal error are
\[
\operatorname{Cov}(\widehat d_i,\widehat d_j)=
\begin{cases}
\dfrac{a_i^2}{T^2}\sum_{\ell\ne i}a_\ell^4,&i=j,\\[4pt]
\dfrac{a_i^3a_j^3}{T^2},&i\ne j,
\end{cases}
\qquad
\mathbb E\|\widehat d-\operatorname{diag}(A)\|_2^2
=\frac{T\sum_i a_i^4-\sum_i a_i^6}{T^2}\le\frac T4.
\]
The bound is sharp, with equality precisely when exactly two diagonal entries are nonzero and equal. With one sign probe the same formula is exact on every diagonal matrix, so the second probe can *increase* its risk from zero to the sharp bound. For \(A=aI_2\), the two component estimates are identical and equal to either \((a/2,a/2)\) or \((3a/2,3a/2)\), each with probability one half; their within-pair disagreement is always zero despite strictly positive diagonal error.

**Formal Gaussian probe substitution.** For every \(n\ge2\) and scalar matrix \(A=aI_n\) with \(a>0\), replacing sign probes in the *literal coordinate-quotient formula* by independent standard Gaussian probes yields the sharp sample-count phase (for every coordinate \(i\)):
\[
\begin{array}{ll}
 k=1\ \text{or}\ k\ge n+1:&\widehat d_i=a\quad\text{almost surely},\\[3pt]
 2\le k\le n:&\displaystyle \mathbb E|\widehat d_i-a|^p<\infty\quad\Longleftrightarrow\quad0<p<1.
\end{array}
\]
Thus the middle regime has no absolutely integrable first moment, regardless of the finite sample count. In the smallest case \(n=k=2\), both signed tails have the same exact constant:
\[
\lim_{t\to\infty}t\Pr(\widehat d_1-a>t)
=\lim_{t\to\infty}t\Pr(\widehat d_1-a<-t)=\frac a{\pi^2}.
\]
The Gaussian statement concerns a **formal change of probe distribution**, not the published sign-based XDiag implementation.

## Assumptions and scope

All matrices and probes are real; arithmetic is exact; projections use Moore–Penrose inverses. For a symmetric matrix \(A\) and probes \(\omega_1,\ldots,\omega_k\), let \(P_{(-j)}\) be the orthogonal projector onto \(\operatorname{range}(A\Omega_{-j})\), where \(\Omega_{-j}\) omits the \(j\)-th probe and \(P_{(-1)}=0\) when \(k=1\). Define, wherever coordinate quotients exist,
\[
 Z_{j,i}=(P_{(-j)}A)_{ii}+
 \frac{[(I-P_{(-j)})A\omega_j]_i}{\omega_{j,i}},\qquad
 \widehat d_i=\frac1k\sum_{j=1}^k Z_{j,i}.
\]
In the sign-probe result \(k=2\), \(\omega_{j,i}\in\{-1,1\}\), so there are no zero denominators. In the Gaussian result \(A=aI_n\), the denominators are nonzero almost surely. The result does not concern XDiag variants that algebraically specialize the update to sign probes, clip denominators, or switch to exact diagonal computation at high probe counts.

## Proof

**1. Two-sign-probe identity.** Write \(\omega_1=x\), \(\omega_2=y\), and \(t_i=x_i y_i\). The independent variables \(t_i\) are uniform signs. Because \(\|Ax\|_2^2=\|Ay\|_2^2=T\), the excluded-probe projector for probe \(x\) is \(P_y=(Ay)(Ay)^\mathsf T/T\). Directly,
\[
 (P_yA)_{ii}=\frac{a_i^3}{T},\qquad
 \frac{(P_yAx)_i}{x_i}=\frac{a_it_i}{T}\sum_\ell a_\ell^2t_\ell.
\]
Hence
\[
 Z_{1,i}=a_i+\frac{a_i^3}{T}
 -\frac{a_it_i}{T}\sum_\ell a_\ell^2t_\ell
 =a_i-\frac{a_i}{T}t_i\sum_{\ell\ne i}a_\ell^2t_\ell.
\]
Interchanging \(x\) and \(y\) leaves \(t_i\) unchanged; thus \(Z_{2,i}=Z_{1,i}\) identically. Independence of the signs gives mean zero error. In the covariance of two coordinate errors, the only nonvanishing pairings are the identical index \(\ell\) when \(i=j\), and the crossed pair \((\ell,m)=(j,i)\) when \(i\ne j\). This proves the covariance formula and, summing diagonal covariances, the asserted risk.

Set \(w_i=a_i^2/T\), so \(\sum_iw_i=1\), \(w_i\ge0\). The normalized risk equals
\[
 \frac RT=\sum_iw_i^2(1-w_i)=\sum_iw_i\,[w_i(1-w_i)]\le\frac14.
\]
Equality forces every positive \(w_i\) to equal \(1/2\), hence precisely two of them, establishing both optimality and the equality classification. For one probe \(P_{(-1)}=0\), and \((A\omega)_i/\omega_i=a_i\). The two-dimensional example follows by inspecting the two possible values of \(t_1t_2\).

**2. Gaussian moment threshold.** For \(A=aI_n\) and \(2\le k\le n\), \(P_{(-j)}\) has almost-sure rank \(k-1\) and is independent of \(\omega_j\). Its distribution is Haar-uniform among proper nonzero subspaces, so for each coordinate \(i\), almost surely \(0<(P_{(-j)})_{ii}<1\). From \(P^2=P\),
\[
 \sum_{\ell\ne i}P_{i\ell}^2=P_{ii}(1-P_{ii})>0.
\]
Since \(A=aI_n\),
\[
 Z_{j,i}-a=-a\sum_{\ell\ne i}(P_{(-j)})_{i\ell}\frac{\omega_{j,\ell}}{\omega_{j,i}}.
\]
For \(0<p<1\), the \(p\)-moment exists by subadditivity \(|\sum z_\ell|^p\le\sum|z_\ell|^p\), the uniform bound \(|P_{i\ell}|\le1\), and finite fractional moments of ratios of independent Gaussians. To show divergence for \(p\ge1\), fix all Gaussian coordinates other than \(\omega_{1,i}=s\). As \(s\to0\), the contribution from \(j=1\) is \(C/s\), with
\[
 C=-\frac a k\sum_{\ell\ne i}(P_{(-1)})_{i\ell}\omega_{1,\ell}.
\]
This coefficient is nonzero almost surely: conditional on \(P_{(-1)}\), it is a nondegenerate centered Gaussian. Every other summand is locally bounded as a function of \(s\), for almost every fixed remaining set of coordinates: its leave-one-out projector has constant rank in a neighborhood of zero (indeed full column rank of the relevant sketch almost surely at zero), and the denominator \(\omega_{j,i}\) is fixed nonzero for \(j\ne1\). Consequently \(\widehat d_i-a=C/s+O(1)\), and the Gaussian density is positive at zero. The conditional integral of \(|C/s+O(1)|^p\) diverges exactly when \(p\ge1\); Tonelli gives unconditional divergence. At \(k=1\), every projector is zero; at \(k\ge n+1\), each leave-one-out sketch spans all of \(\mathbb R^n\) almost surely, so all residual contributions vanish and the projected diagonal is exact.

**3. Exact signed-tail constant.** For \(n=k=2\), put \(U=\omega_{1,2}/\omega_{1,1}\) and \(V=\omega_{2,2}/\omega_{2,1}\). They are independent standard Cauchy variables. The two rank-one projectors give
\[
 \widehat d_1-a=-\frac a2 UV\left(\frac1{1+U^2}+\frac1{1+V^2}\right).
\]
For \(F=UV[(1+U^2)^{-1}+(1+V^2)^{-1}]\), partition the plane into \(|U|\ge|V|\) and \(|V|>|U|\), equal in their limiting contributions. On the first region, with fixed \(V=v\), \(F/U\to v/(1+v^2)\) as \(|U|\to\infty\). The standard Cauchy tail gives
\[
 \lim_{t\to\infty}t\Pr(F>t,\ |U|\ge|V|\mid V=v)
 =\frac{|v|}{\pi(1+v^2)}.
\]
For domination, on this region \(|F|\le 2|U|\,|v|/(1+v^2)\), so the scaled conditional probability is at most \(4|v|/[\pi(1+v^2)]\), integrable against the Cauchy density. Therefore dominated convergence and \(\mathbb E[|V|/(1+V^2)]=1/\pi\) yield \(1/\pi^2\) from each region. The total positive-tail coefficient for \(F\) is \(2/\pi^2\); symmetry supplies the negative tail. Multiplying by \(a/2\) proves the stated \(a/\pi^2\) signed-tail constants for \(\widehat d_1-a\).

## Verification

Run `python verification/check_xdiag.py` with Python 3 and NumPy. The standalone program enumerates exact sign configurations with rational arithmetic; cross-checks the projector identities, covariance, sharp bound, Gaussian leave-one-out phase endpoints and local pole residues; and estimates the sharp signed-tail constant using seeded simulation. The archived run printed `PASS: 8023 analytical/enumerative/Monte Carlo checks`. Its exhaustive *finite* checks and simulation do not substitute for the analytic assertions above. Exact enumeration is only across the finite dimensions and coefficient configurations specified in the program.

## Relationship to prior work

Epperly, Tropp and Webber define the exchangeable leave-one-out diagonal estimator XDiag (their equations (15)–(16)) and explicitly emphasize Rademacher probes for its efficient implementation. This result analyzes the literal formula on nonzero diagonal positive-semidefinite matrices: it supplies the exact two-probe covariance and sharp mean-square error, despite zero disagreement between its two leave-one-out components. The Gaussian statement deliberately studies a formal change of probe law not prescribed by the sign-specialized implementation. Hallman, Ipsen and Saibaba study the distinct standard product-probe diagonal estimator and its Gaussian concentration bounds; those results neither cover nor conflict with moment failure for a *coordinate-quotient* estimator. The older normalized quotient estimator also remains exact on scalar matrices; these risk laws are estimator-specific.

## Limitations

The sign-probe covariance and optimal bound are proved only for two probes and real diagonal positive-semidefinite matrices. The Gaussian heavy-tail phase is proved only for positive scalar matrices with the literal coordinate division, not for a recommended software implementation or clipped/stabilized variant. No claim is made that the supported XDiag implementation fails or that XDiag authors recommend Gaussian probes. The vanishing leave-one-out component disagreement is an illustrative diagnostic, not a claim about a published XDiag variance estimator. The sharp signed-tail constant is proved for exactly two dimensions and two Gaussian probes. No running-time comparison or higher-rank/sketched floating-point guarantee is asserted. Independent audit has not been performed.

## References

1. E. N. Epperly, J. A. Tropp, and R. J. Webber, *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation*, first publicly posted 2023-01-19, arXiv:2301.07825, https://arxiv.org/abs/2301.07825. Primary estimator specification: Section 2.4, equations (15)–(16).
2. E. Hallman, I. C. F. Ipsen, and A. K. Saibaba, *Monte Carlo Methods for Estimating the Diagonal of a Real Symmetric Matrix*, arXiv:2202.02887, https://arxiv.org/abs/2202.02887. Comparison with the standard product-probe diagonal estimator.
