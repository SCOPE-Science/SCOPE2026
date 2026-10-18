# Two-atom random silhouette law for homothetic polygonal frusta

## Finding
Let \(K\subset\mathbb R^2\) be a convex \(n\)-gon with genuine vertices and \(0\in\operatorname{int}K\), where \(n\ge3\). Form the three-dimensional frustum
\[
 F=\operatorname{conv}\left((K,0)\cup(tK,h)\right),\quad 0<t<1,\quad h>0.
\]
Take a uniformly random direction \(u\) on the sphere (identifying \(u\) and \(-u\)), project \(F\) orthogonally onto \(u^\perp\), and let \(N\) be the number of vertices in the projected convex polygon. Put \(\lambda=h/(1-t)\). Then, with probability one,
\[
 N\in\{n,n+2\},\qquad \Pr(N=n)=p_K(\lambda),\qquad \Pr(N=n+2)=1-p_K(\lambda),
\]
where \(p_K(\lambda)=\Omega(K,\lambda)/(2\pi)\) and \(\Omega(K,\lambda)\) is the solid angle of the planar region \(K\) as seen from the point directly above the origin at height \(\lambda\). Writing \(\rho_K(\phi)>0\) for the radial function of \(K\), this probability is exactly
\[
 p_K(\lambda)=1-\frac1{2\pi}\int_0^{2\pi}\frac{\lambda}{\sqrt{\lambda^2+\rho_K(\phi)^2}}\,d\phi.
\]
The map \(\lambda\mapsto p_K(\lambda)\) is a strictly decreasing analytic bijection \((0,\infty)\to(0,1)\). Thus one silhouette-type probability identifies the effective frustum aspect \(\lambda\), whereas \(h\) and \(t\) cannot be recovered individually from this statistic. As \(\lambda\to\infty\),
\[
 p_K(\lambda)=\frac{\operatorname{area}(K)}{2\pi\lambda^2}+O_K(\lambda^{-4}).
\]
For a regular \(n\)-gon of circumradius \(R\), with \(\alpha=2\pi/n\),
\[
 p_K(\lambda)=\frac n\pi\arctan\!\left(\frac{R^2\sin\alpha}{R^2(1+\cos\alpha)+2\lambda^2+2\lambda\sqrt{\lambda^2+R^2}}\right).
\]
In particular, the two-atom support and the solid-angle law hold for nonregular and nonsymmetric polygon bases.

## Assumptions and scope
All polygons have a finite cyclically ordered list of \(n\) vertices with adjacent edges forming interior angles strictly less than \(\pi\). The origin lies strictly inside the polygon, so every radial value is positive. The two bases are positive homothetic copies of the *same* polygon in parallel planes, with \(0<t<1\). The viewing direction is Haar-uniform over unoriented lines in \(\mathbb R^3\); the vertex count is the number of vertices of the convex *orthogonal shadow*, not a line section. Degenerate directions whose projected points have collinear coincidence occur on sets of zero spherical area.

## Proof
**1. Reducing the three-dimensional shadow to two plane polygons.** Let the unit viewing vector be \(u=(u_x,u_y,u_z)\), and suppose \(u_z\ne0\). Projection along \(u\) onto the horizontal plane \(z=0\) is an affine linear isomorphism of the ordinary orthogonal shadow plane \(u^\perp\); hence it preserves its polygonal face lattice. The lower and upper base projections become \(K\) and \(tK+s\), respectively, where
\[
 s=-h(u_x,u_y)/u_z,\qquad c=s/(1-t).
\]
The second polygon is precisely the image of the first under the positive homothety \(x\mapsto c+t(x-c)\).

**2. Exact planar vertex dichotomy.** For any strictly convex vertex polygon \(K\) and \(c\) not on one of its supporting edge-lines, if \(c\in\operatorname{int}K\), the homothetic copy \(c+t(K-c)\) is contained in \(K\); the hull is \(K\), with \(n\) vertices. Conversely, if \(c\notin K\), draw the two polygonal support rays from \(c\) touching \(K\), which touch two distinct vertices \(v_a,v_b\) in general position. Those rays are invariant under homothety about \(c\). The hull of the two homothetic polygons has two bridging segments \([v_a,c+t(v_a-c)]\) and \([v_b,c+t(v_b-c)]\). Its remaining boundary consists of the outer arc of \(K\) between the tangent vertices facing away from \(c\), and the opposite arc from the homothetic copy facing toward \(c\). For each of the \(n-2\) nontangent vertex labels exactly one of these copies contributes a vertex; both copies of the two tangent vertices contribute. Thus the hull has \((n-2)+4=n+2\) vertices. The case \(c\in\partial K\), rays through an edge, or other flat coincidences lies in finitely many lines and is negligible. This proves the claimed two-point support.

