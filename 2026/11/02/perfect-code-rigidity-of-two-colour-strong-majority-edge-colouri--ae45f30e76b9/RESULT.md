# Perfect-code rigidity of two-colour strong-majority edge colourings of cubic graphs

## Finding

**Theorem.** Let \(G\) be a finite, nonempty, connected, simple cubic graph. Fix two named colours, red and blue. Let \(p(G)\) be the number of efficient dominating vertex sets: subsets \(D\subseteq V(G)\) for which every closed neighbourhood \(N[v]\) contains exactly one vertex of \(D\). Then the number \(b(G)\) of strong-majority edge colourings from this palette is exactly
\[
b(G)=2p(G).
\]
More precisely, every such edge colouring is uniquely of the form "colour every edge incident with \(D\) red and every other edge blue" or its global colour swap, for a unique efficient dominating set \(D\). Hence the strong-majority edge index is two if and only if \(p(G)>0\). In particular, \(4\) divides \(|V(G)|\) whenever two colours suffice.

**Classification consequence.** For each \(m\ge2\), if \(G\) is a connected simple cubic vertex-transitive graph on \(2^m\) vertices, its strong-majority edge index is two except for \(m\ge3\) and \(G\cong M_{2^{m-1}}\), where the index is three. Here the Möbius ladder \(M_t\) consists of the cycle of length \(2t\) and chords joining opposite vertices. Furthermore, for every integer \(t\ge2\),
\[
\operatorname{Maj}'(M_t)=\begin{cases}2,&t\equiv2\pmod4,\\3,&t\not\equiv2\pmod4,\end{cases}
\qquad b(M_t)=\begin{cases}8,&t\equiv2\pmod4,\\0,&t\not\equiv2\pmod4.\end{cases}
\]
The existence theorem on efficient dominating sets in vertex-transitive cubic graphs is due to Knor and Potočnik (2012), and is explicitly used as a previously proved input. The colour-index transfer and exact correspondence are the new claims.

## Assumptions and scope

A strong-majority edge colouring assigns a colour to each edge, not necessarily properly, such that for every edge \(e\) and every colour \(\alpha\), at most half of the edges sharing an endpoint with \(e\), other than \(e\) itself, have colour \(\alpha\). For a simple cubic graph each edge has exactly four such neighbouring edges. The palette has two fixed named colours, including possibly unused colours; in fact no colour can be unused. The original graph is finite, connected, simple and \(3\)-regular. All numbers count labelled vertex sets and edge-colour assignments on the given graph; graph-isomorphism classes are not being counted.

An efficient dominating set, also called a perfect \(1\)-code or exact closed-neighbourhood transversal, obeys
\[
\sum_{u\in N[v]}\mathbf 1_{u\in D}=1\qquad\text{for all }v\in V(G).
\]
Consequently, the sets \(N[d]\), \(d\in D\), partition the vertex set, each with four vertices.

## Proof

**1. Every two-colour solution has a rigid local form.** Let \(a_v\in\{0,1,2,3\}\) be the number of red edges incident with vertex \(v\). Since every edge has four distinct neighbours, the two-colour strong-majority condition requires exactly two red and two blue neighbours at every edge. For an edge \(uv\) coloured red the number of red neighbours is \(a_u+a_v-2\), giving \(a_u+a_v=4\). For a blue edge the number of red neighbours is \(a_u+a_v\), giving \(a_u+a_v=2\).

Thus a red edge has endpoint profiles \((1,3),(2,2),(3,1)\); a blue edge has profiles \((0,2),(1,1),(2,0)\). In particular, no edge joins the profile classes \(\{0,2\}\) and \(\{1,3\}\). Since \(G\) is connected, every vertex lies in one of these two classes.

Suppose first all vertices have \(a_v\in\{1,3\}\). Each profile-\(3\) vertex has three red neighbours, all of profile \(1\). Each profile-\(1\) vertex has exactly one red edge, necessarily to a profile-\(3\) vertex, and its other two edges are blue and end at profile-\(1\) vertices. Therefore \(D=\{v:a_v=3\}\) meets each closed neighbourhood exactly once. Moreover the red edges are exactly those incident with \(D\), so \(D\) determines the colouring. A profile-\(3\) vertex necessarily exists: any profile-\(1\) vertex has a red incident edge which leads to one. If instead all vertices have \(a_v\in\{0,2\}\), swap the colours. The same proof applies, with \(D=\{v:a_v=0\}\). The two families are disjoint, and in either family the recovered \(D\) is unique.

