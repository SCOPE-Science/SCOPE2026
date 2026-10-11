# Complete spherical-harmonic linearization of the supercritical dual \(k\)-Minkowski sphere

## Finding
Let \(1\le k\le n\), \(\alpha>k+1\), \(\beta=\binom{n}{k}\), and \(f\equiv f_0>0\). For the normalized support-function flow on \(\mathbb S^n\)
\[
u_t=-f_0\bigl(u^2+|\bar\nabla u|^2\bigr)^{\alpha/2}G(\bar\nabla^2u+u\bar g)+\beta u,
\qquad G(b)=\frac{\sigma_{n-k}(b)}{\sigma_n(b)},
\]
the stationary round sphere has support function \(u_*\equiv R_*\), where \(R_*=f_0^{-1/(\alpha-k-1)}\). Put \(m=\alpha-k-1\). The Fréchet linearization at \(u_*\) is
\[
L=\frac{k\beta}{n}\bar\Delta-\beta m.
\]
Consequently every spherical harmonic of degree \(\ell\ge0\), satisfying \(\bar\Delta Y_\ell=-\ell(\ell+n-1)Y_\ell\), is an eigenmode with exact eigenvalue
\[
\lambda_\ell=-\beta\left(m+\frac{k}{n}\ell(\ell+n-1)\right).
\]
The degree-zero homothetic mode is the unique slow linear mode and decays at the sharp global exponent \(\beta m\) exhibited by the source's homothetic solutions. Every nonconstant infinitesimal shape mode has decay exponent at least \(\beta(m+k)=\beta(\alpha-1)\), so the exact linear scale-to-shape spectral gap is \(\beta k\).

Equivalently, if an infinitesimal perturbation is expanded as
\[
\varphi=\sum_{\ell\ge0}\varphi_\ell,
\]
with \(\varphi_\ell\) in the degree-\(\ell\) spherical-harmonic space, then the linearized evolution is diagonal:
\[
\varphi_\ell(t)=e^{-\beta\left(m+\frac{k}{n}\ell(\ell+n-1)\right)t}\varphi_\ell(0).
\]
Thus the source's universal rate \(e^{-\beta m t}\) is linearly saturated only by scaling, while genuine shape modes separate from it by an explicit positive gap.

## Assumptions and scope
The statement concerns the constant-data specialization \(f\equiv f_0>0\) of the normalized contracting flow of Sheng--Sheng--Yang in \(\mathbb R^{n+1}\), with \(1\le k\le n\) and \(\alpha>k+1\). The perturbation variable is the support function in inverse Gauss-map coordinates. The spherical Laplacian convention is \(\bar\Delta Y_\ell=-\ell(\ell+n-1)Y_\ell\).

This is an exact Fréchet-linearization statement at the stationary round sphere. It does not assert a nonlinear faster-decay theorem on a scale-normalized manifold of initial data, and it does not alter the source's sharp global exponent, which is already attained by homothetic solutions.

## Proof
Write
\[
r(u)=\sqrt{u^2+|\bar\nabla u|^2},\qquad b[u]=\bar\nabla^2u+u\bar g,
\]
and
\[
\mathcal F(u)=-f_0r(u)^\alpha G(b[u])+\beta u.
\]
At a constant support function \(u\equiv R\), one has \(r=R\), \(b=R\bar g\), and
\[
G(R\bar g)=\beta R^{-k}.
\]
Hence \(\mathcal F(R)=0\) exactly when
\[
f_0R^{\alpha-k-1}=1,
\]
which gives \(R=R_*\).

Let \(u_\varepsilon=R_*+\varepsilon\varphi\). Since the gradient term in \(r^2\) is quadratic at a constant function,
\[
\left.\frac{d}{d\varepsilon}r(u_\varepsilon)\right|_{\varepsilon=0}=\varphi.
\]
Also
\[
\left.\frac{d}{d\varepsilon}b[u_\varepsilon]\right|_{\varepsilon=0}=\bar\nabla^2\varphi+\varphi\bar g.
\]
At \(b=R_*\bar g\), the published derivative formula for \(G\) gives, in an orthonormal frame,
\[
\dot G^{ii}=-R_*^{-2}\binom{n-1}{k-1}R_*^{-(k-1)}
=-\binom{n-1}{k-1}R_*^{-(k+1)}.
\]
Since \(\binom{n-1}{k-1}=(k/n)\beta\), for every symmetric tensor \(\eta\),
\[
DG_{R_*\bar g}[\eta]
=-\frac{k\beta}{n}R_*^{-(k+1)}\operatorname{tr}_{\bar g}\eta.
\]
Taking \(\eta=\bar\nabla^2\varphi+\varphi\bar g\) yields
\[
DG_{R_*\bar g}[\bar\nabla^2\varphi+\varphi\bar g]
=-\frac{k\beta}{n}R_*^{-(k+1)}(\bar\Delta\varphi+n\varphi).
\]
Differentiating \(\mathcal F\) and using \(f_0R_*^{\alpha-k-1}=1\),
\[
\begin{aligned}
D\mathcal F_{R_*}[\varphi]
&=-\alpha\beta\varphi+\frac{k\beta}{n}(\bar\Delta\varphi+n\varphi)+\beta\varphi\\
&=\frac{k\beta}{n}\bar\Delta\varphi-\beta(\alpha-k-1)\varphi.
\end{aligned}
\]
This is the claimed operator \(L\).

