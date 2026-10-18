# Exact random-silhouette law along the cube–octahedron interpolation

## Finding

For every real parameter \(1\le t\le3\), define the centrally symmetric convex polytope
\[
K_t=[-1,1]^3\cap\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le t\}.
\]
For a unit viewing normal \(u\), let \(N_t(u)\) be the number of vertices of the two-dimensional orthogonal projection of \(K_t\) onto \(u^\perp\). Put
\[
\delta(u)={\bf1}\bigl\{2\max_i|u_i|>\textstyle\sum_i|u_i|\bigr\}.
\]
For every direction outside the finite union of great circles where a facet normal is perpendicular to \(u\), the complete silhouette-count law is
\[
\boxed{N_t(u)=
\begin{cases}
6-2\delta(u),&t=1,\\
12,&1<t<2,\\
6+2\delta(u),&t=2,\\
12+2\delta(u),&2<t<3,\\
6,&t=3.
\end{cases}}
\]
In particular, every generic orthographic shadow is a dodecagon for the entire open octahedron-truncation regime \(1<t<2\), even though most of these solids are not zonohedra. At the cuboctahedron \(t=2\) there is a sharp count collapse, followed immediately by a two-atom law for the cube-truncation regime \(2<t<3\).

For a viewing normal \(U\) uniformly distributed on the unit sphere, set
\[
p=\Pr(\delta(U)=1)=\frac{12}{\pi}\arctan(3-2\sqrt2)
=0.6490406878163556\ldots.
\]
The five parameter regimes above give the exact joint atom probabilities: at \(t=1\) the counts \(4,6\) have probabilities \(p,1-p\); for \(1<t<2\) the count \(12\) has probability one; at \(t=2\) the counts \(8,6\) have probabilities \(p,1-p\); for \(2<t<3\) the counts \(14,12\) have probabilities \(p,1-p\); and at \(t=3\) the count \(6\) has probability one. These laws are independent of the precise truncation depth inside either open interval.

## Assumptions and scope

The family is normalized as displayed. A silhouette vertex means a genuine extreme vertex of the planar projected convex polygon, not an interior point or a collinear marked edge point. The generic-direction exclusion includes \(u_i=0\) and \(\sigma\cdot u=0\) for any sign vector \(\sigma\in\{-1,1\}^3\). These exclusions have surface measure zero; the formula is asserted only off them and has no claim about the lower-dimensional degenerate-direction cases. At \(t=1,3\), redundant supporting planes are not counted as facets. All probabilities refer to Haar-uniform viewing directions on \(S^2\), equivalently uniform unoriented planes.

## Proof

**1. Exact facet and edge inventories.** Denote the six axis facet normals by \(A_i^{\varepsilon}=\varepsilon e_i\), with \(1\le i\le3\), \(\varepsilon\in\{-1,1\}\), and the eight diagonal facet normals by \(D_\sigma=\sigma\), where \(\sigma\in\{-1,1\}^3\). The defining inequalities are \(A_i^{\varepsilon}\cdot x\le1\) and \(D_\sigma\cdot x\le t\).

For \(1<t<2\), each axis facet is a square with four vertices, and each diagonal facet is a hexagon whose vertices, after sign changes, are the six permutations of \((1,t-1,0)\). The edge adjacency is exactly: all \(24\) pairs \((A_i^{\varepsilon},D_\sigma)\) with \(\varepsilon=\sigma_i\), and all \(12\) pairs of diagonal normals whose signs differ in exactly one coordinate. This follows directly by intersecting the two corresponding facet equations with the remaining inequalities: every listed pair contains a nontrivial segment, and unlisted pairs have at most a common vertex.

For \(2<t<3\), each axis facet is an octagon and each diagonal facet is a triangle with vertices, after sign changes, the three permutations of \((1,1,t-2)\). Now the \(24\) axis–diagonal adjacencies persist, while the other \(12\) edges join pairs of axis normals supported on distinct coordinate axes. At \(t=2\), only the \(24\) axis–diagonal edges remain. At \(t=1\) only the \(12\) diagonal–diagonal edges remain; at \(t=3\) only the \(12\) axis–axis edges remain. Thus the successive \((V,E,F)\) inventories are \((6,12,8)\), \((24,36,14)\), \((12,24,14)\), \((24,36,14)\), and \((8,12,6)\).

**2. Silhouette-edge count.** For a convex polyhedron and a generic direction, an edge belongs to the boundary of its orthographic shadow if and only if its two incident facet normals have dot products with \(u\) of opposite signs. The shadow is a nondegenerate convex polygon, so its number of vertices equals its number of silhouette edges.

Signed coordinate permutations preserve both \(K_t\) and its graph. Consequently assume \(u=(a,b,c)\) with \(a>b>c>0\). The six axis-facet signs are then fixed. Among the eight diagonal-facet signs, all are determined by the first sign coordinate if \(a>b+c\). When \(a<b+c\), the signs at \((+,-,-)\) and \((-,+,+)\) reverse, and the other six signs are unchanged. The number of separating edges of each adjacency class is therefore

