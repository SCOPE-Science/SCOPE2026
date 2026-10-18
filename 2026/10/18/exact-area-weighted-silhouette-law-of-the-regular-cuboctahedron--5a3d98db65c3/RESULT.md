# Exact area-weighted silhouette law of the regular cuboctahedron

## Finding

Let \(K\subset\mathbb R^3\) be the regular cuboctahedron with vertices all signed coordinate permutations of \((1,1,0)\), so its edge length is \(\sqrt2\). Select a uniform direction \(U\in S^2\); let \(P_U\) be the orthogonal projection of \(K\) onto \(U^\perp\), let \(N(U)\) be the number of vertices of the convex projected polygon, and let \(B(U)\) be its area. All distributional statements ignore a set of directions of spherical measure zero, where supporting facets or projected edges can be degenerate.

For the sorted absolute coordinates \(a\ge b\ge c\ge0\) of \(U\), the **complete directionwise silhouette and brightness law** is

\[
(N,B)=\begin{cases}
(8,4a+2b+2c),&a>b+c,\\
(6,3a+3b+3c),&a<b+c.
\end{cases}
\]

Write \(p=\dfrac{12}{\pi}\arctan(3-2\sqrt2)\). Then

\[
\Pr(N=8)=p,\qquad \Pr(N=6)=1-p,
\]

and the exact *area-weighted probabilities* are

\[
\boxed{\mathbb E[B\mathbf 1_{\{N=8\}}]=3,\qquad
\mathbb E[B\mathbf 1_{\{N=6\}}]=\sqrt3.}
\]

Consequently, the two conditional expected projected areas and their covariance with silhouette complexity are

\[
\mathbb E[B\mid N=8]=\frac3p,
\qquad \mathbb E[B\mid N=6]=\frac{\sqrt3}{1-p},
\]
\[
\boxed{\operatorname{Cov}(N,B)=2\bigl(3-(3+\sqrt3)p\bigr)<0.}
\]

Numerically, \(p\approx0.649040687816\), the octagonal mean is \(4.622206367513\), the hexagonal mean is \(4.935189771122\), and the covariance is \(-0.142587021853\). Thus the more complicated octagonal shadow is smaller on average than a hexagonal shadow.

## Assumptions and scope

The polytope is exactly \(K=\operatorname{conv}\{(\pm1,\pm1,0),(\pm1,0,\pm1),(0,\pm1,\pm1)\}\), with all independent sign choices in the displayed pairs. Viewing directions have normalized rotation-invariant surface measure on \(S^2\). The projected area is Euclidean two-dimensional Lebesgue area; a silhouette side or vertex counts as one edge of the projected *convex hull*. No perspective camera, occlusion outside the solid, or sampling uncertainty is included.

On the lower-dimensional transition set \(a=b+c\), the generic formula is not used to define the vertex count. That set has probability zero and does not affect any expectation.

## Proof

**1. Polyhedral faces and visibility.** The cuboctahedron is equivalently
\[
K=[-1,1]^3\cap\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le2\}.
\]
It has six square facets with outward unit normals \(\pm e_i\) and area \(2\), and eight equilateral triangular facets with unit normals \(s/\sqrt3\), where \(s\in\{-1,1\}^3\), each of area \(\sqrt3/2\). Every one of its 24 edges separates a square from a triangle. For a generic direction \(u\), an edge lies on the shadow boundary if and only if its two facet normals have opposite-signed scalar products with \(u\). Each such original edge projects to one distinct polygon edge.

By signed coordinate symmetry assume \(u=(a,b,c)\) with \(a>b>c>0\). For a positive square normal \(e_i\), the adjacent triangle normals have signs \(s_i=+1\); count those satisfying \(s\cdot u<0\). If \(a<b+c\), this gives counts \((1,1,1)\) for \(i=1,2,3\). If \(a>b+c\), the counts are \((0,2,2)\). The three negative square normals contribute identical counts by \(s\mapsto-s\). Therefore the total number of silhouette edges is respectively \(2(1+1+1)=6\) or \(2(0+2+2)=8\). For a generic convex polygon, side and vertex counts coincide.

**2. Spherical probability.** Because both signs and permutations of the direction are symmetries, the absolute coordinate vector is uniform on the positive spherical octant, which has area \(\pi/2\). Within that octant the octagonal event is the disjoint union (up to boundaries) of three congruent spherical triangles
\[
C_i=\{u\in S^2:u_i>u_j+u_k,\ u_1,u_2,u_3>0\}.
\]
For \(C_1\), the vertices are \(e_1\), \((1,1,0)/\sqrt2\), and \((1,0,1)/\sqrt2\). The great-circle side lengths are \(\pi/4,\pi/4,\pi/3\); the internal angles are \(\pi/2,\alpha,\alpha\), where \(\alpha=\arccos(1/\sqrt3)\). Girard's formula gives
\[
\Omega=\operatorname{area}(C_1)=2\alpha-\frac\pi2
=2\arctan(3-2\sqrt2).
\]
Thus \(\Pr(N=8)=3\Omega/(\pi/2)=12\arctan(3-2\sqrt2)/\pi\), as claimed.

**3. Projected-area profile.** Cauchy's projection formula for a convex polyhedron gives the area of the shadow:
\[
B(u)=\frac12\sum_{F}\operatorname{area}(F)|u\cdot\nu_F|
=2\sum_{i=1}^3|u_i|+\frac14\sum_{s\in\{-1,1\}^3}|s\cdot u|.
\]
For sorted absolute coordinates \(a\ge b\ge c\ge0\), direct expansion of the eight terms gives the two expressions in the finding. It also yields \(\mathbb E B=\operatorname{area}(\partial K)/4=(12+4\sqrt3)/4=3+\sqrt3\).

