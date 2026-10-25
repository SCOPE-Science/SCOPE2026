# The Möbius–Kantor two-independence complex is a wedge of three six-spheres

## Finding
Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph with sixteen vertices. Define \(\operatorname{Ind}_2(M)\) to be the abstract simplicial complex whose faces are vertex sets \(S\subseteq V(M)\) for which **every** connected component of the induced graph \(M[S]\) contains at most two vertices. Then the geometric realization has the exact integral homotopy type
\[
\boxed{\left|\operatorname{Ind}_2(M)\right|\simeq\bigvee^{3} S^{6}.}
\]
Equivalently, the first higher-independence complex (also called the three-path-free vertex-subset complex) of this cubic symmetric graph has three free integral homology generators in degree six and no other nonzero reduced homology. The claim is a homotopy classification, not merely a field-coefficient Betti calculation.

## Assumptions and scope
Use distinct labeled vertices \(u_0,\ldots,u_7,v_0,\ldots,v_7\), with indices in \(\mathbb Z/8\mathbb Z\). The undirected, simple edge set is exactly
\[
\bigl\{\{u_i,u_{i+1}\},\{u_i,v_i\},\{v_i,v_{i+3}\}:i\in\mathbb Z/8\mathbb Z\bigr\}.
\]
It has sixteen vertices and twenty-four edges. A face is allowed whenever each induced connected component has size at most two; this is **not** ordinary graph independence (which forbids every edge), nor edge-set matching, nor a graph cut complex. Empty face conventions are standard; discrete-Morse certificates below use only nonempty faces and retain one zero-dimensional critical cell. The result is for this graph and this higher-independence parameter only.

Number the vertices \(u_i\mapsto i\) and \(v_i\mapsto8+i\). A vertex set is encoded by its integer mask \(m=\sum_{i\in S}2^i\). In the following algorithm, \(m\) ranges over the integers from \(1\) through \(65535\); every integer is tested. These masks specify the entire finite object without any hidden data files.

## Proof
**Face description.** For a simple graph, a vertex subset induces a component on at least three vertices if and only if some three of its vertices span a connected three-vertex subgraph, equivalently at least two of the three possible edges. The Möbius–Kantor graph is triangle-free and cubic. Accordingly its minimal forbidden faces are the forty-eight triples comprising a vertex and a pair of distinct neighbors. These can be generated directly from the twenty-four displayed edges, rather than supplied as an unverified lookup table. Enumerating all sixty-five thousand five hundred thirty-five nonempty vertex masks against these triples gives exactly \(6812\) nonempty faces and face vector, in dimensions zero through seven,
\[
(16,120,512,1324,2064,1840,816,120).
\]
The bundled verifier additionally enumerates the same faces by independently traversing all induced connected components for **every** vertex mask and checks equality with the forbidden-triple classification.

**Complete discrete-Morse matching.** Start with the complete set of these \(6812\) nonempty faces, all unpaired. Process pivot vertices in the exact order of integer labels
\[
(13,10,1,12,4,11,2,7,9,6,3,15,0,14,8,5).
\]
At a pivot \(j\), scan the remaining faces in increasing integer-mask order. Whenever a remaining face \(m\) omits \(j\) and the face \(m+2^j\) is also remaining, pair \(m\) with \(m+2^j\) and remove both from subsequent consideration. This specifies a genuine face-poset matching: each pair differs by one vertex and belongs to the simplicial complex, and no face is paired twice.

An exhaustive application of the displayed deterministic rule yields exactly \(3404\) pairs and precisely four unmatched faces, with integer masks
\[
8192,\qquad33637,\qquad33644,\qquad49964.
\]
The first mask has one vertex and is zero-dimensional; each of the other three has seven vertices and is six-dimensional. There are no further critical cells.

**Acyclicity and integral homotopy.** Form the directed Hasse graph of *all* nonempty faces: for every nonempty codimension-one subface \(a\subset b\), orient the cover \(b\to a\), except reverse a matched cover to \(a\to b\). The verifier independently reconstructs all \(35104\) such directed cover incidences and executes a complete topological sorting. It removes **all** \(6812\) vertices of the directed Hasse graph, proving that the matching has no alternating directed cycle; it does not infer acyclicity from the mere size of the matching.