**2. Every efficient dominating set generates both solutions.** Let \(D\) satisfy the exact neighbourhood equations. Vertices of \(D\) are pairwise nonadjacent, and every vertex outside \(D\) has exactly one neighbour in \(D\). Colour each edge with an endpoint in \(D\) red, and all remaining edges blue. For an edge joining \(D\) to its complement, its two other edges at the \(D\)-endpoint are red while its two other edges at the complement endpoint are blue. For an edge with both endpoints outside \(D\), each endpoint has one other red edge and one other blue edge. Both kinds of edge thus have exactly two neighbouring edges of each colour. Swapping red and blue gives a second solution. The two are distinct, because every vertex in \(D\) has three incident edges of one colour. Step 1 proves there are no others, hence \(b(G)=2p(G)\).

Because a monochromatic assignment would put four equal-coloured edges around every edge, the strong-majority index is never one. This proves the index criterion. Also, the disjoint closed neighbourhoods of an efficient dominating set each contain four vertices, establishing \(4\mid |V(G)|\).

**3. Power-of-two vertex-transitive graphs.** Knor and Potočnik, *Efficient domination in cubic vertex-transitive graphs*, Theorem 1.2 (2012), prove that among connected simple cubic vertex-transitive graphs of order \(2^m\), \(m\ge2\), the graphs with no efficient dominating set are exactly \(M_{2^{m-1}}\) for \(m\ge3\). The new correspondence therefore gives index two on every other graph and excludes two colours on precisely these ladders. Each exceptional ladder has a proper three-edge colouring: alternate colours red and blue along its even Hamiltonian cycle and give every antipodal chord a third colour. In a cubic graph, any proper three-edge colouring is strong-majority, because the four edges adjacent to a given edge comprise two edges of each of the other two colours. The exceptional index is therefore exactly three.

**4. All Möbius ladders and exact two-colour counts.** Lemma 2.2 and its constructive proof in the same 2012 paper establish that \(M_t\) has an efficient dominating set exactly when \(t\equiv2\pmod4\). Its proof also forces the entire efficient dominating set once a chosen vertex belongs to it, and a solution exists through every vertex by rotational symmetry. Hence, in the feasible case, the total number of ordered pairs \((v,D)\) with \(v\in D\) is \(2t\), while every \(D\) has \(t/2\) elements; consequently \(p(M_t)=2t/(t/2)=4\). The correspondence yields eight named two-colourings. When \(t\not\equiv2\pmod4\), no two-colouring exists, but the alternating-cycle/chord three-edge colouring above still works. The displayed formulas follow, including the degenerate smallest ladder \(M_2\cong K_4\).

## Verification

The standalone, dependency-free script `verify.py` builds named cubic graphs and checks the *original edge-neighbour* constraints for each of their \(2^{|E|}\) binary edge colourings, independently of checking every candidate efficient dominating set against every closed neighbourhood. It verifies the equality of counts on \(K_4\), \(K_{3,3}\), triangular and four-rung prisms, the cube, two Möbius ladders, and the Petersen graph. It also exhausts all \(70\) labelled simple cubic graphs on six vertices and tests the Möbius code counts for \(2\le t\le8\). Successful execution prints `VERIFY_OK`. The infinite result is a proof from the local equations, not an extrapolation from these tests. The transfer to all power-of-two vertex-transitive graphs explicitly relies on the published 2012 theorem; the tests do not reconstruct that classification.

## Relationship to prior work

The original definition and general bounds for the strong-majority edge index come from Kalinowski, Kamyczura, Pilśniak and Woźniak (public May 22, 2026). Pękała and Przybyło (public August 4, 2026) study strong-majority edge colourings with few colours, particularly higher minimum degrees. Neither inspected treatment gives this two-colour cubic perfect-code bijection or the resulting power-of-two index classification. Knor and Potočnik (2012) independently determine the efficient domination spectrum for the vertex-transitive family and for Möbius ladders; their original perfect-code results are **not** new here. An earlier exact strong-majority result restricted to prisms already handles the prism subclass, so the novelty is explicitly the general connected cubic characterization and the transfer to the larger vertex-transitive and Möbius-ladder classes, not the prism case. The earlier special-case results are consistent with the present theorem.

## Limitations

The exact bijection requires connected simple cubic graphs; graph components may be handled independently but are not included in the displayed count. It does not classify the strong-majority index of an arbitrary cubic graph when no efficient dominating set exists: such an index can be three or four. The proof does not supply a new algorithm for efficient domination, an exact count of efficient dominating sets in arbitrary cubic graphs, or an independent proof of the 2012 vertex-transitive classification. Historical priority beyond the inspected sources remains provisional, and no independent audit is asserted.

## References

1. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828 (first public May 22, 2026), https://arxiv.org/abs/2605.23828.
2. P. Pękała, J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122 (first public August 4, 2026), https://arxiv.org/abs/2608.04122.
3. M. Knor, P. Potočnik, *Efficient domination in cubic vertex-transitive graphs*, European Journal of Combinatorics 33 (2012), 1755–1764, doi:10.1016/j.ejc.2012.04.007, author manuscript https://www.math.sk/knor/PREP/p076.pdf.
