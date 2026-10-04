# The dodecahedral independence complex is a wedge of four 5-spheres
## Finding
Let \(D\) be the dodecahedral graph, presented as the generalized Petersen graph \(GP(10,2)\): its vertices are \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), and its edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). Then
\[
\operatorname{Ind}(D)\simeq\bigvee^{4} S^5.
\]
Here \(\operatorname{Ind}(D)\) is the simplicial complex of independent vertex sets of \(D\).

## Assumptions and scope
The graph is the 20-vertex, 30-edge dodecahedral graph in the explicit \(GP(10,2)\) labeling above. The statement concerns the ordinary independence complex, with the empty face included combinatorially. It is a homotopy-equivalence statement; no claim is made about a particular geometric embedding of the dodecahedron, equivariant homotopy type, or a family \(GP(n,k)\).

## Proof
Enumerating all independent sets of the displayed graph gives 5,828 faces including the empty face. The numbers of nonempty faces by cardinality \(1,\ldots,8\) are
\[
20,160,660,1510,1912,1240,320,5.
\]

On the nonempty face poset, order the graph vertices as \(u_0,\ldots,u_9,v_0,\ldots,v_9\), encoded as \(0,\ldots,19\). Starting with every nonempty face unmatched, process these vertices in order. At vertex \(x\), pair every still-unmatched face \(\sigma\) not containing \(x\) with \(\sigma\cup\{x\}\) whenever the latter is also a still-unmatched face. This produces 2,911 matched cover pairs.

The resulting matching has exactly five critical faces: the vertex \(\{0\}\) and the four 5-simplices
\[
\{3,8,10,11,15,16\},\quad
\{4,9,11,12,16,17\},\quad
\{2,7,10,14,15,19\},\quad
\{1,6,13,14,18,19\}.
\]
The accompanying verifier constructs the complete Hasse diagram on all 5,827 nonempty faces, reverses precisely the 2,911 matched cover relations, and checks by a topological sort that the resulting 27,620-edge directed graph is acyclic. Thus this is an acyclic discrete-Morse matching.

The discrete-Morse theorem gives a CW complex homotopy equivalent to \(\operatorname{Ind}(D)\) with one 0-cell and four 5-cells and no other cells. Each 5-cell therefore attaches to the 0-skeleton by the constant map, so the CW complex is \(\bigvee^4 S^5\).

## Verification
Run `python3 verify_dodecahedron_independence.py`. It reconstructs \(GP(10,2)\) from the edge formula, exhaustively enumerates all \(2^{20}\) vertex subsets, verifies the face vector and all matching cover relations, builds the complete oriented Hasse graph, proves acyclicity by exhausting a topological ordering, checks the critical cells, and checks Euler characteristic \(\chi=-3\). A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Berghoff's 2020 paper develops algebraic-topological machinery for independence complexes and explicitly computes examples including the Petersen graph and the cubical graph; its primary MSC classification is 55U10. The full text contains no dodecahedral or generalized-Petersen calculation. Goyal--Shukla--Singh (2019) use discrete Morse theory to obtain wedge decompositions for different graph families (categorical products of complete graphs and generalized Mycielskians), not \(GP(10,2)\). Targeted literature and semantic-database searches under the aliases “dodecahedral graph” and “generalized Petersen \(G(10,2)\)” found no statement implying the displayed homotopy type. This search evidence supports originality but cannot establish absolute novelty.

## Limitations
The proof is graph-specific and finite. It does not classify independence complexes of all Platonic graphs or generalized Petersen graphs. The acyclicity step is exhaustively machine-checked rather than replaced here by a short symbolic characterization of every gradient path. Unindexed or differently phrased prior computations remain a residual literature risk.

## References
1. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, first submitted 2020-08-14. Primary MSC 55U10.
2. S. Goyal, S. Shukla, A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, first submitted 2019-05-16.
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90--145.
