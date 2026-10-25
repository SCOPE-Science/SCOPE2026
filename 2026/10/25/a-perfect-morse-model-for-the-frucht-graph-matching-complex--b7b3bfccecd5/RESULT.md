# A perfect Morse model for the Frucht-graph matching complex

## Finding

Let \(F\) be the twelve-vertex Frucht graph, given precisely by its order-one LCF description
\[
[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2].
\]
Let \(\mathcal M(F)\) be the ordinary matching complex, whose vertices are the graph edges and whose simplices are the collections of pairwise vertex-disjoint graph edges. Then
\[
\boxed{\mathcal M(F)\simeq \bigvee^{20}S^3.}
\]
Thus its reduced integral homology is free of rank twenty in degree three and zero in every other degree. A complete acyclic discrete-Morse matching realizes the stronger homotopy statement.

## Assumptions and scope

The graph has vertices indexed by \(\{0,1,\ldots,11\}\), with indices taken modulo twelve. Include all twelve edges \(\{i,i+1\}\), and for each index \(i\) also include the chord \(\{i,i+s_i\}\), where \(s_i\) is the \(i\)-th entry of the displayed LCF list. Identical undirected chords are included only once. This gives a finite simple graph with eighteen edges, degree three at each vertex, and the standard Frucht-graph isomorphism type.

No assertion is made for arbitrary cubic graphs, arbitrary planar graphs, all Halin graphs, or a family with a variable number of vertices. The result concerns the *ordinary matching complex*, not the perfect-matching complex or the independence complex on the original twelve vertices.

## Proof

**Complete face set.** Order the eighteen graph edges lexicographically as unordered vertex pairs. Encode a nonempty collection of edges by an eighteen-bit integer. The collection is a simplex exactly when its selected graph edges have pairwise disjoint endpoints. Exhaustively testing every integer from one through \(2^{18}-1\) yields exactly 1,025 nonempty simplices and the simplicial face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(18,117,333,397,152,8).
\]
The complete enumeration and its acceptance predicate are provided in `verify_frucht.py`.

**Explicit discrete-Morse pairing.** Starting with the set of all nonempty simplices, process the eighteen edge labels in this exact order:
\[
(4,6,10,7,15,1,16,2,8,14,17,12,3,13,0,5,9,11).
\]
At stage \(j\), traverse the surviving faces in increasing bitmask order. Whenever a surviving face \(\sigma\) lacks label \(j\) and the face \(\sigma\cup\{j\}\) also survives, pair the two and remove both. Every pair differs by a single vertex of the matching complex and hence is a cover relation in its face poset. There are exactly 502 disjoint pairs. The unpaired simplices are precisely one vertex and twenty simplices of dimension three, with none in any other dimension. The verifier checks all twenty-one critical bitmasks explicitly.

**Acyclicity.** Construct every cover relation \(\tau\subset\sigma\) between nonempty simplices with \(\dim\sigma=\dim\tau+1\). There are exactly 3,629 such incidences. Orient unmatched incidences downward, from \(\sigma\) to \(\tau\), and matched incidences upward, from \(\tau\) to \(\sigma\). The verifier constructs the complete directed graph with 1,025 vertices, then performs Kahn's topological sorting algorithm. All 1,025 vertices are visited. Therefore the directed graph is acyclic, which is exactly the acyclicity condition for the discrete-Morse pairing.

By the finite discrete-Morse theorem, \(\mathcal M(F)\) is homotopy equivalent to a CW complex with one zero-cell, twenty three-cells and no other cells. Since each three-cell is attached along a map from \(S^2\) to the single zero-cell, all attaching maps are constant. The CW complex is therefore the wedge of twenty copies of \(S^3\), as claimed.

## Verification

The included standalone `verify_frucht.py` requires only Python 3 and its standard library. Run `python3 verify_frucht.py` to reconstruct the Frucht graph from the LCF data, enumerate *all* nonempty matching simplices, build all matched pairs, check the exact list and dimensions of critical cells, and verify acyclicity on the complete directed Hasse diagram. Its successful output is reproduced in `verify_output.txt` and ends in `VERIFY_OK`.

As a separate chain-level cross-check, the program computes the full simplicial boundary ranks over \(\mathbb F_2\), yielding \((17,100,233,144,8)\) for boundaries in degrees one through five. These give the expected mod-two reduced homology rank twenty in degree three and zero elsewhere. The integral homotopy conclusion follows from the acyclic Morse matching, **not** from finite-field ranks alone.

## Relationship to prior work

Frucht's 1949 construction describes the cubic graph realizing the trivial automorphism group, but makes no calculation about its matching complex. The published LCF description identifies the exact named graph used here.

Bayer, Jelić Milutinović and Vega prove a wedge-of-spheres theorem for matching complexes of **outerplanar** graphs. The Frucht graph is cubic and therefore cannot be outerplanar: every nonempty outerplanar graph has a vertex of degree at most two. Their theorem does not imply this claim, and in any event it does not specify the twenty three-dimensional sphere summands.

A published homotopy calculation for the *independence complex of the Frucht graph* treats a different construction. In general \(\mathcal M(F)=\operatorname{Ind}(L(F))\), where \(L(F)\) is the line graph; it is not \(\operatorname{Ind}(F)\). A published matching-complex calculation for the Franklin graph treats another twelve-vertex cubic graph and does not imply a Frucht-graph result. Full result statements for both comparisons were examined.

## Limitations

The theorem is a finite, explicitly named-graph classification. It neither establishes a general theorem for planar matching complexes nor determines equivariant homotopy information. Exact finite verification proves the stated claim but does not establish universal bibliographic novelty. The literature comparison could miss an unindexed equivalent result. Independent scientific audit and validation have not been performed.

## References

1. R. Frucht, “Graphs of Degree Three with a Given Abstract Group,” *Canadian Journal of Mathematics* 1 (1949), 365–378, especially Figure 1 and Theorem 2.3. DOI: 10.4153/CJM-1949-033-6. Public issue date: 1949-08-01.
2. E. W. Weisstein, “Frucht Graph,” *MathWorld*, including the order-one LCF encoding.
3. M. Bayer, M. Jelić Milutinović and J. Vega, “Matching Complexes of Outerplanar Graphs,” arXiv:2411.04601, first posted 2024-11-07, Theorem 2. The 2026 revised preprint was inspected.
4. “The Frucht-graph independence complex is a wedge of three 2-spheres,” public homotopy result, identifier `cce46c181e9f`, full result inspected.
5. “Edge-orbit matching-complex splitting for the Franklin graph,” public homotopy result, identifier `be4888fadcca`, full result inspected.
