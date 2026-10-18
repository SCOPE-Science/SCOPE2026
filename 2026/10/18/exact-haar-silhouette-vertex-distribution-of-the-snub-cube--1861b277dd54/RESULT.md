# Exact Haar silhouette-vertex distribution of the snub cube

## Finding
Let \(P\) be either enantiomorph of the Archimedean snub cube and let \(U\) be uniformly distributed on the unit sphere. Write \(N(U)\) for the number of vertices of the orthogonal projection of \(P\) onto \(U^\perp\). Then, with probability one,
\[
N(U)\in\{9,10,11,12\}.
\]
Its **complete exact distribution** is the eighteen-angle algebraic-arccosine law
\[
\Pr(N=k)=\frac{c_k\pi+\sum_{j=0}^{17}b_{kj}\beta_j}{4\pi},\quad k\in\{9,10,11,12\},\qquad
\beta_j=\arccos\sqrt{a_j+d_j\tau+e_j\tau^2},
\]
where \(\tau\) is the unique real root of \(\tau^3-\tau^2-\tau-1=0\). The **complete exact rational triples** \((a_j,d_j,e_j)\), integer coefficients \(b_{kj}\), and \(c_k\), are supplied in the standalone `ANGLE_FORMULA.json`; this is part of the theorem, not a numerical approximation. The resulting probabilities, displayed only for convenience, are

| \(k\) | \(\Pr(N=k)\) (approximately) |
|---|---:|
| 9 | 0.24083187771531622 |
| 10 | 0.44860084954614654 |
| 11 | 0.09167755357971353 |
| 12 | 0.21888971915882371 |

In particular, \(\mathbb E[N]\approx10.288625114182045\). Reflection preserves the distribution, so the two chiral snub cubes have the same law.

## Assumptions and scope
Work in \(\mathbb R^3\) with its standard Euclidean metric and Haar-uniform unoriented orthogonal viewing directions. Scaling and rigid motions do not change projection vertex counts. Take \(P\) as the convex hull of the 24 appropriately oriented signed coordinate permutations of \((1,\tau^{-1},\tau)\), with the parity convention encoded in `check.py`. The resulting polyhedron has 32 triangular facets, 6 square facets, and 60 edges; every vertex is incident to exactly five facets. A viewing normal is **generic** if it avoids the 31 great circles defined by orthogonality to the 31 distinct planes of facet-normal directions. The exceptional set has spherical measure zero; no claim on its silhouette vertex counts is made.

## Proof
**Convex-hull geometry.** The rational algebraic field \(\mathbb Q(\tau)\) has basis \(1,\tau,\tau^2\) with the reduction \(\tau^3=\tau^2+\tau+1\). Construct the 24 signed-permutation points. The 38 face index sets encoded directly in `check.py` are certified by exact supporting-plane inequalities: every listed face is coplanar, every unlisted vertex lies strictly inside its supporting halfspace, every edge belongs to exactly two faces, and each vertex link is a connected five-cycle. These checks give the complete convex boundary, not merely an experimental point set.

**Silhouette edge criterion.** An edge shared by faces with outward normals \(f_i,f_j\) occurs on the apparent contour of the generic projection along \(u\) exactly when \((f_i\cdot u)(f_j\cdot u)<0\). Each such edge contributes exactly one edge and one vertex to the projected polygon. Consequently
\[
N(u)=\sum_{\{i,j\}\text{ adjacent faces}}\mathbf1\{(f_i\cdot u)(f_j\cdot u)<0\}.
\]
This is independent of projection coordinates and holds for every generic view of a convex polytope.

