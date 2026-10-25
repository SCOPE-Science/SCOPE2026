# Complete width laws and stochastic ordering for the dual golden Platonic solids

## Finding

Put \(\varphi=(1+\sqrt5)/2\), and let \(I\) and \(D\) be the regular icosahedron and the regular dodecahedron, respectively, both scaled to circumradius one and centered at the origin. For \(P\in\{I,D\}\), choose a direction \(U\) uniformly on \(S^2\) and define its normalized directional width by
\[
T_P=\frac12\bigl(\max_{x\in P}U\cdot x-\min_{x\in P}U\cdot x\bigr).
\]
The two random variables have the **same exact support** \([r,1]\), with
\[
r=\sqrt{\frac{5+2\sqrt5}{15}}=0.794654472291766\ldots,
\]
but their distributions are *strictly stochastically ordered*:
\[
\boxed{\quad\Pr(T_D>t)>\Pr(T_I>t)\quad\text{for every }r<t<1.\quad}
\]
There is no strict inequality at or outside the common support. The probability laws are given completely by the following elementary functions.

For \(0<c<1\) and \(0<t\le c\), define the spherical circular-segment area
\[
B(t;c)=2\arctan\!\left(\frac{\sqrt{c^2-t^2}}{\sqrt{1-c^2}}\right)
-2t\arccos\!\left(\frac{t\sqrt{1-c^2}}{c\sqrt{1-t^2}}\right).
\]
Extend \(B(t;c)=0\) for \(c\le t\le1\). Let
\[
c_I=\sqrt{1-\frac1{\varphi+2}}=0.850650808352040\ldots,
\qquad c_D=\sqrt{1-\frac1{3\varphi^2}}=0.934172358962716\ldots.
\]
For \(P=I,D\), set \(N_I=12,N_D=20\). The complete survival functions are
\[
\boxed{
\Pr(T_P>t)=\begin{cases}
1,&t<r,\\
\dfrac{N_P}{2}(1-t)-\dfrac{15}{\pi}B(t;c_P),&r\le t\le1,\\
0,&t>1.
\end{cases}}
\]
The central branch is interpreted using the stipulated zero extension of \(B\). The corresponding CDF is \(1-\Pr(T_P>t)\) on the support; all endpoints have zero atoms. Consequently the upper tails are *exactly linear* once \(t\ge c_P\): \(\Pr(T_I>t)=6(1-t)\) and \(\Pr(T_D>t)=10(1-t)\).

The lower endpoint has a quadratic rather than a linear onset. With \(k_P=\sqrt{1-c_P^2}\),
\[
\Pr(T_P\le r+\delta)
=\frac{15k_P}{\pi(1-r^2)\sqrt{c_P^2-r^2}}\,\delta^2+o(\delta^2),
\qquad \delta\downarrow0.
\]
The constants are approximately \(22.4406751794\) for \(I\) and \(9.4131793385\) for \(D\). Thus the strict stochastic order is already visible in their lower-tail asymptotics, despite identical endpoints.

## Assumptions and scope

All probabilities use the rotation-invariant probability measure on \(S^2\); opposite directions give the same width. Both solids are Euclidean, convex, regular, and centrally symmetric. Their normalization is **equal circumradius**, not equal edge length or volume. The icosahedron is the convex hull, after division by \(\sqrt{\varphi+2}\), of all signed coordinate permutations of \((0,1,\varphi)\) with the 12 conventional configurations:
\[
(0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1).
\]
The dodecahedron is the convex hull, after division by \(\sqrt3\), of the 20 points
\[
(\pm1,\pm1,\pm1),\quad(0,\pm\varphi^{-1},\pm\varphi),\quad
(\pm\varphi^{-1},\pm\varphi,0),\quad
(\pm\varphi,0,\pm\varphi^{-1}).
\]
Signs within each displayed family are chosen independently. A real \(t\) in the survival formula always refers to half the physical directional width at circumradius one. For an arbitrary common circumradius \(R>0\), the physical width is \(2RT_P\).

## Proof

**1. Polar support interpretation and the two spherical cells.** Central symmetry gives \(\min_{x\in P}U\cdot x=-\max_{x\in P}U\cdot x\); all vertices have norm one. Thus
\[
T_P=\max_{v\in\mathcal V_P} U\cdot v,
\]
where \(\mathcal V_P\) is the set of normalized vertices. Its spherical Voronoi cells partition \(S^2\), with one cell centered at each vertex. The cell of an icosahedral vertex is a regular spherical pentagon (five adjacent vertices); the cell of a dodecahedral vertex is a regular spherical triangle (three adjacent vertices). Each has area \(4\pi/N_P\).

