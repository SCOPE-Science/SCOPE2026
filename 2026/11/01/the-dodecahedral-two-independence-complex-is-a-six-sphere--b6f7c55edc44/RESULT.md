# The dodecahedral two-independence complex is a six-sphere

## Finding
Let \(D\) be the twenty-vertex dodecahedral graph. Its two-independence complex \(K=\operatorname{Ind}_2(D)\), consisting of vertex subsets whose induced connected components have at most two vertices, has **integral homotopy type**
\[
\boxed{K\simeq S^6.}
\]
In particular, \(\widetilde H_6(K;\mathbb Z)\cong\mathbb Z\) and \(\widetilde H_j(K;\mathbb Z)=0\) for every integer \(j\ne6\). This classifies homotopy type, not only Betti numbers.

## Assumptions and scope
Use the generalized Petersen model \(D=GP(10,2)\), with vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/10\mathbb Z\), and with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). For reproducible face encoding, assign \(u_i\mapsto i\), \(v_i\mapsto10+i\), and encode a vertex subset by the nonnegative integer \(\sum_{i\in S}2^i\). A simplex belongs to \(K\) if and only if every selected vertex has at most one selected neighbor. Equivalently, \(K\) is the independence complex of the hypergraph whose hyperedges are all three-vertex wedges consisting of a vertex and two of its neighbors. There are exactly sixty such forbidden triples.

The theorem concerns this twenty-vertex simple graph and parameter two. The higher-independence complex is distinct from the ordinary independence complex (parameter one), the edge-matching complex, and the face-hypergraph theta complexes of the dodecahedron.

## Proof
**Complete face set.** The verifier supplies two independent exhaustive constructions. In the first, insert vertices in increasing encoding order, adding a vertex only if the induced selected degrees remain at most one. In the second, test all \(2^{20}\) vertex subsets against the sixty forbidden length-two wedges. The resulting face sets agree exactly and contain 63,143 simplices including the empty face. The face vector, in dimensions zero through eleven, is
\[
(20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5).
\]
The maximal faces number 510, occurring in dimensions seven, eight, nine and eleven with multiplicities 25, 60, 420 and 5 respectively. These counts are not substituted for a homotopy argument.

**Explicit matching.** On the nonempty face poset use the vertex order
\[
(11,0,1,15,13,18,9,16,4,19,10,7,12,8,2,6,5,3,14,17).
\]
At each vertex \(v\), scan the remaining simplex masks in increasing numerical order. Whenever \(\sigma\) does not contain \(v\) and both \(\sigma\) and \(\sigma\cup\{v\}\) remain, match them and remove both. This algorithm determines every pairing without discretionary choices. It makes exactly 31,570 disjoint covering pairs and leaves precisely the two simplex masks 2048 and 156434. The first is the vertex \(v_1\); the second is the seven-element set
\[
\{u_1,u_4,u_8,u_9,v_3,v_4,v_7\},
\]
so their dimensions are zero and six. (Here integer vertex 11 is \(v_1\).)

**Acyclicity and conclusion.** Orient every cover edge of the nonempty-face Hasse diagram downward, except each matched cover, which is reversed upward. Exhaustively constructing this directed diagram gives 63,142 vertices and 410,500 arrows. An exact topological sort visits all 63,142 vertices, proving that the matching has no directed cycles. By the discrete Morse theorem, \(K\) is homotopy equivalent to a CW complex with exactly one zero-cell and one six-cell, and no cells of any other dimension. The unique six-cell has a constant attaching map to the zero-cell, so that CW complex is \(S^6\). This finishes the integral homotopy proof.

## Verification
Run `python3 verify_dodecahedron.py` with the Python standard library. The program rebuilds \(GP(10,2)\) from the edge rule above, compares two complete face-enumeration methods, checks the face and facet vectors, builds the deterministic matching, and verifies acyclicity across the full directed Hasse diagram. Expected output is included in `verify_dodecahedron.out`; its final marker is `ALL_CHECKS_PASS`. The source and output reproduce the exact integer mask and incidence counts used in the proof. No field-homology extrapolation is involved.

## Relationship to prior work
Conant and Thistlethwaite's study of independence and theta complexes of hypergraphs (initially public August 5, 2008) motivates studying hypergraphs attached to regular polyhedra. Their explicitly calculated dodecahedral hypergraphs use polytope edges or pentagonal faces, not the three-vertex induced wedges used here. Paolini and Salvetti discuss the broader higher-independence viewpoint in their braid-group construction. Deshpande and Singh develop homotopy classifications for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees; none of those families includes the dodecahedral graph, and their theorems do not determine this case.

Earlier calculations of the dodecahedral *ordinary* independence and matching complexes address different face conditions. A common graph, numerical sphere dimension or graph symmetry is not itself an implication of the present theorem; no previously inspected statement determines the homotopy of the two-independence complex of this graph.

## Limitations
This is a single finite-graph classification. It does not prove an analogous homotopy statement for arbitrary generalized Petersen graphs, higher parameters, or arbitrary three-regular graphs; it does not classify automorphism actions, quotient homology, or equivariant homotopy type. The computational proof is finite and fully exhaustive for the stated complex, but no independent mathematical audit has been performed. Publication-priority uncertainty remains for unindexed or inaccessible equivalent prior calculations.

## References
1. J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739 (first public version 2008-08-05; expanded version 2010), https://arxiv.org/abs/0808.0739 .
2. G. Paolini and M. Salvetti, *Weighted sheaves and homology of Artin groups*, arXiv:1703.02586 (first public version 2017-03-07), https://arxiv.org/abs/1703.02586 .
3. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (first public version 2020-01-15), https://arxiv.org/abs/2001.05448 .
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145; discrete Morse homotopy theorem.
