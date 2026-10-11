# Sharp curvature-radius Hessian phase transition for relative affine area of planar ball-bodies

## Finding

Fix \(R>0\) and \(0<r<R\). For a strictly convex planar body \(K\) with curvature \(\kappa>1/R\), the relative affine area is
\[
\Omega_R(K)=\int_{\partial K}(\kappa-1/R)^{1/3}\,ds.
\]
Let \(K_\varepsilon\) be any two-sided, twice-differentiable \(C^2\)-support-function path through the disk \(B_r\), with \(\operatorname{area}(K_\varepsilon)=\pi r^2\), positive curvature and curvature radius strictly below \(R\) for all sufficiently small \(|\varepsilon|\). Write
\[
h_\varepsilon(\theta)=r+\varepsilon u(\theta)+\varepsilon^2v(\theta)+o_{C^2}(\varepsilon^2),\qquad
w(\theta)=u(\theta)+u''(\theta).
\]
Then \(\int_0^{2\pi}u\,d\theta=0\), and the quadratic deficit is
\[
\Omega_R(B_r)-\Omega_R(K_\varepsilon)
=\varepsilon^2 Q_{R,r}(u)+o(\varepsilon^2),\quad
Q_{R,r}(u)=\frac12\int_0^{2\pi}
\left[\frac{f_R'(r)}r u w-f_R''(r)w^2\right]d\theta,
\]
where \(f_R(t)=[t^2(1-t/R)]^{1/3}\) for \(0<t<R\).

**Sharp area-constrained curvature-radius Hessian law:** for all nontranslation tangent directions, equivalently \(\int w^2>0\),
\[
Q_{R,r}(u)\ge C_{R,r}\int_0^{2\pi}w^2\,d\theta,
\qquad
C_{R,r}=\begin{cases}
\dfrac{f_R(r)(5R-3r)}{18r(R-r)^2},&0<r\le 2R/3,\\[4pt]
\dfrac{f_R(r)R^2}{9r^2(R-r)^2},&2R/3\le r<R.
\end{cases}
\]
Both values agree at \(r=2R/3\). The constant is the exact infimum of the quadratic Rayleigh quotient, not merely an admissible bound. For \(r<2R/3\), equality holds precisely for degree-two Fourier perturbations, up to irrelevant translations; at \(r=2R/3\), every nontranslation tangent direction is an equality direction. For \(r>2R/3\), the infimum is **not attained** by a nontranslation tangent direction and is approached by Fourier degrees tending to infinity. Thus the least-penalized curvature mode changes at the same radius that maximizes the area-unconstrained disk functional.

## Assumptions and scope

The normal angle is \(\theta\in[0,2\pi)\). A support function is \(2\pi\)-periodic, of class \(C^2\), with curvature radius \(\rho=h+h''\) satisfying \(0<\rho<R\). In this class the planar body is an intersection of Euclidean disks of radius \(R\) (a strongly convex or \(R\)-ball-convex body). The path is smooth enough in the perturbation parameter for the displayed second-order expansion; no uniform assertion over perturbation degrees is intended. Invariance under translations leaves the first Fourier harmonics in the nullspace; the area constraint removes the constant harmonic. No assertion concerns the singular endpoints \(r=0\) or \(r=R\), nonsmooth bodies, or finite-amplitude sharpness.

## Proof

For any strictly convex \(C^2\) support function \(h\), the boundary element is \(ds=(h+h'')d\theta\), and \(\kappa=(h+h'')^{-1}\). Thus the displayed definition is exactly
\[
\Omega_R(K)=\int_0^{2\pi} f_R(\rho(\theta))\,d\theta,
\quad f_R(t)=t^{2/3}(1-t/R)^{1/3}.
\]
The area formula is \(\operatorname{area}(K)=\frac12\int h(h+h'')d\theta\). Expand \(h_\varepsilon\) and \(\rho_\varepsilon=r+\varepsilon w+\varepsilon^2(v+v'')+o(\varepsilon^2)\). The first area constraint gives \(\int u=0\), and the second gives
\[
r\int_0^{2\pi}v\,d\theta=-\frac12\int_0^{2\pi}u w\,d\theta.
\]
Since \(\int w=\int u=0\), Taylor expansion of the integrand yields
\[
\Omega_R(K_\varepsilon)=2\pi f_R(r)+\varepsilon^2\left[f_R'(r)\int v+
\frac12 f_R''(r)\int w^2\right]+o(\varepsilon^2).
\]
Substituting the area constraint gives exactly the claimed quadratic form. Direct differentiation, with all quantities evaluated at \(0<r<R\), gives
\[
\frac{f_R'(r)}{f_R(r)}=\frac{2R-3r}{3r(R-r)},\qquad
\frac{f_R''(r)}{f_R(r)}=-\frac{2R^2}{9r^2(R-r)^2}.
\]
Expand the mean-zero real perturbation as
\[
u(\theta)=\sum_{k\ge1}(a_k\cos k\theta+b_k\sin k\theta).
\]
For each \(k\ge2\), the corresponding curvature-radius perturbation is \(w_k=(1-k^2)u_k\). Parseval gives the diagonalization
\[
Q_{R,r}(u)=\frac{\pi}{2}\sum_{k\ge2}(k^2-1)^2(a_k^2+b_k^2)
\left[-f_R''(r)-\frac{f_R'(r)}{r(k^2-1)}\right],
\]
whereas \(\int w^2=\pi\sum_{k\ge2}(k^2-1)^2(a_k^2+b_k^2)\). The exact spectral coefficient is therefore
\[
C_k(R,r)=\frac12\left[-f_R''(r)-\frac{f_R'(r)}{r(k^2-1)}\right].
\]
If \(r<2R/3\), then \(f_R'(r)>0\) and \(C_k\) strictly increases with \(k\), giving its minimum at \(k=2\). Substitution of the two derivatives gives \(C_2=f_R(r)(5R-3r)/[18r(R-r)^2]\). If \(r>2R/3\), then \(f_R'(r)<0\), and \(C_k\) strictly decreases to \(-f_R''(r)/2=f_R(r)R^2/[9r^2(R-r)^2]\), which is never attained by any finite-frequency nonzero perturbation or nonzero square-integrable mixture. At \(r=2R/3\), \(f_R'(r)=0\) and every \(C_k\) coincides. This proves the universal sharp quadratic bounds and all equality/nonattainment statements.

For realizability of every test direction, take
\[
h_\varepsilon(\theta)=\frac{r+\varepsilon\cos(k\theta)}{\sqrt{1-(k^2-1)\varepsilon^2/(2r^2)}}\quad (k\ge2).
\]
Its area is identically \(\pi r^2\) by the support-function area formula, and \(0<h_\varepsilon+h_\varepsilon''<R\) for sufficiently small \(|\varepsilon|\) (depending on \(r,R,k\)). These bodies are \(R\)-ball convex; their quadratic quotient is exactly \(C_k(R,r)\). Consequently the infimum and all claimed attainments are genuine geometric, rather than merely formal, variations. Finally, as \(R\to\infty\) with \(r\) fixed, the degree-two coefficient tends to zero, recovering the affine-symmetry null direction in the classical area-constrained affine surface area problem.

## Verification

The standalone `verify.py` requires Python's standard library only. Run `python verify.py` from the directory containing this document. It independently evaluates the area-preserving harmonic family by numerical midpoint integration and compares the measured second-order deficits with the derived Fourier coefficients at three radius regimes and multiple degrees. It also checks coefficient monotonicity across the transition. The expected success message is `RELATIVE_AFFINE_HESSIAN_FINITE_CHECKS_OK`. These finite tests are a reproducibility cross-check; the derivation above proves the infinite-dimensional result.

## Relationship to prior work

Schütt, Werner and Yalikun introduce the \(R\)-ball floating-body relative affine surface area and its defining curvature integral [1]. Artstein-Avidan and Chor study the unit-radius version and establish an area-unconstrained maximizer at disk radius \(2/3\) [2]. Werner and Yalikun introduce related \(L_p\) relative surface areas [3]. Artstein-Avidan and Florentin establish useful support-function and curvature-radius facts about ball-bodies [4]. The finding here is not a new definition, not the known unconstrained optimum, and not a global finite-amplitude stability inequality: it is the **complete sharp fixed-area curvature-radius Hessian and its mode-selection transition for every disk radius**.

## Limitations

Only strictly positive curvature and strictly sub-\(R\) curvature radii near disks are covered. The Hessian bound is asymptotically sharp along small area-preserving paths, not a global inequality at fixed nonzero Hausdorff distance. At radii larger than \(2R/3\), the optimal coefficient is an unattained spectral infimum approached by increasingly oscillatory perturbations with successively smaller admissible amplitudes. Published mathematical literature not indexed in the cited searches could contain equivalent formulations.

## References

[1] C. Schütt, E. M. Werner and D. Yalikun, *Floating bodies for ball-convex bodies*, first arXiv version of 21 April 2025, arXiv:2504.15488.

[2] S. Artstein-Avidan and A. Chor, *Some inequalities of isoperimetric type for the c-affine surface area*, first arXiv version of 25 May 2025, arXiv:2505.19172.

[3] E. M. Werner and D. Yalikun, *Ball-convex bodies and \(L_p\) relative surface areas*, first arXiv version of 22 December 2025, arXiv:2512.19836.

[4] S. Artstein-Avidan and D. I. Florentin, *An in-depth study of ball-bodies*, first arXiv version of 14 May 2025, arXiv:2505.09200.
