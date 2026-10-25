# Mixed-dimensional integral homotopy of the two-independence complex of the four-cube

## Finding
Let \(Q_4\) denote the graph on \(\{0,1\}^4\), with an edge between two words at Hamming distance one. Write \(\operatorname{Ind}_2(Q_4)\) for the simplicial complex of vertex subsets such that each connected component of the induced subgraph has at most two vertices. Its complete integral homotopy type is
\[
\boxed{\left|\operatorname{Ind}_2(Q_4)\right|\simeq\bigvee^{16}S^3\vee S^4.}
\]
Consequently its only nonzero reduced integral homology groups are \(\widetilde H_3\cong\mathbb Z^{16}\) and \(\widetilde H_4\cong\mathbb Z\). In contrast to previously studied higher-independence graph families having equidimensional sphere wedges, the natural sixteen-vertex four-cube exhibits an integral mixed-dimensional wedge.

## Assumptions and scope
All complexes are finite abstract simplicial complexes, represented by their geometric realizations. Number the sixteen vertices of \(Q_4\) by integers \(0,\ldots,15\), interpreted as four-bit strings. Each vertex \(v\) has neighbors \(v\oplus1\), \(v\oplus2\), \(v\oplus4\), \(v\oplus8\), where \(\oplus\) is bitwise exclusive-or. A nonempty face is an integer mask \(m\in\{1,\ldots,65535\}\) satisfying
\[
\#\bigl(N(v)\cap\operatorname{supp}(m)\bigr)\leq1\quad\text{for every }v\in\operatorname{supp}(m).
\]
This test is equivalent to requiring every connected component of the induced graph to have one or two vertices: a finite graph with maximum degree at most one is a disjoint union of isolated vertices and edges. The statement concerns this graph at this specific higher-independence parameter; no all-dimensional hypercube classification is claimed. Its primary subject is integral homotopy classification (MSC 55P15).

## Proof
**1. Exhaustive face universe.** Every vertex subset has a unique membership mask. The predicate above retains exactly the faces, with counts in dimensions zero through seven equal to
\[
(16,120,464,964,960,440,80,10).
\]
Thus there are exactly \(3054\) nonempty faces, and no face has more than eight vertices. A straightforward enumeration over all \(2^{16}\) masks in the accompanying checker verifies both the universe and its counts.

**2. An acyclic matching of the entire face poset.** Consider the successive vertex pivots
\[
(13,3,2,15,12,1,4,6,9,0,11,5,7,10,8,14).
\]
At pivot \(v\), pair every still-unmatched face \(a\) omitting \(v\) with \(a\cup\{v\}\) when both are still unmatched, then delete both from the unmatched universe before the next pivot. The numbers of matched pairs per pivot are
\[
(848,305,255,33,20,10,9,9,9,6,6,0,2,1,3,1).
\]
These sum to \(1517\) pairs, leaving twenty critical faces: one of dimension zero, seventeen of dimension three and two of dimension four. Their exact masks appear in `certificate.json`. The verifier constructs the full Hasse graph with \(13{,}568\) dimension-one incidences; it directs unmatched incidences downward and matched incidences upward and exhaustively topologically sorts all \(3054\) vertices. The sort visits every face, hence there is no directed cycle. This is a complete acyclic discrete-Morse matching, not a sampled matching or a homology heuristic.

**3. The signed integral Morse boundary.** Orient a face by increasing vertex order. Its simplicial boundary deletes the selected vertices with alternating signs. Algebraically cancel each matched lower/upper pair, propagating its incident signed boundary through the acyclic gradient. The included verifier implements this exact integral recurrence and independently reconstructs the faces and matching rather than trusting precomputed boundary entries. Relative to the critical three-faces, the two critical four-faces, with membership masks \(4741\) and \(6181\), have signed Morse boundaries
\[
\partial^{\mathrm{Morse}}_4 e_{4741}=e_{33285}-e_{36869}+e_{36870},
\qquad
\partial^{\mathrm{Morse}}_4 e_{6181}=-e_{33285}+e_{36869}-e_{36870}.
\]
All other Morse boundary maps vanish for dimensional reasons. The two columns are negatives of the same primitive integral vector, whose nonzero coefficients have greatest common divisor one. Therefore the integral Morse boundary map has Smith form with a single unit pivot and one zero column.

