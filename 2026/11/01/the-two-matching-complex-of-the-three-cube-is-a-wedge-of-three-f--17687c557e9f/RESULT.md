# The two-matching complex of the three-cube is a wedge of three five-spheres

## Finding
For the usual three-dimensional cube graph \(Q_3\), the two-matching simplicial complex satisfies the **integral homotopy equivalence**
\[
M_2(Q_3)\simeq\bigvee^{3}S^5.
\]
Thus its only nonzero reduced integral homology group is \(\widetilde H_5(M_2(Q_3);\mathbb Z)\cong\mathbb Z^3\). This is a homotopy classification, not simply a finite-field calculation.

## Assumptions and scope
The underlying graph has vertex set \(\{0,1,\ldots,7\}\), interpreted as binary triples. Two vertices are adjacent precisely if their binary representations differ in one position. Its twelve graph edges are indexed in this order:

```
index 0: (0,1)     index 1: (0,2)     index 2: (0,4)
index 3: (1,3)     index 4: (1,5)     index 5: (2,3)
index 6: (2,6)     index 7: (3,7)     index 8: (4,5)
index 9: (4,6)     index 10: (5,7)    index 11: (6,7)
```

For every edge subset \(A\subseteq E(Q_3)\), include \(A\) as a face if and only if each graph vertex is incident with at most two edges of \(A\). As every graph vertex has degree three in \(Q_3\), this is equivalent to saying that no complete three-edge vertex star is contained in \(A\). A face is encoded by the twelve-bit integer \(\sum_{i\in A}2^i\); this encoding applies only to the displayed edge ordering. The empty set is a face but is omitted from nonempty face counts.

## Proof
**Exhaustive face characterization.** The two logically independent face predicates in the accompanying executable agree for all \(2^{12}=4096\) graph-edge subsets. Exactly \(1698\) of the nonempty subsets are faces; their numbers in dimensions zero through seven are
\[
(12,66,212,423,516,352,108,9).
\]

**Explicit acyclic matching.** Starting with the nonempty face poset, process graph edges in index order. At stage \(i\), for every still-unmatched face \(A\) that does not contain edge \(i\), match \(A\) with \(A\cup\{i\}\) when the latter also remains unmatched, removing both from further stages. Each stage operates on the current residual face set. The successive numbers of matched pairs are
\[
(665,94,8,51,8,10,7,0,2,1,0,0),
\]
for a total of \(846\) pairs. Exactly six cells remain, with integer bit masks
```
1       dimension 0
598     dimension 4
888     dimension 5
1446    dimension 5
2710    dimension 5
3158    dimension 5
```

The matching is acyclic, as follows. For every lower matched face \(L\) with paired upper face \(H\), draw a transition \(L\to L'\) for each other facet \(L'\) of \(H\) that is also a lower matched face. Every closed discrete gradient path would yield a directed cycle in these transitions. The standalone verifier enumerates **all** \(846\) lower matched faces and their transitions and removes all of them by a topological sort; none remains in a directed cycle. Therefore Forman's discrete Morse theorem gives a CW model with precisely the six listed critical cells and no other cells in positive dimensions.

**Exact integral attachment.** Orient every simplicial cell by increasing edge index. For a face \(A=\{i_0<\cdots<i_k\}\), its integral simplicial boundary is \(\sum_{j=0}^k(-1)^j(A\setminus\{i_j\})\). Compute the Morse boundary by replacing each matched lower four-face, in topological gradient-path order, with the signed boundary of its paired five-face. The resulting exact integral cellular boundary from the four critical five-cells (ordered by masks \(888,1446,2710,3158\)) to the unique critical four-cell (mask \(598\)) is
\[
\partial_5=\begin{pmatrix}-1&1&-1&-1\end{pmatrix}.
\]
The program performs the entire reduction with signed integers and checks that no paired lower four-face retains a coefficient. There are no critical one-, two-, or three-cells and no other positive-dimensional Morse boundaries.

Attaching four five-cells to a four-sphere by the primitive degree row \((-1,1,-1,-1)\) is homotopy equivalent to a point together with three five-spheres: an integral change of five-cell generators turns the row into \((1,0,0,0)\), and the degree-one attachment cancels the four-cell. Since \(\pi_4(S^4)\cong\mathbb Z\), these degrees determine the attaching homotopy classes; this is a homotopy cancellation, not merely a homology argument. Therefore \(M_2(Q_3)\simeq\bigvee^3S^5\), proving the claim.

## Verification
Run `python3 verify.py` using only the Python standard library; `verify_output.txt` records its actual output. It independently constructs faces by degree constraints and by exclusion of all vertex stars; tests all \(4096\) subsets; checks \(1698\) nonempty faces and \(846\) pairs; confirms acyclicity of every matched gradient path; and computes the exact integer Morse boundary row. The complete face-poset Hasse graph has \(7980\) incidence covers between nonempty cells.

As an independent chain check, the complete simplicial boundary ranks over \(\mathbb F_2\), in dimensions one through seven, are \((11,55,157,266,250,99,9)\), yielding reduced mod-two Betti number \(3\) only in degree five. The integral homotopy conclusion follows from the exact Morse certificate, not from these finite-field ranks.

## Relationship to prior work
Vega's foundational study of two-matching complexes introduces the construction and discrete-Morse methods, concentrating on graphs with leaves, wheels, and perfect caterpillars rather than the three-cube. Singh's classifications address bounded-degree complexes of forests and higher-matching complexes of complete and complete bipartite graphs. The cube graph is neither a forest nor complete nor complete bipartite, and the inspected statements do not imply its homotopy type. A previously published calculation of the **ordinary** matching complex of \(Q_3\) gives a wedge of four two-spheres; that calculation concerns degree cutoff one, not two. The present classification is a distinct cutoff and determines its exact integral attachments.

## Limitations
The theorem concerns only the graph \(Q_3\) at cutoff two. It gives no general statement about larger hypercubes, arbitrary cubic graphs, or equivariant homotopy types. The novelty assessment is limited to inspected primary literature, accessible published research records, and searches under several equivalent terms; an unindexed equivalent calculation cannot be categorically excluded. The acyclic matching and signed cellular boundary are fully executable finite proofs, without reliance on floating-point arithmetic.

## References
- J. Vega, *2-Matching Complexes*, first public version 23 September 2019, arXiv:1909.10406; https://arxiv.org/abs/1909.10406 .
- A. Singh, *Bounded degree complexes of forests*, first public version 28 October 2019, arXiv:1910.12793; https://arxiv.org/abs/1910.12793 .
- A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, first public version 24 June 2020, arXiv:2006.13632; https://arxiv.org/abs/2006.13632 .
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145, for discrete Morse theory.
