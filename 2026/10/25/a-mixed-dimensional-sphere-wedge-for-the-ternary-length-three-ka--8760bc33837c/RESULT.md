# A mixed-dimensional sphere wedge for the ternary length-three Kautz directed-forest complex

## Finding
Let \(D\) be the directed Kautz graph whose vertices are the twelve length-three words \(abc\) over \(\{0,1,2\}\) with \(a\ne b\) and \(b\ne c\). Its twenty-four arcs are
\[
abc\longrightarrow bcd\qquad(d\in\{0,1,2\}\setminus\{c\}).
\]
Let \(\operatorname{DT}(D)\) be the simplicial complex on these arcs whose faces have indegree at most one at every vertex and contain no directed cycle. Then the integral homotopy type is
\[
\boxed{\operatorname{DT}(D)\simeq
\bigvee^{8}S^{9}\ \vee\ \bigvee^{12}S^{10}.}
\]
The complex has exactly \(4,608\) ten-dimensional facets and \(132\) nine-dimensional facets, hence is nonpure. Among the latter, exactly twenty-four unordered pairs of roots occur: three root pairs support nine facets each and twenty-one root pairs support five each. In particular, its integral reduced homology is free of ranks eight in degree nine and twelve in degree ten, and is zero in all other degrees.

## Assumptions and scope
The twelve words are ordered lexicographically; arcs are ordered first by their source word and then by the appended symbol. A directed forest means a set of arcs containing no directed cycle and having at most one arc entering each vertex, with all twelve vertices retained (possibly isolated). Faces are the corresponding arc sets, including the empty face by simplicial convention. No statements are made about Kautz graphs with other alphabet sizes or word lengths.

This digraph is a directed line digraph of the corresponding six-vertex, length-two Kautz digraph. The line-digraph relationship concerns the underlying digraphs; it does not identify their directed-forest complexes. The present graph is strongly connected, has no vertex of outdegree eleven, and is not essentially a tree. It has vertices lying on reciprocal directed two-cycles and vertices lying on no reciprocal two-cycle; in particular it is not vertex-transitive.

## Proof
**1. Exhaustive face description.** Each vertex has exactly two incoming arcs. There are therefore \(3^{12}=531,441\) incoming-edge assignments, each independently selecting no incoming arc or one of the two incoming arcs at each vertex. For each assignment, follow the unique predecessor chain from every vertex with an incoming arc; reject precisely those containing a repeated vertex. This enumeration is exhaustive because each set of indegree at most one has a unique incoming-edge assignment. The resulting face numbers in dimensions \(-1,0,1,\ldots,10\) are
\[
(1,24,261,1698,7344,22176,47712,73152,78336,55808,23808,4608).
\]
Thus there are \(314,927\) nonempty faces. Checking all single-edge extensions of every face gives \(4,608\) maximal faces of dimension ten and \(132\) of dimension nine, with no further facets. For the nine-dimensional facets, counting the two vertices without selected incoming arcs gives the stated root-pair distribution.

As an independent consistency check, the directed in-Laplacian has an \(11\)-by-\(11\) principal minor with determinant \(384\). The directed matrix-tree theorem therefore counts \(384\) spanning out-arborescences per possible root, giving \(12\cdot384=4,608\) ten-dimensional facets. A separate disjoint-set test of underlying undirected cycles independently reproduces the complete face membership predicate: with indegree at most one, an undirected cycle exists exactly when a directed cycle exists.

**2. Finite discrete-Morse matching.** Enumerate the arcs \(e_0,\ldots,e_{23}\) as specified above. Begin with every face unmatched. For \(i=0,\ldots,23\), in the complete deterministic face-enumeration order, pair every currently unmatched face \(F\) not containing \(e_i\) with \(F\cup\{e_i\}\) whenever both are currently unmatched faces. This produces \(157,440\) pairs in the augmented face poset. Discard the one pair beginning with the empty face, leaving a critical vertex as basepoint. The ordinary face poset then has \(157,439\) matched pairs and critical cells in dimensions
\[
(0,8,9,10)\quad\text{with multiplicities}\quad(1,3,22,23).
\]
Orient every matched face–coface incidence upward and every other codimension-one incidence downward. A complete topological sort of this directed Hasse graph visits all \(314,927\) nonempty faces across exactly \(2,361,936\) incidences, proving that the matching is acyclic. This provides a CW Morse model with the stated critical cells.

