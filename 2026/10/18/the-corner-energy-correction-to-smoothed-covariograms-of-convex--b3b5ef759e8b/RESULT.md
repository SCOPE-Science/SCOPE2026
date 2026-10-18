# The corner-energy correction to smoothed covariograms of convex polygons

## Finding

Let \(P\subset\mathbb R^2\) be a convex polygon with the origin in its interior. Write its edges in cyclic counterclockwise order, with outward unit normals \(n_i\), support distances \(h_i>0\), edge lengths \(\ell_i\), and exterior normal turning angles \(\Delta_i\in(0,\pi)\) between successive normals. All indices are cyclic. For \(y\in\mathbb R^2\) put
\[
a_i=\frac{y\cdot n_i}{h_i},\quad W_i=\frac{h_i\ell_i}{2},\quad
\Gamma_i=\frac{h_i h_{i+1}}{\sin\Delta_i}.
\]
Define two scalar functions
\[
A(z)=\log\left(\frac{1+e^{-z}}2\right),\qquad
E(z)=-z^2A'(z)-2A(z)^2,
\]
and the nonnegative two-variable corner functional
\[
J(a,b)=\int_{\min\{a,b\}}^{\max\{a,b\}}
\bigl[A(t)-A(\max\{a,b\})\bigr]dt.
\]
For the radial-smoothed covariogram \(g_{P,p}\) defined below, as \(p\to+\infty\), locally uniformly in \(y\),
\[
\boxed{\displaystyle
p\bigl(|P|-g_{P,p}(y/p)\bigr)
=\Phi_P(y)+\frac{B_P(y)}p+O_{P,Y}(p^{-2}),}
\]
where \(Y\) is any specified compact subset of \(\mathbb R^2\), and
\[
\boxed{\displaystyle \Phi_P(y)=\sum_i h_i\ell_i\log\cosh(a_i/2),\qquad
B_P(y)=\sum_i W_i E(a_i)+\sum_i\Gamma_i J(a_i,a_{i+1}).}
\]
The last sum is **a strictly positive corner term for every nonzero \(y\)**. Its sharp small-\(y\) expansion is the positive definite discrete energy
\[
\boxed{\displaystyle
\sum_i\Gamma_i J(a_i,a_{i+1})
=\frac14\sum_i\Gamma_i(a_i-a_{i+1})^2+O_P(\|y\|^3).}
\]
The bulk edge term begins in degree four: \(E(z)=-z^4/32+O(z^5)\). In particular,
\[
B_P(y)=\frac14\sum_i\Gamma_i(a_i-a_{i+1})^2+O_P(\|y\|^3).
\]
Unlike the even leading functional \(\Phi_P\), the second coefficient need not be even. For the triangle with vertices \((-1,-1),(2,-1),(-1,2)\), along \(y=(t,t)\) one has
\[
\boxed{\displaystyle B_P(t,t)-B_P(-t,-t)=-\frac94 t^3+O(t^5),\qquad t\to0.}
\]

## Assumptions and scope

A polygon is compact, convex, full-dimensional, and has at least three nondegenerate edges; consecutive collinear edges are combined, so \(0<\Delta_i<\pi\). The origin is strictly interior. Given a unit direction \(u\), let \(\rho_P(u)\) be the distance from the origin to the boundary along that ray. For \(p>0\), \(x\in\operatorname{int}(-P)\), let
\[
\rho_{P,x,p}(u)^{-p}=\frac{\rho_P(u)^{-p}+\rho_{P+x}(u)^{-p}}2,
\qquad
g_{P,p}(x)=\frac12\int_{\mathbb S^1}\rho_{P,x,p}(u)^2\,du.
\]
The remainder means that for each compact \(Y\) there are finite constants \(C_{P,Y}\) and \(p_{P,Y}\) such that the absolute error is at most \(C_{P,Y}p^{-2}\) for all \(p\ge p_{P,Y}\), \(y\in Y\). No smooth boundary assumption is made, and no claim about higher-dimensional polytopes is implied.

## Proof

**1. Exact polar identity.** Put \(r(u)=\rho_P(u)\), \(r_x(u)=\rho_{P+x}(u)\), and \(z=p\log(r_x/r)\). The definition of the radial mean gives
\[
\rho_{P,x,p}(u)^2=r(u)^2\exp\left[-\frac2p A(z)\right]
\]
and therefore
\[
p(|P|-g_{P,p}(y/p))=
\frac p2\int_{\mathbb S^1}r(u)^2
\left(1-\exp\left[-\frac2p A\left(p\log\frac{r_{y/p}(u)}{r(u)}\right)\right]\right)du.
\tag{1}
\]
Both radial functions are strictly positive for sufficiently large \(p\), uniformly for \(y\) in a prescribed compact set.

**2. Edge-interior sectors.** On a ray meeting edge \(i\), one has \(r(u)=h_i/(n_i\cdot u)\). Wherever the translated ray also meets edge \(i\),
\[
\frac{r_{y/p}(u)}{r(u)}=1+\frac{a_i}{p}.
\]
For bounded \(a\), Taylor expansion, uniform on bounded intervals, gives
\[
\frac p2\left(1-\exp\left[-\frac2p A\left(p\log(1+a/p)\right)\right]\right)
=A(a)+\frac{E(a)}{2p}+O(p^{-2}).\tag{2}
\]
The angular sector for edge \(i\) has \(\frac12\int r(u)^2du=W_i\), because it is the triangle from the origin to that edge. Thus the full-sector bulk contributions are \(2W_i A(a_i)+W_i E(a_i)/p\). We next correct for narrow sectors in which the identity of the active edge changes after translation.

