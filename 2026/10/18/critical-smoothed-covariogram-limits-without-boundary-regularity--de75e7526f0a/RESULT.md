# Critical smoothed-covariogram limits without boundary regularity

## Finding

**Theorem (nonsmooth critical transition and a polytopal rate).** Let \(d\ge2\), and let \(K\subset\mathbb R^d\) be an arbitrary full-dimensional compact convex set with \(0\in\operatorname{int}K\). Write \(\rho_K(u)=\sup\{t\ge0:tu\in K\}\) for \(u\in S^{d-1}\). For \(p>0\) and \(x\in\operatorname{int}(-K)\), define the radial \((-p)\)-mean covariogram by

\[
g_{K,p}(x)=\frac1d\int_{S^{d-1}}\left(\frac{\rho_K(u)^{-p}+\rho_{K+x}(u)^{-p}}2\right)^{-d/p}\,du.
\]

Let \(L_K(p,\delta)=\{x\in\operatorname{int}(-K):\operatorname{vol}_d(K)-g_{K,p}(x)\le\delta\}\) and \(F_{K,p}(y)=p[\operatorname{vol}_d(K)-g_{K,p}(y/p)]\), defined when \(y/p\in\operatorname{int}(-K)\). At almost every \(z\in\partial K\), let \(\nu(z)\) be its exterior unit normal and put \(h(z)=z\cdot\nu(z)>0\). Define

\[
\Phi_K(y)=\int_{\partial K}h(z)\log\cosh\left(\frac{y\cdot\nu(z)}{2h(z)}\right)\,d\mathcal H^{d-1}(z),\qquad T_K=\{y:\Phi_K(y)\le1\}.
\]

Then, without any smoothness or strict-convexity hypothesis on \(\partial K\),

\[
F_{K,p}\longrightarrow\Phi_K\quad\text{uniformly on every bounded subset of }\mathbb R^d,\qquad
pL_K(p,p^{-1})\longrightarrow T_K\quad\text{in Hausdorff distance}.
\]

If \(K\) is additionally a convex polytope, then for each \(R>0\) there exist finite constants \(C_{K,R}\) and \(p_{K,R}\) for which

\[
\sup_{\|y\|_2\le R}|F_{K,p}(y)-\Phi_K(y)|\le\frac{C_{K,R}}p\quad(p\ge p_{K,R}).
\]

Consequently a constant \(C_K<\infty\) exists with

\[
d_H\big(pL_K(p,p^{-1}),T_K\big)\le\frac{C_K}p\quad\text{for all sufficiently large }p.
\]

These limits and rates concern this single critical \(p^{-1}\)-deficit regime; no assertions are made here about fixed-power smoothness or the other simultaneous-scaling regimes.

## Assumptions and scope

The Euclidean sphere is equipped with its ordinary surface-area measure, without normalization to total mass one; the factor \(1/d\) in the radial volume integral is essential. The parameter \(p\) tends to positive infinity through real values. The origin must lie in the *interior* of \(K\), so every radial function and every denominator \(h(z)\) is uniformly positive. The normal \(\nu(z)\) exists at \(\mathcal H^{d-1}\)-almost every boundary point of any convex body. Integrals over \(\partial K\) are therefore well defined even when facets, corners, and edges are present. For polytopes, the rates are allowed to depend on the body's facet geometry and on \(R\); no dimension-free constant is asserted.

## Proof

**1. Translation derivatives of radial functions exist almost everywhere.** Choose \(r>0\) with \(rB_2^d\subset K\), and let \(j_K\) be the Minkowski gauge of \(K\). It is convex, globally Lipschitz, and differentiable at almost every nonzero point by Rademacher's theorem. Homogeneity and polar integration show that \(j_K\) is differentiable at \(\rho_K(u)u\) for almost every \(u\in S^{d-1}\). At such a point, \(z=\rho_K(u)u\), the gradient satisfies

\[
\nabla j_K(z)=\frac{\nu(z)}{h(z)},\qquad \nabla j_K(z)\cdot z=1.
\]

For fixed \(y\), the boundary equation \(j_K(\rho_{K+ty}(u)u-ty)=1\) and differentiability of \(j_K\) at \(z\) give

\[
\left.\frac d{dt}\right|_{t=0}\log\rho_{K+ty}(u)
=\frac{y\cdot\nu(z)}{h(z)}=:q_y(u).
\]

The transversality \(\nabla j_K(z)\cdot u=1/\rho_K(u)>0\) justifies this first derivative by differentiability with an \(o(|t|)\) remainder even where no second derivatives exist. Moreover, for \(\|x\|<r\), the inclusions \((1-\|x\|/r)K\subset K+x\subset(1+\|x\|/r)K\) bound the translated radial functions uniformly above and below. Applying the same argument to two nearby translations shows that on every bounded set of \(y\)'s, the functions

