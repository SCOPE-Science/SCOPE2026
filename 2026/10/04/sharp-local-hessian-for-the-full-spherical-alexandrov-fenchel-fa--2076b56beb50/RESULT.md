# Sharp local Hessian for the full spherical Alexandrov–Fenchel family
## Finding
Let \(n\ge2\), \(-1\le \ell<k\le n-1\), and let \(B_R\subset\mathbb S^{n+1}\) be a geodesic ball of radius \(R\in(0,\pi/2)\). Write \(S_R=\partial B_R\), and use the spherical quermassintegrals \(A_j\) and ball functions \(f_j(r)=A_j(B_r)\) in the normalization of Luo--Wei--Zhou. Define the full-pair deficit
\[
\mathcal D_{\ell,k}(\Omega)=A_k(\Omega)-f_k\!\left(f_\ell^{-1}(A_\ell(\Omega))\right).
\]
Put
\[
c=\cot R,\qquad q=\csc^2R,\qquad d_0=1,\qquad d_j=j\binom nj\quad(1\le j\le n).
\]
For every smooth normal direction \(u\in C^\infty(S_R)\), with
\[
\bar u=\frac1{|S_R|}\int_{S_R}u\,d\mu,
\]
the exact second variation is
\[
D^2\mathcal D_{\ell,k}[B_R](u,u)=\frac{(k-\ell)d_{k+1}c^k}{n}\left(\int_{S_R}|\nabla u|^2\,d\mu-nq\int_{S_R}(u-\bar u)^2\,d\mu\right).
\]
Consequently the Hessian is nonnegative. Its kernel is exactly the direct sum of the constants and the degree-one spherical harmonics. These are precisely the infinitesimal radius and center directions inside the equality family of geodesic balls.

If \(u\) is orthogonal in \(L^2(S_R)\) to constants and degree-one harmonics, then
\[
D^2\mathcal D_{\ell,k}[B_R](u,u)\ge
\frac{(k-\ell)d_{k+1}c^k(n+2)q}{n}\int_{S_R}u^2\,d\mu.
\]
The coefficient is sharp, and equality occurs exactly on degree-two spherical harmonics. Thus, apart from the explicit positive factor \((k-\ell)d_{k+1}\cot^kR/n\), all index pairs have the same local shape Hessian.

## Assumptions and scope
The ambient sphere has sectional curvature one. Principal curvatures are taken with respect to the outward normal. The Laplacian convention is such that degree-\(m\) spherical harmonics on \(S_R\) have eigenvalue
\[
-\frac{m(m+n-1)}{\sin^2R}.
\]
The statement is a Hessian formula at an equality ball. It applies to arbitrary smooth one-parameter variations with prescribed initial normal speed \(u\): because the first variation of \(\mathcal D_{\ell,k}\) vanishes at \(B_R\), the second variation is independent of the chosen acceleration of the path.

No global quantitative stability estimate is asserted. In particular, the theorem does not claim that the displayed quadratic lower bound remains valid with the same constant away from a sufficiently small neighborhood of the equality manifold.

## Proof
The source gives the first-variation formula
\[
\frac{d}{dt}A_{j-1}(\Omega_t)=d_j\int_{M_t}\eta E_j\,d\mu_t,
\]
for a normal variation with speed \(\eta\), where \(E_j\) is the normalized elementary symmetric curvature and \(0\le j\le n\). At \(S_R\), the Weingarten map is \(cI\), so \(E_j=c^j\).

Choose a variation whose initial speed is \(u\), and extend that speed with zero first time derivative at the initial time. The standard hypersurface variation in the unit sphere gives
\[
\delta W=-\nabla^2u-q\,uI.
\]
At the umbilic matrix \(cI\), symmetry of \(E_j\) gives
\[
\delta E_j=-\frac{j}{n}c^{j-1}\Delta u-jc^{j-1}q\,u.
\]
Also \(\delta(d\mu)=nc\,u\,d\mu\). Differentiating the first-variation formula and integrating by parts yields, uniformly for \(0\le j\le n\),
\[
\delta^2A_{j-1}=d_jc^{j-1}\left[\frac{j}{n}\int_{S_R}|\nabla u|^2\,d\mu+\big((n-j)c^2-j\big)\int_{S_R}u^2\,d\mu\right].
\]
For \(j=0\), this reads \(\delta^2A_{-1}=nc\int u^2\,d\mu\), the usual second variation of enclosed volume.

