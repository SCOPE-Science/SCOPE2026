# The Moser spindle has box-complex \(\mathbb Z_2\)-index one despite requiring four colors

## Finding
Let \(M\) be the seven-vertex Moser spindle, presented explicitly by
\[
V(M)=\{0,1,2,3,4,5,6\},\qquad
E(M)=\{01,02,12,13,23,04,05,45,46,56,36\}.
\]
Let \(\mathsf L(M)\) be the Lovász complex of nonempty common-neighbor-closed vertex subsets, with its standard free involution \(A\mapsto\operatorname{CN}(A)\), and let \(\mathsf B(M)\) be the Matoušek–Ziegler box complex. Then \(\mathsf L(M)\) admits **eight complete involution-orbits of free-face collapses** onto a connected one-dimensional free \(\mathbb Z_2\)-complex \(Q\), and
\[
\operatorname{ind}_{\mathbb Z_2}\mathsf B(M)
=\operatorname{ind}_{\mathbb Z_2}\mathsf L(M)=1,
\qquad \chi(M)=4.
\]
In particular the standard box-complex index bound gives only \(\chi(M)\ge3\), not the sharp value four. The collapse also yields the ordinary homotopy types
\[
\mathsf L(M)\simeq\bigvee^5 S^1,
\qquad Q/\mathbb Z_2\simeq\bigvee^3S^1,
\]
with \(Q\) having \(18\) vertices and \(22\) edges, and its quotient having \(9\) vertices and \(11\) edges. The nonequivariant five-circle conclusion is contextual, not claimed as new.

## Assumptions and scope
The graph is the precise simple loopless graph defined above, isomorphic to the usual Moser spindle (Hajós merge of two copies of \(K_4\)). For \(\varnothing\ne A\subseteq V(M)\), define
\[
\operatorname{CN}(A)=\bigcap_{a\in A}N_M(a).
\]
The vertices of \(\mathsf L(M)\) are exactly the nonempty sets \(A\) for which \(\operatorname{CN}(A)\ne\varnothing\) and \(\operatorname{CN}^{2}(A)=A\); its simplices are the strict nonempty inclusion chains. The involution sends the chain \(A_1\subset\cdots\subset A_k\) to \(\operatorname{CN}(A_k)\subset\cdots\subset\operatorname{CN}(A_1)\). The index is the least \(d\ge0\) for which a continuous equivariant map to the antipodal sphere \(S^d\) exists. All homotopies and graph ranks in the finding are integral and no geometric embedding needs to be fixed.

## Proof
**1. Closed sets and involution.** The graph-neighborhood intersections give precisely the eighteen closed subsets, listed in `moser_collapse_certificate.json`. There are \(38\) strict two-term chains, \(16\) three-term chains, and no longer chains. The involution is an order-reversing bijection on these closed subsets, because \(\operatorname{CN}^3=\operatorname{CN}\). Every \(A\) is disjoint from \(\operatorname{CN}(A)\), since the graph is loopless. Therefore no vertex is fixed; also a chain simplex cannot be invariant, because two exchanged sets would have to be comparable, whereas \(A\) and \(\operatorname{CN}(A)\) are nonempty disjoint sets. Hence the induced simplicial involution is free on the realization.

**2. Free-face certificates.** Index the eighteen closed sets in ascending order of cardinality followed by lexicographic order, starting at zero as recorded in the certificate. For each of the eight orbit records in `moser_collapse_certificate.json`, its `edge` occurs in exactly the indicated `triangle` among the triangles present at that stage, and the `partner_edge` occurs uniquely in `partner_triangle`; these two edge–triangle pairs are exchanged by the involution. Delete both free-face pairs in order. Since there are no simplices above dimension two, each deletion is an elementary simplicial collapse. The list exhausts all \(16\) original triangles without deleting a vertex. Consequently the result \(Q\) is a one-dimensional \(\mathbb Z_2\)-equivariant strong deformation retract with \((f_0,f_1)=(18,22)\).

