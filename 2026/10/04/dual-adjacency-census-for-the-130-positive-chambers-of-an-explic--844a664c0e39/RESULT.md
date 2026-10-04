# Dual adjacency census for the 130 positive chambers of an explicit real cubic surface

## Finding
For the explicit real cubic surface used by Sturmfels--Telen and the cyclic intersection order encoded in their Table 2, form the **dual chamber graph** \(D\): its vertices are the \(130\) connected components of the real surface after deleting its \(27\) lines, and two vertices are adjacent exactly when the corresponding chambers share one line-segment wall.

The \(270\) dual edges have the following complete type census:
\[
N_{T,P}=30,\qquad N_{Q,P}=120,\qquad N_{Q,Q}=120,
\]
and
\[
N_{T,T}=N_{T,Q}=N_{P,P}=0.
\]
Here \(T,Q,P\) denote triangular, quadrilateral, and pentagonal chambers.

The chamber-neighbor profiles are likewise complete. Every triangle has three pentagonal neighbors. Every pentagon has one triangular and four quadrilateral neighbors. The \(90\) quadrilaterals split exactly into
\[
20\,(Q,Q,Q,Q),\qquad 20\,(Q,Q,Q,P),\qquad 50\,(Q,Q,P,P).
\]

## Assumptions and scope
The claim concerns the specific running cubic surface in Sturmfels--Telen, equation (1), together with the cyclic order of the ten intersection points on each of its \(27\) real lines given by Table 2 and the associated supplementary file `section3.jl`. No invariance of the full neighbor-profile census over every connected component of the real cubic-surface moduli space is asserted.

The source surface is general in the relevant sense: no three of its \(27\) lines meet. The published chamber decomposition has \(10\) triangles, \(90\) quadrilaterals, and \(30\) pentagons.

## Proof
The supplementary Table-2 data give, for every line \(L\), a cyclic list of the ten other lines meeting \(L\). An intersection point is therefore the unordered pair \(\{{L,M}}\). There are \(135\) such pairs. Consecutive entries around each cyclic list determine the line segments between successive intersection points; after identifying duplicates this gives a graph \(G\) with \(135\) vertices and \(270\) edges, exactly as in the source computation.

A chamber boundary is an induced cycle in \(G\). Exhaustive enumeration of simple induced cycles of lengths \(3,4,5,6\) gives respectively \(10,90,30,0\). Thus the enumerated \(130\) induced cycles recover exactly the published chamber census; no additional short induced cycle is being inserted as a chamber.

For every edge \(e\) of \(G\), record the chamber cycles containing \(e\). Direct exhaustive checking shows that each of the \(270\) edges occurs in exactly two chamber boundaries. Hence each primal wall defines one edge of the dual graph \(D\). Counting the two chamber sizes on those \(270\) walls gives
\[
30\,TP+120\,QP+120\,QQ.
\]
No other unordered pair of chamber types occurs.

Finally, for each chamber, count the types of its dual neighbors. The resulting multiset is
\[
10\,T(P^3),\quad 30\,P(TQ^4),\quad
20\,Q(Q^4),\quad 20\,Q(Q^3P),\quad 50\,Q(Q^2P^2).
\]
This proves the stated profile split. Independent incidence checks agree: pentagonal incidences give \(30\cdot5=30+120\), quadrilateral incidences give \(90\cdot4=2\cdot120+120\), and the total dual degree sum is \(2\cdot270\).

## Verification
`artifacts/verify_dual_adjacency.py` is a standalone Python checker using only the standard library. It embeds the published cyclic-order table, reconstructs \(G\), exhaustively enumerates and tests induced cycles of lengths \(3\) through \(6\), checks two-sided incidence of every wall, forms the dual graph, and asserts the complete wall and neighbor-profile counts. Its recorded output ends in `VERIFY_OK`.

## Relationship to prior work
Sturmfels--Telen prove that a general real cubic surface with all \(27\) lines real has \(130\) chambers of sizes \(10,90,30\), and their supplementary Section 3 code reconstructs those chambers from Table 2. Earlier, Early--Geiger--Panizzut--Sturmfels--Telen--Yun proved the same \(n=6\) face vector and explicitly observed that each triangular chamber shares all three of its edges with pentagons. That triangular subprofile is therefore **not** claimed as new here.

The additional content here is the complete wall-type census and the full pentagon/quadrilateral neighbor profiles for the explicit Table-2 chamber complex. Targeted statement-level searches in the initiating paper, its supplement, the predecessor paper, the semantic research index, and public web search found no statement of the \(30/120/120\) wall split or the \(20/20/50\) quadrilateral profile split.

## Limitations
The computation is exact and exhaustive for the published Table-2 cyclic-order data, but this result does not prove that the full profile is constant throughout the real moduli space. A historically equivalent incidence census may exist under classical cubic-surface terminology not surfaced by the searches. The result is combinatorial incidence data for the chamber decomposition; it does not by itself derive new identities among canonical differential forms.

## References
1. B. Sturmfels and S. Telen, *Positive Geometries from Cubic Surfaces*, arXiv:2605.11909v1, 2026. Supplementary data: Zenodo DOI 10.5281/zenodo.22234416, especially `section3.jl`.
2. N. Early, D. Geiger, M. Panizzut, B. Sturmfels, S. Telen, and C. Yun, *Positive del Pezzo Geometry*, arXiv:2306.13604v3; Ann. Inst. H. Poincaré D 12 (2025).
