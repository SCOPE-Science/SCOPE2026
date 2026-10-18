# Two sharp brightness-orientation transitions along the cube–octahedron interpolation

## Finding
For every real \(1\le c\le3\), set
\[
K_c=[-1,1]^3\cap\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le c\}.
\]
For any unit direction \(u\in S^2\), let \(B_c(u)\) be the Euclidean area of the orthogonal projection of \(K_c\) onto \(u^\perp\). Let \(S(u)=\sum_i|u_i|\) and \(D(u)=\max\{0,2\max_i|u_i|-S(u)\}\). The complete directional area profile is
\[
\boxed{B_c(u)=a(c)S(u)+b(c)D(u)},
\]
with
\[
\boxed{(a(c),b(c))=
\begin{cases}
(2c-1,-2c^2+6c-3),&1\le c\le2,\\
(4-(3-c)^2,(3-c)^2),&2\le c\le3.
\end{cases}}
\]
Define the two distinct shape parameters
\[
\boxed{c_{\rm max}=\frac{7+\sqrt7}{6}\simeq1.60762521851,\qquad
c_{\rm min}=\frac{4-\sqrt2+\sqrt{10-6\sqrt2}}2\simeq1.90826274718.}
\]
The sharp global projection-area extrema are, for all \(1\le c\le3\),
\[
\boxed{\max_{u\in S^2}B_c(u)=
\begin{cases}
\sqrt{3a^2-2ab+3b^2},&1\le c\le c_{\rm max},\\
\sqrt3\,a,&c_{\rm max}\le c\le3,
\end{cases}}
\]
\[
\boxed{\min_{u\in S^2}B_c(u)=
\begin{cases}
\sqrt2\,a,&1\le c\le c_{\rm min},\\
a+b,&c_{\rm min}\le c\le3,
\end{cases}}
\]
where \(a=a(c)\) and \(b=b(c)\).

All equality directions are classified. For \(1<c<c_{\rm max}\), precisely the 24 directed signed coordinate permutations of
\[
\frac{(a+b,a-b,a-b)}{\sqrt{(a+b)^2+2(a-b)^2}}
\]
maximize brightness; for \(c_{\rm max}<c\le3\), precisely the eight normalized signed body-diagonal directions maximize it. At \(c=c_{\rm max}\), both orbits (32 distinct directed directions) attain the maximum. At the octahedral endpoint \(c=1\), the tilted orbit degenerates to the six directed coordinate axes.

For \(1\le c<c_{\rm min}\), precisely the 12 directed signed coordinate permutations of \((1,1,0)/\sqrt2\) minimize brightness; for \(c_{\rm min}<c\le3\), precisely the six directed coordinate axes minimize it. At \(c=c_{\rm min}\), both orbits (18 directed directions) attain the minimum. Both transition parameters lie strictly inside the octahedron-truncation chamber \(1<c<2\), where the combinatorial type of the underlying polytope remains unchanged.

## Assumptions and scope
The parameter is real and ranges over the closed interval \([1,3]\). Projection is orthographic, viewing normals have Euclidean length one, and area means ordinary two-dimensional Lebesgue measure on the perpendicular plane. Signed permutations include independent coordinate sign changes. The endpoints are respectively the unit \(\ell_1\)-octahedron and the cube of side two. The chamber point \(c=2\) is a cuboctahedron; \(c=3/2\) is a regular truncated octahedron, and \(c=1+\sqrt2\) a regular truncated cube. Directions are distinguished from their antipodes for orbit counts; each antipodal pair gives the same geometric projection area.

## Proof
**1. Facet areas and an exact brightness formula.** For \(1<c<2\), there are six coordinate facets (diamonds) each of area \(A_{\rm co}=2(c-1)^2\) and eight diagonal facets (hexagons) each of area \(A_{\rm di}=\frac{\sqrt3}{2}(-2c^2+6c-3)\). This follows by slicing \(|x_1|+|x_2|+|x_3|=c\) with the cube, or by removing three equal corner triangles from a triangular face of the octahedron. For \(2<c<3\), each coordinate facet is a square with four corner triangles removed, of area \(A_{\rm co}=4-2(3-c)^2\), while each diagonal facet is a triangle of area \(A_{\rm di}=\frac{\sqrt3}{2}(3-c)^2\). The two cases coincide at \(c=2\) and extend by continuity to the endpoints.