Set
\[
\Psi(x)=f_k\!\left(f_\ell^{-1}(x)\right).
\]
The ball derivative formula from the source is
\[
f_m'(R)=d_{m+1}|\mathbb S^n|\sin^{n-m-1}R\cos^{m+1}R.
\]
Therefore
\[
\Psi'(A_\ell(B_R))=\frac{d_{k+1}}{d_{\ell+1}}c^{k-\ell},
\]
where \(d_0=1\) covers \(\ell=-1\). Substitution into the first variations shows \(\delta\mathcal D_{\ell,k}=0\), as required at an equality ball.

Subtracting \(\Psi'\delta^2A_\ell\) from \(\delta^2A_k\) makes all index dependence collapse to the factor \(k-\ell\):
\[
\delta^2A_k-\Psi'\delta^2A_\ell
=\frac{(k-\ell)d_{k+1}c^k}{n}\left(\int|\nabla u|^2\,d\mu-nq\int u^2\,d\mu\right).
\]
Differentiating \(\Psi'\) once more gives
\[
-\Psi''(A_\ell(B_R))\,(\delta A_\ell)^2
=(k-\ell)d_{k+1}c^kq\,\frac{\left(\int u\,d\mu\right)^2}{|S_R|}.
\]
Adding this chain-rule term produces exactly the variance form in the finding.

Finally, the first nonzero Laplace eigenvalue on \(S_R\) is \(nq\), with eigenspace the degree-one harmonics. Poincaré's inequality proves nonnegativity and identifies the kernel as constants plus degree one. After projecting both away, the next eigenvalue is \(2(n+1)q\); subtracting \(nq\) leaves the sharp gap \((n+2)q\), attained exactly by degree-two harmonics.

## Verification
The accompanying `verify.py` replays the coefficient cancellations with exact rational arithmetic for a grid of dimensions and index pairs. It checks the first-derivative ratio, the second-variation gradient and zeroth-order coefficient collapse, the chain-rule correction to the mean mode, and the harmonic factors \((m-1)(m+n)\) after quotienting the equality modes.

Those finite checks are not used as a proof of the all-dimensional statement. The all-dimensional proof is the symbolic calculation above from the source's first-variation and ball-derivative formulas together with standard hypersurface variation and the exact Laplace spectrum of a round sphere.

## Relationship to prior work
Luo--Wei--Zhou prove the full spherical Alexandrov--Fenchel inequalities and characterize equality by geodesic balls. Their Section 2.3 records the first variation of every spherical quermassintegral and the exact derivatives of the ball functions. The paper does not state a second-variation formula, a local stability theorem, or a spherical-harmonic Hessian decomposition for the deficits.

VanBlargan--Wang prove quantitative quermassintegral inequalities for nearly spherical sets in Euclidean space. Their deficit and expansion are Euclidean, so they do not contain the ambient-curvature term \(\csc^2R\) or imply the spherical formula here. Sheng--Wang treat weighted inequalities near geodesic spheres in all space forms, but their quantitative Alexandrov--Fenchel results are stated for Euclidean and hyperbolic space; in the spherical case they treat weighted Minkowski-type inequalities rather than the newly completed full quermassintegral family. Sahjwani--Scheuer prove global-style stability estimates for hyperbolic quermassintegral inequalities under additional geometric bounds, again in a different ambient geometry.

## Limitations
The result is local and quadratic. It does not supply a neighborhood size, control a nonlinear distance globally, or prove a sharp finite-deficit stability inequality. The radius restriction \(R<\pi/2\) ensures \(c>0\) and is the convex range of the source theorem. The second variation becomes degenerate exactly along the equality manifold, so any nonlinear stability statement must include a radius-and-center modulation or an equivalent normalization.

## References
1. T. Luo, Y. Wei, R. Zhou, *Alexandrov--Fenchel inequalities for convex domains in the sphere*, arXiv:2609.13829v1, 2026. See Theorem 1.1 and equations (2.16)--(2.17).
2. C. VanBlargan, Y. Wang, *Quantitative Quermassintegral Inequalities for Nearly Spherical Sets*, arXiv:2201.04256v1; Communications in Contemporary Mathematics 26 (2024), 2350026.
3. W. Sheng, Y. Wang, *On the new weighted geometric inequalities near the sphere in space forms*, arXiv:2508.04067v1; Canadian Journal of Mathematics, First View (2026).
4. P. Sahjwani, J. Scheuer, *Stability of the Quermassintegral Inequalities in Hyperbolic Space*, Journal of Geometric Analysis 34 (2024), 13.
