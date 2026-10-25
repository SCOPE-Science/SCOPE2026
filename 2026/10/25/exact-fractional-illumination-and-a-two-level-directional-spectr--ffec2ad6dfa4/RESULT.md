# Exact fractional illumination and a two-level directional spectrum for truncated icosahedra

## Finding
Let \(\varphi=(1+\sqrt5)/2\), let \(I\subset\mathbb R^3\) be the regular icosahedron with vertex set
\[
\mathcal V=\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\},
\]
and write \(E\) for its thirty unoriented edges. For every real \(0<t<1/2\), let
\[
T_t=\operatorname{conv}\{(1-t)v+tw:(v,w)\text{ is an oriented edge of }I\}.
\]
Then \(T_t\) has sixty vertices, twelve pentagonal faces and twenty hexagonal faces. For every generic direction \(u\in\mathbb S^2\), the number \(N_t(u)\) of vertices strictly illuminated by \(u\) belongs to the **two-element set**
\[
\boxed{N_t(u)\in\{20,21\}}.
\]
Both values occur. In fact, the sixteen great circles determined by the thirty-two facet normals partition the direction sphere into exactly \(152\) open chambers: \(132\) chambers illuminate twenty vertices and \(20\) illuminate twenty-one. In particular,
\[
\boxed{\alpha(T_t)=21,\qquad I^*(T_t)=\frac{60}{21}=\frac{20}{7}}
\]
for every \(0<t<1/2\), where \(\alpha\) is the maximum single-direction vertex illumination count and \(I^*\) is the fractional illumination number. At \(t=1/3\), \(T_t\) is the regular truncated icosahedron.

## Assumptions and scope
A direction \(u\ne0\) illuminates a boundary point \(x\) of a convex body \(P\) when \(x+\varepsilon u\in\operatorname{int}P\) for some \(\varepsilon>0\). Fractional illumination means a finite set of nonnegative weighted directions so that every boundary point receives total illuminating weight at least one; \(I^*(P)\) is the infimum of total weight. A direction is *generic* when its scalar product with every facet normal listed in the proof is nonzero. All directions are real and the full dimension is three. The endpoints \(t=0\) and \(t=1/2\) are excluded because vertex and facet incidences change there. No claim concerns norm-weighted point-source illumination.

