# Perfect Morse reduction of the Heawood perfect-matching complex
## Finding
Let \(H\) be the Heawood graph, the incidence graph of the Fano plane, and let \(\mathcal M_{\mathrm p}(H)\) denote the simplicial complex of matchings in \(H\) **extendible to a perfect matching**. Then
\[
\mathcal M_{\mathrm p}(H)\simeq\bigvee^{16} S^2.
\]
In particular, the complex has integral reduced homology \(\widetilde H_2\cong\mathbb Z^{16}\) and no other nonzero reduced integral homology, and its fundamental group is trivial. This is the perfect-matching complex, not the ordinary matching complex of all partial matchings.

## Assumptions and scope
Represent the Fano plane by points and lines indexed by \(\mathbb Z/7\mathbb Z\). The points on line \(i\) are \(i,i+1,i+3\) modulo \(7\). The graph \(H\) is bipartite, with point vertices \(p_0,\ldots,p_6\), line vertices \(\ell_0,\ldots,\ell_6\), and edges \(p_j\ell_i\) exactly when \(j\) is on line \(i\). Its 21 edges are ordered first by the integer representative of \(i\in\{0,\ldots,6\}\), then by the integer representative of \(j\). This ordering fixes all combinatorial certificates below.

Define a perfect matching as seven mutually disjoint graph edges covering all fourteen graph vertices. The vertices of \(\mathcal M_{\mathrm p}(H)\) are graph edges belonging to at least one perfect matching. A nonempty set of graph edges is a face if and only if it lies in a perfect matching. Thus the 24 perfect matchings, each containing seven edges, are exactly the facets. The empty face is conventionally included, but is excluded from the nonempty face-poset matching.

## Proof
There are exactly 24 perfect matchings. To see that the finite enumeration is complete, assign one of the three incident lines to each of the seven point vertices, using every line exactly once. The verifier enumerates every such bijection recursively; independently, its subset-dynamic-programming permanent computation also gives 24. Taking the downward closure of all 24 perfect matchings generates exactly 2,201 nonempty faces. Their face numbers in dimensions \(0\) through \(6\) are
\[
(21,168,560,756,504,168,24).
\]

Construct a partial matching on the **nonempty** face poset as follows. Initially all 2,201 faces are unpaired. Visit the 21 ordered graph-edge labels \(e\) in increasing order. At stage \(e\), take every still-unpaired face \(\sigma\) not containing \(e\), in increasing integer bitmask order, and pair it with \(\sigma\cup\{e\}\) exactly when that larger face is also still unpaired. Each pair is a codimension-one face inclusion. The process produces exactly 1,092 pairs and leaves exactly one unpaired vertex and sixteen unpaired two-simplices.

The crucial nonstandard step is acyclicity. The verifier enumerates every codimension-one inclusion of nonempty faces (8,736 incidences). It directs unmatched inclusions from the larger face to the smaller and reverses the direction on the 1,092 matched inclusions. A complete Kahn topological sort visits all 2,201 vertices of this directed Hasse graph. A topological sort of every vertex exists if and only if this finite directed graph has no directed cycle, so the displayed pairing is an **acyclic discrete-Morse matching**.

Forman's discrete-Morse theorem supplies a homotopy-equivalent CW complex with precisely one 0-cell and sixteen 2-cells, with no cells in any other dimension. Because there are no 1-cells, all sixteen attaching maps \(S^1\to\{\mathrm{pt}\}\) are constant. The resulting CW complex is a wedge of sixteen two-spheres. This proves the claimed integral homotopy type, not merely field-dependent Betti numbers.

## Verification
Run `python3 verify_heawood_perfect_matching.py` with Python 3's standard library. The checker generates all graph incidences, tests the Fano two-point incidence axiom, computes the permanent by independent subset dynamic programming, enumerates all facets and their complete downward closure, builds the stated deterministic 1,092-pair Morse matching, checks every pair and all 8,736 Hasse covers, and exhaustively topologically sorts the reversed-cover graph. It also independently computes simplicial boundary ranks over \(\mathbb F_2\) as \((20,148,396,360,144,24)\) in degrees \(1\) through \(6\), yielding ordinary Betti numbers \((1,0,16,0,0,0,0)\). The expected successful terminal marker is `VERIFY_OK`. The integral homotopy conclusion rests on the acyclic matching rather than on the mod-two calculation.

## Relationship to prior work
An established computation for the **ordinary** Heawood matching complex gives \(\mathcal M(H)\simeq\bigvee^{16}S^4\). That is a different simplicial complex: all matchings are allowed, including those not extendible to a perfect matching, so its 3,461 nonempty faces are not the 2,201 faces considered here. Its sphere-wedge conclusion does not imply the present subcomplex homotopy type. In particular, the coincidence of multiplicity 16 is not a deduction of the present result.

Bayer, Jelić Milutinović and Vega define and classify perfect-matching complexes for specified honeycomb graphs, and raise the problem of understanding such complexes more widely for bipartite graphs. Their honeycomb theorem does not cover the nonplanar Fano-plane incidence graph. General matching/chessboard complex classifications for complete or polygonal graph families similarly do not imply this exact sparse-graph complex. Kozlov's simple-homotopy methods supply background for the acyclic matching approach, rather than the graph-specific conclusion.

## Limitations
The theorem is about one naturally distinguished finite graph and the extendible-matching subcomplex. It does not classify perfect-matching complexes of arbitrary cubic, incidence, or bipartite graphs, and it does not determine the inclusion-induced map into the ordinary matching complex. The proof uses exhaustive finite checks whose source code is supplied; a short pen-and-paper symbolic classification of all gradient paths is not claimed. Targeted searches found no equivalent covering statement, but absence from indexed sources cannot establish absolute historical novelty.

## References
1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613; first publicly submitted 2005-03-28; primary MSC 57Q10.
2. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect matching complexes of honeycomb graphs*, arXiv:2209.02803, first publicly submitted 2022-09-06; particularly the definition and their honeycomb family results and questions about other bipartite graphs.
3. M. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, Algebra Universalis 49 (2003), 345–385.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