**3. Random homothety center.** A uniform spherical direction can be realized as \(u=Z/\|Z\|\) with three independent standard normal coordinates. Its coordinate ratios satisfy
\[
 \left(u_x/u_z,u_y/u_z\right)\ \sim\ f(z)=\frac{1}{2\pi}(1+\|z\|^2)^{-3/2}.
\]
Therefore \(c=-\lambda(u_x/u_z,u_y/u_z)\) has density
\[
 f_\lambda(c)=\frac{\lambda}{2\pi(\lambda^2+\|c\|^2)^{3/2}}.
\]
By the planar dichotomy, \(p_K(\lambda)=\int_K f_\lambda(c)\,dc\). This is one half of the usual solid angle because the Jacobian of radial projection from height \(\lambda\) onto the upper half-sphere is \(\lambda/(\lambda^2+\|c\|^2)^{3/2}\); the remaining factor \(1/(2\pi)\) accounts for unoriented hemispheres. In polar coordinates, integrating \(\int_0^{\rho}\lambda r(\lambda^2+r^2)^{-3/2}dr\) gives the displayed radial identity.

**4. Strict identifiability and asymptotics.** Differentiation under the integral sign yields
\[
 p_K'(\lambda)=-\frac1{2\pi}\int_0^{2\pi}\frac{\rho_K(\phi)^2}{(\lambda^2+\rho_K(\phi)^2)^{3/2}}\,d\phi<0.
\]
Dominated convergence gives the endpoint limits \(1\) and \(0\). A binomial expansion of the planar integral density at large \(\lambda\) yields the stated area coefficient and the remainder \(O_K(\lambda^{-4})\). Real-analyticity follows locally uniformly on compact positive \(\lambda\)-intervals. The law depends on \(h,t\) only through \(\lambda\), demonstrating the precise one-bit identifiable combination.

**5. Regular polygons.** Decompose the regular polygon into \(n\) congruent triangles joining its center to adjacent vertices. For a triangle with vertex vectors \(a,b,c\) from the observation point, the elementary triangular solid-angle formula is
\[
 \Omega_\triangle=2\arctan\left(\frac{\lvert\det(a,b,c)\rvert}{\|a\|\|b\|\|c\|+(a\cdot b)\|c\|+(b\cdot c)\|a\|+(c\cdot a)\|b\|}\right).
\]
Substituting vectors from height \(\lambda\) to the center and two circumcircle vertices separated by \(\alpha\) gives determinant \(\lambda R^2\sin\alpha\) and, after cancelling \(\lambda\), denominator \(R^2(1+\cos\alpha)+2\lambda^2+2\lambda\sqrt{\lambda^2+R^2}\). The sum \(n\Omega_\triangle\), divided by \(2\pi\), gives the closed form. No assumption of an even number of sides was used.

## Verification
The standalone `check_shadow.py` uses NumPy and SciPy to compare the regular-polygon formula against 20 one-dimensional quadratures; numerically reconstruct 2,250 randomly shifted, randomly scaled irregular-polygon pairs and check their hull vertex counts; and test six Monte Carlo random-orientation samples, 3,500 orientations each. Execution in the supplied environment ended with `HOMOTHETIC_FRUSTUM_SHADOW_OK area_integrals=20 irregular_hulls=2250 monte_carlo=21000`. Tests are finite corroboration; the all-polygon and almost-every-direction assertions are established by the preceding geometry and change of variables.

## Relationship to prior work
Finch (2012) treats distributions and moments of uniformly random polyhedral shadows, including cube and tetrahedron; it does not give this universal homothetic-frustum vertex-count distribution. Horváth and Lángi (2022), particularly their Theorem 6, establish the containment equivalence \(tK+s\subseteq K\iff s\in(1-t)K\), which is an acknowledged premise for the \(n\)-vertex event, but do not supply the \(n+2\) exhaustive complement or spherical probability law. Glisse, Lazard, Michel, and Pouget study expected silhouette complexity of random Poisson polytopes rather than fixed homothetic frusta in uniformly random directions. A semantic search of relevant geometric research records located related frustum volume-product and other-polytope silhouette results but no direct equivalent. These comparisons do not prove global priority.

## Limitations
The two-atom law relies on two bases being parallel, directly homothetic without rotation, and having the same genuine polygon-vertex structure. It does not cover nonhomothetic frusta, truncated cones with smooth bases, or degenerate \(t=0\) pyramids (where the vertex support differs). A single observed frequency identifies only \(\lambda\) with known base shape, not base geometry nor \(h,t\) individually; no finite-sample confidence or stability bound is claimed. The mathematical proof and computations are not independently audited, and older unindexed literature may contain equivalent formulations.

## References
1. S. R. Finch, *Planar Projections and Second Intrinsic Volume* (2012), arXiv:1203.2464, https://arxiv.org/abs/1203.2464 . First public posting 2012-03-12.
2. Á. G. Horváth and Z. Lángi, *On the convex hull and homothetic convex hull functions of a convex body*, Geometriae Dedicata 216, 10 (2022), https://doi.org/10.1007/s10711-022-00673-y .
3. M. Glisse, S. Lazard, J. Michel and M. Pouget, *Silhouette of a Random Polytope*, Journal of Computational Geometry 7 (2016), 86–99, https://jocg.org/index.php/jocg/article/download/3009/2717/7784 .
