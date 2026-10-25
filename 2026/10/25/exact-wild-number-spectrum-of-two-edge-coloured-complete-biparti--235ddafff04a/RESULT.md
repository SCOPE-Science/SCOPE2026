# Exact wild-number spectrum of two-edge-coloured complete bipartite graphs

## Finding
For every pair of integers \(2\le a\le b\), the set of wild numbers of all surjective two-edge-colourings of \(K_{a,b}\) is exactly
\[
\boxed{\{L_{a,b},L_{a,b}+1,\ldots,a+b-2\}},\qquad
L_{a,b}=\max\{0,2(a+b-1)-ab\}.
\]
Equivalently, \(L_{a,b}=2\) for \(a=2\), \(L_{3,3}=1\), and \(L_{a,b}=0\) for \(a\ge3\) with \(b\ge4\). Every integer between the extrema is attained by an actual surjective two-colouring. The conclusion does not require balanced colour-class sizes.

## Assumptions and scope
All graphs are finite and simple. The complete bipartite graph has specified parts \(A,B\) of cardinalities \(|A|=a\), \(|B|=b\), with integers \(2\le a\le b\). A colouring \(\chi:E(K_{a,b})\to\{\mathrm{red},\mathrm{blue}\}\) uses each colour on at least one edge and is not required to be proper or equitable. Both monochromatic graphs include all \(a+b\) vertices, including isolated vertices. If a wild set \(W\) is chosen, its edges are available in both colour classes; the wild number \(\operatorname{wld}_{\chi}(K_{a,b})\) is the least \(|W|\) for which each colour together with \(W\) has a spanning connected subgraph, equivalently a spanning tree. Two colourings exchanging colours are counted as separate assignments, although they give the same wild number.

## Proof
**Component identity.** Write \(N=a+b\), and let \(k_R,k_B\) denote the numbers of connected components of the two monochromatic spanning subgraphs. Every blue edge placed in \(W\) can merge at most two red components, and every red edge can merge at most two blue components. Thus at least \(k_R-1\) blue edges and \(k_B-1\) red edges are required. Conversely, contract each red component: all edges between the contracted vertices are blue, and they form a connected quotient because the underlying graph is connected. A tree of the quotient provides exactly \(k_R-1\) blue edges connecting the red components. Similarly, exactly \(k_B-1\) red edges suffice for the blue components. The two sets are disjoint because their original colours differ. Therefore
\[
\operatorname{wld}_{\chi}(K_{a,b})=k_R+k_B-2.
\tag{1}
\]
This is the established two-colour component identity, reproduced here with its justification.

**Universal lower bound.** Let \(r_R=N-k_R\) and \(r_B=N-k_B\) be the graphic ranks of the two colour classes. Each rank is bounded by its number of edges, and neither exceeds \(N-1\); since the colour classes partition the \(ab\) edges,
\[
\operatorname{wld}_{\chi}=2(N-1)-(r_R+r_B)
\ge \max\{0,2(N-1)-ab\}=L_{a,b}.
\tag{2}
\]
For \(2\le a\le b\), a direct integer check gives \(L_{a,b}=2\) when \(a=2\); \(L_{3,3}=1\); and \(L_{a,b}=0\) for all \(a\ge3,b\ge4\).

**Attaining the minimum when \(a=2\).** Write \(A=\{x,y\}\). Colour all edges from \(x\) red and all edges from \(y\) blue. Each monochromatic graph is one star and one isolated vertex, hence \(k_R=k_B=2\). Formula (1) gives wild number \(2\).

**Attaining the minimum for \(K_{3,3}\).** Index the parts by \(A=\{x_0,x_1,x_2\}\) and \(B=\{y_0,y_1,y_2\}\). Give the five edges
\[
\{x_0y_0,x_0y_1,x_0y_2,x_1y_1,x_2y_2\}
\]
red, and the other four edges blue. Red forms a spanning tree; blue forms a connected five-vertex path and one isolated vertex. Thus \(k_R=1\), \(k_B=2\), and (1) gives wild number \(1\).

**Attaining the minimum for \(a\ge3,b\ge4\).** First take \(K_{3,4}\) with parts \(\{x_0,x_1,x_2\}\) and \(\{y_0,y_1,y_2,y_3\}\). Colour these six edges red:
\[
\{x_0y_0,x_0y_1,x_0y_2,x_1y_0,x_1y_3,x_2y_1\}.
\]
The remaining six edges are blue. Both colour classes are connected six-edge spanning trees; this is checked directly by the displayed adjacency lists. For any larger \(K_{a,b}\), keep this coloured core. Each additional left vertex gets one red and one blue edge to distinct vertices of the original right core; each additional right vertex gets one red and one blue edge to distinct vertices of the original left core. Colour every other new edge arbitrarily. Each monochromatic graph remains connected. Therefore \(k_R=k_B=1\) and the wild number is \(0\).