| Regime for the normal | Axis–diagonal | Diagonal–diagonal | Axis–axis |
|---|---:|---:|---:|
| \(a>b+c\) | 8 | 4 | 6 |
| \(a<b+c\) | 6 | 6 | 6 |

The diagonal–diagonal column follows by counting sign changes on the twelve edges of the \(3\)-cube of diagonal normals. The axis–axis column has two opposite-sign pairs for each choice of two distinct axes. Summing just those adjacency classes that exist in each parameter interval proves the displayed law. Equality cases \(a=b+c\) lie on an excluded great circle; coordinate coincidences follow by continuity within generic sign chambers.

**3. Exact spherical probabilities.** The six open cones \(\{u: \pm u_i>|u_j|+|u_k|\}\) are disjoint and constitute the event \(\delta(u)=1\). One such cone, around \(e_1\), splits into four congruent spherical triangles with vertices \(e_1\), \((e_1+e_2)/\sqrt2\), and \((e_1+e_3)/\sqrt2\), with signs adjusted between quadrants. The exact solid-angle identity for three unit vectors \(v_0,v_1,v_2\),
\[
\Omega=2\arctan\frac{|\det(v_0,v_1,v_2)|}{1+v_0\cdot v_1+v_1\cdot v_2+v_2\cdot v_0},
\]
gives \(\Omega=2\arctan(3-2\sqrt2)\) per triangle because the numerator is \(1/2\) and the denominator is \(3/2+\sqrt2\). Six cones with four triangles each cover solid angle \(48\arctan(3-2\sqrt2)\). Division by \(4\pi\) yields \(p\) and hence all stated probabilities.

**4. Non-zonohedral constancy.** For \(1<t<2\), the diagonal facet has vertices permuting \((1,t-1,0)\), with centroid \((t/3,t/3,t/3)\). If this hexagon were centrally symmetric, the reflection of \((1,t-1,0)\) about its centroid would have to be one of those six vertices. Its three coordinates are \((2t/3-1,1-t/3,2t/3)\). In the open interval \((1,2)\), the only way that this reflected vector has a zero coordinate is \(t=3/2\). Hence every other open-interval member has a noncentrally symmetric two-face and is not a zonotope. The regular truncated octahedron at \(t=3/2\) is the well-known zonohedral member; the silhouette count nevertheless remains twelve throughout the interval.

## Verification

The standalone script `verify_silhouette_law.py` uses exact rational half-space intersections to reconstruct all vertices and face-adjacency edges at nine representative parameters, including all three endpoint shapes. It compares the predicted adjacency sets with the independently reconstructed sets; checks every one of the \(96\) signed-permutation chamber representatives; and compares the edge-sign formula against exact two-dimensional convex hulls for \(2358\) rational direction/parameter tests. A separate seeded Haar simulation of \(400000\) Gaussian directions checks the solid-angle probability to sampling accuracy. Exact arithmetic verifies all finite polyhedral checks; the Monte Carlo experiment is not used as proof of the spherical probability or all-direction assertions. To reproduce, run `python verify_silhouette_law.py` with a standard Python 3 interpreter.

## Relationship to prior work

Gantapara, de Graaf, van Roij, and Dijkstra introduced and studied a continuously truncated-cube family interpolating through the cuboctahedron to the octahedron, principally for dense packings and phase behavior. Their 2014 arXiv manuscript (particularly Section II and Equation (1)) gives an equivalent family up to scale and reparametrization, but its results are thermodynamic, not the orientation-by-orientation silhouette vertex law. Standard polyhedral silhouette constructions supply the general front/back-facing edge criterion used here but do not, by themselves, state the parameter-wide classification or the explicit spherical probability. Exact brightness-area and central-section results for selected members or the same family concern different quantities and do not state or imply this cardinality law without further facet-incidence analysis.

## Limitations

The theorem counts planar-shadow vertices but does not describe projected edge lengths, areas, angular perimeter distributions, or nonorthographic perspective views. Non-generic viewing directions may have additional collapsed edges and are deliberately excluded. The proof is mathematical and reproducible; no independent peer review or historical-priority certification is claimed. An exhaustive survey of all older visualization literature has not been completed.

## References

1. A. P. Gantapara, J. de Graaf, R. van Roij, M. Dijkstra, *Phase Behavior of a Family of Truncated Hard Cubes*, arXiv:1412.2597v1, first posted 8 December 2014, especially Section II, Equation (1).
2. A. P. Gantapara, J. de Graaf, R. van Roij, M. Dijkstra, *Phase Diagram and Structural Diversity of a Family of Truncated Cubes: Degenerate Close-Packed Structures and Vacancy-Rich States*, Physical Review Letters 111 (2013), 015501, DOI 10.1103/PhysRevLett.111.015501.
3. M. Glisse, *An upper bound on the average size of silhouettes*, Proceedings of the 22nd ACM Symposium on Computational Geometry (2006). Its general asymptotic silhouette question differs from the present exact fixed-family computation.
