# A sharp tetrahedral transition in cube–octahedron convex hulls

## Finding
For each real parameter \(1<t<3\), let
\[
P_t=\operatorname{conv}\bigl(\{(\varepsilon_1,\varepsilon_2,\varepsilon_3):\varepsilon_i\in\{-1,1\}\}\cup\{\pm t e_1,\pm t e_2,\pm t e_3\}\bigr)\subset\mathbb R^3.
\]
Every tetrahedron \(T\subseteq P_t\), without restrictions on its vertex locations, obeys the **sharp** inequality
\[
\boxed{\operatorname{vol}_3(T)\le\frac16\max\{16,t^2(t+3)\}.}
\]
Let \(\tau\in(1,2)\) be the unique real solution to \(\tau^2(\tau+3)=16\), numerically \(\tau\approx1.821640164404\). There are exactly **two** maximizing tetrahedra when \(1<t<\tau\), precisely **ten** when \(t=\tau\), and exactly **eight** when \(\tau<t<3\). All of their vertices are exposed vertices of \(P_t\); no tetrahedron with a nonvertex corner is optimal.

For \(1<t<\tau\), the maximizing tetrahedra are the two four-corner regular tetrahedra formed from the eight cube vertices (the alternating corner classes). For \(\tau<t<3\), the eight maximizing tetrahedra consist, for each \((\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{-1,1\}^3\), of the one cube corner \((\varepsilon_1,\varepsilon_2,\varepsilon_3)\) and the three opposed axial corners \(-t\varepsilon_1e_1,-t\varepsilon_2e_2,-t\varepsilon_3e_3\). At equality \(t=\tau\), both families are optimal.

The volume of the containing polyhedron and the sharp occupied-volume fraction are
\[
\operatorname{vol}_3(P_t)=\begin{cases}8t,&1<t\le2,\\4t^2,&2\le t<3,\end{cases}
\qquad
\frac{\max_T\operatorname{vol}_3(T)}{\operatorname{vol}_3(P_t)}=
\begin{cases}
1/(3t),&1<t\le\tau,\\
t(t+3)/48,&\tau\le t\le2,\\
(t+3)/24,&2\le t<3.
\end{cases}
\]
In particular, the fraction has its **unique global minimum** at \(t=\tau\), where it equals \(1/(3\tau)\approx0.182985278787\). At the regular rhombic dodecahedron \(P_2\), the fraction is exactly \(5/24\).

## Assumptions and scope
All volumes are three-dimensional Lebesgue volumes. The parameter satisfies \(1<t<3\) strictly, so all fourteen displayed generating points are distinct exposed vertices. The tetrahedra may be skew, irregular, and supported anywhere in the entire convex body; we do not assume vertex support in the statement. The two endpoints are excluded from the optimizer-count assertions because vertices merge into higher-dimensional faces there. All numerical approximations are illustrative; the theorem uses exact polynomials and the uniquely specified algebraic root.

## Proof
**1. The fourteen vertices.** Each axial point \(\pm t e_i\) is uniquely exposed by the corresponding signed coordinate functional, since \(t>1\). Each cube corner \(\varepsilon\) is uniquely exposed by the linear functional \(x\mapsto\langle\varepsilon,x\rangle\): its value is \(3\) on that corner, at most \(1\) on other cube corners, and at most \(t<3\) on the axial points. Hence all fourteen points are vertices and no other vertices exist by definition of the convex hull.

**2. Vertex-supported optimization.** For four points \(p_0,p_1,p_2,p_3\) write
\[
\Delta(p_0,p_1,p_2,p_3)=\det[p_1-p_0,\,p_2-p_0,\,p_3-p_0].
\]
This expression is affine separately in each point. Expressing each \(p_i\in P_t\) as a convex combination of the fourteen vertices expresses \(\Delta\) as a convex combination of signed determinants of four vertices. Therefore the maximum absolute determinant over the **whole** polyhedron equals the maximum over unordered four-vertex subsets, each counted with either orientation.

**3. An exact finite polynomial certificate.** There are precisely \(\binom{14}{4}=1001\) such unordered subsets. Order the six axial vertices by coordinate index and sign, followed by the eight lexicographically ordered cube corners. For every subset, compute the displayed signed determinant as an integer polynomial in \(t\) of degree at most three. Up to multiplication by \(-1\), the resulting **complete list** is:

| Unsigned polynomial representative | Number of four-vertex subsets |
|---|---:|
| \(0\) | 123 |
| \(4\) | 96 |
| \(8\) | 56 |
| \(16\) | 2 |
| \(2t\) | 96 |
| \(4t\) | 168 |
| \(2t^2\) | 168 |
| \(4(t-1)\) | 48 |
| \(4(t+1)\) | 48 |
| \(2t(t-1)\) | 48 |
| \(2t(t+1)\) | 48 |
| \(2t(t-2)\) | 12 |
| \(2t(t+2)\) | 12 |
| \(t^2(t-3)\) | 8 |
| \(t^2(t+3)\) | 8 |
| \(t^2(t-1)\) | 24 |
| \(t^2(t+1)\) | 24 |
| \(2t^3\) | 12 |

The multiplicities sum to \(1001\). These are polynomial identities, not values sampled from the continuum of parameters. The accompanying `verify.py` constructs every subset, computes its polynomial using two independently written integer-coefficient determinant routines, and matches the full table exactly.

For \(1<t<3\), every polynomial on the list other than \(16\) and \(t^2(t+3)\) has absolute value **strictly below** \(\max\{16,t^2(t+3)\}\). Here is an explicit bound to supplement the exhaustive classification. Terms with a factor \(t^2\) other than \(t^2(t+3)\) are bounded by it, including \(2t^3<t^2(t+3)\), \(t^2(3-t)<t^2(t+3)\), and \(2t^2<t^2(t+3)\). Likewise \(2t(t+1)<t^2(t+3)\), because \(t(t+3)-2(t+1)=(t-1)(t+2)>0\). For \(2t(t+2)\), use \(2t(t+2)<16\) when \(1<t<2\), and \(2t(t+2)<t^2(t+3)\) for \(2\le t<3\), the latter because \(t^2+t-4>0\) at \(t\ge2\). The remaining smaller terms are bounded by \(16\): \(4(t+1)<16\), \(4t<12\), \(2t<6\), \(8<16\), \(4(t-1)<8\), \(2t(t-1)<12\), and \(2t|t-2|<6\). All comparisons are strict in the open range. Therefore the exact maximal determinant is \(\max\{16,t^2(t+3)\}\).

The two determinant-\(16\) subsets are exactly the alternating cube-corner tetrahedra. The eight determinant-\(t^2(t+3)\) subsets have three mutually perpendicular axial corners and their opposite cube corner, as described in the finding. Their determinants are attained by those explicit configurations. Since \(t^2(t+3)\) increases strictly on \((1,3)\), crosses \(16\) once at \(\tau\), and no other determinant level reaches the maximum, the displayed vertex-supported counts follow.

**4. Rigidity against nonvertex optimizers.** Among the ten possible maximizing four-vertex subsets identified in Step 3, any two distinct subsets share at most two vertices. This is clear geometrically: the two alternating cube tetrahedra are disjoint; any two mixed tetrahedra of the opposite-axial type share at most two axial vertices; a cube tetrahedron and a mixed one share at most one cube corner. The exact checker also verifies this incidence statement for all \(\binom{10}{2}\) pairs.

Suppose a maximizing tetrahedron had a nonvertex corner. Orient its determinant positively at the maximal value. Expanding each of its four corners into a convex combination of polytope vertices, all terms of the resulting convex average are at most the maximal determinant. Equality of the average therefore forces **every positively weighted term** to be an oriented maximizing vertex quadruple. A nonvertex corner has at least two distinct support vertices; fixing a positively weighted choice from each of the other three supports would then give two different maximizing vertex quadruples sharing those three chosen vertices. This contradicts the just-proved at-most-two intersection property. Thus all maximizing corners must be original polytope vertices, completing the classification for unrestricted tetrahedra.

**5. Polytope volume and sharp minimization.** If \(1<t\le2\), the polyhedron consists of the unit cube (volume \(8\)) with six mutually interior-disjoint square-base pyramids, one over each cube face, each of base area \(4\) and height \(t-1\). Their total volume is \(8+6\cdot4(t-1)/3=8t\). For \(2\le t<3\), begin with the axial regular octahedron \(\{x:\sum_i|x_i|\le t\}\), of volume \(4t^3/3\). The eight cube corners add eight interior-disjoint pyramids, one over each triangular octahedral face, each of volume \(t^2(3-t)/6\). The total is \(4t^3/3+8t^2(3-t)/6=4t^2\). These decompositions follow from the supporting facets through each cube edge and neighboring axis apex for the first regime, and through each octahedron edge and neighboring cube apex for the second.

Dividing the determinant bound by six times these volumes gives the three displayed volume-fraction branches. On \((1,\tau)\) the ratio \(1/(3t)\) is strictly decreasing, and on \((\tau,2)\) and \((2,3)\) the respective ratios \(t(t+3)/48\) and \((t+3)/24\) are strictly increasing. They meet continuously at both junctions. This proves the unique global minimum. Substituting \(t=2\) gives \(\max\operatorname{vol}_3(T)=20/6=10/3\), \(\operatorname{vol}_3(P_2)=16\), and ratio \(5/24\). \(\square\)

## Verification
The standalone Python 3 checker `verify.py` needs no third-party packages. Run `python3 verify.py` and require the exact message beginning `VERIFY_OK`. It evaluates all \(1001\) unordered four-vertex subsets as formal degree-at-most-three polynomials, with two separate determinant expansions; checks all 18 polynomial classes and multiplicities; identifies the two and eight potential maximizers; and tests the no-common-three-vertices property. These finite checks are exhaustive because Step 1 proves the complete vertex set and Step 2 reduces the continuous optimization to the finite list. The inequality comparisons and monotonicity in Steps 3 and 5 are analytic, not inferred from sample points.

## Relationship to prior work
The regular rhombic dodecahedron is the special parameter \(t=2\) in this natural convex hull of a cube and its axial dual octahedron; its \(\Delta\)-zonotope geometry is part of the literature on simplex-generated zonotopes [1]. Existing work on the **intersection** rather than the hull studies \(K_c=[-1,1]^3\cap\{\sum_i|x_i|\le c\}\) and derives a distinct three-phase maximal-tetrahedron law [2]. Indeed \(tP_t^\circ=K_t\), but polarity does **not** take a maximum inscribed tetrahedron of \(P_t\) into a maximum inscribed tetrahedron of \(K_t\); it reverses inclusion and interchanges vertices and facets, and hence [2] does not imply the present volume law. The published five-dimensional simplex-generated zonotope theorem [3] concerns a different dimension and a different extremal body. General cube simplex/determinant work [4] provides relevant methodology, but its cube determinant bounds alone do not establish the mixed axis-and-cube extremizers or the exact crossover.

## Limitations
The statement is restricted to three dimensions, to the explicitly specified one-parameter convex-hull family, and to volume-maximizing tetrahedra. It does not classify all maximal-volume simplices in arbitrary centrally symmetric fourteen-vertex polytopes. The complete determinant table is a finite mathematical certificate, not an external independent audit. Existing published exact results for the **polar intersection** family and for the regular rhombic dodecahedron's elementary geometry are acknowledged. Historical overlap in older, unindexed convex-polytope optimization tables remains possible; absence of a database match alone does not establish priority. Endpoint optimizer classifications at \(t=1\) and \(t=3\) are not asserted.

## References
1. R. T. Živaljević, *Illumination complexes, Δ-zonotopes, and the polyhedral curtain theorem*, arXiv:1307.5138, first publicly submitted 2013-07-19. https://arxiv.org/abs/1307.5138
2. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, published mathematical research record dated 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-tetrahedral-volume-profile-in-the-cube-octahedron-intersec--9ba1a511dacf
3. *The largest simplex in every five-dimensional simplex-generated zonotope*, published mathematical research record dated 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-largest-simplex-in-every-five-dimensional-simplex-generated--9f4a79941cdf
4. M. Hudelson, V. Klee, D. Larman, *Largest j-simplices in d-cubes: Some relatives of the Hadamard maximum determinant problem*, Linear Algebra and Its Applications 241–243 (1996), 519–598. https://doi.org/10.1016/0024-3795(95)00541-2
