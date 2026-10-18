# A sharp tetrahedral-volume polynomial and sixty movable-apex families in truncated icosahedra

## Finding

Put \(\varphi=(1+\sqrt5)/2\) and let \(I\) be the regular icosahedron with vertex set
\[
V=\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}.
\]
Every edge of \(I\) has length \(2\). For \(0\le t\le1/2\), form the convex hull \(P_t\) of the sixty points
\[
w_{uv}(t)=(1-t)u+tv,\qquad (u,v)\text{ an ordered edge of }I.
\]
For an arbitrary tetrahedron \(T\subseteq P_t\), whose vertices need not belong to the displayed sixty-point set, the **sharp maximum volume** is
\[
\boxed{\ \max_{T\subseteq P_t}\operatorname{Vol}_3(T)
=\frac{Q(t)}6,\qquad
Q(t)=4+8\varphi-8\varphi t+(8\varphi-4)t^2+(4-4\varphi)t^3.\ }
\]
The maximum decreases strictly throughout \([0,1/2]\). For every \(0<t<1/2\), precisely **120** unordered four-element subsets of the sixty vertices support maximizing tetrahedra. Their complete continuous equality locus consists of exactly **60 closed line-segment families**: in each, three tetrahedron vertices are fixed truncation vertices and the fourth ranges along the original icosahedron edge surviving between its two new truncation vertices. Every vertex-supported maximizer is an endpoint of exactly one such family; there are no other maximal tetrahedra. The same combinatorial classification holds for every \(0<t<1/2\), with no interior transition.

The parameters \(0\), \(1/3\), and \(1/2\) give the regular icosahedron, the uniform truncated icosahedron, and the regular icosidodecahedron, respectively (at the endpoints some listed vertices coalesce). In particular, for the **unit-edge regular truncated icosahedron**, the largest tetrahedral volume is
\[
\boxed{\frac{25+41\varphi}{12}}.
\]
The above polynomial is valid at both endpoints; the equality classification is asserted only for \(0<t<1/2\).

## Assumptions and scope

All objects are Euclidean three-dimensional compact convex polytopes. A tetrahedron is the convex hull of four affinely independent points anywhere in \(P_t\), considered without ordering. The original regular icosahedron has side length \(2\). Every original edge joins precisely the pairs of distinct vertices \(u,v\in V\) for which \(\|u-v\|_2=2\); there are exactly thirty such unordered edges and sixty directed edges. For \(0<t<1/2\) the sixty points \(w_{uv}(t)\) are distinct vertices of the indicated convex hull. The boundary values remain meaningful using the convex-hull definition even though they contain duplicate parametrized points. By homogeneity the maximum for a homothetically rescaled polytope is multiplied by the cube of the scale factor.

For a fully reproducible indexing convention, list the four sign pairs \((a,b)\in\{(-1,-1),(-1,1),(1,-1),(1,1)\}\) in that order; for each append \((0,a,b\varphi)\), \((a,b\varphi,0)\), and \((a\varphi,0,b)\). List the thirty unordered edges \((i,j)\) with \(i<j\) in lexicographic order, and then the thirty reversed edges in the same order. Index the sixty resulting points from zero. This is the convention in `verify.py`.

## Proof

**1. Reduction to finitely many vertex quadruples.** Write
\[
D(x_0,x_1,x_2,x_3)=\det(x_1-x_0,x_2-x_0,x_3-x_0).
\]
This determinant is affine separately in each argument. Expressing each \(x_i\in P_t\) as a convex combination of its truncation vertices expresses the oriented determinant as a convex combination of determinants of vertex quadruples. Consequently its absolute value is no greater than the maximal absolute determinant of a vertex quadruple. Equality also forces every vertex quadruple in the positive product support to have the same signed extremal determinant; this necessity will determine all continuous equality cases.

**2. Exact algebra and a universal interval certificate.** Calculations use the ring \(\mathbb Z[\varphi]\), with \(\varphi^2=\varphi+1\). Represent \(a+b\varphi\) by the integer pair \((a,b)\); multiply pairs by
\[
(a,b)(c,d)=(ac+bd,ad+bc+bd).
\]
Compare their signs exactly using \(2(a+b\varphi)=2a+b+b\sqrt5\), with integer squared comparisons if the two summands have opposite signs. No floating-point inequality is required.