\[
s_p(u,y)=-p\log\frac{\rho_{K+y/p}(u)}{\rho_K(u)}
\]

are uniformly bounded and uniformly Lipschitz as functions of \(y\), independently of \(u\) and sufficiently large \(p\). For almost every \(u\), \(s_p(u,y)\to-q_y(u)\) pointwise for each fixed \(y\).

**2. First-order limit of the nonlinear radial mean.** Introduce \(b(s)=\log[(1+e^s)/2]\). Exact substitution into the radial volume formula gives

\[
F_{K,p}(y)=\int_{S^{d-1}}\rho_K(u)^d\,
\frac pd\left[1-\exp\left(-\frac d p b(s_p(u,y))\right)\right]du.
\]

For bounded \(s\), the bracketed scalar factor converges uniformly to \(b(s)\), with error \(O(p^{-1})\). Bounded convergence implies, for fixed \(y\),

\[
F_{K,p}(y)\to\int_{S^{d-1}}\rho_K(u)^d\,b(-q_y(u))\,du.
\]

The uniform Lipschitz bounds from Step 1 and the bounded derivative of \(b\) imply equi-Lipschitzness of \(F_{K,p}\) on every fixed ball. A finite-net argument upgrades this pointwise limit to locally uniform convergence.

For the radial parameterization \(z(u)=\rho_K(u)u\), the convex-boundary area formula, valid for Lipschitz radial graphs, gives \(\rho_K(u)^d\,du=h(z)\,d\mathcal H^{d-1}(z)\). Since \(b(-q)=\log\cosh(q/2)-q/2\) and the divergence theorem gives \(\int_{\partial K}\nu(z)\,d\mathcal H^{d-1}(z)=0\), the limit is exactly \(\Phi_K(y)\). No boundary curvature is used.

**3. Geometry of the limiting sublevel set.** Each integrand \(\log\cosh\) is even and smooth. Differentiating under the integral is justified by \(h(z)\ge r\), and

\[
\nabla^2\Phi_K(y)=\frac14\int_{\partial K}
\frac{\nu(z)\otimes\nu(z)}{h(z)}
\operatorname{sech}^2\left(\frac{y\cdot\nu(z)}{2h(z)}\right)
\,d\mathcal H^{d-1}(z).
\]

The normals cannot lie in a proper linear subspace because \(K\) is full-dimensional, so the Hessian is everywhere positive definite. Moreover, \(\log\cosh t\ge|t|-\log2\), and the divergence theorem gives \(\int_{\partial K}h(z)\,d\mathcal H^{d-1}(z)=d\operatorname{vol}_d(K)\). Thus

\[
\Phi_K(y)\ge\frac12\int_{\partial K}|y\cdot\nu(z)|\,d\mathcal H^{d-1}(z)-d\operatorname{vol}_d(K)\log2.
\]

The first term is the support norm of the projection body and is bounded below by a positive constant times \(\|y\|_2\). Hence \(\Phi_K\) is coercive, strictly convex, and has unique minimizer \(0\); \(T_K\) is a compact convex body with nonempty interior and a strictly radially increasing defining function.

**4. No escaping components in the scaled level sets.** Let \(g_K(x)=\operatorname{vol}_d(K\cap(K+x))\) be the ordinary covariogram. By the power-mean inequalities applied pointwise to the two radial functions,

\[
g_K(x)\le g_{K,p}(x)\le2^{d/p}g_K(x).
\]

It follows that \(\operatorname{vol}_d(K)-g_{K,p}(x)\le p^{-1}\) implies

\[
\operatorname{vol}_d(K)-g_K(x)\le
\frac{1+d\operatorname{vol}_d(K)\log2+o(1)}p.
\]

For \(x=tu\), \(t>0\), slicing \(K\) parallel to \(u\) gives the exact chord formula

\[
\operatorname{vol}_d(K)-g_K(tu)=\int_{u^\perp}\min\{t,\ell_u(w)\}\,dw,
\]

where \(\ell_u(w)\) is the length of the chord of \(K\) over \(w\in u^\perp\). Because \(rB_2^d\subset K\), all chords above the ball of radius \(r/2\) in \(u^\perp\) have length at least \(\sqrt3\,r\). Consequently \(\operatorname{vol}_d(K)-g_K(tu)\ge c_K\min(t,r)\), with \(c_K=\omega_{d-1}(r/2)^{d-1}>0\). Every \(x\in L_K(p,p^{-1})\) therefore obeys \(\|x\|_2\le C_K/p\) for large \(p\); all its scaled points lie in a fixed ball.

Locally uniform convergence from Step 2, this tightness, and strict radial increase of \(\Phi_K\) yield the inclusions \((1-\varepsilon)T_K\subset pL_K(p,p^{-1})\subset(1+\varepsilon)T_K\) for all sufficiently large \(p\), for every \(\varepsilon>0\). This establishes Hausdorff convergence.

