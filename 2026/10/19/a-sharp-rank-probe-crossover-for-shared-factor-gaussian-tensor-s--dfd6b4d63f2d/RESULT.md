# A sharp rank–probe crossover for shared-factor Gaussian tensor sketches

## Finding
For a fixed nonzero real matrix \(M\) of rank \(r\) with nonzero singular values \(s_1,\ldots,s_r\) and \(F=\|M\|_F\), consider a Gaussian tensor probe that **reuses one left Gaussian factor** across \(\ell\) right-factor samples. Draw \(u\sim N(0,I_m)\) once and independently draw \(v_1,\ldots,v_\ell\sim N(0,I_n)\). Define the inverse norm estimate
\[
Q_\ell(M)=\frac{\sqrt\ell\,F}{(\sum_{j=1}^\ell(u^\top Mv_j)^2)^{1/2}}.
\]
All denominators are positive almost surely. With \(\tau\to\infty\), the complete sharp lower-tail trichotomy is
\[
\mathbb P\{Q_\ell(M)>\tau\}\sim
\begin{cases}
C_{<}\tau^{-r},&r<\ell,\\
C_{=}\tau^{-r}\log\tau,&r=\ell,\\
C_{>}\tau^{-\ell},&r>\ell,
\end{cases}
\]
with positive finite **explicit** constants
\[
C_{<}=\frac{(\ell F^2)^{r/2}\Gamma((\ell-r)/2)}{2^r\Gamma(1+r/2)\Gamma(\ell/2)\prod_{i=1}^r s_i},
\quad C_{=}=\frac{r^{1+r/2}F^r}{2^r\Gamma(1+r/2)^2\prod_{i=1}^r s_i},
\]
\[
C_{>}=\frac{(\ell F^2)^{\ell/2}}{2^{\ell/2}\Gamma(1+\ell/2)}\;\mathbb E\left(\sum_{i=1}^r s_i^2G_i^2\right)^{-\ell/2},
\]
where the \(G_i\) are independent real standard Gaussians. The expectation in \(C_{>}\) is finite and, writing \(p=\ell/2\), equals
\[
\frac{1}{\Gamma(p)}\int_0^\infty t^{p-1}\prod_{i=1}^r(1+2s_i^2t)^{-1/2}\,dt.
\]
It follows that for every \(p>0\), \(\mathbb E[Q_\ell(M)^p]<\infty\) **if and only if** \(p<\min(r,\ell)\). Thus adding probes beyond matrix rank does not improve the polynomial power of the inverse-estimate tail; at equality there is an additional logarithmic penalty.

More strongly, couple all \(Q_\ell\) using a single left factor and an infinite iid right-factor sequence. Then
\[
Q_\ell(M)\xrightarrow[\ell\to\infty]{\mathrm{a.s.}}
\frac{F}{\|M^\top u\|_2},
\]
a nonconstant nondegenerate random variable. The reused-factor sketch does not concentrate about the true norm even with infinitely many right-side probes.

## Assumptions and scope
The matrices and Gaussians are **real**. The integers \(m,n,r,\ell\) are fixed for each tail limit, \(1\le r\le\min(m,n)\), \(\ell\ge1\), and all \(s_i>0\) are held fixed. The matrix is deterministic, independent of the probes. One left Gaussian vector is shared across all \(\ell\) probes, while the right vectors are independent of each other and of the left vector. No normalization by sample-estimated matrix quantities is used. The limit in \(\tau\) does not assert uniformity for singular values approaching zero. The infinite-probe assertion uses a common probability space for the same left vector and all right draws.

