# A universal half-moment transition for unoversampled Gaussian Nyström error

## Finding

**Theorem (exact residual law and three sharp moment regimes).** Fix integers \(n\ge r\ge2\), positive numbers \(\lambda_1,\ldots,\lambda_{r-1}\), and \(0<\varepsilon<\min_{i<r}\lambda_i\). Let \(A_\varepsilon\) be any real positive-semidefinite \(n\times n\) matrix whose positive eigenvalues, with multiplicity, are \(\lambda_1,\ldots,\lambda_{r-1},\varepsilon\), and whose remaining eigenvalues vanish. Draw \(\Omega\in\mathbb R^{n\times(r-1)}\) with independent standard-real-Gaussian entries. In exact arithmetic form

\[
\widehat A_\varepsilon=A_\varepsilon\Omega
 (\Omega^{\mathsf T}A_\varepsilon\Omega)^\dagger
 \Omega^{\mathsf T}A_\varepsilon,
\qquad L_\varepsilon=\|A_\varepsilon-\widehat A_\varepsilon\|_2.
\]

Then, almost surely, the residual is positive semidefinite of rank one and
\(L_\varepsilon=\|A_\varepsilon-\widehat A_\varepsilon\|_{\mathrm F}=\|A_\varepsilon-\widehat A_\varepsilon\|_*\). For a Haar-uniform \(g\) on the unit sphere in \(\mathbb R^r\), there is an exact distributional identity

\[
L_\varepsilon\overset{d}{=}\left(\sum_{i=1}^{r-1}\frac{g_i^2}{\lambda_i}
 +\frac{g_r^2}{\varepsilon}\right)^{-1}.
\tag{1}
\]

Define \(c_r=\Gamma(r/2)/(\sqrt\pi\,\Gamma((r-1)/2))\). Independently of the last coordinate \(t=g_r\), let \(u\) be Haar-uniform on the unit sphere in \(\mathbb R^{r-1}\), and set \(q(u)=\sum_{i<r}u_i^2/\lambda_i\). For every fixed real \(s>0\), the complete moment asymptotics as \(\varepsilon\downarrow0\) are

\[
\begin{aligned}
0<s<\tfrac12:\quad&
\mathbb E[L_\varepsilon^s]\sim
 \varepsilon^s\frac{\Gamma(r/2)\Gamma(1/2-s)}
 {\sqrt\pi\,\Gamma(r/2-s)},\\
s=\tfrac12:\quad&
\mathbb E[\sqrt{L_\varepsilon}]\sim
 c_r\sqrt\varepsilon\log(1/\varepsilon),\\
s>\tfrac12:\quad&
\mathbb E[L_\varepsilon^s]\sim
 c_r B(1/2,s-1/2)\sqrt\varepsilon\,
 \mathbb E_u[q(u)^{1/2-s}],
\end{aligned}
\tag{2}
\]

where \(B\) is Euler's beta function. Every displayed leading constant is finite and strictly positive. In particular,

\[
\mathbb E L_\varepsilon\sim
\sqrt\pi\frac{\Gamma(r/2)}{\Gamma((r-1)/2)}
\mathbb E_u\left[q(u)^{-1/2}\right]\sqrt\varepsilon.
\tag{3}
\]

The optimal rank-\((r-1)\) error in **each** of the spectral, Frobenius, and nuclear norms is \(\varepsilon\); consequently the expected approximation factor for the unoversampled Gaussian Nyström rule diverges at the sharp rate \(\varepsilon^{-1/2}\), although \(L_\varepsilon/\varepsilon\) converges in distribution to \(g_r^{-2}\) (finite almost surely).

The rare-event mechanism can also be quantified without using moments. For every fixed threshold \(0<y<\min_{i<r}\lambda_i\),

\[
\lim_{\varepsilon\downarrow0}
\frac{\mathbb P\{L_\varepsilon>y\}}{\sqrt\varepsilon}
 =2c_r\mathbb E_u\sqrt{1/y-q(u)}>0.
\tag{4}
\]

For \(r=2\), writing the single large eigenvalue as \(\lambda>0\), the expected error is in fact **exact at every positive** \(\varepsilon\):
\[
\mathbb E L_\varepsilon=\sqrt{\lambda\varepsilon}.
\tag{5}
\]

## Assumptions and scope

All claims concern the **real Gaussian**, exact-arithmetic Nyström approximation with exactly \(r-1\) sketch columns and a matrix with exactly \(r\) positive eigenvalues; there are no independently added oversampling columns. The dimension \(n\) and the positive spectral profile \(\lambda_1,\ldots,\lambda_{r-1}\) are fixed while the single small eigenvalue \(\varepsilon\) tends to zero. No assumption is made that the large eigenvalues coincide; their order does not matter. Singular nullspace directions beyond rank \(r\) do not affect the distribution. In (2), \(s\) indexes the order of a *moment*, not an extra sketch dimension. Gamma and beta functions have their standard Euler integral definitions.

## Proof