The facet normals are \(\pm e_i\) and \(\sigma/\sqrt3\) for all \(\sigma\in\{\pm1\}^3\). Cauchy's projection formula for polytopes gives
\[
B_c(u)=A_{\rm co}\sum_i|u_i|+\frac{A_{\rm di}}{2\sqrt3}\sum_{\sigma\in\{\pm1\}^3}|\sigma\cdot u|.
\]
If the absolute coordinates of \(u\) are \(x\ge y\ge z\ge0\), direct pairing of the eight signs yields
\[
\sum_\sigma|\sigma\cdot u|=4\bigl(x+y+z+(x-y-z)_+\bigr).
\]
Consequently \(B_c(u)=aS+bD\) with \(b=2A_{\rm di}/\sqrt3\) and \(a=A_{\rm co}+b\). Substitution proves both explicit coefficient pairs and all boundary cases without any numerical approximation.

**2. The maximum on two direction cones.** By signed-permutation symmetry assume \(x\ge y\ge z\ge0\) and \(x^2+y^2+z^2=1\). In the balanced chamber \(x\le y+z\), we have \(D=0\) and
\[
B_c(u)=a(x+y+z)\le\sqrt3\,a.
\]
Equality occurs precisely at \(x=y=z=1/\sqrt3\). In the dominant chamber \(x\ge y+z\), we have
\[
B_c(u)=(a+b)x+(a-b)(y+z)
\le\sqrt{(a+b)^2+2(a-b)^2}.
\]
As long as \(b/a\ge2/3\), the Cauchy–Schwarz equality vector \((a+b,a-b,a-b)\), normalized to length one, satisfies \(x\ge y+z\) because \(a+b\ge2(a-b)\). On the entire parameter interval \(a\ge b\ge0\), and the squared difference of the two candidate bounds is
\[
(3a^2-2ab+3b^2)-3a^2=b(3b-2a).
\]
If \(b/a\ge2/3\), the dominant equality direction therefore gives the global maximum; if \(b/a\le2/3\), every dominant direction is bounded by the balanced body-diagonal maximum (whether or not its Cauchy–Schwarz equality vector is feasible). For strict inequalities, the equality conditions above yield precisely the asserted orbits. At equality of the two bounds, both disjoint equality orbits survive.

**3. The minimum on two direction cones.** In the balanced chamber, since the largest coordinate satisfies \(x\le S/2\),
\[
1=x^2+y^2+z^2\le xS\le S^2/2,
\]
so \(B_c(u)=aS\ge\sqrt2\,a\). Equality requires exactly two nonzero equal absolute coordinates.

For the dominant chamber, every nonnegative vector with \(x\ge y+z\) is a nonnegative combination of the three extreme rays \((1,0,0)\), \((1,1,0)\), and \((1,0,1)\):
\[
(x,y,z)=(x-y-z)(1,0,0)+y(1,1,0)+z(1,0,1).
\]
The linear functional \(L=(a+b)x+(a-b)(y+z)\) divided by Euclidean norm takes respectively the values \(a+b,\sqrt2\,a,\sqrt2\,a\) on these rays. Put \(m=\min\{a+b,\sqrt2\,a\}\). Linearity, positivity of the coefficients, and the triangle inequality imply \(L(v)\ge m\|v\|_2\) for every vector in this cone. Equality for a unit vector requires a single extreme ray (the triangle inequality is strict for noncollinear positive ray combinations), so the only possible minimizers are coordinate axes or signed face diagonals, exactly as stated.

**4. Two interior crossings.** For \(1\le c\le2\), write \(r(c)=b(c)/a(c)\). Differentiating gives
\[
r'(c)=-\frac{4c(c-1)}{(2c-1)^2}<0\quad(1<c<2),
\]
with \(r(1)=1\) and \(r(2)=1/3\). For \(2<c<3\), put \(t=3-c\); then \(r(c)=t^2/(4-t^2)\), which strictly decreases from \(1/3\) to zero. Thus each threshold \(2/3\) and \(\sqrt2-1\) is crossed exactly once, both in \((1,2)\). Solving \(b/a=2/3\) gives \(6c^2-14c+7=0\), with the unique admissible root \((7+\sqrt7)/6\). Solving \(b/a=\sqrt2-1\) gives the stated second radical, also uniquely admissible. Their strict order follows from \(2/3>\sqrt2-1\) and monotonicity. Combining the chamber results proves the entire theorem.

