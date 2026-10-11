# Complete graph-metric Vietoris–Rips filtration of the Dürer graph
## Finding
Let \(D=G(6,2)\) be the Dürer graph with vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/6\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). Give every edge length \(1\) and write \(d\) for shortest-path distance. For the inclusive Vietoris–Rips complex, a nonempty finite set \(\sigma\subseteq V(D)\) is a simplex of \(\operatorname{VR}_{\le r}(D)\) exactly when \(d(x,y)\le r\) for all \(x,y\in\sigma\).

For every real \(r\ge0\),
\[
\operatorname{VR}_{\le r}(D)\simeq
\begin{cases}
\bigvee^{11}S^0,&0\le r<1,\\
\bigvee^{5}S^1,&1\le r<2,\\
S^2,&2\le r<3,\\
*,&r\ge3.
\end{cases}
\]
Thus the complex is already contractible at graph-distance threshold \(3\), one step before the diameter \(4\) makes it a full simplex.

## Assumptions and scope
The claim concerns the unweighted generalized Petersen graph \(G(6,2)\) with the explicit edge convention above and the inclusive diameter condition \(\le r\). All graph distances are integers, so the filtration is constant on each interval between successive integers. The statement is a homotopy-type computation for this one finite metric graph; it does not assert a formula for arbitrary generalized Petersen graphs.

## Proof
The graph has \(12\) vertices, \(18\) edges, and diameter \(4\). For \(0\le r<1\), only the \(12\) singletons occur, giving a discrete space homotopy equivalent to \(\bigvee^{11}S^0\). For \(r\ge4\), every vertex pair has distance at most \(4\), so the Rips complex is the full \(11\)-simplex.

It remains to treat thresholds \(1,2,3\). Enumerate every nonempty subset of the \(12\)-vertex set and retain exactly those of diameter at most the threshold. At threshold \(1\) the face vector is
\[
(12,18,2),
\]
at threshold \(2\) it is
\[
(12,48,82,60,18,2),
\]
and at threshold \(3\) it is
\[
(12,63,190,363,456,377,198,60,8).
\]

On each face poset, process vertices in the fixed order \(u_0,u_1,\ldots,u_5,v_0,v_1,\ldots,v_5\). At a stage for vertex \(x\), pair each still-unpaired simplex \(\sigma\) not containing \(x\) with \(\sigma\cup\{x\}\) whenever that cofacet is still unpaired. The supplied verifier constructs the resulting matching explicitly and then orients every matched Hasse cover upward and every other cover downward. A complete topological-sort check proves that the oriented Hasse diagram is acyclic.

The verified critical cells are: one \(0\)-cell and five \(1\)-cells at threshold \(1\); one \(0\)-cell and one \(2\)-cell at threshold \(2\); and only one \(0\)-cell at threshold \(3\). Discrete Morse theory therefore yields a CW complex with exactly those cells. The first is \(\bigvee^5S^1\); the second is \(S^2\), because its single \(2\)-cell attaches to the unique \(0\)-cell; and the third is contractible. Since distances are integral, these types persist throughout \([1,2)\), \([2,3)\), and \([3,4)\), respectively.

## Verification
The standalone script `verify.py` reconstructs \(G(6,2)\) from the edge formula, recomputes all-pairs shortest-path distances, confirms diameter \(4\), exhaustively enumerates every Rips face at thresholds \(1,2,3\), builds the matching, checks every Hasse cover, and proves acyclicity by topological sorting of the fully oriented Hasse diagram.

The exact checks are:

- threshold \(1\): \(32\) nonempty faces, \(42\) Hasse covers, \(13\) matched pairs, critical cells \(c_0=1,c_1=5\), Euler characteristic \(-4\);
- threshold \(2\): \(222\) nonempty faces, \(684\) Hasse covers, \(110\) matched pairs, critical cells \(c_0=1,c_2=1\), Euler characteristic \(2\);
- threshold \(3\): \(1727\) nonempty faces, \(8628\) Hasse covers, \(863\) matched pairs, one critical \(0\)-cell, Euler characteristic \(1\).

The script also checks that threshold \(0\) has exactly \(12\) singleton faces and threshold \(4\) is the full nonempty simplex on \(12\) vertices.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine complete Vietoris–Rips filtrations for the five Platonic solids and explicitly motivate complete computations for other highly structured finite metric spaces. Their theorem lists only the tetrahedron, octahedron, cube, icosahedron, and dodecahedron; the Dürer graph is not among those objects. Their paper supplies the closest direct methodological precedent for a complete finite graph-metric Rips filtration.

Feng and Nukala study scale-\(2\) Rips complexes for specific finite metric spaces built from layers of subsets of a finite set under symmetric-difference distance. Those families do not include the shortest-path metric on \(G(6,2)\).

Searches under both names “Dürer graph” and “generalized Petersen \(G(6,2)\)” found no prior statement matching this filtration. The closest indexed results concern other graph metrics, including the truncated tetrahedron, Euclidean cuboctahedron, and finite-projective-plane incidence graphs; none implies the present four-stage homotopy description.

## Limitations
The novelty comparison is literature-based rather than a proof that no unindexed source contains the same finite computation. The proof is finite and exhaustive for the specified graph and metric, but it does not generalize automatically to other generalized Petersen graphs. The acyclic matching is computationally verified rather than reduced here to a closed-form matching theorem.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, “Vietoris–Rips complexes of Platonic solids,” arXiv:2302.14388v1, first public 2023-02-28; later Innov. Incidence Geom. 21 (2024), DOI 10.2140/iig.2024.21.17.
2. Z. Feng, N. C. P. Nukala, “On Vietoris-Rips complexes of Finite Metric Spaces with Scale \(2\),” arXiv:2302.14664v1, first public 2023-02-28.
