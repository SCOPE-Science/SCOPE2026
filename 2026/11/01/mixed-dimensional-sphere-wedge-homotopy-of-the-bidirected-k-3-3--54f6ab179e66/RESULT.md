# Mixed-dimensional sphere-wedge homotopy of the bidirected \(K_{3,3}\) multipath complex

## Finding
Let \(D=\overleftrightarrow{K}_{3,3}\) be the digraph obtained by replacing each of the nine edges of \(K_{3,3}\) with both opposed arcs. Its simplicial multipath complex \(X(D)\) satisfies the integral homotopy equivalence
\[
|X(D)|\simeq \bigvee^{19}S^3\vee\bigvee^{12}S^4.
\]
The reduced integral homology is therefore free of rank 19 in degree three, free of rank 12 in degree four, and zero in every other degree. These are homotopy, not merely field-homology, conclusions.

## Assumptions and scope
Use vertex set \(L=\{0,1,2\}\) and \(R=\{3,4,5\}\). The arc set is exactly all \((u,v)\) with \(u\in L,v\in R\) or \(u\in R,v\in L\), each of the 18 arcs included once. A simplex of \(X(D)\) is a set of arcs whose spanning directed subgraph is a disjoint union of simple directed paths and isolated vertices. Equivalently, each original vertex has indegree and outdegree at most one and the selected arcs contain no directed cycle, including a length-two cycle. This equivalence is immediate because a finite directed graph with indegree and outdegree at most one decomposes into directed paths and cycles. A simplex with \(k+1\) arcs has simplicial dimension \(k\). Empty simplex is included implicitly.

## Proof
**1. Complete face enumeration.** Sort the 18 arcs lexicographically and identify any nonempty arc subset with its 18-bit characteristic mask. Test the indegree and outdegree bounds and absence of directed cycles for every mask from 1 through \(2^{18}-1\). Independently, build all permissible masks recursively by successively inserting an arc only if neither degree bound nor directed acyclicity is violated. Both algorithms give exactly the same set of 714 faces, with dimension-indexed face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(18,108,264,252,72).
\]
There are 144 inclusion-maximal simplices: 72 of dimension three and 72 of dimension four. The maximal dimension is four.

**2. Complete acyclic matching.** Number the arcs from zero to 17 in their lexicographic order. In turn inspect the arc indices in this fixed order:

`(7,13,2,12,5,9,10,15,6,11,16,14,1,0,8,4,3,17)`.

At an index \(a\), traverse remaining unmatched simplices in ascending integer-mask order. Whenever both \(\sigma\) and \(\sigma\cup\{a\}\) are unmatched and \(a\notin\sigma\), pair and remove them from further consideration. This is a matching of precisely 341 disjoint cover relations in the face poset. Exactly one vertex, 19 three-simplices, and 12 four-simplices remain unmatched. Construct all 2,376 codimension-one incidences on the 714 nonempty simplices, orient unmatched incidences downward and matched incidences upward, and topologically sort this entire directed graph. All 714 nodes are removed; thus no directed cycle exists, and the matching is acyclic in the sense of discrete Morse theory.

**3. Integer Morse attaching degrees.** Orient each simplex by the increasing order of its arc indices. Every codimension-one incidence is then \(+1\) or \(-1\), according to which arc is removed. For each matched pair \((\sigma,\tau)\), the coefficient \([\tau:\sigma]\) is a unit \(\pm1\). Solve the boundary relation of \(\tau\) for \(\sigma\), recursively expanding through any other matched lower cells. Acyclicity ensures termination. This exact integer gradient-path calculation finds that the full \(19\)-by-\(12\) Morse differential from critical dimension four to critical dimension three is the zero matrix. No numerical approximation or modular arithmetic is used in this step.

**4. Recovering the homotopy type.** Discrete Morse theory supplies a CW complex homotopy-equivalent to \(|X(D)|\) with exactly one zero-cell, 19 three-cells, and 12 four-cells, and no other cells. Its three-skeleton is precisely \(\bigvee^{19}S^3\). By the Hurewicz theorem, \(\pi_3(\bigvee^{19}S^3)\cong H_3(\bigvee^{19}S^3;\mathbb Z)\cong\mathbb Z^{19}\). An attaching map of a four-cell is consequently nullhomotopic if and only if its integral degree vector is zero. The zero Morse differential proves that all twelve four-cell attachments are nullhomotopic. Attaching them gives the asserted wedge of 19 three-spheres and 12 four-spheres.

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The checker regenerates the faces by both the exhaustive-mask test and a separate directed-path extension procedure; confirms the face vector and critical dimensions; builds all incidences and topologically sorts the reversed matched-incidence graph; computes the signed integral Morse differential by recursive matched-cell cancellation; and independently reduces all original simplicial boundary matrices over the two-element field. The independent reduced Betti vector is \((0,0,0,19,12)\) for degrees zero through four, agreeing with the exact homotopy result. Expected terminal output begins with `VERIFY_OK` and reports 714 faces, 2,376 incidences, 341 pairs, 19 critical three-cells, 12 critical four-cells, and zero integral Morse differential. The finite computation exhausts this specific 18-arc complex; it is not an extrapolation to other bipartite sizes.

## Relationship to prior work
Caputi, Collari, and Smith [1, Theorems 2.8 and 2.10] study *bidirectional polygonal digraphs*, proving connectivity and integral homology formulas for those polygon families. Their Theorem 1.4 cites an identification with matching complexes under the explicit assumption of **no oriented cycles**, which fails here because each undirected edge yields a directed two-cycle. The present graph is cubic and not a polygon or a bidirectional path. Their T-operation glues a sparse local path configuration; it does not identify the present complete bipartite digraph's homotopy type.

Caputi, Collari, Di Trani, and Smith [2, Section 3.2] compute generating functions for a different **one-way** complete bipartite digraph, whose arcs go from one part to the other only; that complex is a chessboard/matching complex and has different faces. Their homotopy results cover other specified families but not this bidirected six-vertex graph. The cycle-free chessboard complex of the complete bidirected six-vertex graph contains this complex as a subcomplex, but connectivity/homotopy statements about the ambient complex do not determine this subcomplex. Exact and semantic literature comparisons found no equivalent calculation; this is not a proof of universal novelty.

## Limitations
The result is confined to the exact six-vertex bidirected complete bipartite digraph. It neither gives an all-parameter classification for bidirected complete bipartite digraphs nor determines the natural automorphism-group representation on homology. The integer attaching-map argument uses the verified discrete-Morse matching; the field-homology computation alone would not prove the homotopy statement. Independent mathematical audit remains outstanding, and equivalent unindexed literature is a residual originality risk.

## References
[1] Luigi Caputi, Carlo Collari, Jason P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first publicly posted 2026-01-09. https://arxiv.org/abs/2601.05670

[2] Luigi Caputi, Carlo Collari, Sabino Di Trani, Jason P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, first publicly posted 2022-08-09; published in *Mathematika* 70 (2024), e12235. https://arxiv.org/abs/2208.04656
