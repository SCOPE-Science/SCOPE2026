# The first conjectured non-word-representable simplified de Bruijn graph is 3-colourable
## Finding
Let \(S(n,k)\) be the simplified de Bruijn graph whose vertices are the length-\(n\) words over the alphabet \(\{0,1,\ldots,k-1\}\). Two distinct vertices are adjacent when one is obtained from the other by deleting its first symbol and appending one symbol, after directions, loops, and multiple edges are discarded.

Then
\[
\chi(S(4,3))=3.
\]
In particular, \(S(4,3)\) is word-representable, because every \(3\)-colourable graph is word-representable. Therefore \(S(4,3)\) refutes the conjecture that \(S(n,k)\) is non-word-representable for all \(n\ge4\) and \(k\ge3\).

## Assumptions and scope
The parameter convention is the one used in the cited simplified-de-Bruijn literature: \(n\) is word length and \(k\) is alphabet size. Thus \(S(4,3)\) has \(3^4=81\) vertices.

The conclusion uses the standard theorem that every \(3\)-colourable graph is word-representable. No converse is assumed.

## Proof
The bundled certificate assigns one of three colours to each of the \(81\) words in \(\{0,1,2\}^4\). Reconstructing the simplified de Bruijn adjacency relation gives exactly \(237\) undirected edges after loops and duplicate directed overlaps are removed. Direct verification shows that every one of these \(237\) edges has differently coloured endpoints. Hence
\[
\chi(S(4,3))\le3.
\]

For the reverse inequality, the vertices
\[
0000,\qquad0001,\qquad1000
\]
are pairwise adjacent: \(0000\) overlaps \(0001\), \(0000\) overlaps \(1000\) in the reverse direction, and \(0001\) overlaps \(1000\) because the suffix \(000\) of \(1000\) is the prefix \(000\) of \(0001\). They form a triangle, so
\[
\chi(S(4,3))\ge3.
\]
Thus \(\chi(S(4,3))=3\).

Huang, Kitaev, and Pyatkin quote the fundamental implication that every \(3\)-colourable graph is word-representable. It follows immediately that \(S(4,3)\) is word-representable. Since \(n=4\) and \(k=3\), this is the smallest parameter pair in the region of Petyuk's conjecture and is a counterexample to that conjecture.

## Verification
Run `python3 verify.py` beside `coloring.json`. The verifier reconstructs all \(81\) vertices and all \(237\) simplified de Bruijn edges from the definition rather than trusting an edge list. It checks the complete colouring certificate, obtains colour-class sizes \(28,30,23\), and separately verifies the triangle \(0000,0001,1000\).

The finite certificate proves the graph-colouring statement exhaustively. Word-representability is then a theorem-level consequence of \(3\)-colourability; no search over representing words is required.

## Relationship to prior work
Petyuk introduced the simplified de Bruijn graphs in the word-representability setting, proved that \(S(n,2)\) is word-representable for every \(n\), proved that \(S(2,k)\) and \(S(3,k)\) are non-word-representable for \(k\ge3\), and conjectured that \(S(n,k)\) is non-word-representable for all \(n\ge4\) and \(k\ge3\).

Huang, Kitaev, and Pyatkin subsequently restated that conjecture and studied word-representability of induced subgraphs \(S_m(n,k)\). Their full text explicitly gives both the implication from \(3\)-colourability to word-representability and the conjecture for the full graph. Their positive theorems concern restricted induced subgraphs and do not cover the full \(S(4,3)\).

Targeted database and web searches for \(S(4,3)\), exact \(3\)-colourability, and counterexamples to the conjecture did not locate a prior statement of this colouring. A current problem database still labels the conjecture open. These searches support non-coverage but cannot rule out an unindexed computation or note.

## Limitations
This result refutes the universal conjecture with its first parameter pair; it does not classify \(S(n,k)\) for any other pair. A proper \(3\)-colouring proves word-representability but does not determine the representation number or exhibit a shortest representing word.

The originality assessment retains a residual risk that an unpublished or unindexed colouring of \(S(4,3)\) exists.

## References
1. A. V. Petyuk, “On word-representability of simplified de Bruijn graphs,” arXiv:2210.14762, first public version 2022-10-20.
2. S. Huang, S. Kitaev, and A. Pyatkin, “An embedding technique in the study of word-representability of graphs,” Discrete Applied Mathematics 346 (2024), 170–182, DOI 10.1016/j.dam.2023.12.017; arXiv:2312.10377.
3. T. Dwary and K. V. Krishna, “Word-representability of graphs with respect to split recomposition,” Discrete Applied Mathematics (2024), DOI 10.1016/j.dam.2024.06.022. The bibliographic record classifies the topic under MSC \(68R10\).