**Complete orientation partition.** Distinct facet-normal hyperplanes yield exactly 31 great circles on the unit normal sphere. All their intersections, radial directions, cyclic orders, and sign patterns are computed *exactly* in \(\mathbb Q(\tau)\), with strict signs justified by a rational root-isolating interval. There are 762 distinct spherical intersection points and 1,608 circle arcs. Every complementary region is a convex spherical polygon carrying one sign pattern. The exact adjacency construction yields 848 regions, satisfying the spherical Euler identity \(F=2+E-V=848\). Counting the crossed facet pairs on each region gives the exact region census
\[
(\#F_9,\#F_{10},\#F_{11},\#F_{12})=(96,288,336,128).
\]
There is no other region type. The chamber census is **not** asserted to be the probability distribution: chambers have unequal spherical areas.

**Exact spherical areas.** For every region, all of its great-circle boundary edges and vertices are ordered by exact sidedness, so the spherical polygon area is the Gauss–Bonnet angle sum. Each turning angle is \(\beta_j\) or \(\pi-\beta_j\), with its squared cosine an exact element \(a_j+d_j\tau+e_j\tau^2\) of \(\mathbb Q(\tau)\). Aggregation by the four values of \(N\) produces precisely 18 distinct algebraic angle types and the finite integer coefficient table in `ANGLE_FORMULA.json`. Divide their four exact spherical areas by \(4\pi\). Their sum is the area of the full sphere. This proves the displayed complete probability law.

**Implementation and exactness.** `check.py` implements all boundary, intersection, ordering, region, silhouette, and exact angle-coefficient operations using integer arithmetic in \(\mathbb Q(\tau)\). The Tribonacci root is isolated strictly in the rational interval \((183928675521416/10^{14},183928675521417/10^{14})\). For a nonzero algebraic coefficient, its sign is certified by rational interval arithmetic without floating-point tolerance. The only floating-point operations are evaluations of the already explicit angles and a separate projected-hull comparison. The exact coefficient table is asserted equal to the coefficients reconstructed from the entire spherical subdivision.

## Verification
From a folder containing both `check.py` and `ANGLE_FORMULA.json`, run `python3 check.py` (Python standard library only). It verifies 24 vertices, 38 faces, 60 edges, 31 great-circle planes, 762 intersection points, 1,608 arcs, 848 chambers, all chamber counts, and all entries in the shipped 18-angle formula. Additionally, 3,000 random viewing normals are checked against an independently implemented planar convex-hull projection. This last numerical comparison is supplementary; the exact finite great-circle decomposition and angle aggregation prove the all-orientation statement.

## Relationship to prior work
Longuet-Higgins studies the snub cube as one of the optimal spherical-cap packings in an investigation of snub polyhedra; the full article discusses growth and packing, not the distribution of orthogonal projection vertex counts. Glisse, Lazard, Michel, and Pouget study the expected worst-direction silhouette complexity of *random point-set polytopes*, rather than the Haar viewing law of this deterministic Archimedean polyhedron. MathWorld provides the snub cube's construction, size, and illustrations of special projections. The QFBox snub-cube geometry page lists selected octagonal, nonagonal, and dodecagonal silhouettes without an orientation probability law. General silhouettes and tabulations of special views do not give the four probabilities above without the spherical-area computation. Published geometric-record searches did not identify this exact finite law; historical priority should nevertheless be reviewed independently.

## Limitations
Generic orthographic views only: special directions on the 31 great circles can have different silhouette counts. This result does not treat projective/perspective shadows, section polygons, projection areas, or the corresponding 60-vertex snub dodecahedron. The 18-angle formula is exact but is intentionally supplied as a machine-readable coefficient table rather than an artificially abbreviated closed form. Unindexed earlier coverage remains a possible historical-priority risk; no independent mathematical validation has been performed.

## References
1. M. S. Longuet-Higgins, “Snub polyhedra and organic growth,” *Proceedings of the Royal Society A*, 465 (2009), 477–491; first published online **30 October 2008**. DOI: `10.1098/rspa.2008.0219`.
2. M. Glisse, S. Lazard, J. Michel, and M. Pouget, “Silhouette of a random polytope,” *Journal of Computational Geometry* 7 (2016), 86–99. DOI: `10.20382/jocg.v7i1a5`.
3. E. W. Weisstein, “Snub Cube,” *MathWorld*; `https://mathworld.wolfram.com/SnubCube.html`.
4. “The Snub Cube,” *QFBox / Eusebeia*, geometry and representative projections; `https://eusebeia.qfbox.info/4d/snubcube`.
