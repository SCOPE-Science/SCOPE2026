# A mixed-dimensional sphere wedge for the Möbius–Kantor induced-forest complex

## Finding

Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph. The **vertex-induced forest complex** \(\mathcal F(M)\), whose faces are precisely the vertex subsets inducing acyclic subgraphs, has the complete integral homotopy type

\[\boxed{\mathcal F(M)\simeq\bigvee^{25}S^9\vee\bigvee^4 S^{10}.}\]

In particular, \(\widetilde H_9(\mathcal F(M);\mathbb Z)\cong\mathbb Z^{25}\), \(\widetilde H_{10}(\mathcal F(M);\mathbb Z)\cong\mathbb Z^4\), and all other reduced integral homology groups vanish. The mixed-dimensional structure is essential: the complex cannot be homotopy equivalent to a wedge of spheres in a single dimension.

## Assumptions and scope

The sixteen vertices are \(u_0,\ldots,u_7,v_0,\ldots,v_7\), with subscripts modulo eight. The 24 edges are all \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), for \(0\leq i<8\). A nonempty face is a vertex set \(S\) for which the induced graph \(M[S]\) has no cycles. This is the vertex-induced forest complex, not the edge-set graphic-matroid complex and not the ordinary independence complex. The result is only for this finite graph; it asserts neither a generalized-Petersen infinite-family formula nor an equivariant splitting.

## Proof

**Finite face identification.** Encode a subset of the sixteen vertices by the integer obtained from its indicator bitmask, where \(u_i\) occupies bit \(i\) and \(v_i\) bit \(i+8\). An induced subgraph is acyclic exactly when union–find on its internal edges never encounters an edge whose endpoints are already connected. An independent traversal gives the equivalent criterion that its number of induced edges equals the number of selected vertices minus the number of connected components. Both methods agree for every subset. The complex has 50,996 nonempty simplices; the face counts in dimensions zero through ten are

\[(16,120,560,1820,4368,7984,11200,11792,8672,3792,672).\]

**Discrete Morse matching.** Starting with all nonempty faces unmatched, for \(i=0,\ldots,15\), pair every as-yet-unmatched face \(S\) not containing bit \(i\) with \(S\cup\{i\}\), whenever that face also remains unmatched, visiting lower masks in ascending order at each stage. The complete, deterministic matching contains 25,475 pairs. The unmatched faces consist of one vertex, eight eight-dimensional faces, 33 nine-dimensional faces, and four ten-dimensional faces. To verify the nonstandard acyclicity premise, direct each face-poset covering relation downward, except a matched covering relation is directed upward. A topological sort visits every one of the 50,996 face vertices through all 375,040 directed covering relations. Hence the matching is acyclic, and discrete Morse theory supplies a homotopy-equivalent CW complex with exactly those critical cells.

**Integral attaching degrees.** Orient each simplex by increasing bit index. For a lower matched face \(s\) paired with the upper face \(t\), with incidence \(\epsilon=[t:s]\in\{\pm1\}\), recursively project \(s\) to critical cells by \(P(s)=-\epsilon\sum_{w\neq s}[t:w]P(w)\); matched upper faces project to zero, and critical faces project to themselves. The acyclic matching makes this recursive signed gradient reduction well-founded. Applying this projection to oriented boundaries of critical faces yields a Morse boundary \(B_9\) with eight rows and 33 columns, and a boundary \(B_{10}\) with 33 rows and four columns. The latter is the zero matrix. The eight columns of \(B_9\) with zero-based indices \((21,3,2,1,5,10,12,18)\) form an integer matrix with determinant \(-1\). The exact entries and their computation are included in `verify.py` and `verification_output.txt`. This unit minor implies the map \(B_9:\mathbb Z^{33}\to\mathbb Z^8\) is onto and its kernel is a free group of rank 25. Because \(B_{10}=0\), the Morse chain complex has free reduced homology of ranks 25 in degree nine and four in degree ten, and none in other degrees.

**From cellular degrees to homotopy.** The Morse CW model has one zero-cell and no cells in dimensions one through seven. Its eight-skeleton is \(\bigvee^8 S^8\). Since \(\pi_8(\bigvee^8S^8)\cong\mathbb Z^8\), the entire set of nine-dimensional attaching maps is determined by \(B_9\), not merely their homology classes. The unit minor allows eight cellular 8–9 cancellations, leaving a nine-skeleton homotopy equivalent to \(\bigvee^{25}S^9\). The ten-cell attaching maps then lie in \(\pi_9(\bigvee^{25}S^9)\cong\mathbb Z^{25}\) and are determined by their degree vectors. The unchanged zero tenth Morse boundary makes all four maps null-homotopic. They therefore attach four ten-spheres freely, proving the displayed integral homotopy equivalence.

## Verification

Run `python3 verify.py` with the ordinary Python 3 standard library. It constructs the graph and both independent forest-membership tests, exhausts all nonempty vertex subsets, constructs the matching, checks every modified Hasse edge for acyclicity, evaluates the exact signed Morse boundary matrices, asserts the stated unit minor and the all-zero upper differential, and checks the Euler characteristic. The recorded stdout is `verification_output.txt`. The final line is `MOBIUS_KANTOR_INDUCED_FOREST_CERTIFICATE_PASS`. The program performs an exhaustive calculation for this finite graph, rather than using finite examples as evidence for a claim about an infinite family.

## Relationship to prior work

Taylan's 2015 paper formulates devoid complexes \(\mathcal D(G;\mathcal A)\) for arbitrary forbidden graph families; choosing all cycles recovers the induced-forest complex. Taylan's explicit homotopy classifications concern path-/cycle-base instances and forests with forbidden three-vertex paths, not the Möbius–Kantor induced-forest complex. Carnero Bravo's forest-filtration work studies this same vertex-induced forest object and establishes classifications for paths, cycles, cactus graphs, multipartite graphs and selected graph operations; these do not determine the present cubic, non-cactus instance. The earlier result on the ordinary Möbius–Kantor independence complex concerns independent vertex subsets rather than cycle-free induced subsets; the matching complex is an edge-subset complex, also different. The exact mixed-dimensional ranks and integer attaching-map calculation are the specific contribution here.

## Limitations

This is a finite, self-contained integral homotopy computation for one canonical sixteen-vertex graph. Neither the action of graph automorphisms on integral homology nor a family-wide formula is determined. The exhaustive certificate is computational, with explicitly defined graph, faces, matching, and signed incidences. Definitive publication-priority determination and independent mathematical review remain outstanding.

## References

- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first public 2015-01-27. https://arxiv.org/abs/1501.06754
- A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first public 2023-07-25. https://arxiv.org/abs/2307.13271
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145. Discrete Morse theorem used after an explicit verified acyclic matching.