The orientation-preserving symmetry group of the regular icosahedron acts transitively on its sixty directed edges. Therefore any given four-vertex tetrahedron can be rotated so that its first vertex is the indexed truncation vertex \(w_0(t)\). It suffices to check the \(\binom{59}{3}=32509\) unordered triples of the remaining indexed vertices. Their oriented determinants are cubics \(d(t)\) over \(\mathbb Z[\varphi]\).

For a cubic \(p(t)=a+bt+ct^2+dt^3\), its degree-three Bernstein coefficients on \([0,1/2]\), multiplied by \(24\), are
\[
\mathcal B_{24}(p)=(24a,\ 24a+4b,\ 24a+8b+2c,\ 24a+12b+6c+3d).
\]
Here all coefficients belong to \(\mathbb Z[\varphi]\), while the Bernstein basis \(\binom3i s^i(1-s)^{3-i}\) for \(s=2t\) is nonnegative throughout \([0,1]\). For the candidate upper bound \(Q\), the exact certificate is
\[
\mathcal B_{24}(Q)=(96+192\varphi,\ 96+160\varphi,\ 88+144\varphi,\ 84+132\varphi).
\]
The included standalone `verify.py` exhaustively computes the four Bernstein coefficients for **both** cubics \(Q+d\) and \(Q-d\), for all \(32509\) triples. All \(32509\cdot2\cdot4=260072\) coefficients are nonnegative by exact integer–quadratic-irrational comparisons. Since each Bernstein basis function is nonnegative on the entire parameter interval, this establishes \(|d(t)|\le Q(t)\) for **every real** \(0\le t\le1/2\), not merely a grid of parameter values.

An explicit attaining witness is the indexed unordered quadruple \((0,13,16,53)\): its oriented determinant is **identically** \(-Q(t)\) as a polynomial over \(\mathbb Z[\varphi]\). The upper bound is therefore attained throughout the interval. Combined with step 1, this proves the sharp volume formula for arbitrary contained tetrahedra.

**3. Parameter-independent equality sets.** For \(0<t<1/2\), all four degree-three Bernstein basis functions are strictly positive. Equality \(|d(t)|=Q(t)\) at even a single interior parameter therefore forces **each of the four** coefficients of \(Q\pm d\) to vanish. Hence the signed determinant is identically \(\pm Q\), so the set of winning indexed vertex quadruples does not change on the open interval. The exact certificate finds **eight** winning triples when the first index is fixed. By transitivity of the sixty directed-edge vertices, there are precisely \(60\cdot8/4=120\) winning unordered quadruples.

**4. Full classification of all contained equality cases.** Independently from the Bernstein sweep, the checker evaluates all \(\binom{60}{4}=487635\) exact tetrahedral determinants at \(t=1/4\), verifying precisely the same **120** winners. On these 120 unordered four-sets, put an edge between two winning sets when they share exactly three indexed vertices. The exhaustive combinatorial check verifies that this adjacency graph is a **perfect matching**: exactly sixty disjoint pairs, with every winning set having exactly one partner. In each pair, the two differing vertices represent the two oriented copies of the **same original icosahedron edge**; their joining segment is an exposed surviving edge of \(P_t\). The three shared vertices form the fixed base of a maximizing tetrahedron. Since the oriented determinant is affine in its moving fourth vertex and both endpoint determinants have the same extremal orientation, every point of each resulting closed segment supplies a maximizer.

Conversely, express the vertices of an arbitrary maximum-volume tetrahedron as convex combinations of truncation vertices. The equality rule of step 1 requires that every positive-supported four-tuple be a winning four-set, all of common determinant sign. Two varying tetrahedron vertices would produce at least a two-by-two grid of winning quadruples, forcing a winning quadruple to have two distinct neighboring winners—impossible in a perfect matching. Three or more possible vertices for even one moving tetrahedron vertex would likewise force a winning quadruple to have two neighbors. Thus at least three tetrahedron vertices are truncation vertices, and the remaining one is either another such vertex or a convex combination of precisely the two matched endpoint vertices. Those two endpoints form exactly one of the stated sixty segments. Each of the 120 vertex-supported maxima belongs to one such segment, so no other maximizing tetrahedra exist.

