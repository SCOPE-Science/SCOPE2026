# Sharp eighteen-sided central sections of the regular truncated icosahedron

## Finding
Let \(T\) be a regular truncated icosahedron, and let \(H_u=\{x\in\mathbb R^3:u\cdot x=0\}\) for a uniformly distributed unoriented unit normal \(u\). For almost every \(u\), the section \(T\cap H_u\) has \(10\), \(12\), \(14\), \(16\), or \(18\) sides, and all five values occur on sets of positive spherical measure. In particular, the sharp generic maximum is **18 sides**, attained exactly by sections crossing six pentagonal and twelve hexagonal faces.

Its exact Haar probability is
\[
\boxed{\Pr\{N(u)=18\}=\frac5\pi\!\left[2\pi-3\arccos\!\left(\frac{88-\sqrt5}{109}\right)-3\arccos\!\left(\frac{25-4\sqrt5}{109}\right)\right]}
=0.0300246407967537692\ldots .
\]
The successful directions are a disjoint union, up to their boundaries, of **twenty congruent spherical hexagons** centered at the twenty outward face-normal directions of the underlying regular icosahedron.

More precisely, let \(P\) and \(Q\) count intersected original pentagonal and hexagonal faces. Their joint generic support comprises exactly these ten pairs. The numerical probabilities below are given for orientation, rather than uniform choice of cells; the certified combinatorial cell counts are not equiprobabilities.

| \((P,Q)\) | Section sides \(P+Q\) | Refined spherical cells | Approximate probability |
|---:|---:|---:|---:|
| \((0,10)\) | 10 | 24 | 0.093182377 |
| \((2,8)\) | 10 | 72 | 0.066456615 |
| \((2,10)\) | 12 | 120 | 0.018759779 |
| \((4,6)\) | 10 | 72 | 0.326233153 |
| \((4,8)\) | 12 | 192 | 0.270244383 |
| \((4,10)\) | 14 | 72 | 0.013422022 |
| \((6,6)\) | 12 | 120 | 0.004406665 |
| \((6,8)\) | 14 | 144 | 0.151802961 |
| \((6,10)\) | 16 | 120 | 0.025467404 |
| \((6,12)\) | 18 | 32 | 0.030024641 |

## Assumptions and scope
Write \(\varphi=(1+\sqrt5)/2\) and take the regular icosahedron with vertex set
\[
I=\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}.
\]
Its thirty edges join pairs of vertices at Euclidean distance \(2\). Replace each directed edge \((v_i,v_j)\) by the point \(w_{ij}=(2v_i+v_j)/3\). The convex hull of the sixty such points is the uniformly truncated icosahedron \(T\). Its facets are twelve pentagons (one for each old icosahedron vertex) and twenty hexagons (one for each old triangular face). All orientations are measured with rotation-invariant probability on \(S^2/\{\pm1\}\); the finitely many vertex-incidence great circles are excluded from the generic statements because they have probability zero.

## Proof
**1. Exact reduction to vertex signs.** For a generic central plane, a polyhedral edge crosses the plane if and only if its endpoint scalar products with \(u\) have opposite signs. Each such crossing produces one section vertex; equivalently, each section side lies in a unique crossed facet. Consequently, \(N=P+Q\). There are exactly thirty antipodal pairs among the sixty truncated-icosahedral vertices. Their perpendicular great circles are the complete loci where the sign pattern can change. The geometric data used below are thirty such great circles, twelve pentagons, twenty hexagons and ninety edges.

**2. Exhaustive algebraic sign chambers.** Subdivide the sphere initially by the three coordinate great circles into eight spherical octants. In a fixed order, clip each current spherical polygon by both closed hemispheres of each of the thirty vertex-pair circles, discarding empty interiors. This yields **968** octant-refined nondegenerate convex spherical polygons covering the sphere with disjoint interiors. Every resulting vertex is an intersection of planes with coefficients in \(\mathbb Q(\sqrt5)\), so every incidence, sidedness and sign test is exact in that ordered field. The accompanying `CERTIFY.py` implements these operations without any floating-point decisions in the combinatorial proof. An interior positive combination of the corner rays supplies a representative for each cell. Counting crossed facet signs gives exactly the ten pairs and the respective integer cell counts displayed above, with sum \(968\). Hence the sharp bound \(N\le18\), the exhaustive support and all its nonempty cases are established. Numerical areas in the table are not used to certify this enumeration.