Let \(a_P\) be the angular distance from a cell center to its sides. If two adjacent vertices are distance \(\ell_P\) apart as Euclidean unit-sphere points, then \(\sin a_P=\ell_P/2=:k_P\) and \(c_P=\cos a_P\). The Cartesian vertex descriptions give \(\ell_I=2/\sqrt{\varphi+2}\) and \(\ell_D=2/(\sqrt3\varphi)\), hence the \(c_P\) above. For a spherical regular \(q_P\)-gon cell, \(q_I=5,q_D=3\). The farthest point from its center is a Voronoi vertex, lying at angular distance \(b_P\) where
\[
\tan b_P=\frac{\tan a_P}{\cos(\pi/q_P)}.
\]
Substitution gives \(\cos b_I=\cos b_D=r\) as explicitly stated. Equivalently, these Voronoi vertices point toward face centers, whose normalized support value is the ordinary inradius-to-circumradius ratio. Thus \(r\le T_P\le1\) with both bounds attained.

**2. A spherical cap clipped by a regular cell.** Fix a vertex \(v\) and write \(\alpha=\arccos t\). The event \(U\cdot v>t\) cuts out a spherical cap of area \(2\pi(1-t)\). The same cap restricted to the Voronoi cell is exactly the event that \(v\) is a maximizing vertex and \(T_P>t\). If \(t\ge c_P\), the cap is contained in the cell. If \(r\le t<c_P\), it crosses each of the \(q_P\) side great circles. We show the portions cut away by distinct sides are disjoint up to null boundaries: in the gnomonic chart \(u\mapsto u_\perp/(u\cdot v)\), the cell becomes a centered regular Euclidean \(q_P\)-gon of apothem \(\tan a_P\), while the cap becomes a disk of radius \(\tan\alpha\). Two exterior supporting halfplanes cannot meet this disk before it reaches a polygon vertex, of radius \(\tan b_P\). This follows by minimizing radius under two halfplane constraints: the smallest feasible radius occurs for adjacent sides at their intersection. As \(\alpha\le b_P\), all side-loss regions are disjoint.

Each side loss has the same area \(B(t;c_P)\). To derive this expression directly, choose spherical coordinates with pole \(v\), and let \(z=U\cdot v\). A side great circle is at pole distance \(a_P\); its forbidden angular aperture in the level circle is
\[
2\psi_P(z),\qquad \psi_P(z)=\arccos\!\left(\frac{k_Pz}{c_P\sqrt{1-z^2}}\right),\quad t\le z\le c_P.
\]
Since spherical area is \(dz\,d\theta\), the clipped area is
\[
B(t;c_P)=2\int_t^{c_P}\psi_P(z)\,dz.
\]
Integration by parts, using
\[
\psi_P'(z)=-\frac{k_P}{(1-z^2)\sqrt{c_P^2-z^2}},
\]
yields exactly the displayed arctangent–arccosine expression. It is continuous at \(c_P\) and vanishes there. Thus the cap area within a Voronoi cell is \(2\pi(1-t)-q_P B(t;c_P)\). Summing over all \(N_P\) congruent cells, and dividing by \(4\pi\), gives
\[
\Pr(T_P>t)=\frac{N_P}{2}(1-t)-\frac{N_Pq_P}{4\pi}B(t;c_P).
\]
Because \(N_Iq_I=N_Dq_D=60\), both clipped branches have the common coefficient \(15/\pi\). For \(t<r\) every direction is covered and for \(t>1\) none is, completing both distributions.

