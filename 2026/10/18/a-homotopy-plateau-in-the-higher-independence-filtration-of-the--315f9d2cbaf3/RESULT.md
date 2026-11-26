# The fourth higher-independence complex of the Möbius–Kantor graph

## Finding

Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph on vertices \(u_0,\ldots,u_7,v_0,\ldots,v_7\). For \(r\ge1\), let \(\operatorname{Ind}_r(M)\) be the complex of subsets whose induced connected components all have at most \(r\) vertices. Then
\[
\boxed{\operatorname{Ind}_4(M)\simeq\bigvee^{21} S^7.}
\]
In particular its reduced sixth homology vanishes over every field and over \(\mathbb Z\), whereas its integral seventh homology is free of rank 21. In the inclusion from cutoff three to cutoff four, all the degree-six classes in the preceding stage therefore die. This identifies the homotopy type at the first stage after the known cutoff-two to cutoff-three plateau.

## Assumptions and scope

The undirected edges are \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+3}\}\) for \(0\le i<8\), with indices modulo eight. These are components of the induced subgraph on the selected vertices, not a matching or a graph-distance condition. No assertion is made for other graphs or cutoffs beyond the use of the preceding plateau as context.

## Proof

**Admissible faces.** Encode \(u_i\) by bit \(i\) and \(v_i\) by bit \(8+i\). A subset fails the cutoff-four condition precisely when it contains a connected five-vertex subset: if an induced component has at least five vertices, take a spanning tree in that component and grow a connected set to five vertices. Generate the connected five-vertex masks by starting at all singletons and repeatedly adjoining an adjacent vertex. Remove every superset of a connected five-vertex mask from the \(2^{16}\) masks to obtain exactly the allowable faces. The enumeration in `verify.py` gives 21,973 allowable faces (including the empty face).

**Acyclic matching.** Visit bits in the order \(15,14,\ldots,8,0,1,\ldots,7\). For a bit \(j\), pair each still-unmatched face \(a\) not containing that bit with \(a\cup\{j\}\) if both faces are present and still unmatched. At a fixed bit these pairs cannot compete, since each face belongs to a unique bit-toggle pair. Orient all codimension-one face incidences downward except for these pairs, which are reversed. Topological sorting exhausts the 21,973 faces and verifies acyclicity of all 135,760 oriented incidences. The computation gives 10,976 matched pairs including the empty face paired with a vertex, and exactly 21 unmatched faces, each with eight vertices. All counts and the full topological-sort test are recomputed by `verify.py`; see `certificate.json` for the expected output.

**Homotopy conclusion.** Delete the empty face and its pair from the augmented calculation, retaining its former partner as a critical vertex. This gives an acyclic matching on the nonempty face poset: the oriented graph is obtained from the augmented one by deleting the empty vertex and its incident arrows. The discrete Morse theorem for simplicial complexes gives a CW model with that single zero-cell and the 21 critical cells in dimension seven, with no cells in the intervening dimensions. Every seven-cell is attached to a point, so this CW model is a wedge of 21 seven-spheres. No inference from numerical Betti ranks or assumptions on higher attaching maps is required.

## Relationship to prior work

Deshpande and Singh study the same component bound on paths, cycles, multipartite graphs, whiskered graphs and certain trees. The graph here has an induced outer eight-cycle and is not chordal, so the separate chordal higher-independence theorems do not supply its cutoff-four type. The cutoff-two wedge of three six-spheres is known for the same graph, and a separate computation gives a simplicial collapse of the cutoff-three complex onto it. Neither of those calculations gives the cutoff-four homotopy type: the new faces introduced at cutoff four are not part of the relative collapse. The contribution here is only the cutoff-four type and the resulting loss of degree-six homology at the upper end of the plateau, not a new determination of the earlier spaces or of their inclusion.

## Verification and limitations

Run `python3 verify.py` and compare the parsed JSON to `certificate.json`. The discrete computation is exhaustive for this graph and cutoff; the homotopy conclusion uses the discrete Morse theorem as above. No other filtration stage or family of graphs is classified here.

## References

1. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145, Theorem 3.4.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448.
3. P. Deshpande, S. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775.
4. *Three six-spheres in the two-independence complex of the Möbius–Kantor graph*, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-three-six-spheres-in-the-two-independence-complex-of-the-m-bius--2b99cf38fc97.
5. *An elementary collapse between Möbius–Kantor higher independence complexes*, https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-an-elementary-collapse-between-m-bius-kantor-higher-independence--2a89db0cb1fd.
