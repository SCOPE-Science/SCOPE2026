# Three covariogram scaling regimes without boundary smoothness

## Finding

Let \(n\ge2\) and let \(K\subset\mathbb R^n\) be **any** compact full-dimensional convex body with \(0\in\operatorname{int}K\). No differentiability or strict convexity of its boundary is assumed. For \(p>0\), \(x\in\operatorname{int}(-K)\), let \(\rho_x(u)=\rho_{K+x}(u)\), \(u\in S^{n-1}\), and define the smoothed covariogram by
\[
 g_{K,p}(x)=\frac1n\int_{S^{n-1}}\left(\frac{\rho_0(u)^{-p}+\rho_x(u)^{-p}}2\right)^{-n/p}\,du,
 \qquad D_p(x)=|K|-g_{K,p}(x).
\]
Define \(L(p,\delta)=\{x\in\operatorname{int}(-K):D_p(x)\le\delta\}\). At \(\mathcal H^{n-1}\)-almost every boundary point \(z\), write \(\nu(z)\) for the outer unit normal and \(h(z)=z\cdot\nu(z)>0\). Set
\[
 H_K(y)=\frac12\int_{\partial K}|y\cdot\nu|\,dS,\quad
 Q_K(y)=\int_{\partial K}\frac{(y\cdot\nu)^2}{h}\,dS,\quad
 \Phi_K(y)=\int_{\partial K}h\log\cosh\left(\frac{y\cdot\nu}{2h}\right)\,dS.
\]
For every fixed \(\alpha<0\), as real \(p\to\infty\), the following **whole-set Hausdorff limits** hold:
\[
\begin{array}{ll}
 p^{-\alpha}L(p,p^\alpha)\longrightarrow\{y:H_K(y)\le1\}, &-1<\alpha<0,\\[2mm]
 pL(p,p^{-1})\longrightarrow\{y:\Phi_K(y)\le1\}, &\alpha=-1,\\[2mm]
 p^{(1-\alpha)/2}L(p,p^\alpha)\longrightarrow\{y:Q_K(y)\le8\}, &\alpha<-1.
\end{array}
\]
Additionally, for each **fixed** \(p>0\), the nonsmooth body has the second-order Peano expansion
\[
 D_p(x)=\frac{n+p}{8}Q_K(x)+o(|x|^2)\qquad(x\to0).
\]
Thus the quadratic germ and the three scaling phases of the 2026 smooth-boundary construction persist for all convex bodies, including polytopes, without claiming \(C^2\) regularity of the covariogram on a neighborhood.

## Assumptions and scope

The radial function is \(\rho_A(u)=\max\{t\ge0:tu\in A\}\) whenever \(0\in\operatorname{int}A\). Surface measure is \((n-1)\)-dimensional Hausdorff measure. All three forms are defined for arbitrary convex bodies because the unit normal exists almost everywhere, \(h\) is bounded below by the centered inradius, and the surface area is finite. \(Q_K\) is positive definite and \(H_K\) is a norm. The critical function \(\Phi_K\) is continuous, strictly convex, and coercive. The result uses the exact radial \((-p)\)-mean, not the different Gardner--Zhang radial mean body \(R_pK\).

## Proof

**1. Exact nonnegative Jensen gap.** Put \(a=\rho_0(u)\), \(b=\rho_x(u)\). The equality \(|K+x|=|K|\) gives the exact identity
\[
 D_p(x)=\frac1n\int_{S^{n-1}}a^n E_{n/p}\!\left(p\log(b/a)\right)\,du,
\]
where, for \(q>0\),
\[
 E_q(z)=\frac{1+e^{qz}}2-\left(\frac{1+e^{-z}}2\right)^{-q}
 =e^{qz/2}\left[\cosh(qz/2)-\exp\bigl(-q\log\cosh(z/2)\bigr)\right]. \tag{1}
\]
This identity follows by subtracting the radial-mean volume from the average of the two equal volumes. Since \(E_q(z)\ge0\), \(D_p\ge0\). Strictness of the power-mean inequality implies \(D_p(x)=0\) only if \(K+x=K\), hence only at \(x=0\) for compact \(K\).

