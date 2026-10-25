# Optimizer dimension and exact orbit counts for maximal tetrahedra in regular polygonal prisms

## Finding
Let \(n\ge4\), \(R,h>0\). Let \(P_n\) be the regular Euclidean \(n\)-gon of circumradius \(R\) and let \(Z=P_n\times[0,h]\). Denote the maximum three-dimensional volume of a tetrahedron contained in \(Z\) by \(V_n\). Then
\[
V_n=\frac{2hR^2}{3}\begin{cases}
1,&n\equiv0\pmod4,\\
\cos(\pi/n),&n\equiv2\pmod4,\\
\cos^3(\pi/(2n)),&n\text{ odd}.
\end{cases}
\]
This *numerical value* is a consequence of existing planar inner-quadrilateral and outer-parallelogram results; it is included as context, not asserted as an independently new bound.

The classification is as follows. Every maximum tetrahedron has precisely two vertices in each of the horizontal bases. At a prism-vertex-supported maximum, its four projected polygon vertices appear cyclically with the four positive integer gaps as equal as possible (all gaps belong to \(\{\lfloor n/4\rfloor,\lceil n/4\rceil\}\)), and the two same-height pairs are *crossing diagonals* of that cyclic quadrilateral. Conversely every such choice is maximal. The **number of unordered maximum-volume tetrahedra using prism vertices only** is exactly
\[
N_n=\begin{cases}
n/2,&n\equiv0\pmod4,\\
3n,&n\equiv2\pmod4,\\
2n,&n\text{ odd}.
\end{cases}
\]

The *entire continuous equality set* admits a finite face criterion: after designating two lower and two upper points, project the four points onto \(P_n\), and let \(F_1,F_2,F_3,F_4\) be their unique minimal polygon faces (each a vertex or an edge). The tetrahedron is maximal **if and only if** its vertices are on those horizontal bases and, for every choice of one endpoint of each \(F_i\) (at most \(16\) choices), the resulting projected quadruple consists of four distinct regular-polygon vertices with balanced cyclic gaps, with the lower pair crossing the upper pair, and all corresponding *oriented* determinants having one common sign. The criterion is necessary and sufficient, not merely a test for vertex-supported tetrahedra.

In this semialgebraic optimizer set the **largest dimension of a flat optimizer family** is exactly
\[
d_n=\begin{cases}
0,&n\equiv0\pmod4,\\
2,&n\equiv2\pmod4,\\
1,&n\text{ odd}.
\end{cases}
\]
In particular, multiples of four have only isolated maximizing tetrahedra; orders congruent to two modulo four have genuinely two-parameter maximizing families. The dimension means the maximum number of independently movable polygon-edge coordinates in a Cartesian face of the complete equality set, and equals its topological dimension.

## Assumptions and scope
All tetrahedra are nondegenerate Euclidean tetrahedra with their four corners anywhere in the closed prism; they are not required to be vertex-supported. Two tetrahedra differing in any corner position are distinct, but vertex-supported counts do not count vertex permutations separately. The two horizontal bases are labeled by their heights; tetrahedra with the two height assignments interchanged count separately unless they are literally identical, which cannot happen at positive height. Edge interiors are allowed in the continuous classification. No claim about prisms with nonregular bases or higher-dimensional simplices is made.

## Proof
**1. Multiaffine reduction and height rigidity.** For labeled tetrahedron vertices \(x_1,\ldots,x_4\), six times oriented volume is \(\det(x_2-x_1,x_3-x_1,x_4-x_1)\). This is affine in each \(x_i\) with all others fixed. Every point of the prism is a convex combination of its \(2n\) vertices. Consequently every tetrahedron's determinant is a convex combination of determinants of prism-vertex tetrahedra and the maximum absolute volume is attained by one with four prism vertices. More strongly, if an oriented volume is maximal, *every* vertex combination with positive coefficient in such a product decomposition has the same maximal oriented determinant.

For a vertex tetrahedron, distributing its vertices between the two base planes in proportions \(3+1\) gives six times its volume equal to \(h\) times twice the area of its projected triangle. A \(2+2\) split gives \(h\) times the absolute cross product of the projected lower and upper chords. Given four distinct vertices of \(P_n\), the two crossing diagonals intersect in the relative interiors. Representing them from their intersection by vectors \(a u,-b u,c v,-d v\), with all four positive lengths, shows the crossing-diagonal determinant \((a+b)(c+d)|\det(u,v)|\) strictly exceeds the noncrossing opposite-edge determinants. Every triangle using polygon vertices has strictly smaller area than some quadrilateral using polygon vertices when \(n\ge4\). Since the determinant of the two crossing diagonals of the quadrilateral is exactly twice the quadrilateral's area, every \(3+1\) configuration is strictly inferior to a suitable \(2+2\) tetrahedron. Configurations with all four prism vertices on one level have zero volume. Thus all vertex-supported maxima have the \(2+2\) split and crossing diagonals of four distinct projected vertices.