Forman's discrete-Morse theorem therefore provides a CW complex homotopy equivalent to the realization, with exactly one zero-cell, three six-cells and no cells in dimensions one through five or seven. Every six-cell attaches along a map from a five-sphere to the point that is the entire five-skeleton. Each attaching map is null. The CW complex is \(\bigvee^3 S^6\), proving the stated **integral homotopy equivalence**. No field choice, orientability assumption or unknown attaching degree is involved.

## Verification
Run `python3 verify.py` using Python 3 and the standard library only. The standalone program reconstructs the graph and forty-eight forbidden triples; it enumerates all \(2^{16}-1\) nonempty masks twice, by logically independent triple-exclusion and connected-component algorithms. It then regenerates the full matching from the stated pivot order, topologically sorts the entire oriented face-poset Hasse diagram, and independently reduces all simplicial boundary matrices over \(\mathbb F_2\) to check Betti numbers. It terminates with `VERIFY_OK` only after all assertions pass.

The checker obtains exactly \(3404\) matched pairs, critical-mask set \(\{8192,33637,33644,49964\}\), \(35104\) Hasse incidences, and mod-two Betti vector \((1,0,0,0,0,0,3,0)\) in degrees zero through seven. The source code and the actual verification output are included next to this document; the code is executable on its own, with no data downloads. The mod-two calculation is an auxiliary independent consistency check, **not** the source of the integral homotopy conclusion.

## Relationship to prior work
Sawant's 2026 paper proves vertex decomposability of higher independence complexes of **trees** and explicitly identifies three-path-free complexes with \(\operatorname{Ind}_2\) for any graph. The Möbius–Kantor graph has cycles of length six and is not a tree, so that structural theorem does not determine this homotopy type. Deshpande and Singh determine higher independence homotopy for complete multipartite, fully whiskered, cycle and certain tree families; their graph classes do not include this graph. The earlier domination and chordal-graph theorem likewise gives neither this case nor a precise three-sphere count.

A separately published computation identifies the **ordinary** independence complex of the same graph as \(\bigvee^4 S^3\vee S^4\). Ordinary independence means forbidding edges, while the present complex *allows* isolated edges and forbids components of size three; the earlier homotopy type does not imply the displayed six-dimensional classification. A second public computation concerns the total three-cut complex of the same graph, whose facets are complements of independent triples. Its defining faces and degrees are different and likewise do not imply this result. The two cited comparisons were inspected at their full `RESULT.md` texts, not only by title.

No inspected publication, indexed mathematical result or accessible earlier claim gave this two-independence/three-path-free classification. This statement is a best-evidence comparison, not a formal proof of global priority.

## Limitations
The proof is a complete exhaustive finite certificate for the specifically defined \(16\)-vertex graph. It does not give a classification for all generalized Petersen graphs, imply shellability or vertex decomposability, or make an equivariant assertion. The explicit topological sorting is an exhaustive finite proof of acyclicity; the independent mod-two boundary computation alone would not prove a wedge decomposition. An external paper on other topological aspects of the same graph was available at abstract level, but its full PDF was inaccessible in this inspection. Although its abstract concerns Cayley structures, Lefschetz numbers and graph embeddings rather than three-path-free complexes, uninspected text is a remaining bibliographic risk. Independent scientific review has not been performed.

## References
1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first public submission 2026-05-24; Theorem 1.1 and the three-path-free observation in §1.
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448v2 (2021), especially §3 and the classes stated in the abstract.
3. P. Deshpande, S. Shukla and A. Singh, *Distance \(r\)-domination number and \(r\)-independence complexes of graphs*, arXiv:2001.06775v1, and European Journal of Combinatorics 102 (2022), 103508.
4. *Integral homotopy type of the Möbius–Kantor independence complex*, public mathematical record (2026-10-11), comparison identifier `b0d62cfde5f3`; applies to \(\operatorname{Ind}_1\), not \(\operatorname{Ind}_2\).
5. *The total three-cut complex of the Möbius–Kantor graph is a forty-five-sphere wedge*, public mathematical record (2026-10-11), comparison identifier `4936eeabcd8f`; different simplicial complex.
6. O. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799v1 (2026); abstract consulted, full text unavailable in this comparison.
7. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145; acyclic discrete-Morse matchings and CW reductions.
