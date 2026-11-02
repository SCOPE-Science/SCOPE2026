# Two tetrahedral windmills in Pappus edge-Kempe reconfiguration

## Finding
Let \(P\) be the eighteen-vertex Pappus graph (the Levi graph of the Pappus \((9_3)\) configuration). Form the simple graph \(\mathcal K(P)\) on all **proper edge-colourings with the three individually named colours** \(0,1,2\). An edge of \(\mathcal K(P)\) interchanges two colours on precisely one whole connected component of the bichromatic subgraph. Let \(\overline{\mathcal K}(P)\) identify configurations under all six global permutations of the colour names, remove loops, and retain one edge between each distinct pair of orbits.

Then \(\mathcal K(P)\) has exactly \(120\) vertices and \(324\) edges, partitioned into **two isomorphic bipartite components of order \(60\)**. Each component has \(162\) edges, radius \(4\) and diameter \(4\), with \(54\) degree-five and \(6\) degree-nine vertices. Every vertex has eccentricity \(4\). Moreover,

\[
\overline{\mathcal K}(P)\cong
\bigl(K_1\vee(3K_3)\bigr)\ \sqcup\
\bigl(K_1\vee(3K_3)\bigr).
\]

Thus each ten-state colour-unlabelled sector is a union of three copies of \(K_4\) sharing exactly one vertex. The labelled sectors are bipartite although each colour-unlabelled quotient contains triangles.

Within either sixty-state component, the distance spheres from a degree-five vertex have sizes \((1,5,17,25,12)\), while those from a degree-nine vertex have sizes \((1,9,27,21,2)\). The counts of unordered vertex pairs at distances \(1,2,3,4\) are respectively \((162,540,738,330)\).

## Assumptions and scope
All graphs are finite, undirected and simple. The Pappus graph has vertices \(0,\ldots,17\) and the edges of an eighteen-cycle, together with the third edges prescribed by the repeated LCF offsets \([5,7,-7,7,-7,-5]^3\): for each vertex \(i\), include \(\{i,(i+s_i)\bmod18\}\). Duplicates are removed, giving \(27\) edges. A proper named-colour edge-colouring assigns one of \(0,1,2\) to each edge so that the three incident colours at each vertex differ. A Kempe move swaps two colours on one entire bichromatic cycle; the swap must be nontrivial. The theorem concerns precisely this graph and these moves, with colour labels preserved except in the explicitly defined quotient.

## Proof
**Exhaustive state enumeration.** Order the \(27\) edges lexicographically. Backtracking assigns each colour at most once at each incident vertex, recording a state precisely when all edges are coloured. The complete enumeration gives \(120\) named colourings, independently corroborated by the representation as ordered triples of disjoint perfect matchings. The Pappus graph has exactly \(42\) perfect matchings, and exactly \(20\) unordered three-factor partitions of its edge set, each having \(6\) colour namings.

**Complete move classification.** Every bichromatic subgraph is an even two-factor. For each colouring and each of the three unordered colour pairs, traverse all connected cycles and interchange those two colours on precisely one cycle; canonicalize the resulting named colouring. Exhaustive traversal gives \(108\) colourings for which the three two-factor cycle-length profiles are \((6,6,6),(18),(18)\), and \(12\) for which they are \((6,6,6),(6,6,6),(6,6,6)\). Hence precisely \(108\) vertices have degree \(3+1+1=5\) and \(12\) have degree \(3+3+3=9\), with \((108\cdot5+12\cdot9)/2=324\) undirected moves. The adjacency certificate lists all \(120\) states and all neighbours.

**Components and quotient shape.** Breadth-first search on the complete adjacency list yields two components, each containing \(60\) states and \(162\) moves. Canonicalizing each colouring under the six palette permutations gives \(20\) distinct colour-unlabelled states. In each quotient component, one state has nine distinct quotient neighbours, the other nine states each have three. Deleting the degree-nine state leaves three disjoint triangles: each of the remaining vertices has precisely its two triangle partners as neighbours. This is exactly \(K_1\vee(3K_3)\) in each sector. The explicit vertex permutation

`(0,1,8,7,6,5,4,3,2,13,14,15,16,9,10,11,12,17)`

is a graph automorphism of \(P\), and its action on edge-colourings maps one of the sixty-state sectors bijectively onto the other while preserving the Kempe adjacencies. Therefore the two components are isomorphic.

**Bipartiteness and exact metric.** Fix a bipartition side of \(P\) containing nine vertices and, at each vertex on that side, order its three incident edges. Multiply the signs of the induced permutations of the three colours across that side. Every allowed bichromatic cycle has length six or eighteen, and so passes through exactly three or nine vertices on the fixed side. A Kempe switch reverses the local two-colour order at each of those vertices, changing the product sign. Therefore every edge of \(\mathcal K(P)\) flips the sign, establishing bipartiteness. Full breadth-first searches from every named colouring in each component give eccentricity exactly \(4\), the stated two distance-sphere sequences, and the unordered pair-distance counts. These finite searches are exhaustive, not samples; the complete list of states and edges is retained in `certificate.json`.

## Verification
Run `python3 verify_lcf.py --check certificate.json` and `python3 verify_incidence.py certificate.json` from the directory containing the three files. Both programs use only Python's standard library. The former constructs \(P\) in LCF coordinates and generates all colourings by assigning colours to edges; the latter constructs \(P\) from the nine Pappus incidence triples, generates perfect matchings recursively, and builds all ordered one-factorizations. They independently construct Kempe moves and recompute complete shortest-path distances and the two ten-vertex quotient graphs. They compare the independently constructed named-state and adjacency lists with the stored finite certificate. No probabilistic or approximate arithmetic is used.

## Relationship to prior work
Belcastro and Haas (arXiv:1209.1730, first posted 2012-09-08) developed edge-Kempe equivalence-class counting for three-edge-coloured cubic graphs. Belcastro and Haas (2017) further defined and studied the full named-colouring edge-Kempe graph, with general theorems and explicit examples on cyclic prisms, but no Pappus-specific theorem in the inspected journal text. Goedgebeur and Östergård (arXiv:2105.01363, first posted 2021-05-04) provided extensive equivalence-class census data through thirty vertices for cubic graphs, without a component-level distance classification in their inspected text. Thus the existence or count of two equivalence classes is not asserted as a discovery on its own. The proposed new content is the exact **two-windmill quotient decomposition**, the isomorphism of the labelled sectors, their bipartite yet self-centered metric, and the complete degree and distance-sphere statistics. The 2021 work's general census does not imply those metric or quotient-adjacency assertions from its published tables alone.

## Limitations
This is an exact theorem about one canonical eighteen-vertex graph; no infinite-family generalization or mixing-time bound follows. The calculation does not establish absolute historical priority: an equivalent component metric or quotient description could be implicit in unindexed graph databases or older computational manuscripts. The six vertex colours are named, whereas the quotient explicitly forgets global colour names; confusing these conventions changes every state count. The graph-theoretic distance-four conclusion applies only to pairs within a Kempe component, not to pairs in different components.

## References
1. S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730 (2012-09-08), https://arxiv.org/abs/1209.1730.
2. S.-M. Belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, Australasian Journal of Combinatorics 69(2) (2017), 197–214, https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf.
3. J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, arXiv:2105.01363 (2021-05-04), https://arxiv.org/html/2105.01363v1.
4. Pappus graph, LCF representation \([5,7,-7,7,-7,-5]^3\), https://en.wikipedia.org/wiki/Pappus_graph (graph identification only).