**4. The nontrivial area-weighted event integral.** It suffices to integrate over \(C_1\), where \(B(u)=4u_1+2u_2+2u_3\). For a spherical polygon \(C\) with piecewise great-circle boundary and outward unit conormal \(\nu\), the spherical divergence theorem applied to the tangent vector field \(w-(w\cdot u)u\) gives
\[
\int_Cu\,d\omega=-\frac12\int_{\partial C}\nu\,ds.
\]
The three boundary arcs of \(C_1\) have lengths \(\pi/4,\pi/4,\pi/3\) and outward unit conormals respectively \(-e_2,-e_3,-(1,-1,-1)/\sqrt3\). Hence
\[
I:=\int_{C_1}u\,d\omega
=\frac12\left[\frac\pi4(e_2+e_3)+\frac\pi{3\sqrt3}(1,-1,-1)\right].
\]
It follows that \(\int_{C_1}B\,d\omega=(4,2,2)\cdot I=\pi/2\). Since there are three congruent octagonal triangles in an octant and the positive-octant probability density is \(2/\pi\),
\[
\mathbb E[B\mathbf 1_{\{N=8\}}]=\frac2\pi\cdot3\cdot\frac\pi2=3.
\]
Subtracting from \(\mathbb E B=3+\sqrt3\) gives the second weighted expectation.

**5. Covariance and strict sign.** Because \(N=6+2\mathbf1_{\{N=8\}}\) almost surely,
\[
\operatorname{Cov}(N,B)=2\left(\mathbb E[B\mathbf1_{\{N=8\}}]-\Pr(N=8)\mathbb EB\right),
\]
which equals the stated expression. For an exact sign check, let \(\delta=3-2\sqrt2\). Elementary bounds \(6/35<\delta<1/5\), \(\arctan\delta>\delta-\delta^3/3\), and \(\pi<22/7\) imply
\[
p>\frac{42}{11}\left(\frac6{35}-\frac1{375}\right)=\frac{886}{1375}>\frac{16}{25}.
\]
But \((3-\sqrt3)/2<16/25\) because \(\sqrt3>43/25\), so \((3+\sqrt3)p>3\). Thus the covariance is strictly negative, and the conditional octagonal mean is strictly smaller.

## Verification

A standalone Python checker is included as `verify_cuboctahedron.py`. It independently computes polygonal convex hulls of projections of the twelve original vertices for 500 directions; compares hull areas and side counts to the piecewise formulas; integrates the spherical triangle using two-dimensional Gaussian quadrature (5,184 nodes); and checks the conditional first moments with 240,000 seeded random directions. The recorded successful execution is:

`CUBOCTAHEDRON_SILHOUETTE_OK quadrature_nodes=5184 direct_hulls=500 monte_carlo=240000 p_octagon=0.649040687816 mean_oct_area=4.622206367513 mean_hex_area=4.935189771122 covariance=-0.142587021853`

The spherical triangle geometry, divergence identity, and elementary sign count—not simulations or floating-point checks—establish the exact theorem.

## Relationship to prior work

The *unweighted* mean silhouette edge count of a polyhedron has a classical dihedral-angle identity, as explicitly given by McGuire (2004). Since the cuboctahedron has only six- and eight-sided generic shadows, that identity already determines \(\Pr(N=8)\) once the dichotomy is known. **Neither the dihedral-angle identity nor the classical Cauchy mean-area identity is claimed as new.** The principal additional result is the exact partition of projected-area expectation into \(3\) and \(\sqrt3\), and hence the conditional means, their strict order, and the negative area–complexity covariance. The complete directionwise chamber formulas make this joint information explicit.

Glisse and Lazard study asymptotic expected silhouette size of surface approximations, Biedl–Hasan–López-Ortiz investigate prescribed silhouette viewpoints and inverse reconstruction from projection counts, and Black–Criado obtain general bounds on expected vertices of random two-dimensional polytope shadows. The inspected portions of these works do not give the cuboctahedral area-weighted identity or its negative covariance. General-purpose integral and silhouette rules provide proof ingredients but not a documented earlier evaluation of this exact joint statistic.

## Limitations

This is an exact population law for one canonically scaled regular cuboctahedron and uniformly random *orthographic* viewing directions. The unweighted octagon probability is already implied by prior dihedral-angle theory; novelty is not asserted for that marginal alone. The proof does not yield a closed form for every conditional area quantile, finite-sample error bounds, or conclusions for deformed cuboctahedra. Historical priority of the weighted identity is assessed only against the inspected sources and remains subject to older or differently named projection literature. No external independent validation has been performed.

## References

1. M. McGuire, *Observations on Silhouette Sizes*, Journal of Graphics Tools 9(1), 1–12 (2004), DOI: 10.1080/10867651.2004.10487594. Author-uploaded full text: https://www.researchgate.net/publication/228524924_Observations_on_Silhouette_Sizes.
2. M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087 (first arXiv public posting 2007-02-14). Author full text: https://geometrica.saclay.inria.fr/team/Marc.Glisse/publications/silh/dcg.pdf.
3. T. C. Biedl, M. Hasan, and A. López-Ortiz, *Efficient View Point Selection for Silhouettes of Convex Polyhedra*, https://cs.uwaterloo.ca/~alopez-o/files/EVPSfSoCP_2011.pdf (author preprint, inspected).
4. T. C. Biedl, M. Hasan, and A. López-Ortiz, *Reconstructing Convex Polygons and Convex Polyhedra from Edge and Face Counts in Orthogonal Projections*, https://cs.uwaterloo.ca/~alopez-o/files/Rcpacpfeafciop_2010.pdf (author preprint, inspected).
5. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1 (2024-06-11), https://arxiv.org/html/2406.06936v1.