The standard spectrum of \(\bar\Delta\) on \(\mathbb S^n\) now gives
\[
\lambda_\ell=-\beta\left(m+\frac{k}{n}\ell(\ell+n-1)\right).
\]
For \(\ell=0\), \(\lambda_0=-\beta m\). For every \(\ell\ge1\), \(\ell(\ell+n-1)\ge n\), with equality only at \(\ell=1\), so
\[
-\lambda_\ell\ge\beta(m+k)=\beta(\alpha-1).
\]
Therefore the constant mode is the unique slow eigenspace and the distance from its decay exponent to the nearest shape exponent is exactly \(\beta k\).

## Verification
The bundled script `artifacts/verify.py` checks the binomial derivative identity
\[
\binom{n-1}{k-1}=\frac{k}{n}\binom nk,
\]
reconstructs the first variation of \(G=\sigma_{n-k}/\sigma_n\) at an isotropic radius tensor using exact rational arithmetic, and checks the degree-zero and degree-one spectral specializations over a finite parameter grid. These computations are consistency checks only; the universal statement is proved symbolically above.

There are two independent source-level checks. The degree-zero eigenvalue \(-\beta m\) is the derivative of the source's exact homothetic logistic ODE. For \(\ell=1\), one has \(\bar\nabla^2\varphi+\varphi\bar g=0\), so the curvature-radius tensor has no first-order change and the remaining radial/support terms give \(-\beta(\alpha-1)\varphi\), exactly as the formula predicts.

## Relationship to prior work
Sheng, Sheng, and Yang, arXiv:2609.35241v1 (first public 2026-09-28), prove global existence and exponential convergence for arbitrary positive angular data when \(\alpha>k+1\). In the constant-data case they identify the limiting sphere \(R_*=f_0^{-1/(\alpha-k-1)}\). Their Remark 6.1 gives an exact homothetic solution and proves that the global exponent \(\beta(\alpha-k-1)\) cannot be improved in general. Their support-function equation and derivative formula for \(G\) are the inputs used here. The paper does not state a spherical-harmonic linearization or a mode-by-mode spectrum.

Li, Sheng, and Wang, *Journal of Geometric Analysis* 30 (2020), 834--860, DOI 10.1007/s12220-019-00169-4, study the isotropic predecessor flow and prove convergence after normalization to a centered sphere. The complete 27-page article was inspected: it derives the normalized support/radial equations, curvature estimates, and exponential gradient decay, but no spherical-harmonic spectral decomposition is stated.

The closest indexed comparison results concern different flows: `2026/10/4/SCOPE-exact-full-linearization-of-a-spherical-alexandrov-fenchel-flow--e83160512089` treats a nonlocal flow in the round sphere, while `2026/10/4/SCOPE-a-curvature-forced-resonance-in-normalized-spherical-sigma-k-alp--ea561adab016` treats centered geodesic spheres for a different spherical \(\sigma_k^\alpha\)-flow. Neither implies the Euclidean dual \(k\)-Minkowski linearization above.

## Limitations
The result is linear. It does not prove that nonlinear solutions whose scale mode has been removed converge globally at the faster exponent \(\beta(\alpha-1)\), nor that a nonlinear modulation can maintain exact orthogonality to the constant mode. An equivalent calculation could exist in unindexed curvature-flow literature under different normalization conventions.

## References
1. H. Sheng, W. Sheng, J. Yang, *Supercritical dual \(k\)-Minkowski flows with general prescribed data: a priori estimates and asymptotic convergence*, arXiv:2609.35241v1, 2026.
2. Q.-R. Li, W. Sheng, X.-J. Wang, *Asymptotic Convergence for a Class of Fully Nonlinear Curvature Flows*, Journal of Geometric Analysis 30 (2020), 834--860, DOI 10.1007/s12220-019-00169-4.