**3. Signed integral Morse boundaries.** Give every face the orientation induced by ascending arc indices. Projecting boundaries of critical cells along reversed matching paths gives matrices
\[
\partial_9\colon\mathbb Z^{22}\longrightarrow\mathbb Z^{3},\qquad
\partial_{10}\colon\mathbb Z^{23}\longrightarrow\mathbb Z^{22}.
\]
With zero-based critical-cell indices, the complete nonzero entries \((\text{row},\text{column},\text{value})\) of \(\partial_9\) are
\[
(0,10,1),\ (0,11,-1),\ (1,12,-1),\ (2,19,-1).
\]
Those of \(\partial_{10}\) are
\[
\begin{gathered}
(0,20,-1),\ (2,21,-1),\ (2,22,1),\ (3,12,1),\ (5,8,-1),\\
(6,9,1),\ (8,10,1),\ (9,11,1),\ (10,13,1),\ (11,13,1),\\
(13,22,-1),\ (15,19,1),\ (18,18,1),\ (20,22,1),\ (21,22,-1).
\end{gathered}
\]
Exact multiplication confirms \(\partial_9\partial_{10}=0\). Each of the three rows of \(\partial_9\) has a unit pivot in a distinct column (columns 10, 12, 19). Cancel those three critical eight/nine-cell pairs. In the resulting basis, deletion of the corresponding three nine-cell coordinates leaves a nineteen-by-twenty-three boundary matrix. Exact integer elimination gives eleven further unit pivots and zero residual boundary. No torsion is introduced because every canceled pivot is \(\pm1\). There remain one zero-cell, eight nine-cells and twelve ten-cells, with zero cellular differentials.

**4. Homotopy, not only homology.** These integral cancellations correspond to CW homotopy equivalences in the present dimension range: initially the eight-skeleton is a wedge of three eight-spheres, so the attaching maps of nine-cells are classified by \(\pi_8\cong H_8\); eliminating the three unit pivots leaves a wedge of nineteen nine-spheres as the nine-skeleton. Its degree-nine Hurewicz map is an isomorphism, so the eleven unit pivots of the ten-cell attaching matrix can likewise be canceled by homotopy-preserving basis changes, leaving a wedge of eight nine-spheres. The twelve residual ten-cell attaching maps have zero degree against every remaining nine-sphere and are nullhomotopic by \(\pi_9\cong H_9\). The claimed wedge follows.

## Verification
Run `python3 verify.py` from the directory containing the accompanying source file. It uses only the Python standard library, regenerates the complete graph and all \(531,441\) assignments, independently checks the forest predicate by a disjoint-set algorithm, verifies all face and facet counts, verifies the determinant \(384\), builds and checks the entire Morse matching and acyclic Hasse orientation, reconstructs both signed integer Morse matrices, and executes explicit unit cancellations. A successful run ends with `VERIFY_OK`.

All arithmetic used for determinants, boundary entries, products, and cancellations is exact integer arithmetic; no floating-point topological inference is used.

## Relationship to prior work
Kozlov introduced and studied complexes of directed forests and classified important double-directed string/tree cases. Engström proved shellability and explicit sphere-wedge results for directed acyclic graphs. Jojić developed complete-source and essentially-tree shelling results. The graph here is cyclic, has no complete source, and is neither essentially a tree nor a bidirected tree; therefore those theorems do not imply the homotopy classification. A complete six-vertex classification for a predecessor digraph also does not imply the behavior of its twelve-vertex directed line digraph, whose arc set and forest condition are different.

The Kautz digraph is a classical bounded-degree shift network. Determining the full topology of its directed-forest complex goes beyond its well-known degree, order, diameter, Hamiltonicity, and spanning-arborescence counts. Searches for the exact twelve-vertex complex and the line-digraph/branching-complex formulations did not identify a covering calculation; this is a statement about the inspected evidence, not a proof that no equivalent theorem exists.

## Limitations
This is one exact finite graph, not a uniform theorem for all Kautz graphs. The calculation is reproducible but has not undergone independent mathematical validation. The available abstracts of the 1999 foundational directed-tree paper and a 2020 thesis were not sufficient for a full-section comparison; an unindexed calculation or a stronger unpublished result is a residual originality risk. The homotopy decomposition is nonequivariant and does not classify the action of the digraph automorphism group.

## References
1. D. N. Kozlov, *Directed trees in a string, real polynomials with triple roots, and chain mails*, arXiv:math/0210045v1, first public 2002-10-03. https://arxiv.org/abs/math/0210045
2. A. Engström, *Complexes of directed trees and independence complexes*, arXiv:math/0508148v1, first public 2005-08-08. https://arxiv.org/abs/math/0508148
3. D. Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475v1, first public 2011-09-21; revised version inspected. https://arxiv.org/abs/1109.4475
4. K. Courtney, *The Directed Forest Complex of Cayley Graphs*, Boise State University thesis, 2020, DOI:10.18122/td/1684/boisestate (abstract accessible; full text not obtained). https://doi.org/10.18122/td/1684/boisestate
5. D. N. Kozlov, *Complexes of Directed Trees*, Journal of Combinatorial Theory A 88 (1999), 112–122, DOI:10.1006/jcta.1999.2984 (bibliographic record/abstract accessible; full text not established). https://doi.org/10.1006/jcta.1999.2984
