# Exact Haar polygon-type law for central sections of the regular dodecahedron

## Finding

Let \(D\subset\mathbb R^3\) be the regular dodecahedron with vertex set
\[
V=\{(\pm1,\pm1,\pm1)\}\cup
\{(0,\pm\varphi^{-1},\pm\varphi),
(\pm\varphi^{-1},\pm\varphi,0),
(\pm\varphi,0,\pm\varphi^{-1})\},
\qquad \varphi=(1+\sqrt5)/2.
\]
Choose an unoriented plane \(H=U^\perp\) through the origin with Haar-uniform normal \(U\in S^2\). Write \(N(U)\) for the number of sides of \(D\cap H\). Put
\[
\alpha=\arccos(1/3),\qquad \beta=\arccos(\sqrt5/3).
\]
Then, almost surely, \(N\in\{6,8,10\}\), with the **complete exact law**
\[
\begin{aligned}
\Pr\{N=6\}&=\frac{20(2\pi-3\alpha-3\beta)}{4\pi}
=0.6384088115593409\ldots,\\
\Pr\{N=8\}&=\frac{60(2\alpha+\beta-\pi)}{4\pi}
=0.2389894688997700\ldots,\\
\Pr\{N=10\}&=\frac{12(2\pi-5\alpha)}{4\pi}
=0.1226017195408904\ldots .
\end{aligned}
\]
The ten great circles perpendicular to the antipodal pairs of dodecahedral vertices partition the sphere into **exactly 92 chambers**: twenty spherical hexagons with interior-angle multiset \(\{\pi-\alpha\text{ (three times)},\pi-\beta\text{ (three times)}\}\), sixty spherical triangles with angles \(\{\alpha,\alpha,\beta\}\), and twelve spherical pentagons with angles \(\{\pi-\alpha\text{ (five times)}\}\). The corresponding section side counts are respectively \(6,8,10\). In particular,
\[
\mathbb E N=\frac{30\beta}{\pi}=6.968385815963099\ldots.
\]

## Assumptions and scope

The vertex coordinates above specify a circumradius-\(\sqrt3\) regular dodecahedron; uniform scaling or rigid motion does not change the law. The probability measure is normalized spherical area on \(S^2\), equivalently uniform unoriented planes through the center. Normals orthogonal to any vertex have measure zero and are excluded from assertions about generic section combinatorics. No statement is made about random *affine* planes with nonzero offsets or about a distribution weighted by section area.

## Proof

**1. Vertices, edges, and sign patterns.** The displayed set consists of twenty vertices, twelve exposed pentagonal faces, and thirty edges. Each edge joins a pair of vertices at distance \(2/\varphi\). If \(U\) is not orthogonal to a vertex, the plane meets an edge if and only if its endpoints have opposite signs under the functional \(x\mapsto\langle U,x\rangle\). Such a crossing is one vertex of the section, and every section vertex arises this way. Therefore
\[
N(U)=\sum_{\{i,j\}\in E(D)}
\mathbf1_{\langle U,v_i\rangle\langle U,v_j\rangle<0}.
\]
Central symmetry reduces the twenty signs to ten independent antipodal axes. The pattern can change only on the ten great circles orthogonal to those axes.

**2. Complete finite chamber classification.** Every three distinct chosen great circles meet transversely in the sense that their corresponding normal vectors are linearly independent. Thus the ten circles have \(2\binom{10}{2}=90\) distinct intersection points, and Euler's formula gives \(90-180+92=2\) for their spherical arrangement. To determine the shapes and associated \(N\), intersect the signed hemispheres for each of the \(2^{10}\) sign patterns. A nonempty chamber is a spherical convex polygon; its vertices are *exactly* the oriented cross products of pairs of active circle normals that satisfy all inequalities. This is exhaustive because every extreme ray of a pointed three-dimensional polyhedral cone is determined by two active bounding planes.

The finite classification is

| Number of chambers | Spherical chamber | Interior-angle multiset | Section sides |
| ---: | --- | --- | ---: |
| 20 | hexagon | \(\pi-\alpha\) three times, \(\pi-\beta\) three times | 6 |
| 60 | triangle | \(\alpha,\alpha,\beta\) | 8 |
| 12 | pentagon | \(\pi-\alpha\) five times | 10 |