**1. An exact spherical representation.** Restrict to the \(r\)-dimensional support of \(A_\varepsilon\), use an orthonormal eigenbasis, and write \(D_\varepsilon=\operatorname{diag}(\lambda_1,\ldots,\lambda_{r-1},\varepsilon)\). The projected sketch \(G\in\mathbb R^{r\times(r-1)}\) remains iid standard Gaussian and has rank \(r-1\) almost surely. For \(Y=D_\varepsilon^{1/2}G\), the identity for orthogonal projectors gives

\[
\widehat D_\varepsilon=D_\varepsilon^{1/2}P_YD_\varepsilon^{1/2},
\quad E_\varepsilon=D_\varepsilon^{1/2}(I-P_Y)D_\varepsilon^{1/2}.
\]

The one-dimensional kernel of \(G^{\mathsf T}\) has a Haar-uniform unit normal \(g\). Since \(Y^{\mathsf T}D_\varepsilon^{-1/2}g=G^{\mathsf T}g=0\), the unit normal to \(\operatorname{range}(Y)\) is

\[
h=\frac{D_\varepsilon^{-1/2}g}
 {\sqrt{g^{\mathsf T}D_\varepsilon^{-1}g}}.
\]

Consequently \(E_\varepsilon=D_\varepsilon^{1/2}hh^{\mathsf T}D_\varepsilon^{1/2}\) is positive semidefinite of rank one, with unique positive eigenvalue \(\operatorname{tr}E_\varepsilon=h^{\mathsf T}D_\varepsilon h=(g^{\mathsf T}D_\varepsilon^{-1}g)^{-1}\). The nonzero eigenvalues and all three asserted residual norms coincide. This proves (1).

**2. Spherical disintegration.** Write \(g=(\sqrt{1-t^2}\,u,t)\). Here \(u\) and \(t\) are independent, \(u\) is Haar-uniform on \(S^{r-2}\), and \(t\) has density

\[
f_r(t)=c_r(1-t^2)^{(r-3)/2}\mathbf1_{\{|t|<1\}}.
\]

Therefore, using \(q=q(u)\),
\[
L_\varepsilon=\bigl[(1-t^2)q+t^2/\varepsilon\bigr]^{-1}.
\tag{6}
\]

Uniform bounds \(0<1/\max_{i<r}\lambda_i\le q\le1/\min_{i<r}\lambda_i<\infty\) justify the following conditional limits uniformly in \(u\).

**3. Subcritical moments.** When \(0<s<1/2\), (6) gives

\[
0\le (L_\varepsilon/\varepsilon)^s
 =\bigl[t^2+\varepsilon(1-t^2)q\bigr]^{-s}
 \le |t|^{-2s}.
\]

The dominating function is integrable against \(f_r\) precisely when \(s<1/2\). Dominated convergence yields \(\mathbb E |t|^{-2s}\), evaluated by \(t^2\sim\operatorname{Beta}(1/2,(r-1)/2)\); this is the first line of (2).

**4. Supercritical moments.** If \(s>1/2\), separate \(|t|>1/2\), where \(L_\varepsilon^s\le (4\varepsilon)^s\) and its contribution is \(o(\sqrt\varepsilon)\). On \(|t|\le1/2\), put \(t=\sqrt\varepsilon v\). The rescaled integrand converges to \(c_r(q+v^2)^{-s}\) and, using the uniform positive lower bound on \(q\) and the bounded density on this central interval, is dominated by \(C(a+v^2)^{-s}\) for a fixed \(a>0\). This is integrable on the full real line exactly when \(s>1/2\). Hence the limiting integral is

\[
 c_r\mathbb E_u\int_{\mathbb R}(q(u)+v^2)^{-s}\,dv
 =c_r B(1/2,s-1/2)\mathbb E_u q(u)^{1/2-s},
\]

proving the last line of (2) and (3) at \(s=1\).

**5. Critical moment.** At \(s=1/2\), split \(|t|\le1/2\) and its complement. The latter contributes \(O(\sqrt\varepsilon)\). On the central interval, replace \(f_r(t)\) by \(c_r\) and \((1-t^2)q\) by \(q\); since \(q\) ranges in a fixed compact subset of \((0,\infty)\) and \(f_r(t)=c_r(1+O(t^2))\), the combined change is \(O(\sqrt\varepsilon)\) after integration. The leading central contribution is

\[
2c_r\int_0^{1/2}\frac{dt}{\sqrt{q+t^2/\varepsilon}}
 =2c_r\sqrt\varepsilon\,
 \operatorname{arsinh}\left(\frac1{2\sqrt{\varepsilon q}}\right)
 =c_r\sqrt\varepsilon\log(1/\varepsilon)+O(\sqrt\varepsilon).
\]

The error is uniform over the allowed \(q\). This proves the middle line of (2).

**6. Relative error and rare-event tail.** Formula (6) implies \(L_\varepsilon/\varepsilon\to t^{-2}\) almost surely under the fixed spherical coupling, since \(\mathbb P(t=0)=0\). Fix \(0<y<\min_{i<r}\lambda_i\), so \(1/y>q\) for all \(u\). For sufficiently small \(\varepsilon\), conditional on \(u\), the event \(L_\varepsilon>y\) is precisely