**2. Almost-everywhere radial linearization without smoothness.** Choose \(r>0\) with \(rB_2^n\subset K\). For small translations \(x\), convexity gives
\[
 (1-|x|/r)K\subset K+x\subset(1+|x|/r)K.
\]
Consequently \(t_u(x)=\log(\rho_x(u)/\rho_0(u))\) satisfies \(|t_u(x)|\le C_K|x|\), uniformly in \(u\). At almost every radial contact \(z=\rho_0(u)u\), the gauge of \(K\) is differentiable at \(z\) with gradient \(\nu(z)/h(z)\). Linearizing the equation \(\gamma_K(\rho_x(u)u-x)=1\) therefore gives the Frechet derivative
\[
 t_u(x)=\frac{x\cdot\nu(z)}{h(z)}+o_u(|x|). \tag{2}
\]
The radial area formula, valid for Lipschitz radial graphs, is \(\rho_0(u)^n du=h(z)dS(z)\). Dominated convergence applied to (2), uniformly over translation directions by compactness of the unit sphere, yields
\[
 \int_{S^{n-1}}\rho_0(u)^n t_u(x)^2\,du=Q_K(x)+o(|x|^2). \tag{3}
\]
The normal vectors cannot be supported in a proper hyperplane, since \(K\) is bounded and full-dimensional, so \(Q_K\) is positive definite.

**3. A uniform coercive lower bound.** For \(p\ge n\) and \(|x|\) sufficiently small, use (1), \(\cosh(qz/2)\ge1\), and \(q\log\cosh(z/2)\le n|t_u(x)|/2\) to obtain
\[
 E_{n/p}(pt_u(x))\ge c_K\frac np\log\cosh\left(\frac{pt_u(x)}2\right).
\]
The elementary bound \(\log\cosh s\ge c\,s^2/(1+|s|)\), the uniform estimate \(|t_u(x)|\le C_K|x|\), and (3) give constants \(c_K,\varepsilon_K>0\) such that
\[
 D_p(x)\ge c_K\frac{p|x|^2}{1+p|x|}\quad
 (p\ge n,\ |x|\le\varepsilon_K). \tag{4}
\]
This is the key localization estimate at all three scales; it does not assume a uniform second derivative of the boundary.

**4. Quadratic germ and fine scale.** The analytic scalar identity (1), with \(q=n/p\), has
\[
 E_q(z)=\frac{q(q+1)}8z^2+O\bigl(q(q+1)|z|^3\bigr)
 \quad (|z|\le1), \tag{5}
\]
with an absolute implied constant for bounded \(q\). At fixed \(p\), equations (3),(5) yield the stated Peano expansion. Uniformly whenever \(p\to\infty\), \(x\to0\), and \(p|x|\to0\), they yield
\[
 D_p(x)=\frac{p+n}{8}\bigl(Q_K(x)+o(|x|^2)\bigr)+O_K(p(p+n)|x|^3).
\]
With \(x=p^{(\alpha-1)/2}y\), \(\alpha<-1\), dividing by \(p^\alpha\) gives locally uniformly in \(y\)
\[
 \frac{D_p(p^{(\alpha-1)/2}y)}{p^\alpha}\longrightarrow\frac18 Q_K(y). \tag{6}
\]

**5. Critical scale.** Put \(x=y/p\). By (2), \(p t_u(y/p)\to (y\cdot\nu)/h\) for almost every \(u\), while \(|p t_u(y/p)|\le C_K|y|\). The exact factorization (1) gives
\[
 \frac pn E_{n/p}\bigl(pt_u(y/p)\bigr)
 \longrightarrow\log\cosh\left(\frac{y\cdot\nu}{2h}\right).
\]
Dominated convergence and the radial area formula imply
\[
 pD_p(y/p)\longrightarrow\Phi_K(y), \tag{7}
\]
locally uniformly in \(y\); local uniformity follows from the uniform translation Lipschitz bound and equicontinuity of (1) on bounded arguments. The integrand is strictly convex as a function of its scalar argument, and surface normals span every direction, so \(\Phi_K\) is strictly convex. Also \(\log\cosh s\ge |s|-\log2\) gives \(\Phi_K(y)\ge H_K(y)-n|K|\log2\), proving coercivity.

