# Central-section complementarity between the cube and the rhombic dodecahedron

## Finding
Let \(C=[-1,1]^3\) and let \(R\) be the rhombic dodecahedron with vertex set
\[
\{\pm2e_1,\pm2e_2,\pm2e_3\}\cup\{(\pm1,\pm1,\pm1)\}.
\]
For a nonzero vector \(u\), write \(S(u)=u^\perp\), and let \(N_C(u)\) and \(N_R(u)\) denote the numbers of vertices in the planar sections \(C\cap S(u)\) and \(R\cap S(u)\), respectively. Except for finitely many great circles of normal directions, the following **pointwise complementarity** holds:
\[
\boxed{N_C(u)+N_R(u)=12.}
\]
More precisely, set \(a=|u_1|\), \(b=|u_2|\), \(c=|u_3|\). If the largest of \(a,b,c\) is strictly smaller than the sum of the other two, the two sections are both hexagons: \((N_C,N_R)=(6,6)\). If the largest is strictly greater, then \((N_C,N_R)=(4,8)\): the cubical section is a quadrilateral and the rhombic-dodecahedral section an octagon.

When \(u\) is uniformly distributed on the sphere, the complete joint distribution is
\[
\boxed{\Pr\{(N_C,N_R)=(6,6)\}=1-\frac6\pi\arcsin\frac13}
\]
and
\[
\boxed{\Pr\{(N_C,N_R)=(4,8)\}=\frac6\pi\arcsin\frac13.}
\]
Numerically these probabilities are approximately \(0.35095931218\) and \(0.64904068782\), respectively. In particular an octagonal central section is more likely than a hexagonal one for the rhombic dodecahedron.

## Assumptions and scope
The solids are in the specified common coordinate frame and centered at the origin. The random plane passes exactly through their shared center; its unoriented normal is uniformly distributed in projective spherical measure, equivalently a uniform normal on the unit sphere. The claims hold for all \(u\) with no zero coordinate and with no equality of the form \(|u_i|=|u_j|+|u_k|\); the omitted set has spherical measure zero. Normal scaling and reversal do not change a section. The theorem is not a statement about independently oriented planes or off-center cuts.

## Proof
**(1) Edges and sign changes.** The rhombic dodecahedron has the equivalent halfspace description
\[
R=\{x\in\mathbb R^3:|x_i|+|x_j|\le2\text{ whenever }1\le i<j\le3\}.
\]
Its twelve facets are the planes \(\pm x_i\pm x_j=2\). They meet in precisely the fourteen vertices displayed above, and its twenty-four edges join each axial vertex \(2s e_i\), \(s\in\{\pm1\}\), to the four cubic vertices \(w\in\{\pm1\}^3\) with \(w_i=s\). The cube has its usual twelve edges between pairs of vertices differing in exactly one sign. A plane through the interior of a convex polytope meets an edge in an interior point exactly when the scalar products of its endpoints with the normal have opposite signs. For generic \(u\), every crossing edge contributes one distinct polygon vertex, so counting edges with opposite endpoint signs computes each \(N\).

**(2) Reduction to two chambers.** Both solids are invariant under coordinate permutations and independent sign changes. We may therefore assume \(a=u_1\ge b=u_2\ge c=u_3>0\). The signs of the eight cubic-vertex scalar products \(\pm a\pm b\pm c\) can change only at \(a=b+c\).

If \(a<b+c\), the four negative cubic vertices are \((-1,-1,-1)\) and the three with exactly one positive coordinate. In the cube, those four vertices form a vertex star; six of the twelve cube edges cross the plane. To count the edges of \(R\), observe that each negative cubic vertex \(w\) contributes two crossing axial-to-cubic edges for each positive coordinate \(w_i=1\): the edge \((2e_i,w)\) and its antipodal edge. There are exactly three positive coordinates among the four negative cubic vertices, giving \(N_R=2\cdot3=6\).

If \(a>b+c\), the negative cubic vertices are the four with first coordinate \(-1\). They form a square face of the cube, so exactly four cube edges cross. Among those four negative cubic vertices, the total number of positive coordinates is four (two in the other two coordinates, each appearing positive twice), giving \(N_R=2\cdot4=8\). Thus the pointwise assertion holds in both open chambers and, by symmetry, in every generic direction.

**(3) Haar probabilities.** In the positive octant, the triangle-inequality chamber is the spherical geodesic triangle with unit vertices
\[
\frac{(1,1,0)}{\sqrt2},\quad\frac{(1,0,1)}{\sqrt2},\quad\frac{(0,1,1)}{\sqrt2}.
\]
Each side has spherical length \(\pi/3\). The spherical cosine rule gives each interior angle \(\arccos(1/3)\); Girard's theorem gives area \(3\arccos(1/3)-\pi\). There are eight identical octants and the sphere has area \(4\pi\), hence
\[
\Pr\{(N_C,N_R)=(6,6)\}=\frac8{4\pi}\bigl(3\arccos(1/3)-\pi\bigr)
=1-\frac6\pi\arcsin\frac13.
\]
The complementary octagon/quadrilateral probability follows. Every step uses complete facet-edge incidence and exact spherical area, not extrapolation from sampling.

## Verification
Run `python rd_cube_checker.py` with Python 3 and NumPy. The checker enumerates every vertex of \(R\) by solving all independent triples of its twelve integer facet inequalities in exact rational arithmetic, reconstructs all twenty-four edges by intersections of facets, independently constructs the cube's twelve edges, and tests all coordinate sign/permutation types in both open chambers. It checks the exact spherical-angle identity and corroborates the probabilities with \(150000\) seeded independent Gaussian normal vectors. The finite and Monte Carlo components are supplementary to the analytic case analysis and Girard formula.

## Relationship to prior work
The cube marginal \(\Pr(N_C=6)=1-6\arcsin(1/3)/\pi\) is known, including Yawen Zhang's 2020 geometric derivation. It is **not** newly claimed here. The new assertion concerns the canonically cooriented central sections of the **different** rhombic-dodecahedral solid, and the pointwise complementarity \(N_C+N_R=12\). The previously known cube probability becomes the joint law only after the distinct rhombic-dodecahedral edge-incidence theorem has been proved. The shape's classical vertex and facet structure is also not new.

## Limitations
Only the specified rhombic dodecahedron and cube in their common symmetry frame are covered; arbitrary affine distortions, independently chosen normals, off-center planes, and other polyhedra are not classified. Prior descriptions of central sections of these solids in older geometric or crystallographic literature may exist; no independent historical-priority certification is claimed. Boundary normals can produce sections containing original vertices and require separate degeneracy conventions.

## References
1. Y. Zhang, *A purely 3-D geometrical solution to Mathematics Magazine Problem 2065*, arXiv:2010.12349, first public preprint October 20, 2020. https://arxiv.org/abs/2010.12349 .
2. *OEIS A349605*, probability of a hexagonal central section of the cube, https://oeis.org/A349605 .
3. M. Ferraro and L. Zaninetti, *Statistics of cross sections of Voronoi tessellations*, Physical Review E **84** (2011), 041107, https://doi.org/10.1103/PhysRevE.84.041107 . This considers different Voronoi cross-section statistics and uses spherical approximations; it is not a source of the present theorem.