**5. Rate for a polytope.** Write a nonredundant facet description as \(K=\{z:a_i\cdot z\le1,\ 1\le i\le m\}\), with distinct, nonzero outward facet vectors \(a_i\). Then

\[
\rho_{K+x}(u)^{-1}=
\max_{1\le i\le m}\frac{a_i\cdot u}{1+a_i\cdot x}
\]

for all small \(x\), and each maximizing value is positive. On \(\|y\|_2\le R\), the perturbation of each term of this maximum when \(x=y/p\) is bounded by \(C_{K,R}/p\). Except in the finite union of spherical bands

\[
E_{p,R}=\bigcup_{i<j}\left\{u\in S^{d-1}:
|(a_i-a_j)\cdot u|\le C_{K,R}/p\right\},
\]

the maximizing facet is identical before and after translation. Each band has spherical measure \(O_{K,R}(p^{-1})\) for \(d\ge2\); hence so does \(E_{p,R}\). Outside the bands, if the common maximizing facet is \(i\), one has exactly

\[
\frac{\rho_{K+y/p}(u)}{\rho_K(u)}=1+\frac{a_i\cdot y}{p},\qquad
s_p(u,y)=-p\log(1+a_i\cdot y/p)=-a_i\cdot y+O_{K,R}(p^{-1}).
\]

Thus the integrands defining \(F_{K,p}\) and \(\Phi_K\) differ by \(O_{K,R}(p^{-1})\) outside \(E_{p,R}\). Inside it, both are bounded uniformly in \(p,u,y\), so their integral differs by at most \(O_{K,R}(p^{-1})\) as well. This gives the asserted locally uniform \(1/p\) bound.

Choose a fixed ball containing the eventual scaled level sets and \(T_K\). On the compact hypersurface \(\Phi_K=1\), strict convexity gives a positive lower bound on the outward radial derivative. The preceding uniform error therefore sandwiches the scaled sublevel set between \((1-C/p)T_K\) and \((1+C/p)T_K\) for all large \(p\). The stated Hausdorff \(O_K(p^{-1})\) rate follows.

## Verification

A standalone, standard-library Python checker `check_critical_polytope.py` computes the finite-parameter radial integral from translated facet inequalities and separately computes the boundary-normal integral for a rectangle and for a noncentrally symmetric triangle. Four displacement vectors and parameters \(p\in\{40,80,160,320\}\) were checked with 20,000 angular quadrature nodes each. Independent polar-area integration verifies the base areas. Each error decreased by a factor consistent with \(O(1/p)\); the script exits successfully with an explicit PASS statement. Numerical quadrature is not used to prove the all-dimensional limit, the band estimate, or the sublevel convergence.

## Relationship to prior work

Haddad, Jiménez, and Resende [1], Theorem 5(2), first established the same critical-transition functional and Hausdorff limit for convex bodies with \(C^3\) boundary. The transition integral itself is **not** claimed as new. Their hypotheses do not include arbitrary polytopes or all nonsmooth convex bodies, nor do they supply the polytopal \(O(1/p)\) rate. The new contribution is the general nonsmooth validity plus the effective polytope estimate proved above.

Langharst, Roysdon, and Zvavitch [2], Sections 6–7, study covariograms weighted by external measures and functions, with projection-body connections; those definitions retain intersection integrals and do not coincide with the nonlinear radial \((-p)\)-mean construction. General Gardner–Zhang radial mean bodies [3] involve integration over translations of a *single* body and are different from the two-body smoothed covariogram. Previously published parallelotope work on regularity of that different radial mean body also does not imply the present critical transition. These distinctions are substantive, not merely differences of notation.

## Limitations

Only the critical deficit \(\delta=p^{-1}\) is considered; no fixed-\(p\) Hessian formula or noncritical simultaneous-scaling theorem for arbitrary nonsmooth bodies is asserted. The general convex-body convergence is not assigned a uniform rate. The \(O(1/p)\) estimate has geometry-dependent constants for each fixed polytope, and optimality of its order is not claimed. Independent external verification and exhaustive historical priority certification have not been performed; an equivalent nonsmooth extension in unindexed literature remains possible.

## References

[1] J. Haddad, C. H. Jiménez, and M. Resende Guedes, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1, 2026-10-08, particularly Theorem 5 and Section 5. https://arxiv.org/html/2610.11700v1

[2] D. Langharst, M. Roysdon, and A. Zvavitch, *General measure extensions of projection bodies*, Proceedings of the London Mathematical Society 125 (2022), 1083–1129, DOI: 10.1112/plms.12477, particularly Sections 6–7. https://doi.org/10.1112/plms.12477

[3] R. J. Gardner and G. Zhang, *Affine inequalities and radial mean bodies*, American Journal of Mathematics 120 (1998), 505–528, DOI: 10.1353/ajm.1998.0021.
