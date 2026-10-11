# The Grötzsch graph matching complex is a wedge of twenty-four three-spheres

## Finding
Let \(G=\mu(C_5)\) denote the eleven-vertex Grötzsch graph, obtained by applying the ordinary Mycielski construction to the five-cycle. If \(\mathcal M(G)\) is the simplicial complex whose simplices are matchings (pairwise vertex-disjoint sets of graph edges), then
\[\mathcal M(G)\simeq\bigvee^{24}S^3.\]
In particular, \(\widetilde H_3(\mathcal M(G);\mathbb Z)\cong\mathbb Z^{24}\), and all other reduced integral homology groups vanish. The assertion is a homotopy equivalence, not merely a statement about homology.

## Assumptions and scope
The graph has labeled vertices \(\{0,1,\dots,10\}\). Original five-cycle vertices are \(0,\dots,4\), clone vertices are \(5,\dots,9\), and \(10\) is the apex. For every \(i\in\{0,1,2,3,4\}\), with indices of original vertices taken modulo five, add the edge \(\{i,i+1\}\), the two edges \(\{5+i,i-1\}\) and \(\{5+i,i+1\}\), and \(\{5+i,10\}\). This produces exactly twenty distinct edges. Only ordinary matchings of distinct edges are allowed. The statement concerns this graph only, not arbitrary Mycielski graphs, and not the independence complex of \(G\) itself.

## Proof
Write the twenty graph edges in lexicographic order and represent a simplex by its increasing tuple of edge indices. Explicit enumeration of every admissible tuple gives the face vector
\[(f_0,f_1,f_2,f_3,f_4)=(20,135,365,360,87),\]
with no simplices in dimension greater than four.

Apply the following deterministic partial matching to the **nonempty** face poset. For edge index \(v=0,\dots,19\) successively, list remaining faces not containing \(v\) by increasing size and then lexicographic order. Whenever both \(\sigma\) and \(\sigma\cup\{v\}\) are remaining simplices, pair them and remove both. The resulting matching has 466 pairs, leaving exactly one critical zero-simplex, five critical two-simplices, and twenty-nine critical three-simplices.

To verify this is an acyclic discrete-Morse matching, orient every cover relation in the face-poset Hasse graph downwards except matched relations, oriented upwards. A complete topological sort visits all 968 faces when the empty face is included; its 3,260 directed incidences contain no cycle. Therefore the matching admits a Morse CW complex of the stated critical-cell inventory.

Compute its integral signed boundary between the 29 critical three-cells and the five critical two-cells by eliminating all matched face pairs. The oriented simplicial boundary is \(\partial[v_0,\dots,v_k]=\sum_{j=0}^k(-1)^j[v_0,\dots,\widehat v_j,\dots,v_k]\). The accompanying verifier implements the elimination recurrence with memoization and constructs the entire \(5\times29\) integer boundary matrix. Taking its columns of **zero-based indices** \((2,3,4,12,18)\) gives a \(5\times5\) minor with determinant \(-1\). Consequently the boundary is integrally split-surjective: all five nonzero Smith invariant factors are units.

The Morse two-skeleton is a wedge of five two-spheres. The 29 three-cell attaching classes therefore lie in \(\pi_2(\bigvee^5 S^2)\cong\mathbb Z^5\) and are completely described by the signed integral boundary matrix. A unimodular change of three-cell generators followed by cellular cancellation removes five pairs of two- and three-cells. The remaining 24 three-cells attach to the point, yielding \(\bigvee^{24}S^3\). No assertion about a higher-dimensional family follows from this finite calculation.

## Verification
Run `python3 verify_grotzsch.py` and `python3 check_homology.py` from the extracted package, using Python standard libraries only. The first enumerates all faces, checks the global matching acyclicity, reconstructs the signed Morse differential and independently evaluates the displayed determinant. The second uses a different recursive face enumeration and computes simplicial boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). The calculated ranks in degrees one to four are \((19,116,249,87)\) in each field, compatible with reduced third Betti number 24. These field checks are corroborative; the integral minor and Morse argument prove the homotopy statement.

## Relationship to prior work
Engström's foundational connectivity results for independence complexes of claw-free graphs apply generally to line graphs, but do not calculate this exact matching-complex homotopy type. Donovan and Scoville's star-cluster treatments determine matching-complex homotopy types for particular paths, cycles and other graph constructions, not the ordinary Mycielski transform of the five-cycle. The outerplanar-graph theorem of Bayer, Jelić Milutinović and Vega does not cover the nonplanar Grötzsch graph. Results on independence complexes of Mycielski graphs concern a different simplicial complex: \(\mathcal M(G)=\operatorname{Ind}(L(G))\), not \(\operatorname{Ind}(G)\).

## Limitations
This is a finite, self-contained graph calculation with a complete combinatorial verifier, not a theorem about all Mycielski constructions. Independent scientific validation has not been performed. The cited sources and searches do not rule out equivalent work in unindexed or inaccessible literature. The scripts test exactly the specified eleven-vertex graph; they are not proofs of a result for infinite graph families.

## References
1. Alexander Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420, first public version 17 December 2005, primary MSC 57M15.
2. Connor Donovan and Nicholas Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780.
3. Margaret Bayer, Zorana Jelić Milutinović, and Julianne Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601.
4. Jonathan A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418 (related independence-complex methodology; not a covering matching-complex theorem).
