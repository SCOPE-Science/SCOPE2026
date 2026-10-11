# Complete graph-metric Vietoris–Rips filtration of the Möbius–Kantor graph
## Finding
Let \(M=G(8,3)\) be the Möbius–Kantor graph, with outer vertices \(u_i\), inner vertices \(v_i\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\) for \(i\in\mathbb Z/8\mathbb Z\). Give \(V(M)\) the shortest-path metric and use the inclusive Vietoris–Rips convention. Then, for every real \(r\ge 0\),
\[
\operatorname{VR}_{\le r}(M)\simeq
\begin{cases}
\bigvee^{15}S^0,&0\le r<1,\\
\bigvee^{9}S^1,&1\le r<2,\\
\bigvee^{9}S^2\vee\bigvee^{2}S^3,&2\le r<3,\\
S^7,&3\le r<4,\\
\ast,&r\ge4.
\end{cases}
\]

## Assumptions and scope
The graph is exactly the generalized Petersen graph \(G(8,3)\) under the displayed presentation. Distances are unweighted graph distances. A finite vertex set is a simplex of \(\operatorname{VR}_{\le r}(M)\) exactly when all pairwise distances are at most \(r\). Since graph distances are integral, the filtration is constant on each interval between consecutive integers.

The claim concerns only these homotopy types. It does not classify Vietoris–Rips complexes of all generalized Petersen graphs, and it does not assert formulas for the inclusion-induced maps beyond what follows formally from the displayed filtration.

## Proof
The graph has \(16\) vertices, \(24\) edges, and diameter \(4\).

For \(0\le r<1\), only singleton simplices occur, so the space is a discrete set of \(16\) points and hence is homotopy equivalent to \(\bigvee^{15}S^0\).

For \(1\le r<2\), the Rips complex is the graph itself. Exhaustive clique checking shows that there are no triangles, so its face vector is \((16,24)\). The graph is connected, and therefore its cycle rank is \(24-16+1=9\). Hence it is homotopy equivalent to \(\bigvee^{9}S^1\).

For \(2\le r<3\), exhaustive diameter checking gives the face vector
\[
(16,72,112,48).
\]
On the \(248\) nonempty faces, perform successive vertex-toggle matchings in the vertex order
\[
13,2,12,11,7,1,5,3,0,10,4,8,6,9,14,15.
\]
This matches \(118\) face-coface pairs. The complete oriented Hasse diagram is acyclic. The unmatched cells consist of one \(0\)-cell, nine \(2\)-cells, and two \(3\)-cells. Exact signed gradient-path summation gives the Morse boundary matrix from the two critical \(3\)-cells to the nine critical \(2\)-cells as the zero \(9\times2\) matrix.

Thus the Morse CW model has one \(0\)-cell, no \(1\)-cells, nine \(2\)-cells, and two \(3\)-cells. Its \(2\)-skeleton is \(\bigvee^{9}S^2\). Since this wedge is simply connected, the Hurewicz map \(\pi_2\to H_2\) is an isomorphism. The zero cellular boundary vectors therefore mean that both \(3\)-cell attaching maps are nullhomotopic. Consequently
\[
\operatorname{VR}_{\le2}(M)\simeq\bigvee^{9}S^2\vee\bigvee^{2}S^3.
\]

For \(3\le r<4\), the only vertex pairs not joined in the Rips graph are the eight distance-\(4\) pairs
\[
\{0,4\},\{1,5\},\{2,6\},\{3,7\},\{8,12\},\{9,13\},\{10,14\},\{11,15\}.
\]
They form a perfect matching. Hence the Rips complex is the clique complex of the complement of a perfect matching, equivalently the join of eight copies of \(S^0\), which is \(S^7\).

For \(r\ge4\), every pair of vertices has distance at most \(4\), so the Rips complex is the full \(15\)-simplex and is contractible.

## Verification
The standalone verifier `verify.py` reconstructs \(G(8,3)\) from the defining edges, computes all-pairs shortest-path distances, enumerates all simplices at the nontrivial integer scales, checks the scale-\(2\) matching against every Hasse edge, verifies acyclicity by a complete topological sort, and computes the exact signed gradient-path boundary. Its deterministic output is stored in `verification_output.json`.

The verified scale-\(2\) critical cells are one critical \(0\)-cell, nine critical \(2\)-cells, and two critical \(3\)-cells, with zero exact Morse boundary. At scale \(3\), the verifier checks that the distance-\(4\) graph is a perfect matching and that the face numbers agree with the boundary of the \(8\)-dimensional cross-polytope.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine complete Vietoris–Rips filtrations for the vertex sets of the Platonic solids, working explicitly with combinatorial distance and inclusive Rips complexes. Their paper is classified primarily under MSC \(55N31\), lists only the five Platonic solids in its main finite graph-metric table, and points to structured extensions beyond those examples. The Möbius–Kantor graph is not among those spaces.

Goričan and Virk develop general structural results about critical edges and low-dimensional changes in Rips persistence for compact metric spaces. Those results do not determine the exact higher homotopy types in the present finite graph filtration. Adamaszek and Adams determine Rips complexes of hypercube graphs at small scales; the present metric is the shortest-path metric of \(G(8,3)\), not the Hamming metric of a hypercube graph, so those formulas do not imply the claim here.

Searches for the Möbius–Kantor graph under its standard aliases, together with checks for graph powers, shortest-path Rips complexes, and exact scale-\(2\)/scale-\(3\) homotopy statements, located nearby results for other symmetric graphs but no statement implying this filtration.

## Limitations
This is an exact result for one natural symmetric cubic graph, not a family theorem. The scale-\(2\) homotopy equivalence is certified by a specific exhaustive discrete-Morse matching; a different labeling may produce a different certificate. The literature comparison cannot exclude an uncatalogued source, although the directly relevant primary papers and targeted database searches were checked.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris-Rips complexes of Platonic solids*, arXiv:2302.14388v1, first public 2023-02-28; DOI 10.2140/iig.2024.21.17.
2. P. Goričan and Ž. Virk, *Critical edges in Rips complexes and persistence*, arXiv:2304.05185v1, first public 2023-04-11; DOI 10.1007/s00009-023-02533-9.
3. M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040v1, first public 2021-03-01.
