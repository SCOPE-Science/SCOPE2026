# Exact essential norm of the Hilbert matrix on the nonclassical Bloch scale

## Finding

Let \(1<\alpha<2\). On the complex disk Bloch-type Banach space \(\mathcal B^\alpha\), equipped with the particular norm
\[
\|f\|_{\mathcal B^\alpha}=|f(0)|+\sup_{z\in\mathbb D}(1-|z|^2)^\alpha|f'(z)|,
\]
let \(\mathcal H\) denote the classical Hilbert matrix operator, realized equivalently by
\[
(\mathcal Hf)(z)=\int_0^1\frac{f(t)}{1-tz}\,dt.
\]
Then \(\mathcal H:\mathcal B^\alpha\to\mathcal B^\alpha\) is bounded, and its **exact essential norm** (operator-norm distance to all compact endomorphisms) is
\[
\boxed{\|\mathcal H\|_{\mathrm e}=\operatorname B(\alpha-1,2-\alpha)
=\Gamma(\alpha-1)\Gamma(2-\alpha)
=\frac{\pi}{\sin(\pi(\alpha-1))}.}
\]
For instance the essential norm at \(\alpha=3/2\) is \(\pi\). The assertion concerns the standard derivative-weighted Bloch norm displayed above; changing to an equivalent but differently normalized norm need not preserve the numerical constant.

## Assumptions and scope

The domain is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), the scalar field is \(\mathbb C\), and \(\alpha\) is a fixed real number strictly between \(1\) and \(2\). The norm has the additive value-at-origin component, not merely the Bloch seminorm. Compactness and essential norm are those of bounded complex-linear operators on this Banach space. No endpoint \(\alpha=1\) or \(\alpha=2\), measure-valued generalized Hilbert operator, or other target space is covered.