The table is certified by the included exact-arithmetic program `verify_dodecahedron_haar.py`. It checks all 1024 patterns and all 90 candidate oriented rays over the quadratic integer ring \(\mathbb Z[\varphi]\), without making floating-point sign choices. It also independently certifies the twelve supporting pentagonal faces and thirty edges. The proof of enumeration completeness is the cone-extreme-ray argument just given; the program performs the finite exact cases.

**3. Angles and spherical area.** Each selected circle normal has squared norm \(3\), and the absolute dot product of distinct normals is always \(1\) or \(\sqrt5\). At an arrangement vertex, with inward signed circle normals \(w_i,w_j\), the interior spherical angle equals
\[
\pi-\arccos\!\left(\frac{\langle w_i,w_j\rangle}{3}\right),
\]
which is one of \(\alpha,\beta,\pi-\alpha,\pi-\beta\). Girard's spherical excess formula gives chamber areas
\[
A_6=2\pi-3\alpha-3\beta,\qquad
A_8=2\alpha+\beta-\pi,\qquad
A_{10}=2\pi-5\alpha.
\]
Multiplying by the chamber counts and dividing by total spherical area \(4\pi\) proves the probability formulas. The identity \(20A_6+60A_8+12A_{10}=4\pi\) provides a consistency check.

**4. Independent expectation check.** Adjacent vertex vectors have normalized dot product \(\sqrt5/3\) and angular separation \(\beta\). For uniform \(U\), the probability that the signs at the ends of an edge differ is \(\beta/\pi\). By linearity of expectation over all thirty edges, \(\mathbb E N=30\beta/\pi\), agreeing with the three-point distribution.

## Verification

Run `python3 verify_dodecahedron_haar.py` with the Python standard library. Its exact-integer arithmetic verifies: all twenty vertices and twelve supporting five-vertex facets; the thirty actual edge pairs; pairwise-normal dot-product types; no triple concurrency of the great circles; all \(1024\) candidate sign patterns; ninety candidate intersections; precisely ninety-two feasible cells; their exact angle multisets and section counts; and the spherical area sum. The computation is an exhaustive proof of a finite classification, not a sample from the sphere. An independent numerical orientation check with random unit normals and direct edge crossings supported the three probabilities but is not used to prove them.

## Relationship to prior work

Brandenburg, De Loera, Luo, and Meroni (2026) provide an algebraic-combinatorial chamber framework for polyhedral slices and slabs, illustrating it principally on cubes and calculating section volumes and moments. Their inspected full text does not evaluate the Haar spherical-chamber areas or side-count probabilities for the regular dodecahedron. Zupanič and Bončina (2016) study plane sections of dodecahedral and other icosahedrally symmetric quasicrystal models using seven representative section orientations and varying offsets. They identify possible polygonal shapes but do not integrate over central-plane orientations to obtain the present law. A published calculation of central sections of the *icosahedron* treats a different polytope and a different two-value side-count distribution. Polarity transforms the current central dodecahedron sections into planar projections of the icosahedron, **not** central sections of the icosahedron; the latter result does not imply this law.

## Limitations

Historical priority has not been established conclusively. A geometrically equivalent formula could exist in older stereology, crystallography, planar projection, or icosahedral great-circle literature under different terminology. The published central-icosahedron calculation was available as a searchable summary, not as inspected full text. The result is for central cuts with Haar-uniform orientation; no affine-offset section distribution is claimed. Independent mathematical audit has not been performed.

## References

1. M.-C. Brandenburg, J. A. De Loera, Y. Luo, C. Meroni, *Critical moments of slices and slabs of the cube (and other polyhedral norms)*, arXiv:2603.25643, first submitted March 26, 2026, https://arxiv.org/abs/2603.25643.
2. F. Zupanič and T. Bončina, *Determination of shapes and preferred growth directions of icosahedral quasicrystals from the 2D-sections*, Journal of Alloys and Compounds **681** (2016), DOI:10.1016/j.jallcom.2016.04.255.
3. M.-C. Brandenburg, J. Curtis, C. Giardino, C. Meroni, A. Padrol, *Reconstruction of slices of cubes*, arXiv:2610.09939, first submitted October 7, 2026, https://arxiv.org/abs/2610.09939 (related but cube-specific).
4. *Exact Haar polygon-type law for central icosahedron sections*, 2026, publicly indexed mathematical research record (related different polytope; summary inspected).