**4. Upgrade from homology to integral homotopy.** The acyclic matching produces a CW complex with one zero-cell, seventeen three-cells, two four-cells, and no cells in any other dimensions. Before attaching the four-cells, the space is a wedge of seventeen three-spheres. Its homotopy group of dimension three identifies via the Hurewicz theorem with \(\mathbb Z^{17}\), and the signed degree vector specifies each four-cell attaching map completely. Because the first degree vector is primitive, an invertible integral basis change among the three-spheres identifies it with a coordinate attaching map of degree one. Attaching that four-cell kills one sphere homotopically. The second attaching vector is its negative, so it becomes nullhomotopic after this first attachment. Its four-cell therefore contributes a single freely attached four-sphere. The resulting CW complex is exactly \(\bigvee^{16}S^3\vee S^4\). Forman's discrete-Morse equivalence transfers this homotopy type to the original complex.

## Verification
Run from the same directory, with Python 3.9 or later and no third-party packages:

`python3 verify_q4_ind2.py certificate.json`

The executable enumerates all masks; reconstructs all \(3054\) faces, \(1517\) matching pairs, \(13{,}568\) directed face incidences and signed integral Morse differentials; tests acyclicity over the complete face poset; and cross-checks reduced Betti numbers using an independently formed simplicial boundary over \(\mathbb F_2\). The seven positive-degree boundary ranks, in ascending degree, are \((15,105,359,589,370,70,10)\); the reduced Betti vector in degrees zero through seven is \((0,0,0,16,1,0,0,0)\). The decisive homotopy proof is the acyclic Morse matching plus its **integral**, not just mod-two, signed attaching vectors. The verifier must end with `VERIFY_OK` and the displayed counts. The source and complete finite certificate are included; they are fully reproducible, not references to external output logs.

## Relationship to prior work
Deshpande and Singh [1] established higher-independence homotopy types for several natural families including complete multipartite, fully whiskered, cycle and perfect rooted-tree graphs. Their classifications do not include the four-dimensional hypercube, which has squares and is not a tree, a cycle or one of their stated families. Sawant [2] subsequently established vertex decomposability for higher-independence complexes of **trees**; that theorem does not apply to the square-rich four-cube. Both are important motivations rather than sources of the conclusion here.

A separately published computation [3] gives the ordinary independence complex of \(Q_4\), which is \(\bigvee^7S^3\). This is \(\operatorname{Ind}_1(Q_4)\), with \(742\) nonempty faces, not the \(3054\)-face \(\operatorname{Ind}_2(Q_4)\). Neither its statement nor its proof implies the present two-independence classification. The total three-cut and graph Čech complexes of the four-cube address different simplicial face conditions and also do not imply this result.

## Limitations
This is one exact, motivated, finite graph-complex homotopy type. It is not a formula for \(\operatorname{Ind}_2(Q_n)\) for all dimensions, nor a formula for larger toroidal grids, and it provides no intrinsic equivariant splitting under the full automorphism group. The integral homotopy splitting is noncanonical. The originality comparison cannot exclude an unindexed or inaccessible equivalent calculation. No independent scientific audit has been performed. Acyclic matching implies homotopy equivalence to a Morse CW complex; it does not assert a literal simplicial collapse of the original complex onto an embedded sphere wedge.

## References
[1] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, originally posted 2020-01-15. https://arxiv.org/abs/2001.05448

[2] R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, originally posted 2026-05-24. https://arxiv.org/abs/2605.25150

[3] *The four-cube independence complex is a wedge of seven three-spheres*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c

[4] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
