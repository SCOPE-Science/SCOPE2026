# A sharp two-edge reserve for induced-matching reconfiguration in the Pappus graph

## Finding
Let \(P\) be the eighteen-vertex Pappus graph. It has induced-matching number \(\nu_s(P)=5\) and exactly \(27\) maximum induced matchings. Every maximum induced matching is frozen under one-edge replacement.

For \(b\in\{3,4\}\), let \(\mathcal T_b(P)\) have as vertices all induced matchings of sizes between \(b\) and \(5\), with adjacent matchings differing by adding or deleting exactly one graph edge. Then
\[
\mathcal T_4(P)\cong 27K_{1,5},\qquad
\mathcal T_3(P)\cong B_{396}\sqcup 153K_1,
\]
where \(B_{396}\) is connected and contains all \(27\) maximum induced matchings. Thus a reserve of two deleted edges is necessary and sufficient to connect every pair of optima by legal single-edge additions/deletions. There are exactly \(153\) inclusion-maximal induced matchings of size \(3\), and no inclusion-maximal induced matchings of any other size besides \(3\) and \(5\).

Let \(\mathcal H\) have the \(27\) maximum induced matchings as vertices, joining distinct \(M,N\) when \(|M\cap N|=3\). Then \(\mathcal H\) is a four-regular graph with \(54\) edges, isomorphic to the line graph \(L(P)\), and for every pair of maximum matchings,
\[
d_{\mathcal T_3(P)}(M,N)=4d_{\mathcal H}(M,N).
\]
The \(351\) unordered pairs of different maximum induced matchings have exact distance spectrum \(54\) pairs at distance \(4\), \(108\) at distance \(8\), \(162\) at distance \(12\), and \(27\) at distance \(16\). In particular the largest optimum-to-optimum distance is \(16\).

## Assumptions and scope
The labeled graph has nine point vertices \(p_{x,y}\) and nine line vertices \(\ell_{m,b}\), where \(x,y,m,b\in\mathbb F_3\); incidence is \(p_{x,y}\sim\ell_{m,b}\) exactly when \(y=mx+b\). Order the points and lines lexicographically by their coordinate pairs; number points \(0,\ldots,8\), lines \(9,\ldots,17\), and the \(27\) graph edges lexicographically as \(e_0,\ldots,e_{26}\). This is the standard biaffine incidence realization of the Pappus graph. An *induced matching* \(M\subseteq E(P)\) is an edge set whose endpoints induce exactly \(|M|\) independent copies of \(K_2\). A matching is *maximum* if its cardinality is \(\nu_s(P)\), and *maximal* if it cannot be enlarged by adding an edge. These notions are not interchangeable.

The reserve is measured relative to the optimum five edges: a path in \(\mathcal T_b(P)\) may never use fewer than \(b\) edges, and each step changes the edge set by exactly one element. Distances in the theorem are shortest-path distances inside \(\mathcal T_3(P)\), restricted to its \(27\) optimum vertices; no claim is made about the full component's diameter.

## Proof
Two distinct graph edges \(uv\) and \(ab\) are mutually compatible for an induced matching if and only if the four endpoints are distinct and neither endpoint of the first is adjacent to either endpoint of the second. Consequently induced matchings are exactly the independent sets in the conflict graph on the \(27\) Pappus edges, with conflict defined by shared or adjacent endpoints.

**Exhaustive bounded search.** Let \(C_i\) be the bit mask of all graph edges that conflict with edge \(e_i\), including itself. Recursively enumerate masks \(S\) in increasing edge-index order, and after including index \(i\) restrict the remaining candidates to indexes not in \(C_i\). Every induced matching appears exactly once: its sorted index tuple supplies the unique recursion path, and all other paths are excluded by the increasing order. The resulting cardinality counts for \(k=0,1,2,3,4,5,6\) are
\[
(|I_0|,\ldots,|I_6|)=(1,27,189,387,135,27,0).
\]
Because every induced matching of size more than six contains one of size six, \(I_6=\varnothing\) proves \(\nu_s(P)=5\). Examine all single-edge additions to all enumerated masks. Exactly \(153\) size-three masks and all \(27\) size-five masks have no extension; there are no other maximal masks. No pair of distinct size-five masks shares four edges, so direct one-edge replacements cannot move between optima.

**Reserve-four graph.** Every size-five set has exactly five size-four subsets. The \(135=5\cdot27\) size-four masks each have a unique size-five extension, as checked against the exhaustive list. Addition/deletion changes cardinality parity, so size-four states are adjacent only to size-five states in \(\mathcal T_4(P)\); therefore its components are precisely \(27\) stars \(K_{1,5}\).

**Reserve-three graph.** Enumerate all \(549=387+135+27\) masks of cardinality at least three. Insert an undirected transition whenever the two masks differ by exactly one graph edge, obtaining \(675\) transitions. Exact connected-component traversal gives a single \(396\)-vertex component and \(153\) isolated size-three masks. All \(27\) optima lie in the large component.

