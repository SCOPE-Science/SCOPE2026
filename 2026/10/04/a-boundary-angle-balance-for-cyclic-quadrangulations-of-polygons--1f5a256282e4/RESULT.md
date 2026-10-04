# A boundary-angle balance for cyclic quadrangulations of polygons

## Finding

Let \(P\) be a simply connected Euclidean polygon with a finite edge-to-edge tiling by nondegenerate convex cyclic quadrilaterals. Let \(G\) be the embedded mesh graph and \(F\) its number of quadrilateral faces. The graph is bipartite; fix \(V(G)=X\sqcup Y\). For \(C\in\{X,Y\}\), let \(I_C\) be the number of interior mesh vertices of color \(C\), and for each boundary mesh vertex \(v\) let \(\theta_v\) be the interior angle of \(P\) there, with \(\theta_v=\pi\) at a subdivision point on a straight side. Then
\[
F\pi=2\pi I_C+\sum_{v\in C\cap\partial P}\theta_v.
\]
Consequently,
\[
\sum_{v\in X\cap\partial P}\theta_v-\sum_{v\in Y\cap\partial P}\theta_v=2\pi(I_Y-I_X).
\]

For a square, let \(e_1,e_2,e_3,e_4\) be the numbers of boundary tile edges along its four sides in cyclic order. Then exactly two adjacent values among them cannot be odd. Thus cyclic geometry imposes a boundary-parity obstruction stronger than the purely topological requirement that \(e_1+e_2+e_3+e_4\) be even.

## Assumptions and scope

The tiling is finite and edge-to-edge and fills a simply connected polygonal region. Two distinct tiles meet, if at all, in a whole common edge or in vertices; T-junctions are excluded. Every tile is a nondegenerate convex cyclic quadrilateral, but the tiles need not be congruent. The square conclusion is necessary only; no sufficiency or rectangle classification is claimed.

The literature motivation is the odd-congruent-square-dissection problem. Rao, Ren, and Wang ask what quadrilaterals can tile a square and single out the angle pattern \((\alpha,\pi/2,\pi-\alpha,\pi/2)\), which is cyclic because opposite angles are supplementary. Maldonado and Roldán-Pensado later settle the congruent problem for seven and nine tiles, while their finite classification does not supply an all-size cyclic boundary invariant.

## Proof

Let \(B\) be the number of boundary edges and \(E_{\mathrm{int}}\) the number of interior edges. Counting edge incidences of quadrilateral faces gives
\[
4F=2E_{\mathrm{int}}+B,
\]
so \(B\) is even. Every bounded face has length four and the outer face has even length \(B\), hence the connected plane graph \(G\) is bipartite.

Fix one color class \(C\). On each quadrilateral face the two \(C\)-colored vertices are opposite. Because the face is cyclic, those two angles are supplementary, so their sum is \(\pi\). Summing over all faces yields total \(C\)-colored face-angle mass \(F\pi\). Re-indexing by mesh vertices, each interior vertex contributes \(2\pi\), while a boundary vertex \(v\) contributes exactly \(\theta_v\). This proves
\[
F\pi=2\pi I_C+\sum_{v\in C\cap\partial P}\theta_v.
\]
Subtracting the two color identities gives the alternating boundary-angle formula.

Now let \(P\) be a square. The boundary cycle alternates colors, so each color class has \(B/2\) boundary mesh vertices. Let \(m_C\) be the number of the four geometric square corners belonging to \(C\). The other boundary vertices have angle \(\pi\), while square corners have angle \(\pi/2\). Therefore
\[
F=2I_C+\frac{B}{2}-\frac{m_C}{2}.
\]
Thus \(m_C\) is even, so the square corners cannot split \(3\)-to-\(1\) between the two colors. Traversing side \(i\) flips the corner color exactly when \(e_i\) is odd. With even total boundary length, exactly two adjacent odd \(e_i\) produce precisely a \(3\)-to-\(1\) corner-color split, contradiction.

## Verification

The argument was checked at every dependency: edge-incidence parity, plane-graph bipartiteness, supplementary opposite angles for cyclic quadrilaterals, and angle filling at interior and boundary vertices. The eight parity vectors \((e_1,e_2,e_3,e_4)\bmod 2\) with even total parity were exhaustively checked; precisely the four patterns with two adjacent odd entries give a \(3\)-to-\(1\) corner-color split.

No numerical approximation is used. The edge-to-edge condition is essential to this proof; a T-junction subdivision need not preserve cyclic quadrilateral faces.

## Relationship to prior work

Rao, Ren, and Wang formulate the odd congruent-square-dissection conjecture and identify a cyclic quadrilateral angle class among the candidate square-tiling shapes; they do not state this boundary-angle balance. Maldonado and Roldán-Pensado prove the rectangle conclusion for seven and nine congruent pieces by finite graph-and-angle search, not by an all-size cyclic identity.

Takayama, Panozzo, and Sorkine-Hornung prove at the level of quad-mesh connectivity that prescribed boundary subdivision counts are topologically realizable once their total is even. Their result does not impose Euclidean cyclic geometry. Hence the present condition is strictly stronger in its domain: \((1,1,2,2)\) passes their even-total topological test but is excluded for an edge-to-edge tiling by cyclic quadrilaterals.

## Limitations

This does not settle the odd congruent-square-dissection conjecture, does not prove that a cyclic quadrilateral tile must be a rectangle, and does not cover T-junction tilings. Targeted literature searches and direct source inspection did not locate an equivalent statement, but that is not a proof that no equivalent observation appears under different terminology.

## References

H. Rao, L. Ren, and Y. Wang, “Dissecting a square into congruent polygons,” arXiv:2001.03289, first submitted 2020-01-10.

G. L. Maldonado and E. Roldán-Pensado, “Dissecting the square into seven or nine congruent parts,” arXiv:2104.04940, first submitted 2021-04-11.

K. Takayama, D. Panozzo, and O. Sorkine-Hornung, “Pattern-Based Quadrangulation for N-Sided Patches,” Computer Graphics Forum 33 (2014), 177–184, DOI 10.1111/cgf.12443.