**6. Coarse scale.** The two positive radial values have \(\min(a,b)\le ((a^{-p}+b^{-p})/2)^{-1/p}\le2^{1/p}\min(a,b)\), hence
\[
 0\le D_K(x)-D_p(x)\le(2^{n/p}-1)|K|=O_K(p^{-1}), \tag{8}
\]
where \(D_K(x)=|K|-|K\cap(K+x)|\). For each unit \(u\), integrating the lengths of chords of \(K\) parallel to \(u\) gives
\[
 \lim_{t\downarrow0}\frac{D_K(tu)}t=\operatorname{vol}_{n-1}(K|u^\perp)=H_K(u).
\]
This convergence is uniform over unit \(u\): \(D_K\) is Lipschitz in translations, and \(H_K\) is continuous. Thus, if \(-1<\alpha<0\), equation (8) gives locally uniformly
\[
 \frac{D_p(p^\alpha y)}{p^\alpha}\longrightarrow H_K(y). \tag{9}
\]

**7. Whole-set convergence.** Inequality (8) and the strict maximum of the ordinary covariogram at zero first show that all \(L(p,p^\alpha)\) lie in arbitrarily small fixed neighborhoods of zero for large \(p\). Inequality (4) then bounds the rescaled level sets: for \(\alpha>-1\) it gives \(|x|=O(p^\alpha)\); for \(\alpha=-1\), \(|x|=O(p^{-1})\); for \(\alpha<-1\), it gives \(|x|=O(p^{(\alpha-1)/2})\). The limiting functions in (6),(7),(9) are continuous, positive away from zero and strictly increasing along every ray. Local uniform convergence plus these global bounds implies the three full Hausdorff limits: interior points persist, points strictly outside are excluded, and boundary points are approximated along their inward radial segments. This completes the proof.

## Verification

The scalar identity (1) can be checked by substituting \(\log((1+e^{-z})/2)=-z/2+\log\cosh(z/2)\). Differentiating twice at zero yields \(E_q(0)=E'_q(0)=0\), \(E''_q(0)=q(q+1)/4\), verifying (5). For the nonsmooth square \(K=[-1,1]^2\), the formulas specialize to
\[
 H_K(y)=2(|y_1|+|y_2|),\quad Q_K(y)=4(y_1^2+y_2^2),\quad
 \Phi_K(y)=4\left[\log\cosh(y_1/2)+\log\cosh(y_2/2)\right].
\]
The accompanying `check_square.py` evaluates the **original radial definition** by midpoint angular quadrature (200,000 nodes), compares the three expected limits, and asserts the exact symbolic scalar identities using SymPy. Finite quadrature is diagnostic only; the theorem rests on the preceding arbitrary-body proof.

## Relationship to prior work

Haddad, Jiménez, and Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1 (8 October 2026), Theorems 3--5 and Section 5, establish the same three limits under a \(C^3\) boundary assumption and a Hessian formula under a \(C^2\) assumption. Those hypotheses exclude polygons and polytopes. The present argument proves the same conclusions without boundary regularity by replacing boundary Taylor expansion with an exact Jensen gap and almost-everywhere radial differentiation. It does not claim that the smooth case or the form of the limiting bodies is newly discovered.

Haddad et al., *Affine isoperimetric inequalities for higher-order projection and centroid bodies* (2025), examine ordinary and higher-order covariograms and the different Gardner--Zhang radial mean bodies; the full accessible Sections 1--4 distinguish those operators from the translated-pair smoothing used here. Earlier Orlicz projection bodies supply a framework for \(\Phi_K\), but their definition alone does not imply the three-parameter asymptotic statement for nonsmooth translated bodies. An unindexed direct nonsmooth extension remains a literature risk.

## Limitations

Constants implicit in localization depend on \(K\) and the dimension. The result asserts a Peano quadratic germ at the origin, not \(C^2\) regularity in a neighborhood of an arbitrary polytope. There is no uniform convergence rate over all convex bodies, no stability estimate for varying \(K\), and no new volume inequality for the limiting Orlicz body. The illustrative square computation is finite numerical evidence only.

## References

1. J. Haddad, C. H. Jiménez and M. Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1, 8 October 2026, https://arxiv.org/html/2610.11700v1 .
2. J. Haddad, D. Langharst, E. Putterman, M. Roysdon and D. Ye, *Affine isoperimetric inequalities for higher-order projection and centroid bodies*, Mathematische Annalen 393 (2025), 1073--1121, https://doi.org/10.1007/s00208-025-03271-x .
3. R. J. Gardner and G. Zhang, *Affine inequalities and radial mean bodies*, American Journal of Mathematics 120 (1998), 505--528.
4. E. Lutwak, D. Yang and G. Zhang, *Orlicz projection bodies*, Advances in Mathematics 223 (2010), 220--242.