**Compressed optimum geometry.** Two distinct optima admit a legal four-step path descending to three edges and returning to five if and only if they share three edges. The direct four-step relation is therefore exactly \(|M\cap N|=3\). Checking all \(351\) optimum pairs produces a four-regular, \(54\)-edge graph \(\mathcal H\). The accompanying certificate specifies a bijection from all \(27\) optimum masks to the \(27\) indexed edges of \(P\). Checking all \(351\) pairs verifies that optimum overlap-three adjacency is equivalent to the corresponding graph edges sharing an endpoint. This supplies an explicit graph isomorphism \(\mathcal H\cong L(P)\), not merely a numerical or spectral resemblance.

**Exact distances.** Breadth-first searches in the complete \(549\)-state graph, rooted separately at each optimum, visit \(396\) states each. A second family of breadth-first searches in \(\mathcal H\) verifies for all \(27\cdot27\) ordered optimum pairs that the first distance is exactly four times the second. The distance histogram in the finding follows by counting unordered pairs. Since no shorter path has been missed in an exhaustive breadth-first traversal, the equality is exact for this finite graph.

## Verification
The supplied `verify_incidence.py` constructs the graph from affine incidence, enumerates all compatible edge sets recursively using explicit conflict masks, checks inclusion-maximality, reconstructs the reserve-four and reserve-three transition graphs, compares every optimum-to-optimum distance, and checks the complete bijective line-graph certificate. `verify_lcf.py` independently constructs the graph from the LCF sequence `[5,7,-7,7,-7,-5]` repeated three times, enumerates edge sets by direct combinations with a separate endpoint test, verifies an explicit vertex isomorphism between the two graph presentations, and independently reconstructs all reserve-three transitions and optimum distances. Both scripts require only Python's standard library and `induced_matching_certificate.json`. Run them in the same folder with `python3 verify_incidence.py` and `python3 verify_lcf.py`. Both must print `VERIFY_OK`. The certificate provides all \(549\) reserve-three states, all \(675\) transitions, all \(27\) optimum masks, and an explicit \(27\)-entry line-graph isomorphism.

## Relationship to prior work
Basavaraju, Heggernes, van 't Hof, Saei and Villanger (2013) establish general bounds and algorithms for maximal induced matchings in triangle-free graphs. Their results do not imply the particular maximum-size census, reconfiguration threshold, or metric for the Pappus incidence graph. Ito, Kamiński and Ono (2014) study token jumping of independent sets and shortest transformation algorithms; representing induced matchings by independent sets in the square of a line graph relates the general concepts, but their results do not supply this explicit two-edge-deficit metric. Dabrowski, Demange and Lozin (2013) study maximum induced matchings in bipartite and regular graph classes; the accessible record describes complexity results and a hypercube formula, but its complete text was not accessible for comparison. Its possible overlap remains a stated limitation.

Previously published computations of the ordinary Pappus matching complex concern pairwise vertex-disjoint graph edges (not induced matchings), and establish its homotopy type. Those face counts or topological conclusions do not determine which disjoint matchings are induced, or the present length-constrained transformation graph. Other published affine constructions demonstrate locally non-improvable induced matchings in separate graph families; they neither identify these \(27\) Pappus optima nor determine reserve-three transformations. Exact priority against unindexed material is not certified by search alone.

## Limitations
This is a finite, exhaustive classification of the specified eighteen-vertex graph, not a theorem for all cubic bipartite graphs. The line-graph isomorphism is witnessed by a completely checked explicit permutation; a more conceptual automorphism-equivariant description is not claimed. The metric statement concerns only pairs of optimum states inside the reserve-three configuration graph. A relevant general paper on regular bipartite induced matchings was available only through its abstract and bibliographic details; hidden Pappus-specific work could in principle overlap. No independent external scientific audit has been performed.

## References
1. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei and Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180v1, first public 2013-12-18. https://arxiv.org/abs/1312.5180
2. T. Ito, M. Kamiński and H. Ono, *Fixed-Parameter Tractability of Token Jumping on Planar Graphs*, arXiv:1406.6567, first public 2014-06-25. https://arxiv.org/abs/1406.6567
3. K. K. Dabrowski, M. Demange and V. V. Lozin, *New results on maximum induced matchings in bipartite graphs and beyond*, Theoretical Computer Science 478 (2013), 33–40. https://doi.org/10.1016/j.tcs.2013.01.027
4. *Integral homotopy type of the Pappus graph matching complex*, publicly available mathematical calculation (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-pappus-graph-matching-complex--db6c6c11f317
5. *Order-Optimal Affine Locality Witnesses*, publicly available mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/16/SCOPE010
6. *Pappus Graph*, Wolfram MathWorld, for the standard incidence/LCF descriptions. https://mathworld.wolfram.com/PappusGraph.html