Write \(\|f\|_* = \sup_z (1-|z|^2)^\alpha|f'(z)|\), and set
\[
F(t)=\int_0^t(1-s^2)^{-\alpha}\,ds,\qquad
A_\alpha(r)=(1-r^2)^\alpha\int_0^1\frac{tF(t)}{(1-tr)^2}\,dt,
\qquad
B_\alpha(r)=(1-r^2)^\alpha\int_0^1\frac{t}{(1-tr)^2}\,dt.
\]

## Proof

**1. Boundary-kernel computation and boundedness.** Every \(f\in\mathcal B^\alpha\) obeys
\[
|f(t)|\le |f(0)|+\|f\|_*F(t)\qquad(0\le t<1).
\]
Since \(\alpha<2\), \(F\) is integrable on \((0,1)\): as \(t\uparrow1\),
\[
F(t)\sim\frac{2^{-\alpha}}{\alpha-1}(1-t)^{1-\alpha}.
\]
In particular the Hilbert integral is locally uniformly convergent in \(z\) and differentiable under the integral:
\[
(\mathcal Hf)'(z)=\int_0^1\frac{tf(t)}{(1-tz)^2}\,dt.
\]
Hence for \(r=|z|\),
\[
(1-r^2)^\alpha |(\mathcal Hf)'(z)|\le |f(0)|B_\alpha(r)+\|f\|_*A_\alpha(r).
\]
Put \(h=1-r\) and substitute \(u=(1-t)/h\). The displayed asymptotic for \(F\), together with \(1-tr=h(1+(1-h)u)\), gives
\[
\lim_{r\uparrow1}A_\alpha(r)
=\frac{1}{\alpha-1}\int_0^\infty\frac{u^{1-\alpha}}{(1+u)^2}\,du
=\frac{\operatorname B(2-\alpha,\alpha)}{\alpha-1}
=\operatorname B(\alpha-1,2-\alpha)=:C_\alpha.
\]
Here dominated convergence is valid because \(F(1-hu)\le C(hu)^{1-\alpha}\) for \(0<hu<1\), and, for \(h\le1/2\), the scaled integrand is bounded by a constant times \(u^{1-\alpha}/(1+u/2)^2\), integrable at both endpoints exactly when \(1<\alpha<2\). Similarly \(B_\alpha(r)=O((1-r)^{\alpha-1})\to0\). Both functions are continuous and bounded on \([0,1)\). The derivative estimate and \(|(\mathcal H f)(0)|\le |f(0)|+\|f\|_*\int_0^1F(t)dt\) prove boundedness.

**2. Essential-norm upper bound.** For \(0<\rho<1\), let \((D_\rho g)(z)=g(\rho z)\). The operator \(D_\rho\mathcal H\) is compact from \(\mathcal B^\alpha\) to itself: its unit-ball images have uniformly bounded analytic extensions on a disk of radius greater than one, so their Taylor polynomials approximate them uniformly in the Bloch norm. Equivalently, use normal-family compactness on \(|z|\le R>\rho\) and Cauchy bounds on the derivatives.

The difference \(\mathcal H-D_\rho\mathcal H\) vanishes at the origin. Its derivative kernel has a power series with nonnegative coefficients:
\[
\frac{1}{(1-tz)^2}-\frac{\rho}{(1-\rho tz)^2}
=\sum_{k=0}^\infty(k+1)(1-\rho^{k+1})t^kz^k.
\]
Thus the modulus is at most the corresponding expression at \(r=|z|\), and this nonnegative radial expression is bounded by \((1-tr)^{-2}\). Define
\[
A_{\alpha,\rho}(r)=(1-r^2)^\alpha\int_0^1tF(t)
\left(\frac1{(1-tr)^2}-\frac{\rho}{(1-\rho tr)^2}\right)dt
\]
and define \(B_{\alpha,\rho}\) by replacing \(F(t)\) with \(1\). Then
\[
\|\mathcal H-D_\rho\mathcal H\|
\le\sup_{0\le r<1}\max\{A_{\alpha,\rho}(r),B_{\alpha,\rho}(r)\}.
\]
On every compact interval \(0\le r\le R<1\), both expressions tend uniformly to zero as \(\rho\uparrow1\), by dominated convergence and the integrability of \(F\). On \(R<r<1\), positivity gives \(A_{\alpha,\rho}(r)\le A_\alpha(r)\) and \(B_{\alpha,\rho}(r)\le B_\alpha(r)\). First take \(R\uparrow1\), then \(\rho\uparrow1\): the boundary limits in Step 1 yield
\[
\limsup_{\rho\uparrow1}\|\mathcal H-D_\rho\mathcal H\|\le C_\alpha.
\]
Since every \(D_\rho\mathcal H\) is compact, \(\|\mathcal H\|_{\mathrm e}\le C_\alpha\).

**3. Weakly-null boundary spikes and lower bound.** For integers \(n\ge2\), define \(w_n=1-n^{-4}\), and take the unique analytic function \(f_n\) with \(f_n(0)=0\) and
\[
f_n'(z)=\frac{z^n}{2^\alpha(1-w_nz)^\alpha}.
\]
The branch is the analytic branch equal to one at \(z=0\). For \(r=|z|\),
\[
(1-r^2)^\alpha|f_n'(z)|
\le r^n\left(\frac{1-r^2}{2(1-w_nr)}\right)^\alpha\le1.
\]
In particular \(\|f_n\|_{\mathcal B^\alpha}\le1\). Each \(f_n\) is in the *little* Bloch-type space \(\mathcal B^\alpha_0\), since its derivative is bounded on the closed disk, and \(f_n\to0\) locally uniformly, by the factor \(z^n\).

Crucially, \(f_n\rightharpoonup0\) weakly in the full \(\mathcal B^\alpha\). Indeed, \(\mathcal B^\alpha_0\) is isometrically a closed subspace of \(\mathbb C\oplus_1 C_0(\mathbb D)\) under
\[
f\longmapsto\big(f(0),\ (1-|z|^2)^\alpha f'(z)\big).
\]
The second components are uniformly bounded and converge pointwise to zero, so they converge weakly to zero in \(C_0(\mathbb D)\) by dominated convergence against every finite regular Borel measure. Hahn--Banach transfers this weak convergence to \(\mathcal B^\alpha_0\); continuous inclusion transfers it to \(\mathcal B^\alpha\). Thus any compact \(K:\mathcal B^\alpha\to\mathcal B^\alpha\) has \(\|Kf_n\|\to0\).

Set \(h_n=n^{-2}\) and \(r_n=1-h_n\). For each \(u>0\), a change of variables in the integral defining \(f_n\) gives
\[
\lim_{n\to\infty}h_n^{\alpha-1}f_n(1-h_nu)
=\frac{u^{1-\alpha}}{2^\alpha(\alpha-1)}.
\]
To see this rigorously, express the left side by substituting \(s=1-h_nv\) in the defining integral. Its positive integrand is
\[
2^{-\alpha}(1-h_nv)^n\big(v+n^{-2}(1-h_nv)\big)^{-\alpha},
\]
integrated for \(v\) from \(u\) to \(h_n^{-1}\); it converges pointwise to \(2^{-\alpha}v^{-\alpha}\), and is dominated by \(2^{-\alpha}v^{-\alpha}\) on \([u,\infty)\). Consequently the claimed limit follows for each \(u>0\).

The same substitution in the derivative of \(\mathcal Hf_n\), together with \(0\le f_n(t)\le F(t)\) on \([0,1)\), gives by dominated convergence
\[
\begin{aligned}
\lim_{n\to\infty}(1-r_n^2)^\alpha(\mathcal Hf_n)'(r_n)
&=\frac1{\alpha-1}\int_0^\infty\frac{u^{1-\alpha}}{(1+u)^2}\,du\\
&=C_\alpha.
\end{aligned}
\]
For clarity, the domination after rescaling is the same integrable function \(Cu^{1-\alpha}/(1+u/2)^2\) used in Step 1, because \(f_n(t)\le F(t)\). Thus \(\liminf_n\|\mathcal Hf_n\|\ge C_\alpha\). For any compact \(K\),
\[
\|\mathcal H-K\|\ge\limsup_{n\to\infty}
(\|\mathcal Hf_n\|-\|Kf_n\|)\ge C_\alpha.
\]
Taking the infimum over \(K\), and combining with Step 2, proves the exact essential norm formula.

## Verification

The boundary rescaling can be checked independently by observing
\[
\int_0^\infty\frac{u^{1-\alpha}}{(1+u)^2}\,du
=\operatorname B(2-\alpha,\alpha)=(\alpha-1)\Gamma(\alpha-1)\Gamma(2-\alpha).
\]
The analytic upper and lower bounds are exact; no finite-dimensional truncation, numeric extrapolation or external computer algebra is needed to establish the infinite-dimensional statement. The included `CHECK_NUMERICS.py` evaluates the positive kernel integral and compares it with the Beta constant for selected values; it is a diagnostic only, not a proof.

## Relationship to prior work

Cui, Lin and Lu determine the **full operator norm** and norm-attaining functions for this Hilbert operator on \(\mathcal B^\alpha\). The present result instead determines its **distance to every compact operator**. Even when operator and essential norms happen to agree, an exact operator-norm calculation alone does not prove that equality: one needs a weakly-null lower-bound family. The boundary spikes above supply that missing obstruction and the radial compact approximation gives its matching upper bound.

Li and Zhou study generalized Hilbert matrices with source Bloch-type spaces but target **classical** Bloch or BMOA, which differs from the target \(\mathcal B^\alpha\) here. Lindström, Miihkinen and Norrbo compute essential norms on weighted Bergman, Hardy, and weighted sup-norm spaces, rather than on derivative-weighted Bloch spaces. Beltrán-Meneu, Bonet and Jordá study weighted sup-norm growth spaces. Their results and methods do not directly imply the particular formula stated here. The construction requires the derivative-weighted boundary geometry.

## Limitations

The assertion is established only for \(1<\alpha<2\) and the precise additive Bloch norm displayed. The argument does not determine the operator norm nor its norm-attaining functions, and does not extend automatically to generalized moment measures or logarithmic Bloch targets. The available abstract of the most directly related recent preprint does not report an essential-norm result, but its full text was inaccessible during literature examination; overlap in uninspected sections cannot be excluded. The same caution applies to unindexed literature. The theorem receives no independent external proof certification here.

## References

1. P. Cui, Z. Lin, Y. Lu, *Norm of the Hilbert Matrix Operator on Bloch-Type Spaces*, arXiv:2609.27812v1 (2026), https://arxiv.org/abs/2609.27812.
2. S. Li, J. Zhou, *Essential norm of generalized Hilbert matrix from Bloch type spaces to BMOA and Bloch space*, AIMS Mathematics **6** (2021), 3305--3318, https://doi.org/10.3934/math.2021198.
3. M. Lindström, S. Miihkinen, D. Norrbo, *Exact essential norm of generalized Hilbert matrix operators on classical analytic function spaces*, arXiv:2201.09591 (2022), https://arxiv.org/abs/2201.09591.
4. M. Beltrán-Meneu, J. Bonet, J. Jordá, *Generalized Hilbert operators acting on weighted spaces of holomorphic functions with sup-norms*, Banach Journal of Mathematical Analysis (2024), https://doi.org/10.1007/s43037-024-00395-1.
