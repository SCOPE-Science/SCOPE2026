# The four-by-four grid perfect-matching complex is a mixed-dimensional sphere wedge

## Finding
Let \(G=P_4\square P_4\) be the ordinary Cartesian square grid with four vertices on each side. Define \(\mathcal P(G)\) to be the simplicial complex whose vertices are edges belonging to at least one perfect matching of \(G\), and whose simplices are exactly the edge sets extendable to a perfect matching. Then
\[
\mathcal P(P_4\square P_4)\simeq S^2\vee S^2\vee S^3.
\]
In particular, \(\widetilde H_2(\mathcal P(G);\mathbb Z)\cong\mathbb Z^2\), \(\widetilde H_3(\mathcal P(G);\mathbb Z)\cong\mathbb Z\), all other reduced integral homology groups vanish, and \(\mathcal P(G)\) is not shellable.

## Assumptions and scope
The four-by-four *grid* means \(P_4\square P_4\), not a torus, a complete bipartite graph, or the graph \(Q_4\). Its 16 graph vertices are \((r,c)\) with \(r,c\in\{1,2,3,4\}\); edges connect vertices differing by one in exactly one coordinate. There are 24 graph edges and 36 perfect matchings. Every perfect matching contains eight edges, so the perfect-matching complex is pure of dimension seven. This is the perfect-matching subcomplex, **not** the ordinary matching complex, which also includes nonextendable matchings.

Edges are indexed \(0,\ldots,23\) by iterating \((r,c)\) in row-major order, placing the downward edge \((r,c)(r+1,c)\), if any, first, followed by the rightward edge \((r,c)(r,c+1)\), if any. A simplex is represented by the bitmask of its edge indices; the empty face has mask zero. All certificates and assertions below are checked by the included standalone program `check_4x4_perfect_matching.py`, which uses only Python's standard library.

## Proof
**Enumeration and a finite acyclic discrete-Morse field.** Enumerate perfect matchings recursively, choosing the least unmatched graph vertex and pairing it with each currently unmatched neighbor. The resulting 36 maximal eight-edge faces generate exactly 5,407 faces including the empty face, with augmented face-size vector
\[
(1,24,212,796,1516,1596,938,288,36).
\]
In the augmented face poset apply vertex-toggle matchings successively at edge indices
\[
(21,14,0,1,23,20,12,4).
\]
At each stage, on all *remaining* faces, pair a face missing the chosen edge with its union with that edge whenever both remain, and then remove those pairs. This creates 2,702 disjoint cover pairs and leaves exactly three unmatched nonempty faces: two triangles indexed \(\{9,11,14\}\) and \(\{10,14,17\}\), and one tetrahedron indexed \(\{1,4,14,20\}\). The empty face is paired. To verify the essential acyclicity lemma rather than assume that greedy matching is acyclic, orient every one of the 24,812 Hasse cover incidences downward except the matched incidences, which are oriented upward. The provided checker performs complete directed topological sorting and verifies that all 5,407 face-poset nodes are removed. Consequently discrete Morse theory provides a CW model with one base vertex, two two-cells and one three-cell, with no one-cells.

**Integral obstruction to a nonzero three-cell boundary.** Independently of the Morse pairing, perform ordinary elementary simplicial collapses: at each step choose the free face of greatest dimension, breaking ties by lowest face bitmask, where a free face has exactly one immediate coface. Delete it and its coface, and repeat. The checker tests free-face uniqueness at every deletion. Exactly 2,628 elementary pairs collapse, leaving a 3-dimensional simplicial complex with face vector \((14,49,62,25)\). For its 25 oriented tetrahedra in increasing bitmask order, use the integral coefficient vector
\[
(1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1).
\]
Direct signed boundary expansion over the integers is zero; the vector is nonzero. The full third boundary matrix of the collapsed complex has rank 24 over \(\mathbb F_2\), verified by complete binary Gaussian elimination. Its rank over \(\mathbb Q\) is therefore at least 24, while the displayed exact nonzero integral kernel vector makes it at most 24. Thus the top reduced rational homology has rank one, and this remains true for the original complex by the elementary collapses.

**Homotopy conclusion.** In the Morse CW model the attaching matrix of its only three-cell is a column in \(\mathbb Z^2\). If that column were nonzero, third rational homology would vanish. The independently verified one-dimensional third rational homology forces the *integral* attaching column to be zero. The two-skeleton is \(S^2\vee S^2\); it is simply connected, and the Hurewicz isomorphism \(\pi_2\cong H_2\) identifies a three-cell attaching map with this integer column. Hence the attaching map is null-homotopic and the complex has the claimed wedge homotopy type. The complex is pure of dimension seven but has nonzero reduced homology in dimension two, precluding pure shellability.

## Verification
Run `python check_4x4_perfect_matching.py`. It reproduces every perfect matching and every face, builds and fully checks the acyclic matching Hasse digraph, verifies each elementary simplicial collapse, checks the two successive chain-boundary compositions are zero, and verifies the integral top cycle and ranks \((13,36,24)\) of the collapsed first, second and third boundary maps modulo two. The final output marker is `MORSE_AND_EXACT_TOP_CYCLE_GRID_4X4_OK`. Its exact integral top-cycle calculation, combined with the mod-two third-boundary rank and the acyclic matching, is a proof for this finite complex, not a numerical homology extrapolation.

## Relationship to prior work
Chandrakar and Singh's 2024 preprint (arXiv:2407.05809, subsequently revised in 2025) classifies the perfect-matching complex for \(2\times n\) rectangular grids, not \(4\times4\), and explicitly proposes the wedge-of-spheres problem for general rectangular grids in Conjecture 6.1. The present calculation verifies that conjecture for the first fully square \(4\times4\) example and identifies a wedge spanning two homological degrees; it does not imply the conjecture in general. Bayer, Jelić Milutinović and Vega study honeycomb rather than square grids. Results concerning the **ordinary** matching complex of \(P_4\square P_4\) cannot determine its perfect-matching subcomplex, since the face sets differ substantially.

## Limitations
The assertion is specific to \(P_4\square P_4\). It neither establishes a recurrence for larger grids nor classifies all \(3\times n\) grids. The exact verification is a finite combinatorial certificate, with a checker and an explicit integral top-cycle witness, and has not received independent mathematical review. Bibliographic novelty is assessed against the identified literature, with a residual possibility of equivalent work elsewhere.

## References
1. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first public version July 8, 2024, especially Theorem 1.1 and Conjecture 6.1, https://arxiv.org/abs/2407.05809.
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803, first public version September 6, 2022, https://arxiv.org/abs/2209.02803.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; discrete Morse theory for acyclic face pairings.
