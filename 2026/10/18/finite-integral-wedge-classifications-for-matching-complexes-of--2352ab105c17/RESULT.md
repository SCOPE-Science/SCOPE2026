# Finite integral wedge classifications for matching complexes of \(3\times n\) grids through width eight

## Finding
Let \(G_n=P_3\square P_n\), with vertices \((r,c)\) for \(0\le r<3\), \(0\le c<n\), adjacent when their Manhattan distance is one. Let \(\mathcal M(G_n)\) be the ordinary matching complex: vertices are graph edges, and simplices are matchings. For each integer \(2\le n\le8\), an exhaustive integral discrete-Morse certificate proves
\[
\mathcal M(G_n)\simeq\bigvee^{b_n}S^{n-1},\qquad
(b_2,b_3,b_4,b_5,b_6,b_7,b_8)=(2,5,9,16,31,55,94).
\]
This is **only a seven-width finite classification**; no assertion is made for \(n\ge9\), and the sphere counts themselves are not asserted to have been unknown.

## Assumptions and scope
Graphs are simple undirected Cartesian grids. Vertex labels are ordered pairs in row-major lexicographic order, edges are unordered endpoint pairs sorted lexicographically, and faces are subsets of pairwise vertex-disjoint graph edges. Every bit in a face mask corresponds to exactly one such graph edge. The complete augmented face poset includes the empty face; after pairing it with one vertex, the remaining matching is the ordinary face-poset matching needed for the CW construction. Only the specified integer widths are covered.

## Proof
**Exhaustive face generation.** Process the \(5n-3\) sorted graph edges in strictly increasing index order, selecting an edge only when both endpoints are unused. This recursively constructs each matching exactly once. No unknown face is inferred from a sample. The augmented face counts for \(n=2,3,4,5,6,7,8\) are respectively \(22,131,823,5096,31687,196785,1222550\).

**Elementary acyclic matchings for widths two through seven.** In increasing horizontal-edge order, followed by increasing vertical-edge order, toggle the chosen edge between every pair of still-unpaired incident faces. Toggling is applied only if both faces remain. The resulting matched-pair counts are respectively \(10,63,407,2540,15828,98365\). The only unmatched faces have dimension \(n-1\), numbering \(2,5,9,16,31,55\), respectively; the empty face is paired with a vertex. For each width, orient every matched Hasse cover upward and all other Hasse covers downward, and exhaustively topologically sort all face-poset vertices. The complete directed Hasse graph is acyclic. Deleting the empty-face pair leaves precisely one ordinary critical vertex and the given top cells; since there are no intermediate-dimensional cells, the Morse CW complex is the displayed wedge of spheres.

**The eighth width and its nontrivial attaching boundary.** Here toggle first the horizontal edges sorted by the parity of their left endpoint's column, then by column and row, followed by all vertical edges in increasing lexicographic order. Of the \(1222550\) augmented faces, \(611227\) pairs are matched; exactly \(95\) seven-faces and a single eight-face remain. The complete directed Hasse graph again admits a topological ordering. To compute the integral Morse differential, orient faces by increasing edge index; for each boundary seven-face of the unique critical eight-face, recursively eliminate matched seven-to-eight pairs with the signed unit-pivot rule. Matched upper seven-faces contribute zero. The resulting column is supported on exactly five critical seven-face masks, with exact signed entries
\[
(2753634376,1),\ (2755666018,1),\ (36509401192,-1),\ (36542940232,1),\ (36544987234,1).
\]
The second coordinate is the signed coefficient and the first is the integer face mask under the edge ordering above. Thus the integral attaching-degree column is primitive (its coefficients have greatest common divisor one). Since the Morse CW complex has one vertex, \(95\) seven-cells and one eight-cell, its eight-cell attaches to \(\bigvee^{95}S^7\) by a primitive element of \(\pi_7(\bigvee^{95}S^7)\cong\mathbb Z^{95}\). An integral change of wedge-sphere basis carries this element to a coordinate generator. Its cofiber is therefore \(\bigvee^{94}S^7\).

## Verification
The self-contained `grid3_morse_verify_full.py` constructs all faces, all matching pairs, and the complete directed Hasse graph for each width, checks the topological sort rather than sampling paths, and reconstructs the signed integral eighth-width boundary from the actual matching. The accompanying `grid3_morse_verify_output.txt` is its exact successful execution output. Reproduce with `python3 grid3_morse_verify_full.py` (standard library only). In particular, numerical mod-two homology alone would not certify this integral homotopy conclusion; the acyclic matching and signed attaching-degree calculation do.

## Relationship to prior work
Goyal, Shukla and Singh's 2021 paper originally asserted a much stronger all-width wedge theorem, but its proof of the nullhomotopy of several inclusions was subsequently found erroneous; the journal PDF is marked retracted, and the later correction discusses the failure of that argument. We do not use the unsupported original statement as a theorem. Chauhan, Sharma and Shukla's September 23, 2026 preprint establishes connectivity and homology concentration for all widths; its publicly accessible abstract does not assert these explicit certified integral finite homotopy decompositions. Independent published records about matching complexes of \(4\times4\) grids and equivariant Lefschetz numbers of \(3\times n\) grids concern different invariants and do not entail this finite homotopy classification.

## Limitations
No assertion for \(n\ge9\). The present result is a finite computationally certified homotopy classification, not an infinite recurrence, a minimal-cutoff theorem, or a claim that its Betti numbers were previously uncomputed. The complete text of the 2026 preprint could not be inspected; the potential presence there of an overlapping argument is a residual originality risk. Independent scientific audit has not been performed.

## References
1. P. Chauhan, A. Sharma, and S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366, first public September 23, 2026, https://arxiv.org/abs/2609.27366.
2. S. Goyal, S. Shukla, and A. Singh, *Matching complexes of \(3\times n\) grid graphs*, Electronic Journal of Combinatorics 28(4), P4.16 (2021), DOI 10.37236/10496, retracted/error notice in the publisher PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v28i4p16/pdf/.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