**3. Vertex-switching sectors.** Let the consecutive supporting lines of edges \(i\) and \(i+1\) intersect at vertex \(v\), whose polar angle is \(\theta_v\). Their radial candidates are \(r_i(u)=h_i/(n_i\cdot u)\), \(r_{i+1}(u)=h_{i+1}/(n_{i+1}\cdot u)\). Differentiating at \(u=v/\|v\|\) yields, up to angular orientation,
\[
\left|\frac{d}{d\theta}\log\frac{r_i}{r_{i+1}}\bigg|_{\theta=\theta_v}\right|
=\kappa_i:=\frac{\|v\|^2\sin\Delta_i}{h_i h_{i+1}}.\tag{3}
\]
All remaining edges are strictly inactive in a fixed neighborhood of this ray. In the translated polygon the switching ray passes through \(v+y/p\), hence lies at angular distance \(O_Y(p^{-1})\); these neighborhoods are pairwise disjoint for large \(p\). Across the intervening angular strip, the argument of \(A\) in (1) is, to uniformly bounded error \(O_Y(p^{-1})\), an affine interpolation between \(a_i\) and \(a_{i+1}\), under the change of coordinate \(t=p\kappa_i(\theta-\theta_v)\). The baseline bulk value is \(A(\max\{a_i,a_{i+1}\})\): the old active edge on the strip has the larger scaled support increment.

The leading strip correction to (1), using \(r(u)^2=\|v\|^2+O_Y(p^{-1})\), is consequently
\[
\frac{\|v\|^2}{p\kappa_i}
\int_{\min\{a_i,a_{i+1}\}}^{\max\{a_i,a_{i+1}\}}
\bigl[A(t)-A(\max\{a_i,a_{i+1}\})\bigr]dt
=\frac{\Gamma_i}{p}J(a_i,a_{i+1}).\tag{4}
\]
The strip has width \(O_Y(p^{-1})\); its integrand, angular Jacobian, and endpoint positions have uniform \(O_Y(p^{-1})\) perturbations after rescaling, so their integrated error is \(O_{P,Y}(p^{-2})\). The same bound holds when the two facet arguments agree, because the switching strip then collapses to first order. Summing finitely many edge and vertex sectors gives the asserted two-term expansion.

**4. Identification of the first coefficient.** The polygon divergence identity \(\sum_i\ell_i n_i=0\) implies \(\sum_i h_i\ell_i a_i=y\cdot\sum_i\ell_i n_i=0\). Since \(A(a)=\log\cosh(a/2)-a/2\), the leading term \(\sum_i h_i\ell_i A(a_i)\) equals the stated \(\Phi_P(y)\).

**5. Corner positivity and odd correction.** Since \(A'(t)=-1/(1+e^t)<0\), each \(J(a,b)\) is nonnegative and vanishes precisely for \(a=b\). If all adjacent facet parameters were equal, then every polygon supporting line would be concurrent after rescaling by that common value; for a full-dimensional polygon this forces \(y=0\). This proves strict positivity for nonzero \(y\). The uniform Taylor expansion \(A(t)=-t/2+t^2/8+O(t^4)\) gives the Dirichlet energy. More precisely, for \(a,b\) near zero,
\[
J(a,b)-J(-a,-b)=-\frac18(a+b)(a-b)^2+O((|a|+|b|)^5),\tag{5}
\]
whereas \(E(a)-E(-a)=O(a^5)\). For the specified triangle, the cyclic facet values along \((t,t)\) are \((-t,2t,-t)\), all three corner weights equal one, and the cubic term in (5) sums to \(-9t^3/4\).

## Verification

The accompanying `CHECKER.py` uses only the Python standard library and independently evaluates the defining radial integral, with angular cuts at all original and translated vertex rays. It computes \(\Phi_P\) and \(B_P\) from the proposed closed formulas, then tests convergence of \(p[p(|P|-g_{P,p}(y/p))-\Phi_P(y)]\) at three increasing smoothing parameters on a triangle, a nonsymmetric pentagon, and a square. It separately checks the triangular cubic antisymmetric coefficient. Expected program output:

`VERIFY_OK polygons=3 angular_integrals=9 cubic_asymmetry=2`

The exact analytic proof is steps 1–5, not the finite numerical tests. The checker uses adaptive quadrature and accepts explicit numerical tolerances.

## Relationship to prior work

Haddad, Jiménez and Resende Guedes introduced this smoothed covariogram and determined the critical \(\log\cosh\) functional for smoothly bounded convex bodies. The leading critical functional has also been extended to nonsmooth convex bodies, with an order-of-magnitude error bound on polytopes. Those first-order results do not specify the next coefficient. Here the full \(p^{-1}\) correction for planar polygons is identified, separating a bulk edge contribution from a positive vertex-switching energy, and displaying a non-even correction for an asymmetric triangle. The standard polar radial-area formula, the polygon divergence identity, and elementary support geometry are used without priority claims.

## Limitations

This is a planar, fixed-polygon theorem, with estimates locally uniform in the displacement; constants may deteriorate when polygon angles or edge lengths degenerate. The displayed coefficient does not establish an optimal finite-\(p\) global remainder constant, uniformity across all polygons, higher-dimensional analogues, or an inverse reconstruction theorem. An equivalent earlier corner calculation in unindexed integral geometry literature cannot be ruled out.

## References

1. J. Haddad, C. H. Jiménez, M. Resende Guedes, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1 (first posted 2026-10-08), https://arxiv.org/html/2610.11700v1 .
2. E. Lutwak, D. Yang, G. Zhang, *Orlicz projection bodies*, Advances in Mathematics 223 (2010), 220–242, https://doi.org/10.1016/j.aim.2009.08.002 .
