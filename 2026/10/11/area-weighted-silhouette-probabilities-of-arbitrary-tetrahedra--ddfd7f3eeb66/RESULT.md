# Area-weighted silhouette probabilities of arbitrary tetrahedra
## Finding
Let \(T\subset\mathbb R^3\) be any nondegenerate tetrahedron, and choose a viewing direction \(U\) uniformly from \(S^2\). Write \(B(U)\) for the Euclidean area of its orthogonal projection onto \(U^\perp\), and \(N(U)\) for the number of vertices of that shadow. Apart from a null set of directions, \(N(U)\in\{3,4\}\). This finding gives *finite geometric formulas* for
\[
\mathbb P(N=3),\qquad
\mathbb E[B\mathbf1_{N=3}],\qquad
\mathbb E[B^2\mathbf1_{N=3}],
\]
and hence both conditional area moments for both shadow types, for **every** nondegenerate tetrahedron.

Write the vertices \(v_0,v_1,v_2,v_3\). For each vertex \(v_i\), let \(F_i\) denote the opposite face, with area \(A_i>0\) and **outward** unit normal \(n_i\). Let
\[
e_{ij}=\frac{v_j-v_i}{\|v_j-v_i\|}\qquad (j\ne i),
\]
and let \(C_i\) be the spherical triangle enclosed by the three rays \(e_{ij}\), of spherical area \(\Omega_i\). For distinct \(i,j,k\), set \(\theta_{ijk}=\arccos(e_{ij}\cdot e_{ik})\in(0,\pi)\) and let \(\ell\) be the remaining vertex index (so \(\{i,j,k,\ell\}=\{0,1,2,3\}\)). All sums \(\sum_{\{j,k\}}\) below run over the three unordered pairs of the other vertices.

The two elementary **spherical cone integrals** are
\[
I_{1,i}=-\frac12\sum_{\{j,k\}}\theta_{ijk}(n_i\cdot n_\ell),
\tag{1}
\]
\[
I_{2,i}=\frac{\Omega_i}{3}-\frac13\sum_{\{j,k\}}
(n_i\cdot n_\ell)\tan\!\left(\frac{\theta_{ijk}}2\right)
[n_i\cdot(e_{ij}+e_{ik})].
\tag{2}
\]
The exact **area-weighted silhouette identities** are
\[
\boxed{\mathbb P(N=3)=\frac{\sum_i\Omega_i}{2\pi},\qquad
\mathbb E[B\mathbf1_{N=3}]=\frac{\sum_i A_i I_{1,i}}{2\pi},\qquad
\mathbb E[B^2\mathbf1_{N=3}]=\frac{\sum_i A_i^2 I_{2,i}}{2\pi}.}
\tag{3}
\]
For completeness, the unconditional moments are
\[
\mathbb E[B]=\frac14\sum_i A_i,
\tag{4}
\]
\[
\mathbb E[B^2]=\frac1{12}\sum_i A_i^2+
\frac1{3\pi}\sum_{i<j}A_i A_j
\left(\sqrt{1-c_{ij}^2}+c_{ij}\arcsin c_{ij}\right),
\qquad c_{ij}=n_i\cdot n_j.
\tag{5}
\]
Equations (3)--(5) give the first and second **conditional** moments directly. Specifically, write \(p_3\), \(m_{1,3}\), \(m_{2,3}\) for the three quantities in (3), put \(p_4=1-p_3\), and write \(m_1,m_2\) for (4)--(5). Then
\[
\mathbb E[B^k\mid N=3]=\frac{m_{k,3}}{p_3},\qquad
\mathbb E[B^k\mid N=4]=\frac{m_k-m_{k,3}}{p_4},\quad k\in\{1,2\}.
\tag{6}
\]
Both denominators are positive for every full-dimensional tetrahedron.

For the regular tetrahedron with coordinates
\[
(1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1),
\]
whose edges have length \(2\sqrt2\), define
\[
\alpha=\arcsin(1/3),\qquad\Omega=\frac\pi2-3\alpha.
\]
Then \(p_3=2\Omega/\pi\), \(p_4=6\alpha/\pi\), and
\[
\boxed{\begin{aligned}
\mathbb E[B\mid N=3]&=\frac{\pi}{\sqrt3\,\Omega},&
\mathbb E[B^2\mid N=3]&=4+\frac{8\sqrt2}{3\Omega},\\
\mathbb E[B\mid N=4]&=\frac{2\pi}{3\sqrt3\,\alpha},&
\mathbb E[B^2\mid N=4]&=\frac{16}{3}+\frac{16\sqrt2}{9\alpha}.
\end{aligned}}
\tag{7}
\]
Numerically, the conditional first moments are approximately \(3.29012651408161\) and \(3.55817612071177\), while the conditional second moments are approximately \(10.8408029831561\) and \(12.7314627721201\). The conditional variances are approximately \(0.0158705044933\) and \(0.0708454661166\). The strict first-moment selection bias is
\[
\mathbb E[B\mid N=3]<\mathbb E[B\mid N=4].
\tag{8}
\]