**3. Identify the extremal locus.** The thirty vertex-circle sign patterns arising in the preceding calculation show that the thirty-two refined cells with \((P,Q)=(6,12)\) belong to exactly twenty distinct complete sign chambers. Each matches the sign pattern at the center direction of a different original triangular face of the icosahedron. Eight such chambers lie within one octant; the remaining twelve are bisected by an octant coordinate plane, giving \(8+2(12)=32\) refined cells. The exact field comparisons establishing this identification are included in the executable certificate. The full icosahedral symmetry acts transitively on the twenty original face normals, so the twenty extremal regions are congruent.

**4. Exact solid angle.** Consider the hexagonal extremal region surrounding \(c=(1,1,1)/\sqrt3\). Six of the vertex-circle hemispheres bound it, in alternating order. Its six exact algebraic vertices are obtained by crossing successive inward-facing boundary normals; every other vertex-circle inequality is strict at all six vertices, as verified by exact algebraic comparisons in `CERTIFY.py`. For successive inward unit boundary normals, the pairwise dot products alternate between
\[
 a=\frac{88-\sqrt5}{109},\qquad b=\frac{25-4\sqrt5}{109}.
\]
A convex spherical polygon bounded by inward-facing great-circle hemispheres has interior angle \(\arccos(-a)=\pi-\arccos(a)\), respectively \(\pi-\arccos(b)\), at these vertices. Girard's formula therefore gives the area of one successful spherical hexagon:
\[
\Omega=3\bigl(\pi-\arccos a\bigr)+3\bigl(\pi-\arccos b\bigr)-4\pi
=2\pi-3\bigl(\arccos a+\arccos b\bigr).
\]
The twenty disjoint hexagons have total spherical area \(20\Omega\). Dividing by \(4\pi\) proves the displayed probability exactly. The same result applies to unoriented planes because the successful set is antipodally invariant. \(\square\)

## Verification
Run `python3 CERTIFY.py` (Python standard library only). The script constructs the exact icosahedron, verifies the thirty edges and the ninety truncated edges, identifies the twelve and twenty facet sets, exhaustively clips thirty great circles, and checks the ten joint cell-count classes, the twenty distinct favorable sign chambers, the six bounding-plane inequalities and the exact alternating boundary-normal dot products. It uses integer pairs to represent elements of \(\mathbb Z[\sqrt5]\); their signs are decided by integer comparisons. `CHECKS.txt` records one run of this checker. Floating-point arithmetic is used **only** to report numerical spherical areas, not for exact sign classification or the equality/inequality certificates. The exact probability is separately evaluated by the closed analytic formula; numerical agreement is a supplemental consistency check.

## Relationship to prior work
The classical facial structure of the regular truncated icosahedron is not new. Matteo's analysis of two-orbit convex polytopes documents the highly symmetric icosahedral and quasiregular polyhedra, but does not give this truncated solid's central-section distribution. Padrol and Pfeifle study which polygons can be represented as sections of higher-dimensional polytopes and general intersection-complexity bounds, not the Haar measure of an eighteen-sided section of this specific polyhedron. Kim, Yaskin and Zvavitch study the distributions of **areas** of convex-body central sections, a different observable. The present claim concerns the exact extremal **facet-incidence count** and its spherical measure, with an explicit golden-ratio angle formula. A complete historical-priority search, especially in unindexed stereological section tables, remains an independent task.

## Limitations
The theorem is for uniformly oriented **central** planes and a mathematically regular, planar-faced truncated icosahedron, not a curved/inflated soccer ball. Nongeneric directions lying on vertex-incidence great circles are excluded from the polygon-count classification. The ten-type probability table is numerical except for the exact eighteen-sided probability, although its support and integer chamber counts are exactly certified. This is a self-contained finite enumeration with an analytic area formula, not an externally independently audited theorem; literature priority is subject to the stated residual risk.

## References
1. N. Matteo, *Two-orbit convex polytopes and tilings*, arXiv:1403.2125, first submitted 2014-03-10. https://arxiv.org/html/1403.2125v1
2. A. Padrol and J. Pfeifle, *Polygons as sections of higher-dimensional polytopes*, arXiv:1404.2443, first submitted 2014-04-09. https://arxiv.org/abs/1404.2443
3. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289, first submitted 2015-12-22. https://arxiv.org/html/1512.07289v1
