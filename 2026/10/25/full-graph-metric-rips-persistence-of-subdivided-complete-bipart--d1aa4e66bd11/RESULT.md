# Full graph-metric Rips persistence of subdivided complete bipartite graphs

## Finding

Let \(m,n\ge2\) be arbitrary integers and let \(X_{m,n}=S(K_{m,n})\) be the graph obtained by subdividing every edge of the complete bipartite graph once. Endow its vertices with shortest-path distance and use the inclusive Vietoris--Rips convention. Set \(b=(m-1)(n-1)\) and \(N=m+n+mn\). Then, for all real \(r\ge0\),
\[
\operatorname{VR}_{\le r}(X_{m,n})\simeq
\begin{cases}
\bigvee^{N-1}S^0,&0\le r<1,\\
\bigvee^{b}S^1,&1\le r<3,\\
\bigvee^{b^2}S^3,&3\le r<4,\\
\ast,&r\ge4.
\end{cases}
\]
The inclusion from radius one to radius two induces an isomorphism on integral first homology. Consequently the *complete reduced persistence barcode*, with any field coefficients, consists of \(N-1\) degree-zero intervals \([0,1)\), \(b\) degree-one intervals \([1,3)\), and \(b^2\) degree-three intervals \([3,4)\), and no other intervals. The homotopy classifications and the radius-one-to-two persistence claim hold integrally.

## Assumptions and scope

Write the two parts of \(K_{m,n}\) as \(U=\{u_1,\ldots,u_m\}\) and \(V=\{v_1,\ldots,v_n\}\). The subdivided edge \(u_iv_j\) has a new midpoint vertex \(e_{ij}\), adjacent in \(X_{m,n}\) only to \(u_i\) and \(v_j\). There are exactly \(N=m+n+mn\) vertices, all graph edges have length one, and a simplex at parameter \(r\) is any vertex subset whose diameter is at most \(r\) in the vertex metric. The formulation does *not* concern points in the geometric realization of a metric graph or Euclidean lengths of a drawing.

## Proof

**Radius zero and radius one.** The graph has no triangles and is connected. At radius zero there are \(N\) isolated vertices; at radius one the clique complex is the graph itself. It has \(2mn\) edges, so its first Betti number is \(2mn-N+1=mn-m-n+1=b\); hence it is a wedge of \(b\) circles.

**Radius two and the inclusion map.** The radius-two threshold graph is exactly the *total graph* \(T(K_{m,n})=S(K_{m,n})^2\). By Adamaszek's general theorem on clique complexes of total graphs [1, Theorem 5.1], \(\operatorname{Cl}(T(H))\simeq\operatorname{Cl}(H)\vee\bigvee^{t(H)}S^2\), where \(t(H)\) counts triangles. Here \(H=K_{m,n}\) is triangle-free; thus \(\operatorname{VR}_{\le2}(X_{m,n})\simeq K_{m,n}\simeq\bigvee^{b}S^1\). For the persistence map, that theorem's explicit collapse pairs centered edge-subdivision simplices while retaining each filled triple \(\{u_i,e_{ij},v_j\}\). Under the collapse each original subdivided two-edge path \(u_i-e_{ij}-v_j\) represents the original edge \(u_iv_j\). This supplies a homotopy identification taking all cycle classes of the subdivided graph to the corresponding cycles of \(K_{m,n}\); it induces an isomorphism of their full integral \(H_1\) lattices. Hence no radius-one classes die at radius two.

**Exact metric taxonomy at radius three.** Distinct original vertices in opposite parts have distance two, while distinct original vertices in the same part have distance four. Two midpoint vertices \(e_{ij},e_{kl}\) have distance two precisely if \(i=k\) or \(j=l\), and otherwise distance four. Each original vertex is within distance three of every midpoint vertex: incident pairs have distance one; nonincident pairs have a length-three path through the other endpoint of a suitable subdivided edge. Thus the entire radius-three threshold graph, *as an exact graph isomorphism*, is the graph join of \(K_{m,n}\) on the originals and \(L(K_{m,n})\) on the midpoints (the rook graph). Taking clique complexes gives an exact simplicial identity
\[
\operatorname{VR}_{\le3}(X_{m,n})
=\operatorname{Cl}(K_{m,n})*\operatorname{Cl}(L(K_{m,n})).
\]