The stronger product-decomposition equality statement shows that any maximum tetrahedron with a corner at an interior height would have a positive-weight vertex combination using a \(3+1\), \(4+0\), or \(0+4\) level split, contradicting the strict comparison. Therefore *every* maximum tetrahedron has its four corners on the bases, with exactly two on each base. For fixed other three corners, the oriented determinant varies nontrivially with each base point's two-dimensional position: its gradient is perpendicular to the nonzero segment joining the other corner on the same base. Maximization of this nonconstant linear functional over \(P_n\) forces that point to lie on an exposed proper face (vertex or edge).

**2. Exact discrete gap maximum.** Let the four projected regular-polygon vertices be cyclically ordered and let \(g_1,g_2,g_3,g_4\) be their positive cyclic index gaps, totaling \(n\). Direct chord trigonometry (chord length \(2R\sin(\pi k/n)\), and the inscribed angle theorem) gives the crossed-chord determinant
\[
D(g_1,g_2,g_3,g_4)=4R^2\sin\frac{\pi(g_1+g_2)}{n}\;\sin\frac{\pi(g_2+g_3)}{n}\;\sin\frac{\pi(g_1+g_3)}{n}.
\]
The function \(\log D\) is strictly concave on the open simplex of positive real gaps with fixed sum \(n\): each \(\log\sin\) factor is strictly concave on \((0,\pi)\), and the three pair sums, together with the total gap sum, uniquely determine all four gaps. The product is symmetric in the four gaps; its three pair sums merely permute or are replaced by complementary sums under permutations, leaving their sines invariant. A symmetric strictly concave function is strictly increased by averaging any two unequal coordinates. On the positive integer gap vectors the maximizing vectors are consequently exactly those in which no pair differs by more than one. Substituting the balanced gaps into the displayed chord identity gives the stated three-branch formula for \(V_n=hD_{\max}/6\). This independently checks the volume normalization although the numerical bound also follows from known planar results.

**3. Exact finite optimizer counts.** Write \(n=4k+s\), \(s\in\{0,1,2,3\}\). A balanced cyclic gap quadruple has \(s\) entries \(k+1\) and \(4-s\) entries \(k\). There are \(\binom4s\) labeled cyclic gap words. Starting at any of the \(n\) polygon vertices and quotienting by the four choices of initial vertex gives exactly \(n\binom4s/4\) unordered projected quadruples. For each such quadruple, crossing diagonals must be the two horizontal chords, with precisely two choices of which diagonal is lower. Thus
\[
N_n=\frac n2\binom4s,
\]
which reduces to the stated \(n/2,2n,3n,2n\) sequence as \(s=0,1,2,3\).

**4. All continuous equality cases.** Every maximizing point projects to a vertex or an edge by Step 1. Expand each edge position into its two endpoint vertices. By determinant multiaffinity, the oriented determinant at the original tetrahedron is the positive-weight average of all endpoint-combination determinants. Every endpoint determinant is bounded in absolute value by \(6V_n\). Equality of the average at \(\pm6V_n\) holds if and only if **all** endpoint determinants are identically that same signed extremal value. By Steps 1–2 this is equivalent to the explicit balanced-gap, crossed-diagonal, common-orientation finite-face criterion in the theorem. Conversely that criterion makes every multiaffine interpolation identically extremal, proving sufficiency.