## Verification
The standalone `verify.py` uses only Python 3 standard-library modules and reconstructs the projected polygon directly from signed-permutation vertex coordinates. A monotone-chain planar convex hull and shoelace area calculation provide a separate direct geometric evaluation, compared to the analytic brightness identity at 5,460 direction-parameter pairs across 15 parameters, including endpoints and both exact crossings. It additionally compares claimed extrema and the numerical algebraic crossing identities. Successful replay prints `DIRECT_PROJECTED_HULL_AREA_OK 5460 cases`, `TWO_SHARP_ORIENTATION_THRESHOLDS_OK 1.60762521851076 1.90826274717861`, and `ALL_BRIGHTNESS_CHECKS_OK`. These finite checks corroborate the exact analytic proof; neither finite samples nor floating-point comparisons are used as proofs of the all-parameter extremal statements.

## Relationship to prior work
Cauchy's projection formula is classical and is explicitly used, not claimed as new. Burger and Gritzmann study algorithms and complexity for optimal polytope shadows; Zefiro describes the cube–octahedron truncation family. Neither inspected publicly accessible description states a two-crossing brightness-orientation profile. The full available geometric treatment by Zefiro concerns construction and truncation ratios rather than optimizing orthographic projected area.

Two previous object-specific results are expressly **subsumed special cases**, not independent contributions: an exact projected-area theorem for the regular truncated octahedron \(c=3/2\), and a joint shadow-type/brightness theorem for the cuboctahedron \(c=2\). Their fixed-parameter formulas alone do not imply the extrema or equality transitions at the two new interior algebraic parameters for the continuum family. A separate published full theorem computes the facet-network spectrum of this same family, including the individual facet areas also used here; those facet data supply inputs to the classical Cauchy formula but do not classify the globally maximizing and minimizing projection directions. Other complete published statements for the family concern illumination numbers and largest contained tetrahedra, not the brightness optimization. In particular a spectral crossover \((7+\sqrt{13})/6\) is a different geometric invariant from the brightness crossover \((7+\sqrt7)/6\).

## Limitations
The theorem concerns planar orthogonal projections of the exact three-dimensional cube–octahedron intersection family, not arbitrary polytope deformations or higher-dimensional sections. Its extremal area and equality sets do not determine the entire distribution of shadow areas, nor other geometric quantities such as projected perimeter. While direct comparison found no statement of both parameter-dependent brightness transitions, a differently phrased or presently inaccessible earlier result remains a historical-priority risk. The two fixed-body special cases and the face-area inputs are already known. Independent mathematical validation is not asserted.

## References
1. H. R. Tiwary, *On Computing the Shadows and Slices of Polytopes*, arXiv:0804.4150, first public 2008-04-25, https://arxiv.org/abs/0804.4150.
2. T. Burger and P. Gritzmann, *Finding Optimal Shadows of Polytopes*, *Discrete & Computational Geometry* 24 (2000), 219–240, DOI:10.1007/s004540010029. Only the accessible abstract and bibliographic description were inspected.
3. L. Zefiro, *Vertex- and edge-truncation of the Platonic and Archimedean solids leading to vertex-transitive polyhedra*, VisMath (2011), https://www.mi.sanu.ac.rs/vismath/zefirosept2011/_truncation_Archimedean_polyhedra.htm. The publicly available complete article was read for the cube–octahedron family.
4. E. W. Weisstein, *Cauchy's Projection Formula*, MathWorld, https://mathworld.wolfram.com/CauchysProjectionFormula.html.
5. *Exact brightness moments and extremal directions of the regular truncated octahedron*, earlier publicly recorded mathematical finding, identifier `9442beb3-c40f-4055-88e9-2d5874e8e7af`.
6. *Joint silhouette–brightness law of the regular cuboctahedron*, earlier publicly recorded mathematical finding, identifier `5a3d98db-65c3-4dc6-8115-8e4c665f98af`.
7. *Sharp centro-affine spectral gap along the cube–octahedron interpolation*, publicly indexed mathematical result, identifier `4397c6b224a3`; full public theorem/proof compared.
8. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, publicly indexed mathematical result, identifier `9ba1a511dacf`; full public theorem/proof compared.
9. *Exact illumination phase profile of the cube–octahedron intersection family*, publicly indexed mathematical result, identifier `20022a556c31`; full public theorem/proof compared.
