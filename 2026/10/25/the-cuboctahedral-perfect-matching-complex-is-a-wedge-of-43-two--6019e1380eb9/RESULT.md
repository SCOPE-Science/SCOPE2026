# The cuboctahedral perfect-matching complex is a wedge of 43 two-spheres

## Finding

Let \(Q_3\) be the three-dimensional cube graph and \(C=L(Q_3)\) its line graph, the twelve-vertex cuboctahedral graph. Define \(\mathcal P(C)\) to be the simplicial complex with vertex set \(E(C)\), in which a set of graph edges is a simplex exactly when it is contained in some perfect matching of \(C\). Then there is an integral homotopy equivalence
\[
\mathcal P(C)\simeq\bigvee^{43}S^2.
\]
In particular, its reduced integral homology is \(\mathbb Z^{43}\) in degree two and zero in every other degree. The theorem concerns the **perfect-matching subcomplex**, not the ordinary matching complex.

## Assumptions and scope

Give the cube the labeled vertex set \(\{0,1,\ldots,7\}\). Its twelve edges are the pairs \(\{u,v\}\) with \(u<v\) and binary exclusive-or \(u\oplus v\in\{1,2,4\}\). List these pairs lexicographically as \(q_0,\ldots,q_{11}\). The vertices of \(C\) are the indices \(0,\ldots,11\), and distinct indices \(a,b\) are adjacent precisely when \(q_a\cap q_b\neq\varnothing\). Lexicographically list the resulting twenty-four graph edges as \(e_0,\ldots,e_{23}\).

A *perfect matching* of \(C\) is a collection of six graph edges meeting all twelve vertices exactly once. A face of \(\mathcal P(C)\) is any subset of such a collection. We include the empty face solely in the enumeration, not as a topological cell. All ensuing counts and the matching certificate refer to this labeled graph.

## Proof

**Exhaustive facet and face enumeration.** Recursively enumerate perfect matchings by taking the least uncovered graph vertex and matching it in turn to each available adjacent uncovered vertex. Every perfect matching has exactly one choice at each recursion step and therefore appears exactly once. This produces precisely 32 perfect matchings. For each resulting six-edge facet, enumerate all its subsets, encoding each subset by its 24-bit edge-index mask and deduplicating by mask. This gives, in cardinalities zero through six,
\[
(1,24,192,520,468,192,32).
\]
There are therefore 1,428 nonempty simplices, all accounted for by the 32 facets. The ordinary Euler characteristic is \(24-192+520-468+192-32=44\).

**A complete acyclic discrete-Morse certificate.** On the augmented face set (including the empty face), initialize every face as unpaired. For successive pivots \(j=0,\ldots,23\), and for each then-unpaired mask \(s\) in increasing numerical order, pair \(s\) with \(s\cup\{e_j\}\) whenever the latter face exists, is unpaired, and \(e_j\notin s\). Delete both from the pool of available faces. Exactly 693 pairs result, including the empty-face pair \((\varnothing,\{e_0\})\); the other 43 unpaired faces all have cardinality three.

Discard the empty-face pair and retain the other 692 pairs as a matching on the ordinary nonempty face poset. Its critical faces are exactly the vertex \(\{e_0\}\) and 43 triangles, with no critical cells of any other dimension. All pairs, graph edges, perfect matchings, and critical masks appear in `morse_certificate.json`.

To check acyclicity, direct every matched codimension-one Hasse incidence *upward* and every unmatched one *downward*. The enumerated ordinary face poset has exactly 4,968 such incidences. The finite directed graph has 1,428 vertices, and Kahn's topological sorting procedure exhausts all 1,428 vertices. Since a directed graph is acyclic precisely when a complete topological sort exists, this is a complete finite proof of acyclicity, not a sample calculation. The standard discrete-Morse theorem therefore supplies a CW model with one zero-cell, 43 two-cells, and no one-cells or higher-dimensional cells. All two-cell attaching maps have target a point, so the CW model is \(\bigvee^{43}S^2\). This proves the stated integral homotopy equivalence.

## Verification

The package includes `verify_cubocta_perfect.py` and `morse_certificate.json`. From the same directory, run `python3 verify_cubocta_perfect.py` (Python 3.10+; standard library only). The program reconstructs the graph and all perfect matchings by exhaustive recursion, independently checks their number with an exact subset recurrence, reconstructs all faces, checks every certificate pair and critical face, and topologically sorts the complete directed face-incidence graph. It separately performs exact mod-two boundary reductions for the five nonzero boundary maps.

The observed boundary ranks over \(\mathbb F_2\), in successive positive chain degrees, are \((23,169,308,160,32)\); these independently reproduce the Betti rank 43 in degree two. The **integral homotopy theorem** follows from the verified acyclic matching and the dimension of its critical CW cells, not from those mod-two calculations. On successful execution the program prints `VERIFY_OK`.

## Relationship to prior work

Gévay and Pisanski describe the cuboctahedron as the medial of the cube, equivalently the line graph of a square prism; their 2012 work provides a historical graph construction but no perfect-matching-complex homotopy theorem. Bayer, Jelić Milutinović and Vega define and investigate perfect-matching complexes for honeycomb graphs, proving homotopy results for specific honeycomb families; the cuboctahedral graph instead has triangular and square faces and is not one of those families. The published classification of the **ordinary** cuboctahedral matching complex gives \(\bigvee^{57}S^3\); that larger complex contains all matchings, including nonextendable ones, and its homotopy type does not determine the homotopy type of the subcomplex studied here.

The identification \(C=L(Q_3)\) also admits an equivalent cube-edge-pairing interpretation: each edge of \(C\) pairs adjacent cube edges, and perfect matchings of \(C\) partition all twelve cube edges into six adjacent pairs. The exhaustive comparison included this alias, the medial-of-prism description, and the distinction between maximal, ordinary and perfect matchings. No covering result was found in the inspected sources or accessible mathematical index; this is not a proof of global literature uniqueness.

## Limitations

This is an exact classification for one canonical finite graph, not for all medial graphs or all line graphs. The number 43 is the number of two-dimensional spheres in an integral homotopy type, not merely a mod-two Betti number. Reproducibility is conditional on running the included finite certificate verifier correctly. Further independent mathematical audit has not been performed, and an unindexed or otherwise inaccessible equivalent classification is a residual originality risk.

## References

1. G. Gévay and T. Pisanski, *Kronecker covers, V-construction, unit-distance graphs and isometric point-circle configurations*, arXiv:1206.5477v1, first publicly submitted 2012-06-24, especially Section 5 on generalized cuboctahedra and the cube medial graph. https://arxiv.org/abs/1206.5477
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first submitted 2022-09-06, Definition 1 and Sections 2–4. https://arxiv.org/abs/2209.02803
3. *The cuboctahedral matching complex is a wedge of 57 three-spheres*, published mathematical research record dated 2026-10-11; the inspected `RESULT.md` classifies the ordinary matching complex of \(L(Q_3)\), a different complex.
