# The two-independence complex of the Pappus graph is a mixed-dimensional sphere wedge

## Finding
Let \(P\) be the canonical eighteen-vertex, twenty-seven-edge Pappus (Levi) graph and let \(\operatorname{Ind}_2(P)\) be its two-independence complex: the face set consists of subsets of vertices for which each connected component of the induced subgraph has at most two vertices. There is an integral homotopy equivalence

\[
\operatorname{Ind}_2(P)\simeq \bigvee^{9}S^{5}\,\vee\,S^{6}.
\]

In particular, all reduced integral homology vanishes except for \(\widetilde H_5\cong\mathbb Z^9\) and \(\widetilde H_6\cong\mathbb Z\); these groups have no torsion. The original complex is nonpure, with maximal simplex dimension nine, so the homotopy conclusion is stronger than any face enumeration or Betti calculation.

## Assumptions and scope
The vertices are precisely the integers from \(0\) through \(17\). Edges are the following unordered pairs; this adjacency list fixes the graph independently of software conventions:

```
(0,1) (0,5) (0,17) (1,2) (1,8) (2,3) (2,13)
(3,4) (3,10) (4,5) (4,15) (5,6) (6,7) (6,11)
(7,8) (7,14) (8,9) (9,10) (9,16) (10,11) (11,12)
(12,13) (12,17) (13,14) (14,15) (15,16) (16,17)
```

The admissible faces are exactly the subsets \(A\) satisfying \(\deg_{P[A]}(v)\leq1\) for every \(v\in A\). Indeed, a finite graph has all connected components of size at most two if and only if its maximum degree is at most one. All statements are about this specific graph and its *vertex*-based higher-independence complex, not the edge-based matching complex.

## Proof
**1. Complete finite simplicial model.** Represent each vertex subset by an eighteen-bit mask. A mask is a face if and only if every selected vertex has at most one selected neighbor in the explicitly specified graph. The complete nonempty face vector, indexed by dimensions zero through nine, is

\[
(18,153,762,2394,4806,6027,4428,1728,308,27).
\]

Thus the complex has exactly \(20651\) nonempty simplices. This is an exhaustive enumeration of all \(2^{18}\) subsets, not a sample. There are \(407\) inclusion-maximal simplices: \(9\) of dimension five, \(333\) of dimension seven, \(38\) of dimension eight, and \(27\) of dimension nine; hence nonpurity is also directly certified.

**2. Constructive discrete-Morse reduction.** Use the fixed vertex-pivot order

```
11, 9, 0, 16, 2, 15, 10, 3, 5, 17, 14, 6, 7, 8, 4, 1, 13, 12
```

At each pivot \(v\), pair every still-unmatched nonempty face \(A\) not containing \(v\) with \(A\cup\{v\}\) whenever the latter remains a face and is also unmatched. Remove both faces before advancing to the next pivot. This defines \(10319\) distinct codimension-one matching pairs. The unmatched cells consist of exactly one vertex, ten five-cells, and two six-cells. Their masks are, respectively,

```
0: 2048
5: 18054 38162 78128 83014 98502 106600 135576 157216 197832 198024
6: 87174 205160
```

A matching is acyclic if the Hasse graph, with every unmatched cover oriented from coface to face and every matched cover reversed, contains no directed cycle. The verifier constructs **all** \(120222\) nonempty-face cover relations and performs an exact topological sort of the directed graph. It visits all \(20651\) faces, which proves acyclicity exhaustively. The algebraic/discrete-Morse theorem therefore supplies a CW model having precisely the listed critical cells and no others.

**3. Exact signed attaching degrees.** Orient every simplex by ascending vertex labels. For the ten critical five-cells in the displayed order, and the two critical six-cells in the displayed order, integral elimination of the matched unit-incidence pairs gives the Morse differential, displayed here with one row per six-cell:

\[
\partial_6^{\mathrm{Morse}}=\begin{pmatrix}
-1&0&0&-1&-1&0&0&0&0&0\\
 1&0&0& 1& 1&0&0&0&0&0
\end{pmatrix}^{\!\mathsf T}.
\]