## Proof
**Step 1: exact probability factorization.** Let \(M=U\operatorname{diag}(s_i)V^\top\) be its compact singular-value decomposition. By rotational invariance, \(G_i=(U^\top u)_i\) are iid \(N(0,1)\), and
\[
S=\|M^\top u\|_2^2=\sum_{i=1}^r s_i^2G_i^2.
\]
Conditionally on \(u\), the numbers \(u^\top Mv_j\) are iid \(N(0,S)\). Dividing by \(\sqrt S\) gives an independent iid standard-Gaussian family even after unconditioning: its conditional law does not depend on \(u\). Hence
\[
\sum_{j=1}^\ell(u^\top Mv_j)^2\;\stackrel d=\;S W,
\qquad W\sim\chi^2_\ell,\quad S\perp W.
\]
In particular, \(\mathbb P(Q_\ell>\tau)=\mathbb P\{SW<\ell F^2/\tau^2\}\).

**Step 2: small-ball coefficients.** The Gaussian density of \((s_1G_1,\ldots,s_rG_r)\) is smooth at the origin and takes the value \((2\pi)^{-r/2}(\prod_i s_i)^{-1}\). Integrating over the radius-\(\sqrt t\) ball gives
\[
\mathbb P(S<t)=a_S t^{r/2}(1+O(t)),\quad
 a_S=\frac{1}{2^{r/2}\Gamma(1+r/2)\prod_i s_i}.
\]
Likewise \(\mathbb P(W<t)=a_Wt^{\ell/2}(1+O(t))\), with \(a_W=[2^{\ell/2}\Gamma(1+\ell/2)]^{-1}\). Their positive densities have derivatives at the corresponding powers: \(f_S(t)\sim (r/2)a_St^{r/2-1}\) and \(f_W(t)\sim(\ell/2)a_Wt^{\ell/2-1}\), obtained directly by differentiation of their radial integral formulas.

**Step 3: an elementary product small-ball lemma.** Suppose independent strictly positive random variables \(X,Y\) have near-zero distribution functions \(a_Xt^\alpha(1+O(t))\) and \(a_Yt^\beta(1+O(t))\), and corresponding densities \(\alpha a_Xt^{\alpha-1}(1+O(t))\) and \(\beta a_Yt^{\beta-1}(1+O(t))\). If \(\alpha<\beta\), then
\[
\mathbb P(XY<t)\sim a_Xt^\alpha\,\mathbb E[Y^{-\alpha}].
\]
Indeed, \(\mathbb P(X<t/y)/t^\alpha\to a_X y^{-\alpha}\), bounded above by \(Cy^{-\alpha}\) uniformly in \(t\) and \(y>0\), since \(F_X(z)\le Cz^\alpha\) globally; this is integrable because \(\beta>\alpha\). The case \(\alpha>\beta\) is symmetric. For \(\alpha=\beta\), in the integral \(\int_0^\infty F_X(t/y)f_Y(y)dy\), fix a small \(\varepsilon>0\) and split at \(y=t/\varepsilon\) and \(y=\varepsilon\). The two outer pieces are \(O_\varepsilon(t^\alpha)\), using the same small-ball bounds. Uniform asymptotic expansions on the central interval give
\[
\alpha a_Xa_Yt^\alpha\int_{t/\varepsilon}^{\varepsilon}\frac{dy}{y}
+O_\varepsilon(t^\alpha)=\alpha a_Xa_Yt^\alpha\log(1/t)+O_\varepsilon(t^\alpha).
\]
To justify the uniform error estimate, the density and CDF relative errors are \(O(y)\) and \(O(t/y)\); the integrals of these error terms over the central interval are \(O_\varepsilon(t^\alpha)\). This proves the critical logarithmic coefficient without inferring an infinite-dimensional conclusion from experiments.