\[
 |t|<\left(\frac{1/y-q}{1/\varepsilon-q}\right)^{1/2}
 =\sqrt\varepsilon\,\sqrt{1/y-q}\,(1+o(1)),
\]

uniformly over \(u\). Since \(f_r\) is continuous at zero with value \(c_r\), its probability is \(2c_r\sqrt\varepsilon\sqrt{1/y-q}(1+o(1))\); averaging yields (4). Finally, rank-\((r-1)\) Eckart–Young–Mirsky best-error identities give \(\varepsilon\) in the three norms for this one-eigenvalue tail, so the expected-factor claim follows from (3).

**7. Exact two-dimensional mean.** For \(r=2\), parameterize the uniform unit vector as \(g=(\cos\theta,\sin\theta)\), with \(\theta\) uniform on \([0,2\pi)\). Then

\[
\mathbb E L_\varepsilon
 =\frac2\pi\int_0^{\pi/2}
 \frac{d\theta}{\cos^2\theta/\lambda+\sin^2\theta/\varepsilon}
 =\sqrt{\lambda\varepsilon},
\]

using \(z=\tan\theta\) and the elementary Cauchy integral. This proves (5).

## Verification

A standalone Python checker, `verify.py`, recomputes the Nyström residual directly from the matrix and independently from a null vector of the unweighted Gaussian sketch. It checks positivity/rank-one norm equalities in 140 deterministic-seeded random configurations across four ranks; 16 two-dimensional exact mean quadratures; isotropic asymptotic coefficients at four ranks; moments on both sides of the half-order transition; the rank-three rare-event tail; and an anisotropic two-large-eigenvalue coefficient. Run `python verify.py` with packages pinned in `requirements.txt`. The recorded results appear in `verification_output.txt`. The finite tests only check formulas and implementations; the argument above establishes the statements for all specified sizes and parameter values.

## Relationship to prior work

Persson, Boullé, and Kressner's analysis [1] treats exactly this Gaussian Nyström reconstruction (including singular matrices) but its Frobenius expectation theorem assumes at least four extra sketch columns; its spectral and nuclear expectation bounds assume at least two, and its tail bounds assume at least four. Those bounds neither imply nor preclude this sharp unoversampled one-weak-eigenvalue phase transition. Tropp, Yurtsever, Udell, and Cevher [2] derive expected Schatten-one guarantees using an index strictly below the sketch size in the real case; their formulas do not yield the fixed equal-target-rank, zero-oversampling constants of (2). Gittens and Mahoney [3] derive deterministic error and oversampled Gaussian projection estimates, but not these exact near-singular moments. Carson and Daužickaitė [4] focus on finite precision and quote bounds with nonzero oversampling. Tropp and Webber's survey [5] studies related randomized range-finding algorithms, rather than the present Nyström error law. The identity \(A-\widehat A=A^{1/2}(I-P)A^{1/2}\) is standard and is not claimed as new; the claim is the complete sharp moment and rare-event scaling derived from it.

## Limitations

The result concerns one real-Gaussian, unregularized, untruncated sketch with exactly one weak positive eigenvalue and one-dimensional positive-definite residual. It does **not** analyze power iteration, correlated sketches, multiple weak eigenvalues, complex-Gaussian sketches, rounding errors, regularized cores, additional oversampling, or large-dimensional simultaneous limits. Its moment transition describes \(\varepsilon\to0\), not finiteness of moments for fixed \(\varepsilon>0\) (the error is then bounded). A potentially unindexed equivalent spherical-integral formulation in older matrix-approximation or directional-statistics work cannot be ruled out by targeted indexing searches alone; the exact law (1) is a transformation of standard projection and Haar-sphere identities. Independent validation has not been performed.

## References

[1] D. Persson, N. Boullé, D. Kressner, *Randomized Nyström approximation of non-negative self-adjoint operators*, arXiv:2404.00960 (first submitted 2024-04-01), especially §2.2, Theorems 2.1, 2.4, 2.6. https://arxiv.org/abs/2404.00960

[2] J. A. Tropp, A. Yurtsever, M. Udell, V. Cevher, *Fixed-Rank Approximation of a Positive-Semidefinite Matrix from Streaming Data*, NeurIPS 2017, especially supplementary Theorem A.1. https://www.tropp.caltech.edu/conf/TYUC17-Fixed-Rank-Approximation-supp.pdf

[3] A. Gittens, M. W. Mahoney, *Revisiting the Nyström Method for Improved Large-Scale Machine Learning*, JMLR 17 (2016), §4 and Appendix. https://www.jmlr.org/papers/volume17/gittens16a/gittens16a.pdf

[4] E. Carson, I. Daužickaitė, *Single-Pass Nyström Approximation in Mixed Precision*, SIAM J. Matrix Anal. Appl., DOI 10.1137/22M154079X, §2. https://epubs.siam.org/doi/full/10.1137/22M154079X

[5] J. A. Tropp, R. J. Webber, *Randomized algorithms for low-rank matrix approximation: Design, analysis, and applications*, arXiv:2306.12418, §§2–3. https://arxiv.org/abs/2306.12418