The first displayed row is primitive (contains a unit), and the second is its negative. Consequently this integral boundary has rank one, Smith invariants consisting of a single \(1\), a nine-dimensional free cokernel, and a one-dimensional free kernel. No unreduced boundary maps occur between dimensions one and four or above dimension six in the Morse CW model. Thus \(\widetilde H_5\cong\mathbb Z^9\) and \(\widetilde H_6\cong\mathbb Z\).

**4. Passage from homology to homotopy.** The critical zero-cell is the only zero-cell, and there are no critical cells of dimensions one through four. Therefore the five-skeleton of the Morse CW model is a wedge of ten five-spheres. Its fifth homotopy group maps isomorphically to its fifth homology by Hurewicz; thus both six-cell attaching maps are determined by the two integer rows above. An integral change of basis sends the primitive first attaching vector to a coordinate unit and the second to its negative. The first six-cell and that five-sphere then form a contractible summand. The remaining six-cell attaches trivially to the wedge of nine other five-spheres because its attaching class becomes zero after this cancellation. This yields the claimed homotopy equivalence \(\bigvee^9S^5\vee S^6\).

## Verification
Run `python3 verify_morse.py` and `python3 verify_mod2.py` in the same directory as this document. Both require only Python's standard library. The former independently reconstructs the graph, all faces, all matching pairs, all face-poset covers, the entire directed acyclicity test, and the signed integral Morse differential. Its stable output is included as `morse_output.txt`.

The second program independently determines face membership by scanning every induced vertex degree and computes the full simplicial boundary ranks directly over \(\mathbb F_2\), without using the Morse matching. Its ranks in dimensions one through nine are

\[
(17,136,626,1768,3038,2980,1447,281,27),
\]

which independently yield mod-two reduced Betti numbers nine in degree five and one in degree six. Its output is `mod2_output.txt`. The direct mod-two computation is corroboration; the integral homotopy assertion depends on the exhaustive acyclicity check and signed unit-pivot calculation, not on mod-two ranks alone.

## Relationship to prior work
Deshpande and Singh's foundational 2020 study classifies complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees, none of which contains the canonical Pappus graph as an instance. Sawant's 2026 study of higher-independence vertex decomposability resolves the case of arbitrary **trees**, whereas the Pappus graph is a cubic graph with cycles. Ghosh and Selvaraja (2025) develop chordality and shellability theory for higher-independence complexes, focusing in particular on forests and block graphs; their stated classifications do not determine the present Pappus example. The ordinary independence complex of the Pappus graph has previously been reported as a wedge of ten four-spheres, but ordinary one-independence differs from two-independence: it excludes induced edges altogether. Its edge-based matching complex is another separate construction. A known two-independence classification for the Petersen graph concerns a different cubic graph and does not imply the present mixed-dimensional homotopy type.

## Limitations
This is a complete exact computation for one canonical finite graph, **not** a classification for all cubic, incidence, or generalized Petersen graphs. No general statement on shellability, torsion for other graphs, or higher-independence parameters is asserted. The proof combines a reproducible finite exhaustive acyclicity check with standard integral discrete-Morse and homotopy arguments; it does not claim a shorter uniform symbolic matching theorem. A targeted literature/database comparison found no prior equivalent result, but absence from a search does not establish bibliographic uniqueness; unindexed results remain a possibility. Independent scientific validation has not been performed.

## References
1. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first posted 2020-01-15.
2. Rutuja Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first posted 2026-05-24.
3. Arka Ghosh and S. Selvaraja, *Chordality and Shellability of Higher Independence Complexes*, arXiv:2505.06614, first posted 2025-05-10.
4. Published mathematical record, *The Pappus independence complex is \(\bigvee^{10}S^4\)*, identifier `2026/10/11/SCOPE-the-pappus-independence-complex-is-bigvee-10-s-4--81f85f0cc9c6`.
5. Published mathematical record, *The two-independence complex of the Petersen graph is a three-sphere*, identifier `2026/10/11/SCOPE-the-2-independence-complex-of-the-petersen-graph-is-a-3-sphere--156dc9567f6a`.