**5. Strict decrease and the soccer-ball specialization.** Differentiate:
\[
Q'(t)=-8\varphi+2(8\varphi-4)t+3(4-4\varphi)t^2,
\qquad Q''(t)=16\varphi-8+(24-24\varphi)t.
\]
The latter is strictly positive on \([0,1/2]\), while \(Q'(1/2)=-1-3\varphi<0\). Thus \(Q'(t)<0\) throughout the entire interval. At \(t=1/3\) the original icosahedral edges are divided into three equal pieces, so the uniform truncated icosahedron has edge length \(2/3\). Substitution yields \(Q(1/3)/6=(50+82\varphi)/81\); multiplying by \((3/2)^3\) to normalize the resulting solid to unit edge gives \((25+41\varphi)/12\).

## Verification

The self-contained `verify.py` needs Python 3.10 or later and only the standard library; execute `python3 verify.py`. It regenerates all twelve icosahedron vertices and thirty undirected edges, checks their exact distances, forms all sixty directed-edge points, and validates the polynomial witness. It uses exact arithmetic in \(\mathbb Z[\varphi]\) to verify all 260072 Bernstein-sign assertions for the continuous parameter interval. An independent exhaustive determinant pass at \(t=1/4\) checks all 487635 four-sets, counts 120 maxima, and verifies the exact sixty-pair matching and its original-edge correspondence. The concluding line contains `PASS`. The exhaustive computations are finite certificates with an explicit mathematically justified search space; the separate affine and Bernstein arguments establish the infinite-domain theorem. There is no probabilistic sampling, external service, or numerical tolerance in the certificate.

## Relationship to prior work

Horváth and Lángi, *Maximum volume polytopes inscribed in the unit sphere*, `arXiv:1402.6496` (2014), study volume extremality with vertices freely constrained to a sphere. Their optimization does not prescribe the truncated-icosahedral container \(P_t\) or produce this cubic profile and its sixty moving-apex equality families. Di Summa, Eisenbrand, Faenza, and Moldenhauer, *On largest volume simplices and sub-determinants*, `arXiv:1406.3512` (2014), establish general computational and approximation connections for largest-volume simplices, not the present exact family. Akopyan and Glazyrin, *On maximum volume simplices in polytopes* (2014), give structural properties involving Radon's theorem and prisms/parallelotopes; their general lemmas do not determine the present sharp golden-ratio polynomial or its family-by-family equality locus.

Related previously published calculations for the **regular icosahedron itself** classify the untruncated endpoint's extremal tetrahedra, and a separate calculation classifies the **regular icosidodecahedron** endpoint. These special-point results match \(t=0\) and \(t=1/2\) but do not imply the universal continuous cubic formula or the 120-vertex, sixty-segment classification on \(0<t<1/2\). An exact treatment of the distinct cube–octahedron intersection family uses similar Bernstein-sign certification techniques but does not cover the icosahedral truncation family. The present claim is the continuous profile and complete interior equality classification, not priority for the general determinant method or endpoint evaluations.

## Limitations

The maximum value is established at the endpoints, but the continuous equality classification is not claimed there because indexed truncation vertices coincide and the equality geometry changes. The theorem concerns this specific Euclidean truncation path, not arbitrary deformations of an icosahedron, all Archimedean solids, or other geometric objectives. The finite classification uses a supplied exhaustive exact-arithmetic program whose source is fully disclosed and can be independently inspected and rerun. The priority search covers identified works and database comparisons, not the totality of historical mathematical literature; an earlier equivalent published formula remains a residual risk. Independent proof auditing has not yet been performed.

## References

1. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, `arXiv:1402.6496`, first public version 2014-02-26; https://arxiv.org/abs/1402.6496 .
2. M. Di Summa, F. Eisenbrand, Y. Faenza, and C. Moldenhauer, *On largest volume simplices and sub-determinants*, `arXiv:1406.3512`, first public version 2014-06-13; https://arxiv.org/abs/1406.3512 .
3. A. V. Akopyan and A. A. Glazyrin, *On maximum volume simplices in polytopes*, *Periodica Mathematica Hungarica* **69** (2014), 251–256, DOI `10.1007/s10998-014-0051-2`; https://users.mccme.ru/akopyan/papers/Akopyan-Glazyrin-Maximum-Volume.pdf .
4. *Complete tetrahedron-volume spectrum and continuous maximum families in the regular icosahedron*, public research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-tetrahedron-volume-spectrum-and-continuous-maximum-fami--801a8f440668 .
5. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, public research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-tetrahedral-volume-profile-in-the-cube-octahedron-intersec--9ba1a511dacf .
