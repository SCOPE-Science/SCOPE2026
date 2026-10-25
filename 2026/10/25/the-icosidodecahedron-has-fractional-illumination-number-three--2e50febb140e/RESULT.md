# The icosidodecahedron has fractional illumination number three

## Finding
Let \(\varphi=(1+\sqrt5)/2\). Take the regular icosahedron
\[
I=\operatorname{conv}\{(0,\pm1,\pm\varphi),\ (\pm1,\pm\varphi,0),\ (\pm\varphi,0,\pm1)\}
\]
and let \(R\) be the convex hull of the midpoints of its thirty edges, the regular icosidodecahedron. Write \(\alpha(R)\) for the largest number of vertices of \(R\) illuminated by any single parallel direction and \(i^*(R)\) for its fractional illumination number. Then
\[
\boxed{\alpha(R)=10,\qquad i^*(R)=3.}
\]
More precisely, the six antipodal pairs of vertices of \(I\) have \(64\) antipodal transversals, and their induced-edge counts have exact distribution
\[
\#\{T:e(I[T])=j\}=\begin{cases}
12,&j=5,\\20,&j=6,\\20,&j=9,\\12,&j=10,\\0,&\text{otherwise}.
\end{cases}
\]
The ten-vertex illumination maximum is attained by a direction proportional to \((-2,0,-1)\). In comparison, the regular icosahedron and dodecahedron both have fractional illumination number four by prior work; the rectification has smaller value three.

## Assumptions and scope
A direction \(u\ne0\) illuminates a boundary point \(x\) of a full-dimensional convex body \(K\subset\mathbb R^3\) if \(x+tu\in\operatorname{int}K\) for some \(t>0\). A finite nonnegative weighted collection of directions is a fractional illumination if, at every boundary point, the illuminating weights add to at least one. Its minimum total mass is \(i^*(K)\). For polytopes, checking vertices suffices because a direction illuminating a vertex of a face also illuminates every point of that face's relative interior. The finding uses these *parallel-direction* definitions, not distance-weighted exterior light sources.

The thirty midpoints are the vertices of \(R\). Its thirty-two facets are the twelve pentagons associated with the vertices of \(I\) and the twenty triangles associated with the triangular facets of \(I\). A vertex indexed by an edge \(ab\) of \(I\) lies on the two pentagonal facets with outward normals \(a,b\), and on the two triangles with outward normals \(a+b+c\) and \(a+b+d\), where \(abc,abd\) are the incident icosahedral triangular facets. The exact certificate `CHECK.py` verifies all supporting planes and their incidence cardinalities directly in \(\mathbb Q(\sqrt5)\), and verifies that the resulting sixty surface edges are each incident with precisely two of these facets; hence the specified thirty-two faces give the complete boundary.

## Proof
**1. A transversal obstruction.** If \(u\) illuminates the rectified vertex indexed by the edge \(ab\), the inward condition on its pentagonal facets implies \(\langle u,a\rangle<0\) and \(\langle u,b\rangle<0\). The twelve icosahedral vertices form six antipodal pairs; a strict negative halfspace contains at most one vertex from each pair. Therefore every vertex illuminated by \(u\) is an original icosahedral edge with both ends in some antipodal transversal \(T\) of six vertices. Consequently,
\[
\alpha(R)\le\max_{T}\,e(I[T]).
\]

**2. The exact spectral bound.** Choose one representative from each antipodal pair. Each original icosahedral vertex has degree five and meets exactly one vertex in each of the other five antipodal pairs (its five neighbors cannot form an antipodal pair). Consequently, exactly one of the two sign products for a pair of antipodal pairs induces an original edge. For a sign vector \(s\in\{-1,1\}^6\), the selected vertices induce an icosahedral edge between the \(i\)-th and \(j\)-th selected representatives precisely when \(A_{ij}s_is_j=1\), where the exact signed adjacency matrix is
\[
A=\begin{pmatrix}
0&1&1&-1&-1&-1\\
1&0&1&1&-1&1\\
1&1&0&-1&1&1\\
-1&1&-1&0&-1&1\\
-1&-1&1&-1&0&1\\
-1&1&1&1&1&0
\end{pmatrix}.
\]
Direct matrix multiplication gives \(A^2=5I_6\). Thus every eigenvalue of \(A\) has absolute value \(\sqrt5\). The induced edge count is
\[
e(I[T_s])=\frac{15+\sum_{i<j}A_{ij}s_is_j}{2}.
\]
The sum \(S=\sum_{i<j}A_{ij}s_is_j\) satisfies
\[
S=\frac12s^\top As\le3\sqrt5<7.
\]
As a sum of fifteen signs, \(S\) is an odd integer; hence \(S\le5\), so \(e(I[T_s])\le10\). Enumerating the six signs using this explicit matrix also gives the stated exact distribution of all \(64\) transversal edge counts. This establishes \(\alpha(R)\le10\) without an assumption that every combinatorial transversal is realizable by a halfspace.