## Assumptions and scope
The tetrahedron must be nondegenerate. No regularity, edge-length equality, symmetry, or assumed distribution of face normals is used for (1)--(6). The viewing direction is Haar-uniform; \(U\) and \(-U\) define the same plane. The excluded nongeneric projection directions form a spherical null set.

All faces use outward normals. The sign in (1)--(2) depends on that convention. The spherical area \(\Omega_i\) can be evaluated directly from the three directed vertex-edge unit vectors \(a,b,c\) by
\[
\Omega_i=2\operatorname{atan2}\!\left(\left|\det(a,b,c)\right|,\,1+a\cdot b+b\cdot c+c\cdot a\right).
\tag{9}
\]
Here \(\operatorname{atan2}\) takes the positive-angle branch, so (9) is valid for every full-dimensional tangent trihedral cone. The numerical computation in `verify.py` uses precisely this convention.

Under a uniform spatial rescaling by factor \(\lambda>0\), \(B\) scales by \(\lambda^2\), its second moment by \(\lambda^4\), and the silhouette probabilities are unchanged. Thus (7) is given at the explicitly stated edge length \(2\sqrt2\), not at unit edge length.

## Proof
**1. Exact division into four spherical vertex cones.** The projected vertex \(v_i\) lies inside the projected triangle \(F_i\) exactly when the projection direction belongs to \(C_i\cup(-C_i)\), except on null boundaries. For a generic projection at most one vertex of a tetrahedron can become interior to its projected convex hull. Therefore the four cone pairs are disjoint up to measure zero and their union is precisely the event \(N=3\). On \(C_i\), the outward opposite-face normal satisfies \(n_i\cdot u>0\), and the projected triangle is exactly the projection of \(F_i\), of area \(A_i(n_i\cdot u)\). Evenness under \(u\mapsto-u\) consequently gives
\[
\mathbb E[B^k\mathbf1_{N=3}]
=\frac1{2\pi}\sum_{i=0}^3 A_i^k
\int_{C_i}(n_i\cdot u)^k\,d\sigma(u),
\qquad k=0,1,2.
\tag{10}
\]
Here the convention \(B^0=1\) yields the unweighted probability already proved by Feldman and Klain.

**2. The first-moment boundary integral.** On the unit sphere set \(f(u)=n_i\cdot u\). The spherical Laplacian satisfies \(\Delta_{S^2}f=-2f\). By the surface divergence theorem,
\[
\int_{C_i}f\,d\sigma=-\frac12\int_{\partial C_i}\partial_\nu f\,ds.
\tag{11}
\]
The boundary geodesic from \(e_{ij}\) to \(e_{ik}\) lies in the plane of face \(F_\ell\), with outward spherical conormal \(n_\ell\): the cone interior lies on the inner side of that face plane. Since \(n_\ell\cdot u=0\) along this great-circle arc, its constant tangential gradient derivative is
\[
\partial_\nu f=n_i\cdot n_\ell.
\]
The arc length is \(\theta_{ijk}\). Summing its three edges in (11) proves (1).

**3. The second-moment boundary integral.** For \(g(u)=(n_i\cdot u)^2\), the traceless degree-two spherical harmonic \(g-1/3\) satisfies
\[
\Delta_{S^2}(g-1/3)=-6(g-1/3).
\]
As \(\partial_\nu g=2f\,\partial_\nu f\), the spherical divergence theorem yields
\[
\int_{C_i}g\,d\sigma
=\frac{\Omega_i}{3}-\frac13\int_{\partial C_i}
f(u)(n_i\cdot\nu)\,ds.
\tag{12}
\]
For the shorter great-circle arc of length \(\theta\in(0,\pi)\) with unit endpoints \(p,q\), direct trigonometric parametrization gives
\[
\int_{\mathrm{arc}(p,q)}u\,ds
=\tan(\theta/2)(p+q).
\tag{13}
\]
Substitution of the outward conormals \(n_\ell\) and arc integral (13) into (12) gives (2). Together with (10), this proves the three identities (3), with no quadrature or regularity assumption beyond nondegeneracy.

**4. Complementary quadrilateral moments.** Cauchy's projected-area formula for a convex polyhedron is
\[
B(u)=\frac12\sum_{i=0}^3 A_i|n_i\cdot u|.
\tag{14}
\]
For uniform \(U\in S^2\),
\[
\mathbb E|n_i\cdot U|=\frac12,
\qquad \mathbb E[(n_i\cdot U)^2]=\frac13.
\]
For two unit normals of dot product \(c\in(-1,1)\), the exact angular kernel is
\[
\mathbb E[|n_i\cdot U||n_j\cdot U|]
=\frac{2}{3\pi}\left(\sqrt{1-c^2}+c\arcsin c\right).
\tag{15}
\]
One proof writes \(G=RU\) for a rotationally invariant Gaussian in \(\mathbb R^3\), uses \(\mathbb E[R^2]=3\), and evaluates the product of absolute values of two correlated standard Gaussian coordinates by a two-dimensional polar integral. Expanding the square in (14), applying (15), and collecting diagonal terms proves (4)--(5). Subtracting the triangular-shadow contributions yields (6), as claimed.