**3. Connectivity and index.** The residual graph has a connected spanning search from vertex zero visiting all eighteen vertices. Its involution has no fixed vertex and no edge mapped to itself, as explicitly checked. The graph quotient therefore has nine vertex orbits and eleven edge orbits, and is connected. A connected finite graph with \(V\) vertices and \(E\) edges is a wedge of \(E-V+1\) circles, yielding five and three circles before and after quotient. Since \(Q\) is a free one-dimensional \(\mathbb Z_2\)-complex, an equivariant map \(Q\to S^1\) exists (choose antipodally paired, generic image vertices in the circle and extend linearly along edges, avoiding the origin, then normalize). Thus \(\operatorname{ind}_{\mathbb Z_2}Q\le1\). Because \(Q\) is connected and the involution is nontrivial, there is no equivariant map \(Q\to S^0\); therefore the index is exactly one. Equivariant strong deformation retraction preserves index. The theorem of Csorba–Lange–Schurr–Wassmer identifies the box and Lovász complex indices by a \(\mathbb Z_2\)-equivariant deformation, giving the asserted box index.

**4. Chromatic boundary.** The induced subgraphs on \(\{0,1,2,3\}\) and \(\{0,4,5,6\}\) are two diamonds (\(K_4\) with missing edges \(03\) and \(06\)). In any proper three-coloring of a diamond, its two nonadjacent degree-two vertices have the same color. Hence both \(3\) and \(6\) must receive the color of \(0\), contradicting the edge \(36\). Conversely \(0,3\) may receive color one, \(1,4\) color two, \(2,5\) color three, and \(6\) color four, proving \(\chi(M)=4\).

## Verification
Run `python3 verify_moser_box.py` from the directory containing the files; it generates and checks `moser_collapse_certificate.json` using only the Python standard library. The exact finite replay independently enumerates all subsets, closure and involution maps, chains, free-face-orbit pairs, residual connectivity, quotient orbit counts, and all possible three-colorings versus existence of a four-coloring. The recorded successful check is `MOSER_BOX_INDEX_VERIFY_OK`. The certificate is not an infinite-family extrapolation: the theorem concerns one explicitly defined seven-vertex graph, and all relevant faces are exhaustively enumerated. The passage from an equivariant graph collapse to index one is the mathematical argument in Step 3, not a numerical inference.

## Relationship to prior work
Matoušek–Ziegler, *Topological lower bounds for the chromatic number: A hierarchy* (arXiv:math/0208072, 2002), compare the box-complex index with other chromatic bounds. Csorba–Lange–Schurr–Wassmer, *Box complexes, neighborhood complexes, and the chromatic number* (arXiv:math/0310339, 2003), provide the equivariant identification of box and Lovász complex and an index upper bound in the absence of certain complete bipartite subgraphs. The Moser spindle contains two four-cycles, hence contains \(K_{2,2}\), and their \(K_{2,2}\)-free index-one bound does not apply. Braun–Vega, *Hajós-Type Constructions and Neighborhood Complexes* (arXiv:1812.07991, 2018), obtain nonequivariant circle-wedge phenomena under Hajós merges but not this exact free \(\mathbb Z_2\) index. The recorded result *Graph-like neighborhood complexes with edge-disjoint four-cycles* directly implies the ordinary five-circle homotopy type in this graph (\(v=7\), \(e=11\), two edge-disjoint squares), but explicitly makes no equivariant claim. The present finding is limited to the exact involution-orbit collapse and topological index distinction.

## Limitations
No new nonequivariant circle multiplicity is claimed; a broader earlier result covers it. The construction determines the index for this graph only, not arbitrary Hajós merges, arbitrary four-chromatic unit-distance graphs, or every topological chromatic invariant. Although relevant literature and indexed mathematical results were compared, publication priority over inaccessible or unindexed equivalent treatments is not proven. The rank statements concern the Lovász complex and its quotient, not a classification of the box complex as a simplicial object.

## References
1. J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: A hierarchy*, arXiv:math/0208072 (first public posting 2002-08-09), https://arxiv.org/abs/math/0208072.
2. P. Csorba, C. Lange, I. Schurr, and A. Wassmer, *Box complexes, neighborhood complexes, and the chromatic number*, arXiv:math/0310339 (first public posting 2003-10-21), https://arxiv.org/abs/math/0310339.
3. B. Braun and J. Vega, *Hajós-Type Constructions and Neighborhood Complexes*, arXiv:1812.07991 (first posted 2018-12-19), https://arxiv.org/abs/1812.07991.
4. *Graph-like neighborhood complexes with edge-disjoint four-cycles*, public record https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-graph-like-neighborhood-complexes-with-edge-disjoint-four-cycles--d8f86495e49d/RESULT.md.
5. E. W. Weisstein, *Moser Spindle*, MathWorld, https://mathworld.wolfram.com/MoserSpindle.html.