## Proof
**Geometry and active inequalities.** The edges of \(I\) are precisely vertex pairs of squared Euclidean distance \(4\). Its twenty triangular faces are the triples of pairwise adjacent vertices; each triangular face \(\{a,b,c\}\) has an outward normal proportional to \(a+b+c\). For \(0<t<1/2\), the regular equal-depth truncation replaces each original vertex by a pentagonal face, while each triangular face becomes a hexagon. Every oriented original edge \((v,w)\) labels exactly one vertex \(p_{vw}=(1-t)v+tw\). The three faces incident to \(p_{vw}\) have outward normals
\[
\boxed{v,\quad a+b+c,\quad a'+b'+c'},
\]
where \(\{a,b,c\}\) and \(\{a',b',c'\}\) are the two triangles containing \(\{v,w\}\). Thus \(u\) illuminates \(p_{vw}\) if and only if all three scalar products are strictly negative. These facet normals depend on \(I\) but not on \(t\); consequently the entire illumination-incidence pattern is independent of \(t\) throughout the open interval. The self-contained checker also reconstructs all facets and their exact incidence from the sixty vertex coordinates at \(t=1/3\), verifying five supporting vertices on each pentagon, six on each hexagon and the stated three incident facets at every vertex.

**Exhaustion of the direction arrangement.** Take the twelve vectors \(v\in\mathcal V\) and the twenty triangle sums \(a+b+c\). They form thirty-two signed normal vectors, in sixteen antipodal pairs. Every generic direction defines an open cell of their central great-circle arrangement on \(\mathbb S^2\), and the illuminated vertices depend only on its thirty-two strict signs.

Here is a finite *exhaustive* chamber certificate, rather than a random-direction experiment. For each linearly independent pair \(n_i,n_j\), take both intersection rays \(q=\pm(n_i\times n_j)\). For every normal \(n_k\) with \(n_k\cdot q=0\), take the two tangent rays \(\pm(q\times n_k)\) and approach each ray from both sides in the tangent plane using \(\pm n_k\). At such a perturbation, the sign of any \(n\) is the first nonzero entry of the exact lexicographic triple
\[
\bigl(n\cdot q,\;\sigma n\cdot(q\times n_k),\;\tau n\cdot n_k\bigr),\qquad \sigma,\tau\in\{-1,1\}.
\]
The triple cannot vanish completely: if \(n\cdot q=n\cdot(q\times n_k)=0\), then \(n\) is parallel to \(n_k\) within the plane perpendicular to \(q\). Every open chamber has an arrangement vertex on its boundary, and every local sector at such a vertex touches an incident tangent ray. Accordingly these perturbations visit *every* open chamber; repeated sign vectors are deduplicated.

All coordinates lie in \(\mathbb Z[\varphi]\). The identity \(\varphi^2=\varphi+1\) and comparison of \((2a+b)+b\sqrt5\) with zero give exact addition, multiplication and sign tests for \(a+b\varphi\). The executable `verify.py` implements the preceding exhaustive argument without floating point, produces exactly \(152\) distinct strict sign cells, and compares each against all sixty active-facet triples. The accompanying `cells.csv` supplies their complete ordered sign-and-count certificate. The exact distribution is
\[
\#\{\text{cells with }N_t=20\}=132,\qquad
\#\{\text{cells with }N_t=21\}=20.
\]
For illustration, the integer direction \(u=(1,1,1)\) is generic and illuminates twenty-one vertices, whereas \(u=(-2,0,1)\) is generic and illuminates twenty. Any nongeneric direction illuminating \(r\) vertices has arbitrarily close generic perturbations illuminating at least those same \(r\) vertices, because all relevant inequalities are strict. Hence \(\alpha(T_t)=21\) globally, not only on the generic locus.

**Fractional optimality.** For any polytope, fractional illumination constraints at its vertices suffice: an illuminating direction for a vertex of the smallest face containing a boundary point also illuminates that boundary point. Summing the sixty vertex constraints for any fractional illumination of \(T_t\) gives total weight at least \(60/21\), because each direction illuminates at most twenty-one vertices. Conversely, the icosahedral symmetry group is transitive on the sixty *oriented* edges, hence on the sixty vertices of \(T_t\). Average a direction attaining twenty-one illuminated vertices over that finite symmetry group, assigning each group image weight \(60/(21|G|)\). Transitivity gives each vertex total illuminating weight exactly one, and total weight \(60/21\). This proves \(I^*(T_t)=20/7\).

## Verification
Run `python verify.py` in a directory containing `verify.py` and `cells.csv` (Python standard library only). The exact checker constructs the twelve icosahedral vertices, thirty edges and twenty faces from squared-distance tests; checks the regular truncated solid's thirty-two supporting facets and sixty vertex-incidence triples; enumerates the great-circle chamber sectors by a complete infinitesimal combinatorial construction; and compares all 152 certified sign vectors and illumination counts with `cells.csv`. It also tests the two explicit integer witnesses. Its expected terminating output is:

`EXACT_OK normals=32 great_circles=16 cells=152 spectrum_20=132 spectrum_21=20 max=21 fractional=20/7`

The finite certificate establishes a global fact because the proof above covers every chamber, including all degenerate pairwise-circle intersections. It is not an extrapolation from random samples. The infinite continuum of truncation parameters is covered by the analytic independence of the normal fan from \(t\), not by numerical testing at sample values.

## Relationship to prior work
Naszódi introduced fractional illumination and established general bounds but did not compute this truncated-icosahedral value. Gorodzha's September 2026 theorem proves the universal bound \(I^*(K)\le2^d\), with equality classification, but does not specify this non-parallelotope's exact value. A published evaluation of the regular dodecahedron and icosahedron found fractional illumination four for both and established the general vertex-transitivity averaging identity used above; that result is about the untruncated Platonic solids. The previous exact result for the rectified icosahedron, the icosidodecahedron, also concerns a *different* sixty-to-thirty vertex degeneration at \(t=1/2\), not the open family. Kiss and Oloff de Wet analyzed the truncated icosahedron under a different norm-weighted point-source illumination parameter; their Table in Theorem 3.4 provides a four-source ordinary upper bound, but no fractional number or single-direction spectrum. The main new claim is the exact \(20/7\) value and complete two-level spectrum throughout the natural open truncation family.

## Limitations
The result is limited to regular-icosahedral equal-depth truncations and their invertible affine images, not arbitrary combinatorially equivalent sixty-vertex polyhedra. The endpoints are not included. An exact finite cell certificate is part of the correctness proof, so a reader must execute or independently review the simple field-arithmetic enumeration to reproduce the numerical integers \(152,132,20,21\). Historical priority remains provisional under alternate terminology or as-yet-unindexed tables; it has not been independently reviewed. The theorem does not establish any sharp ordinary illumination bound not already in the cited literature.

## References
1. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1, first public 20 September 2026, https://arxiv.org/abs/2609.23913.
2. M. Naszódi, *Fractional illumination of convex bodies*, *Contributions to Discrete Mathematics* 4 (2009), 83–88, DOI: 10.55016/ojs/cdm.v4i2.62022.
3. G. Kiss and P. Oloff de Wet, *Notes on the illumination parameters of convex polytopes*, *Contributions to Discrete Mathematics* 7 (2012), 58–67, DOI: 10.55016/ojs/cdm.v7i1.62108.
4. *Exact fractional illumination of the regular dodecahedron and icosahedron*, publicly available mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-the-regular-dodecahedron-and-ic--760696b5ce34.
5. E. W. Weisstein, *Truncated Icosahedron*, MathWorld, https://mathworld.wolfram.com/TruncatedIcosahedron.html.