**5. Evaluating the regular tetrahedron.** With the displayed coordinates, all \(A_i=2\sqrt3\), all \(n_i\cdot n_j=-1/3\) for \(i\ne j\), and every planar vertex angle \(\theta_{ijk}=\pi/3\). The spherical cone area is \(\Omega=3\arccos(1/3)-\pi=\pi/2-3\arcsin(1/3)\). Each cone therefore has the exact moments
\[
I_{1,i}=\frac\pi6,\qquad
I_{2,i}=\frac\Omega3+\frac{2\sqrt2}{9}.
\tag{16}
\]
Substituting (16) in (3) and dividing by \(p_3=2\Omega/\pi\) gives the two triangular entries in (7). The unconditional moments specialize to
\[
\mathbb E B=2\sqrt3,\qquad
\mathbb E B^2=4+\frac8\pi(2\sqrt2+\alpha).
\tag{17}
\]
Subtracting the triangular weighted moments and dividing by \(p_4=6\alpha/\pi\) gives the two quadrilateral entries in (7).

The first-moment strict inequality (8) reduces algebraically to \(9\alpha<\pi\), equivalently \(\arcsin(1/3)<\pi/9\). To check it without numerical approximation, note \(3\alpha<\pi/2\) and
\[
\sin(3\alpha)=3(1/3)-4(1/3)^3=\frac{23}{27}<\frac{\sqrt3}{2}=\sin(\pi/3).
\]
Monotonicity of sine on \((0,\pi/2)\) yields \(3\alpha<\pi/3\), proving (8).

## Verification
The bundled standalone `verify.py` calculates all face areas, outward normals, tangent-cone spherical areas, and finite sums (1)--(5) from raw vertex coordinates. It evaluates (16)--(17) and all four entries of (7) against independent analytic expressions.

As an independent check of the *critical nonstandard cone-integral step*, the checker parametrizes each spherical cone by normalized affine combinations of its three edge-ray unit vectors and evaluates its area, linear, and quadratic moments with tensor-product Gauss--Legendre quadrature. The largest absolute error for twelve cones from three tetrahedra (one regular, two irregular) was \(3.55\times10^{-15}\). It also samples 600,000 spherical directions and compares 2,800 independently computed convex hulls of projected vertices with the face-normal brightness and shadow-type identities.

Run with `python verify.py` after installing `numpy` and `scipy`; the final line `VERIFY_OK` indicates all assertions passed. These finite diagnostics are not an all-tetrahedra proof; the all-tetrahedra identities rest on the exact divergence-theorem argument above.

## Relationship to prior work
Feldman and Klain established the **unweighted** tetrahedral triangular-shadow probability through interior solid angles. The first identity in (3) is their result and is not claimed as new.

Finch studied regular tetrahedral planar projection area and perimeter. His §2.1 already gives both unconditional area moments and the probability of three-versus-four shadow vertices. His §5 provides an angular piecewise expression for the area random variable. Those contributions are prior work; they are not renamed here. The distinction is a closed conditional first- and second-moment table together with formulas holding for **arbitrary asymmetric tetrahedra** using only face normals, edge angles, and solid angles. The face-angle weighted identities are not immediate numerical restatements of unconditional moments.

Black and Criado studied expected **combinatorial shadow complexity** and projected-edge length, rather than joint moments of shadow area and silhouette type. Their work supplies useful context but is not required by the proof.

The comparison therefore concerns **implications**, not words in titles: unweighted cone masses and unconditional face-normal moments alone do not determine the separate area-weighted masses; the boundary-integral step computes them.

## Limitations
The result is for uniformly random **orthogonal** projections of tetrahedra in three-dimensional Euclidean space. It neither computes the entire conditional area distribution nor covers nonuniform viewing directions, arbitrary higher-dimensional simplices, or the joint law of perimeter and silhouette type. It gives the first two conditional moments, not all orders.

The regular-tetrahedron unconditional moments and unweighted silhouette probabilities are known and are credited explicitly. An older unindexed stereology or projection-moment source might contain an equivalent conditional calculation; this is a residual historical originality risk. No independent audit has been performed.

## References
1. D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459v1 (19 September 2008), especially Theorem 1 and its spherical-vertex-cone proof.
2. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1 (12 March 2012), especially §2.1 and §5.
3. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1 (11 June 2024), especially §2 on projected-edge and combinatorial shadow complexity.