**3. Strict stochastic ordering.** Write \(H(t)=\Pr(T_D>t)-\Pr(T_I>t)\). The parameters satisfy
\[
r<c_I<c_D<1,
\qquad k_I>k_D>0.
\]
For \(r<t<c_I\), differentiate the two survival laws, noting \(B'(t;c)=-2\psi(t;c)\):
\[
H'(t)=-4+\frac{30}{\pi}\bigl(\psi_D(t)-\psi_I(t)\bigr).
\]
At \(t=r\), the regular-cell vertex geometry gives \(\psi_D(r)=\pi/3\) and \(\psi_I(r)=\pi/5\); hence \(H'(r+)=0\). Moreover
\[
\frac{d}{dt}(\psi_D-\psi_I)
=\frac1{1-t^2}\left(
\frac{k_I}{\sqrt{c_I^2-t^2}}-\frac{k_D}{\sqrt{c_D^2-t^2}}
\right)>0.
\]
The strict sign follows from \(k_I>k_D\) and \(c_I<c_D\). Therefore \(H'(t)>0\) for \(r<t<c_I\), and since \(H(r)=0\), also \(H(t)>0\) there. For \(c_I\le t<c_D\),
\[
H'(t)=-4+\frac{30}{\pi}\psi_D(t),
\]
which is strictly decreasing. Consequently \(H\) has no interior minimum on this interval. Its endpoints are strictly positive (the first by the preceding argument, the second because \(H(c_D)=4(1-c_D)>0\)). For \(c_D\le t<1\), the formula simplifies to \(H(t)=4(1-t)>0\). This proves strict stochastic dominance for every interior threshold.

**4. Endpoint behavior.** For \(t\uparrow1\), the disjoint-cap branch is exact, not asymptotic. At the common lower endpoint, \(\psi_P(r)=\pi/q_P\) makes the CDF's first derivative vanish. Differentiating once more gives
\[
\frac{d^2}{dt^2}\Pr(T_P\le t)\bigg|_{t=r+}
=\frac{N_Pq_P k_P}{2\pi(1-r^2)\sqrt{c_P^2-r^2}},
\]
and Taylor's formula supplies the asserted quadratic coefficient. No limiting numerical experiment is used as a proof of either tail.

## Verification

A standalone script `verify_golden_widths.py` reconstructs the vertices from the explicit Cartesian coordinates above and calculates widths by maximization of their scalar products with uniformly distributed directions. It independently compares 220,000 sampled directions for each solid at seven thresholds with the exact CDF. It checks the shared support, cell-angle identities, strict stochastic order on a dense grid, and the computed tail constants. It uses only the Python standard library. These finite computations corroborate but do not replace the spherical-geometry proof or the analytic monotonicity argument. Run from the extracted package directory using `python3 verify_golden_widths.py`.

As an independent quantitative consistency test, integrating the icosahedral law yields \(\mathbb E[T_I^2]\approx0.841278529664\). Under unit-edge scaling, multiplication by \(\varphi+2\) gives \(3.04377431433\), consistent with the previously published exact second moment \((5+\sqrt5)/6+10\sqrt3/(3\pi)\). This moment identity is not presented as a new discovery.

## Relationship to prior work

Finch's 2011 width-distribution study examines the tetrahedron and cube, notably their first two moments; it does not give the complete golden-polyhedron width distributions or a comparison of them. Mazonka's 2012 solid-angle formulas furnish a general method for spherical cap intersections but do not identify the strictly ordered width laws here. Abas (2026) proves a general normal-fan coarea density theorem for arbitrary three-dimensional polytopes and works out the tetrahedron, rhombic dodecahedron, and truncated octahedron. That theorem provides general machinery for specializations, and the present explicit CDFs should be viewed as computations compatible with it, **not** as claiming a new general polytope-density existence theorem. The substantive comparative assertion—the strict ordering between the two dual golden polyhedra at equal circumradius—is not stated or implied merely by the general density representation. Public mathematical records also give moments for the icosahedron and dodecahedron, but finitely many moments alone do not settle pointwise stochastic ordering. An unknown earlier specialized width or spherical-cap paper remains a legitimate priority risk.

## Limitations

The result is specific to the two regular dual golden Platonic solids with **the same circumradius**. Replacing equal circumradii by equal edge lengths, equal surface areas, or equal volumes changes the comparison and is not treated. The proof uses both central symmetry and the one-shell regularity of their spherical Voronoi cells; it makes no universal stochastic-order assertion for arbitrary polar-dual polyhedra or spherical codes. The exact CDF is derived from standard spherical cap geometry and should not be mistaken for a new general method. All mathematical claims are supported by the analytic derivations above; no independent audit has yet been performed.

## References

1. Steven R. Finch, *Width Distributions for Convex Regular Polyhedra*, first publicly submitted 4 October 2011, arXiv:1110.0671, https://arxiv.org/abs/1110.0671.
2. Oleg Mazonka, *Solid Angle of Conical Surfaces, Polyhedral Cones, and Intersecting Spherical Caps*, 2012, arXiv:1205.1396, https://arxiv.org/abs/1205.1396.
3. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, first submitted 10 August 2026, arXiv:2609.26202, https://arxiv.org/abs/2609.26202; especially Sections 3, 4 and 8.
4. Steven R. Finch, *Planar Projections and Second Intrinsic Volume*, first submitted 12 March 2012, arXiv:1203.2464, https://arxiv.org/abs/1203.2464.