**5. Sharp dimensions of optimizer families.** Any equality cell is a Cartesian product of at most four polygon edges or fixed vertices with two assigned lower and two upper locations; its dimension is the number of freely moving edge coordinates. Fix a cyclic ordering of the four projected endpoints and write their gaps as \(g_i\in\{k,k+1\}\). If endpoint \(i\) may move forward along one polygon edge, its binary endpoint choice \(\delta_i\in\{0,1\}\) changes adjacent gaps by \(g_{i-1}\mapsto g_{i-1}+\delta_i\) and \(g_i\mapsto g_i-\delta_i\). To remain balanced for both choices, it requires \(g_{i-1}=k\) and \(g_i=k+1\). Two neighboring endpoints cannot be freely movable *independently*, since their common gap would have to range through two values separated by two. Hence at most two of the four endpoints can move, and if two move they must be opposite. For opposite endpoints both to be free their four adjacent gaps must consist of exactly two \(k\)'s and two \(k+1\)'s; this forces \(s=2\). When \(s=0\) no endpoint can move. If \(s=1\) or \(s=3\), there is at least one adjacent \(k,k+1\) pair, which yields a genuine one-parameter family by moving its separating endpoint. If \(s=2\), the cyclic gap vector \((k+1,k,k+1,k)\) permits both opposite endpoints to move independently (all four endpoint choices retain balanced gaps and the crossing orientation). This constructs a two-dimensional equality rectangle. All optimizer cells are Cartesian products of intervals, so the largest such cell dimension is the dimension of the complete equality set, proving the residue-class trichotomy.

## Verification
A self-contained Python checker in `check_prism.py` enumerates all \(398733\) four-vertex selections from the \(2n\) prism vertices for \(3\le n\le20\), computes every determinant, and compares the precise maxima and optimizer counts. It also enumerates every pair of polygon chords for \(3\le n\le48\), confirming both the trigonometric maximum and the balanced-gap equality criterion, and checks all binary endpoint possibilities for optimizer-face dimensions at \(4\le n\le17\). Expected terminal lines are `PRISM_TETRAHEDRON_CHECK_OK tetra_subsets= 398733 tested_orders= 46` and `OPTIMIZER_FACE_DIMENSION_OK orders=14`. Only Python's standard library is required; run `python3 check_prism.py`. The full infinite-parameter theorem rests on the foregoing analytical argument; the finite sweeps are cross-checks only.

## Relationship to prior work
Rote, *The Largest Contained Quadrilateral and the Smallest Enclosing Parallelogram of a Convex Polygon* (2019), proves a general conjugacy theorem: the largest inscribed quadrilateral has half the area of the smallest enclosing parallelogram, with anchored equality descriptions. The 2026 exact area formula for minimum enclosing parallelograms of every regular polygon therefore **already implies the displayed maximal tetrahedron *value*** after the elementary prism determinant reduction, and the 2026 even-regular-polygon rectangle classification also gives a related planar optimum. These previously known implications are expressly **not claimed as original**.

The new statement is the full three-dimensional equality locus: it proves two-versus-two height rigidity, gives all balanced-gap crossing-diagonal optimizer orbits, enumerates distinct vertex-supported maxima, supplies a necessary-and-sufficient face test for *all* continuous tetrahedra, and establishes the sharp dimension phase transition \(0,1,2\) as \(n\) varies modulo four. None of these exact prism equality classifications appears in the materially inspected primary Rote manuscript or the inspected regular-polygon enclosing and rectangle reports. Rote's general characterization does not directly state these counts or dimensions; specialized prior work on polygonal prisms could nevertheless subsume this result. Hoehner and Ledford's 2026 inscribed-polytope volume paper motivates the present exact extremal-volume question but concerns different bodies and does not supply the prism classification.

## Limitations
This is a classification of *tetrahedral maximizers in regular right prisms*, not a new universal maximal-volume formula, an algorithm improvement for arbitrary prisms, or a theorem for nonregular bases. The result is a deduction using standard determinant and strict-concavity methods plus new gap/combinatorial equality analysis. The main historical-priority risk is an older or unindexed regular-prism specialization of general largest-quadrilateral theory. A complete independent audit has not been performed; computational checks are finite only.

## References
1. G. Rote, *The Largest Contained Quadrilateral and the Smallest Enclosing Parallelogram of a Convex Polygon*, arXiv:1905.11203v2, June 18, 2019. In particular Lemmas 1–3 and Section 3.
2. *Exact minimum-area enclosing parallelograms for regular polygons*, research result published October 11, 2026, identifier `2026/10/11/SCOPE-exact-minimum-area-enclosing-parallelograms-for-regular-polygons--827c68cd7bad`.
3. *Exact maximum-area rectangles in every regular even polygon*, research result published October 4, 2026, identifier `2026/10/4/SCOPE-exact-maximum-area-rectangles-in-every-regular-even-polygon--10bad5e59427`.
4. S. Hoehner and J. Ledford, *The maximum volume polytope with nine vertices inscribed in the sphere*, arXiv:2608.04392v1, first submitted August 5, 2026.
5. D. Ismailescu, M. J. Kim, and E. Wang, *On the maximum area of inscribed polygons*, arXiv:2104.12172v1, 2021.
