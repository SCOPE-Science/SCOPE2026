# Two sphere classes and full symmetry of the Tietze independence complex

## Finding
Let \(T\) be Tietze's twelve-vertex cubic graph, obtained by replacing one vertex of the Petersen graph by a triangle and attaching its three former neighbors to the three triangle vertices. Its ordinary independence complex satisfies the integral homotopy equivalence
\[
\operatorname{Ind}(T)\simeq S^2\vee S^2.
\]
The full automorphism group is \(G\cong S_2\times S_3\), where \(S_2\) permutes the two labels defining the replaced Petersen vertex and \(S_3\) permutes the other three labels. The complete rational second-homology representation is
\[
\widetilde H_2(\operatorname{Ind}(T);\mathbb Q)\cong
\operatorname{sgn}_{S_3}\boxtimes(\mathbf1_{S_2}\oplus\operatorname{sgn}_{S_2}).
\]
Thus a three-label transposition reverses both homology classes, while the independent two-label transposition has one even and one odd eigendirection. No nonzero second-homology class is fixed by all graph automorphisms.

## Assumptions and scope
Index the ten Petersen vertices by the two-element subsets of \(\{0,1,2,3,4\}\); two are joined exactly when they are disjoint. Remove \(\{0,1\}\), whose three neighbors are \(\{2,3\},\{2,4\},\{3,4\}\). Add a three-clique with vertices indexed by these neighbors and attach each new vertex to its indexed former neighbor. This defines \(T\) without using an embedding. An independence-complex simplex is a nonempty set of graph vertices containing no edge; integral statements concern the geometric realization.

## Proof
The graph has \(12\) vertices and \(18\) edges and a unique triangle, the replacement triangle. The verifier enumerates all \(177\) nonempty independent simplices; the face vector in dimensions \(0\) through \(4\) is
\[
(12,48,75,39,3).
\]
Represent each face by its twelve-bit membership mask. In increasing order of masks, successively toggle vertex indices
\[
(6,2,10,11,7,5,1,4,9,0,8,3).
\]
At each stage, match every still-unmatched face missing the current vertex with its union with that vertex, whenever both are still unmatched. Exactly \(87\) face pairs are formed. The only unmatched masks, with dimensions in parentheses, are \(64\) (dimension \(0\)), \(388\) (dimension \(2\)), and \(2096\) (dimension \(2\)). Reversing the matched edges in the full face-poset Hasse diagram leaves an acyclic directed graph; this is checked directly by a complete topological sort of its \(177\) nodes. Forman's acyclic-matching theorem therefore produces a CW complex with one zero-cell, two two-cells and no other cells. Both two-cell attaching maps are constant, proving the integral wedge of two two-spheres.

The unique triangle is characteristic. Contracting it back to a vertex identifies every automorphism of \(T\) with an automorphism of the Petersen graph stabilizing \(\{0,1\}\). Since \(\operatorname{Aut}(KG(5,2))=S_5\), this stabilizer is exactly \(S_2\times S_3\) of order \(12\), and every such permutation extends uniquely across the replacement triangle. For each \(g=(\alpha,\beta)\in S_2\times S_3\), the verifier enumerates oriented fixed simplices and their orientation signs. The resulting signed simplicial Lefschetz number is
\[
L(g)=1+\operatorname{sgn}(\beta)\bigl(1+\operatorname{sgn}(\alpha)\bigr).
\]
Because the only nonzero unreduced rational homology groups are \(H_0\cong\mathbb Q\) and \(H_2\cong\mathbb Q^2\), the Lefschetz formula yields
\[
\chi_{H_2}(\alpha,\beta)=\operatorname{sgn}(\beta)\bigl(1+\operatorname{sgn}(\alpha)\bigr).
\]
This is the character of the displayed direct sum. Character equality identifies rational representations by Maschke semisimplicity.

## Verification
Run `python3 verify.py` using the Python standard library. The program rebuilds the Petersen graph from disjoint two-subsets, constructs \(T\), proves uniqueness of its graph triangle, enumerates every independent face, checks all \(87\) Morse pairs and the acyclicity of every reversed Hasse arrow, constructs all \(12\) induced automorphisms from \(S_2\times S_3\), and verifies the signed Lefschetz-character identity element by element. Exact output begins `VERIFY_OK`. Neither modular sampling nor an unverified computational log is used in place of these finite exhaustive checks.

## Relationship to prior work
Barmak's star-cluster theorem (Theorem 3.4 in the cited 2010 preprint) shows that an independence complex is a suspension when its graph has a vertex on no triangle, as \(T\) does. That theorem neither identifies the two sphere summands for \(T\) nor gives the representation of its full symmetry group. The Tietze graph is the classical nonhamiltonian cubic graph obtained by replacing one Petersen vertex by a triangle; its graph-theoretic characterization does not imply the asserted simplicial homotopy type or symmetry character. The corresponding Petersen graph, its higher-independence complex and various other twelve-vertex cubic graphs have also been studied; their topological results do not determine the invariants of this vertex-replacement graph.

## Limitations
This is a statement about exactly the Tietze graph and ordinary independence complexes, not arbitrary snarks or all Petersen vertex replacements. The rational representation statement does not claim an integral splitting of the rank-two homology lattice. The finite computation establishes the stated homotopy and rational character; it does not establish publication priority. Special-purpose unindexed calculations remain a residual originality risk. No independent scientific audit has been performed.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02, especially Theorem 3.4.
2. E. W. Weisstein, *Tietze Graph*, MathWorld, https://mathworld.wolfram.com/TietzeGraph.html (graph construction and canonical graph properties).
3. H. Tietze, *Einige Bemerkungen zum Problem des Kartenfärbens auf einseitigen Flächen*, 1910 (historical graph origin; a precise public day of that publication is not asserted).
