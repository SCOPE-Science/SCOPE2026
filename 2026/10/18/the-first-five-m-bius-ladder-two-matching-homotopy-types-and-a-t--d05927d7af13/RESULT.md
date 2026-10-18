# The first five Möbius-ladder two-matching homotopy types and a three-sphere spike

## Finding
For the cubic Möbius ladder \(L_n\) defined below, the first five nontrivial two-matching complexes have **integral homotopy types**
\[
\begin{aligned}
M_2(L_3)&\simeq S^3,\\
M_2(L_4)&\simeq S^5,\\
M_2(L_5)&\simeq S^7,\\
M_2(L_6)&\simeq \bigvee^3 S^8,\\
M_2(L_7)&\simeq S^9.
\end{aligned}
\]
The triple wedge at \(n=6\) is the first nonsingle-sphere term and is followed by a single sphere at \(n=7\). The starting \(n=3\) term is included to specify the natural sequence; it is already covered by Singh's complete-bipartite theorem. The subsequent four exact homotopy classifications are the contribution here.

## Assumptions and scope
For every integer \(3\le n\le7\), set \(V(L_n)=\mathbb Z/(2n)\) and
\[
E(L_n)=\{\{i,i+1\}:i\in \mathbb Z/(2n)\}\cup \{\{i,i+n\}:0\le i<n\}.
\]
Indices are reduced modulo \(2n\). The \(3n\) edges are placed in lexicographic order as unordered pairs. The vertices of \(M_2(L_n)\) are these edges; a subset is a face if **every vertex of the selected-edge subgraph has degree at most two**. The empty face is included. The result is a statement of nonequivariant integral homotopy equivalence, not a complete family theorem.

## Proof
Encode a set of selected graph edges by a bitmask \(F\in[0,2^{3n})\). Membership is decided by intersecting \(F\) with the incidence masks of the \(2n\) graph vertices and checking that each intersection contains at most two selected edges. Independently, because the graphs are cubic, a mask is invalid exactly when it contains all three edges incident to some graph vertex.

Construct a finite matching on the augmented face poset by scanning edge-bit positions in increasing order. At position \(b\), for every still-unmatched face \(F\) not containing \(b\), pair it with \(F\cup\{b\}\) if the latter is a still-unmatched face. Thus each pair differs by one edge and has incidence coefficient a unit. Delete the pair consisting of the empty face and a singleton to obtain the standard (nonaugmented) Morse matching with one extra critical vertex. The accompanying program generates *every* face and pair from these rules and verifies that the full directed Hasse diagram, with matched incidences reversed, is acyclic by topological sorting; this is an exact discrete-Morse certificate, rather than an inference from ranks.

The complete finite counts, including the empty face, are:

| \(n\) | Faces | Matched pairs | Nonempty critical cells by dimension | Hasse incidences |
| --- | ---: | ---: | --- | ---: |
| 3 | 265 | 132 | one of dimension 3 | 936 |
| 4 | 1,697 | 848 | one of dimension 5 | 7,976 |
| 5 | 10,897 | 5,446 | two of dimension 6, three of dimension 7 | 64,040 |
| 6 | 69,941 | 34,968 | one of dimension 7, four of dimension 8 | 493,212 |
| 7 | 448,945 | 224,471 | two of dimension 9, one of dimension 10 | 3,693,564 |

For the nontrivial adjacent-dimensional Morse chain complexes, calculate signed gradient-path contributions using the recursive elimination of every matched lower simplex \(F\) against its unique matched upper simplex \(H\). Write \(B_q\) with rows indexed by critical \(q\)-cells and columns by critical \((q-1)\)-cells. The exact matrices, in the program's canonical bitmask order, are
\[
B_7(L_5)=\begin{pmatrix}1&0\\0&1\\-1&1\end{pmatrix},\qquad
B_8(L_6)=\begin{pmatrix}-1\\1\\-1\\1\end{pmatrix},\qquad
B_{10}(L_7)=\begin{pmatrix}1&1\end{pmatrix}.
\]
Their maximal nonzero Smith factors are all \(1\), and the first matrix contains an identity minor of size two. Consequently the CW models reduce by elementary unit cancellations to a vertex and, respectively, one \(7\)-cell, three \(8\)-cells, and one \(9\)-cell. The other two cases have one critical top cell with no lower positive-dimensional critical cells. There is no higher attaching-map ambiguity: after elimination, all remaining positive-dimensional cells occur in a single dimension, and each cancellation is between consecutive cells of dimensions at least six. These are integral homotopy equivalences.

## Verification
Run `python3 verify.py` with Python 3.10 or later. The program reconstructs the graphs, enumerates all face masks, and for all five cases checks a second characterization of valid faces using forbidden incident triples. It checks each matching and its cardinality, orients and exhaustively topologically sorts all Hasse incidences, recomputes signed Morse differentials by exact integer recursion, and verifies the listed unimodular minors. Successful completion prints `MOBIUS_LADDER_TWO_MATCHING_CERTIFIED`. The complete enumeration is finite, with exactly \(448{,}945\) faces in the largest case. No external algebra libraries are required.

## Relationship to prior work
Vega [1] introduced and investigated two-matching complexes and classified wheel and caterpillar families, not this sequence of Möbius ladders. Singh [2] classifies \(M_{n-1}(K_{n,n})\), which includes the \(n=3\) baseline because \(L_3\cong K_{3,3}\), but it does not cover \(L_4,\ldots,L_7\) with degree bound two. Agarwal and Basak [3] study the same Möbius-ladder graphs but different complexes: ordinary independence and extendable perfect-matching complexes. Published mathematical records on the Wagner graph concern ordinary matching or Morse complexes; neither is the bounded-degree-two complex used here. Thus those statements do not imply the new four-case homotopy classification, although unidentified equivalent literature remains possible.

## Limitations
This is an exact finite classification for \(3\le n\le7\), not a recurrence or conjectured general formula. Nothing is claimed about \(n\ge8\), inclusion-induced maps between different degree bounds, graph-automorphism actions, or equivariant homotopy. The fully indexed proof is computationally exhaustive in its specified range; its finiteness does not extend it to all Möbius ladders. The most closely named 2026 paper [3] was accessible by its abstract, but its complete text was not available during the comparison.

## References
[1] Julianne Vega, *2-Matching Complexes*, first posted September 23, 2019, arXiv:1909.10406, https://arxiv.org/abs/1909.10406 (full text read: definitions, wheel/caterpillar results and concluding remarks).

[2] Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632 (2020), https://arxiv.org/abs/2006.13632 (relevant theorem and proof read).

[3] Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601 (2026), https://arxiv.org/abs/2608.30601 (abstract inspected; complete text was inaccessible).