**3. Sharpness.** Set \(u=(-2,0,-1)\). In the coordinate ordering specified by `CHECK.py`, the ten edges
\[
(3,7),(3,9),(3,11),(7,8),(7,11),
(8,10),(8,11),(9,10),(9,11),(10,11)
\]
all have strictly negative pairing of \(u\) with *each* of the four incident facet normals described above. Thus \(u\) illuminates ten distinct vertices, yielding \(\alpha(R)=10\). This is a strict, exact-algebraic witness, not a numerical tolerance test.

**4. Fractional value.** Every direction illuminates at most ten of the thirty vertices. Summing the thirty vertex constraints of an arbitrary fractional illumination therefore gives total weight at least \(30/10=3\). Conversely, the icosahedral rotation group acts transitively on the thirty edges. Uniformly averaging the sharp ten-vertex direction over this finite group gives a weighted direction multiset of total mass three illuminating each vertex with total weight exactly one. The relative-interior property extends this to the whole boundary. Hence \(i^*(R)=3\).

## Verification
Run `python3 CHECK.py` using only the Python standard library. The program represents \(a+b\varphi\) exactly by integer coefficient pairs. It reconstructs the twelve icosahedral vertices, thirty edges (squared length four), and twenty triangular faces. It verifies every proposed rectified facet supports all thirty edge midpoints and touches exactly five or three midpoints, respectively. It also checks the complete sixty-edge, two-facets-per-edge incidence structure. It reconstructs all six antipodal pairs and the displayed signed adjacency matrix, checks \(A^2=5I_6\), exhausts the \(64\) transversals with independent induced-edge recount, and checks all ten illuminated vertices against their four actual facets. It reports `EXACT_OK` and the distribution \(\{5:12,6:20,9:20,10:12\}\).

The mathematical proof uses the exact signed-matrix identity, parity, and one strict direction witness; neither floating-point sampling nor finite enumeration over candidate directions is used to certify the infinite family of possible directions.

## Relationship to prior work
Naszódi introduced the fractional illumination invariant. Gorodzha's 2026 theorem establishes the dimension-dependent universal bound \(i^*(K)\le2^d\), with equality only for parallelotopes; it does not calculate this specific Archimedean example. A prior exact study of the regular dodecahedron and icosahedron found \(i^*=4\) for each and proved the general vertex-transitive relation \(i^*(P)=f_0(P)/\alpha(P)\), which is used here rather than claimed anew. Its polyhedral certificates concern the two Platonic solids, not the rectification and its signed-conference obstruction.

Kiss and Oloff de Wet's 2012 primary article includes the icosidodecahedron in its Archimedean table, but the table computes **upper estimates for a distinct norm-weighted illumination parameter**, achieved with six exterior light sources. Neither that numerical bound nor its six-source configuration implies the exact fractional-direction value three. A targeted comparison of full texts and exact-name searches found no earlier evaluation of this particular invariant; failure to locate one is not a uniqueness or priority proof.

## Limitations
The result applies to the *regular* icosidodecahedron and all its invertible affine images. It does not determine the fractional illumination of arbitrary combinatorial realizations, related truncated solids, the ordinary unweighted illumination number, or distance-weighted illumination parameters. The matrix certificate and geometry are reproducible, but independent mathematical review and exhaustive historical priority validation have not been performed.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, *Contributions to Discrete Mathematics* 4 (2009), 83–88; DOI 10.55016/ojs/cdm.v4i2.62022.
2. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1, first public 20 September 2026.
3. G. Kiss and P. Oloff de Wet, *Notes on the illumination parameters of convex polytopes*, *Contributions to Discrete Mathematics* 7 (2012), 58–67; DOI 10.55016/ojs/cdm.v7i1.62108.
4. *Exact fractional illumination of the regular dodecahedron and icosahedron* (2026), published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-the-regular-dodecahedron-and-ic--760696b5ce34 .