**Universal upper bound.** We first prove a rank observation: in a connected graph with a red/blue edge-colouring, the presence of a simple cycle containing edges of both colours implies
\[
r_R+r_B\ge N.
\tag{3}
\]
Indeed, choose spanning forests \(F_R,F_B\) of the red and blue subgraphs. Their union is connected, because any monochromatic edge can be replaced by a path in its monochromatic forest. If \(r_R+r_B=N-1\), their union is a spanning tree \(T\). For every edge outside \(T\), the unique path in \(T\) connecting its endpoints lies in its own monochromatic forest, so every fundamental cycle of \(T\) is monochromatic. These fundamental cycles generate the binary cycle space. The red-edge part of any cycle must therefore itself have even degree at every vertex, being a symmetric difference of red cycles. But the red edges of a genuinely mixed *simple* cycle are a nonempty proper subset of its cycle edges and have a vertex of odd degree. Contradiction. As connectedness always gives \(r_R+r_B\ge N-1\), (3) follows.

Now select any red edge and any blue edge in \(K_{a,b}\). Because \(a,b\ge2\), a four-cycle contains both edges: if they are disjoint, use their four endpoints; if they share an endpoint, supply one additional vertex from its bipartition class. Hence every surjective two-colouring has a mixed four-cycle. By (1) and (3),
\[
\operatorname{wld}_{\chi}=2(N-1)-(r_R+r_B)\le N-2=a+b-2.
\tag{4}
\]
This maximum is attained by colouring any single edge red and all other edges blue. The red graph has \(N-1\) components, while removing one edge from \(K_{a,b}\) leaves a connected blue graph. Therefore (1) gives exactly \(N-2\).

**No gaps between the extrema.** Let \(m=ab\ge4\). A surjective red/blue colouring is a nonempty proper subset \(R\subsetneq E\) of red edges. The graph of all such subsets, adjacent when they differ by one edge, is connected: shrink each subset to a chosen singleton, move between different singletons by passing through the intervening two-element subset, then reverse the shrink operations to reach any target. No intermediate subset is empty or the full \(m\)-edge set. Under a one-edge recolouring, the component count of the colour losing the edge increases by at most one, and the component count of the colour gaining it decreases by at most one. Thus, by (1), the wild number changes by at most one. Along a path from the explicitly constructed minimum-wild-number colouring to the maximum-wild-number colouring, every integer between the two values is taken. Together with (2)–(4), this proves the asserted complete interval. \(\square\)

## Verification
The accompanying standalone script `verify_wild.py` enumerates every labelled surjective two-colouring of ten small complete bipartite graphs, calculates both monochromatic component counts by an independent union-find implementation, and compares the exact observed spectrum with the asserted interval. In particular it checks all \(262142\) colourings of \(K_{3,6}\) and all \(65534\) colourings of \(K_{4,4}\), as well as eight other dimension pairs; all checks produce `VERIFY_OK`. This finite computation supports the theorem but does not replace the proof for arbitrary part sizes.

## Relationship to prior work
Anders, Foster-Greenwood, Garcia and Krawzik (2025), Theorem 6.4(2), established (1) for arbitrary connected two-coloured graphs, and Theorem 2.3 characterized zero wild number through edge-disjoint spanning trees; neither gives the all-colouring integer spectrum for arbitrary \(K_{a,b}\). Dawkins, Nappo, Tong and Zimbizi (2026), Section 4, study **equitable** two-colourings and minimum **proper** edge-colourings of complete bipartite graphs and obtain a sharp equitable upper bound and a proper-colouring exact value; they do not state the unrestricted spectrum classified here. The new content is the uniform extremal classification for *all surjective* two-colourings, the exceptional dimension thresholds, and gap-free attainability, including unbalanced colour classes. Existing general formulas and the spanning-tree-packing equivalence are credited, not claimed as new.

## Limitations
The range theorem does not count how many colourings give each wild number, characterize the analogous spectrum under balanced/proper colouring restrictions, treat three or more colours, or extend to arbitrary connected bipartite graphs. Finite verification does not establish an infinite claim. No independent mathematical audit or definitive bibliographic-priority certification has been performed. An equivalent unindexed theorem, possibly using graphic-matroid rank rather than wild-number terminology, remains a literature risk.

## References
1. Katie Anders, Briana Foster-Greenwood, Rebecca Garcia and Naomi Krawzik, *The wild number of an edge-colored graph*, arXiv:2508.06711 (first publicly submitted 2025-08-08), Sections 2, 6. https://arxiv.org/abs/2508.06711
2. Aleyah Dawkins, Alexander Nappo, Jessie Tong and Christopher Zimbizi, *Wild number for spanning trees in complete and complete bipartite graphs*, arXiv:2610.22142v1 (first publicly submitted 2026-10-15), Section 4. https://arxiv.org/abs/2610.22142
3. C. St. J. A. Nash-Williams, *Edge-disjoint spanning trees of finite graphs*, Journal of the London Mathematical Society (1961), as cited in the two preceding articles.