**The rook factor.** Cover \(\operatorname{Cl}(L(K_{m,n}))\) by its maximal simplices: the \(m\) complete row simplices \(\{e_{ij}:1\le j\le n\}\) and the \(n\) complete column simplices \(\{e_{ij}:1\le i\le m\}\). Every clique of rook positions lies in one row or one column, because pairwise intersections of the corresponding bipartite graph edges force a common endpoint. Two different row simplices have empty intersection; likewise two different column simplices; each row and column intersect in the single vertex \(e_{ij}\). Every nonempty intersection is therefore contractible, and the nerve is exactly the bipartite graph \(K_{m,n}\). The nerve lemma shows \(\operatorname{Cl}(L(K_{m,n}))\simeq K_{m,n}\simeq\bigvee^b S^1\), in agreement with the general line-graph result of Goyal, Shukla and Singh [2, Corollary 3.3]. The simplicial join respects homotopy equivalences for nonempty simplicial complexes, and \(A*B\simeq\Sigma(A\wedge B)\) for based connected CW complexes. Therefore the radius-three join is \(\bigvee^{b^2}S^3\), with no torsion or homotopy components in other positive degrees.

**Radius four and the barcode.** Every two vertices of \(X_{m,n}\) are at graph distance at most four, by the metric classification above and bipartite incidence. Thus at radius four the Rips complex is the full \((N-1)\)-simplex, a point up to homotopy. Distances are integer-valued, so there are no changes between integer thresholds. The only nontrivial positive-dimensional persistence between successive stages is the integral radius-one-to-two isomorphism already shown. The complete interval decomposition follows. \(\square\)

## Verification

The accompanying dependency-free checker `verify_bipartite.py` constructs the incidence subdivision, independently computes all vertex-pair shortest paths by breadth-first search, tests the radius-three adjacency taxonomy and the radius-four full-simplex threshold, and verifies radius-one cycle rank for \((m,n)\) equal to \((2,2),(2,3),(3,3),(3,4),(4,5)\). Its executed output records these five passing cases. The finite checks test the metric combinatorics and boundary examples, but the proof for all \(m,n\ge2\) relies on the symbolic metric classification, the nerve argument, and the explicitly identified radius-two homotopy equivalence, not numerical extrapolation.

## Relationship to prior work

Adamaszek [1, Theorem 5.1] proves the general **radius-two** result for subdivided graphs, so the radius-two homotopy identification here is an acknowledged special case, *not* presented as new. His Theorem 5.2 also identifies line-graph clique complexes with two-skeleta of original clique complexes. Neither theorem states the radius-three **cross-part adjacency** property specific to this bipartite subdivision, its exact Rips join, or the complete persistence intervals. In fact the cited paper treats the total graph (second power) and line graph, not the third-power filtration of the subdivided biclique.

Goyal, Shukla and Singh [2, Corollary 3.3] compute the line-graph clique complex of triangle-free graphs; its value for \(K_{m,n}\) is explicitly used as a factor, not reclaimed. Their paper does not form the join with original graph vertices or derive a graph-metric Rips filtration. Saleh, Titz Mite and Witzel [3] classify graph-metric Rips filtrations of Platonic solids, a different natural graph family. The closest indexed comparison, the published complete-graph-subdivision filtration [4], concerns \(S(K_t)\): its radius-three term is contractible, so it cannot imply the nontrivial \(S(K_{m,n})\) radius-three representation by specializing the parameter. Other relevant graph-Rips results on generalized quadrangles and multipartite prisms use different metric graphs and do not subsume the present claim.

## Limitations

The statement is for \(m,n\ge2\), the unit-edge graph shortest-path metric on vertices, and inclusive filtration parameters. It does not assert equivariant module structure under row and column permutations, and does not classify subdivisions of arbitrary bipartite graphs. The central second-power and line-graph homotopy facts are established in earlier literature; the new input is the radius-three exact join and its full-filtration consequences. The comparison covers inspected primary sources and indexed semantic searches, not all possible unindexed equivalent statements; an older differently worded graph-power theorem is a residual originality risk.

## References

1. Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public 2011-04-03, especially Theorems 5.1--5.2; *Israel Journal of Mathematics* 196 (2013), 295--319. https://arxiv.org/html/1104.0433v3
2. Shuchita Goyal, Samir Shukla and Anurag Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first public 2020-09-25, especially Section 3 and Corollary 3.3. https://arxiv.org/pdf/2009.12130
3. Nada Saleh, Thomas Titz Mite and Stefan Witzel, *Vietoris-Rips complexes of Platonic solids*, arXiv:2302.14388, first public 2023-02-28. https://arxiv.org/abs/2302.14388
4. *The Rips filtration of the complete-graph subdivision has two consecutive sphere wedges*, public record of 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-rips-filtration-of-the-complete-graph-subdivision-has-two-co--fb5f0359b702
