# The Heawood two-matching complex is a wedge of six 10-spheres
## Finding
Let \(H\) be the Heawood graph, realized as the point-line incidence graph of the Fano plane: the point vertices are \(p_j\), the line vertices are \(\ell_i\), and \(p_j\) is adjacent to \(\ell_i\) exactly when \(j-i\pmod 7\in\{0,1,3\}\). Let \(M_2(H)\) be the simplicial complex whose vertices are the edges of \(H\) and whose faces are edge sets in which every graph vertex has degree at most \(2\). Then
\[
M_2(H)\simeq \bigvee^{6} S^{10}.
\]

## Assumptions and scope
The graph is finite and simple, and the complex uses the standard higher-matching convention: an edge subset is a face exactly when the induced spanning subgraph has maximum degree at most \(2\). The statement concerns only this Heawood graph and this value of the matching parameter.

## Proof
Order the \(21\) graph edges lexicographically in the explicit Fano-incidence presentation above. Exhaustive enumeration gives \(447859\) nonempty faces with face vector
\[
(21,210,1316,5733,18228,43246,76968,101892,98042,65730,28560,7091,798,24).
\]
Apply successive element-toggle matchings in that edge order. Repeated element matching is acyclic by the standard patchwork/cluster-lemma construction. The exhaustive matching has \(223925\) pairs and leaves precisely one critical \(0\)-cell, one critical \(9\)-cell, and seven critical \(10\)-cells.

Using the natural orientation from the same edge order, algebraic Morse elimination gives the boundary from the seven critical \(10\)-cells to the unique critical \(9\)-cell as
\[
(1,1,0,0,0,-1,1).
\]
This row is primitive. Thus the Morse CW model is the cofiber of a map \(\bigvee^7 S^9\to S^9\) whose degree vector is primitive. A unimodular change of basis on \(\bigvee^7 S^9\) sends that vector to \((1,0,0,0,0,0,0)\). The degree-one summand forms a contractible \(9\)-/\(10\)-cell pair, and the six remaining top cells give \(\bigvee^6 S^{10}\).

## Verification
The standalone verifier `verification/heawood_m2_verify.py` reconstructs the graph and all faces, recomputes the complete repeated-toggle matching, checks the critical-cell counts, evaluates the signed Morse boundary recursively, checks that its entries have greatest common divisor \(1\), and confirms the Euler characteristic \(7\). Running it prints `HEAWOOD_M2_VERIFY_OK`.

## Relationship to prior work
Vega's paper on two-matching complexes defines \(M_2(G)\), develops repeated-toggle discrete Morse methods, and studies clawed graphs, wheel graphs, and perfect caterpillar graphs. Singh's later paper on higher matching complexes states that exact homotopy types are known for only a few graph classes and proves formulas for complete graphs and complete bipartite graphs. The Heawood graph is cubic and bipartite but not complete bipartite, so those theorems do not imply the result here. Searches for “Heawood graph 2-matching complex”, “Heawood higher matching complex”, and the bounded-degree-complex alias located no published statement of this homotopy type.

## Limitations
This is a finite exact computation for one named graph, not a family theorem. The originality comparison covers the primary two-matching and higher-matching papers inspected, targeted exact-phrase web searches, and the indexed mathematical-record search described in the review; a differently indexed computation could remain undiscovered. No independent audit has been performed.

## References
1. Julianne Vega, *2-Matching Complexes*, arXiv:1909.10406v1, first public version 2019-09-23.
2. Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632v1, first public version 2020-06-24.
3. MSC2020, \(55P15\): classification of homotopy type.