**Step 4: constants, moments, and infinite-probe limit.** Apply Step 3 with \(\alpha=r/2\), \(\beta=\ell/2\), and \(t=\ell F^2/\tau^2\). For \(r<\ell\), the standard chi-square integral gives \(\mathbb EW^{-r/2}=2^{-r/2}\Gamma((\ell-r)/2)/\Gamma(\ell/2)\), hence \(C_<\). For \(r>\ell\), the Gaussian Laplace transform \(\mathbb Ee^{-tS}=\prod_i(1+2s_i^2t)^{-1/2}\) and the Gamma integral produce \(C_>\), finite exactly when \(r>\ell\). At \(r=\ell\), the factor \(\log(1/t)\sim 2\log\tau\) yields \(C_=\). Since these constants are strictly positive, integrating \(p\int_0^\infty\tau^{p-1}\mathbb P(Q_\ell>\tau)\,d\tau\) proves the precise inverse-moment cutoff, including divergence at equality. Finally the conditional strong law gives \(\ell^{-1}\sum_j(u^\top Mv_j)^2\to S>0\) almost surely. This proves the final nonconcentration statement.

**Example.** At \(r=\ell=2\) and \(M=I_2/\sqrt2\), the factors \(S\) and \(W/2\) are independent unit exponentials. In this example \(\mathbb P(Q_2>\tau)\sim 2\tau^{-2}\log\tau\), despite using two right-side probes. At \(r=2\), \(\ell=3\), with \(M=I_2/\sqrt2\), the leading law is instead \(3\tau^{-2}\). Both facts follow from the stated constants, not a finite sample fit.

## Verification
The accompanying standalone `checks.py` evaluates the exact chi-square product integral for isotropic matrices, compares it with the leading constants, and checks the closed-form critical example. The checker is a finite numerical cross-check, not the proof of the asymptotic statement. The proof above covers **all** finite dimensions, matrix ranks, probe counts, and fixed nonzero singular spectra satisfying the hypotheses.

## Relationship to prior work
Bujanović, Grubišić, Kressner and Lam (2024; arXiv:2405.11962v1), especially Theorems 3 and 5, study Khatri–Rao products of **two independent Gaussian matrices**, hence independent Gaussian factor columns across samples. The present construction replaces the columns of **one** factor by the same Gaussian vector; the published embedding bound does **not** cover that altered dependence. Bujanović and Kressner (2020; arXiv:2004.06433v2), sections 2–3, analyze random rank-one estimators and independently repeated probes, not reuse of a single factor. Güttel, Kressner and Vandereycken (2022; arXiv:2211.12175v1) analyze independent bilinear Gaussian probes in randomized nonlinear eigenvalue approximation, a related motivation without this shared-factor law. Meyer and Avron (2023; arXiv:2309.04952v1) investigate tensor probe trace estimators, again with different sampling dependencies. The elementary product-distribution lemma is classical probability in spirit; originality asserted here is the **sharp rank-versus-probe trichotomy and fixed-factor inconsistency for the explicitly dependent tensor-sketch model**, not a novel Gamma identity or a claim about all tensor sketches.

## Limitations
This is a norm-estimation/validation calculation for a *specified* shared-factor sketch, not a new convergence or subspace embedding guarantee for standard Khatri–Rao sketches. It does not apply to fully independent left and right factors, complex Gaussians without adjusting constants, correlated right factors, matrices fitted using the same sketch, or singular spectra varying with the tail threshold. The lower-tail constants may be of limited practical size outside the extreme-tail regime. The literature comparison does not constitute exhaustive proof that no equivalent special case appears in unindexed work. No independent external audit has been performed.

## References
1. Z. Bujanović, L. Grubišić, D. Kressner, and H. Y. Lam, *Subspace embedding with random Khatri–Rao products and its application to eigensolvers*, arXiv:2405.11962v1 (first publicly posted 2024-05-20), especially Sections 1–2.
2. Z. Bujanović and D. Kressner, *Norm and trace estimation with random rank-one vectors*, arXiv:2004.06433v2 (originally posted 2020-04-14), Sections 2–3. Primary MSC 65F35.
3. S. Güttel, D. Kressner, and B. Vandereycken, *Randomized sketching of nonlinear eigenvalue problems*, arXiv:2211.12175v1 (2022-11-22), Section 3.
4. R. A. Meyer and H. Avron, *Hutchinson's estimator is bad at Kronecker-trace-estimation*, arXiv:2309.04952v1 (2023), for contrasting independently sampled tensor-probe behavior.
