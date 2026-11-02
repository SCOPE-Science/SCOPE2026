# Preference-stable chromatic numbers of clique joins with degree-two cores

## Finding
For a finite nonempty simple graph \(H\) with maximum degree at most two and any integer \(t\geq1\), let \(G=K_t\vee H\) be the graph obtained by adding a \(t\)-vertex clique adjacent to every vertex of \(H\). Define
\[
\sigma(H)=\begin{cases}
1,&E(H)=\varnothing,\\
2,&E(H)\ne\varnothing\text{ and each component of }H\text{ is a path on at most three vertices},\\
3,&\text{otherwise}.
\end{cases}
\]
The following exact formula holds:
\[
\boxed{\chi_{\mathrm{stable}}(K_t\vee H)=t+\sigma(H).}
\]
In the last case, \(H\) contains a path on at least four vertices or a cycle of any length. In particular, every fan \(K_1\vee P_n\) with \(n\geq4\) and every wheel \(K_1\vee C_n\) with \(n\geq3\) has stable chromatic number four. Every clique fan \(K_t\vee P_n\) with \(n\geq4\) and every clique wheel \(K_t\vee C_n\) has stable chromatic number \(t+3\).

## Assumptions and scope
All graphs are finite, simple, and undirected; \(H\) is nonempty, \(\Delta(H)\leq2\), and \(t\geq1\) is an integer. The join \(X\vee Y\) adds every edge between the disjoint vertex sets of \(X\) and \(Y\). Isolated vertices of \(H\) are permitted, and its components are paths or cycles.

For a fixed palette of \(k\) named colors, every vertex has an arbitrary strict ordering of those colors. A proper coloring is *preference-stable* when its directed envy graph has no directed cycle: the arc \(u\to v\) is present exactly when \(uv\in E(G)\) and \(u\) strictly prefers the color assigned to \(v\) over the color assigned to \(u\). The stable chromatic number \(\chi_{\mathrm{stable}}(G)\) is the least \(k\) such that every profile of strict preferences admits a stable proper coloring using the \(k\)-color palette. Unused colors are allowed. The terminology and definition follow Koana, Oh and Yoneda [1].

## Proof
**Step 1: Stable coloring of a degree-two core.** By [1, Propositions 3.5 and 3.6], the stable chromatic numbers of paths are one for a one-vertex path, two for paths on two or three vertices, and three for paths on at least four vertices; every cycle has value three. Stable chromatic number of a disjoint union is the maximum of the component values: given any preference profile, use a stable coloring on each component from the same palette, which creates no envy arcs between components. Conversely, restricting a stable coloring to a component proves the reverse inequality (or use subgraph monotonicity). Every degree-two graph is a disjoint union of paths and cycles. Hence
\[
\chi_{\mathrm{stable}}(H)=\sigma(H).
\]
The statement also holds when the palette consists of any designated \(\sigma(H)\) colors, by relabeling colors and restricting the preferences.

**Step 2: Clique-join upper bound.** More generally, for any nonempty graph \(H\) and any integer \(t\geq1\), we prove
\[
\chi_{\mathrm{stable}}(K_t\vee H)\leq t+\chi_{\mathrm{stable}}(H).
\]
Fix an arbitrary preference profile over \(k=t+\chi_{\mathrm{stable}}(H)\) colors. Order the vertices of the added clique as \(a_1,\ldots,a_t\). For each \(i=1,\ldots,t\), assign \(a_i\) its most preferred color not previously used on \(a_1,\ldots,a_{i-1}\). Thus all clique colors are distinct. No clique vertex has an envy arc to any vertex colored later, since its assigned color was preferred to every color not previously used. There are exactly \(\chi_{\mathrm{stable}}(H)\) remaining colors. Color the vertices of \(H\) stably using those remaining colors, which is possible for their induced preference orders by the definition of the invariant.

Every edge between clique and core is proper because their color sets are disjoint. No clique vertex envies any core vertex. Among clique vertices, every possible envy arc points from a later-assigned to an earlier-assigned vertex. Thus any directed cycle would have to lie entirely inside the core, where stability excludes it, or entirely inside the added clique, whose envy arcs respect a strict linear order. This proves the upper bound, and with Step 1 gives \(\chi_{\mathrm{stable}}(G)\leq t+\sigma(H)\).

**Step 3: Lower bounds for the first two cases.** If \(H\) has no edge, \(K_t\vee H\) contains a complete graph on \(t+1\) vertices, so proper coloring requires at least \(t+1\) colors. If \(H\) has an edge, the join contains a complete graph on \(t+2\) vertices, forcing at least \(t+2\). These match the upper bound when \(\sigma(H)\leq2\).

**Step 4: Third-case lower bound.** If \(H\) has a triangle, the join contains a complete graph on \(t+3\) vertices, giving the desired lower bound. Otherwise, when \(\sigma(H)=3\), some component of \(H\) has a path on at least four vertices or is a cycle on at least four vertices. In either case \(P_4\) is a subgraph (not necessarily induced), so \(K_t\vee P_4\) is a subgraph of \(K_t\vee H\).

Here is an explicit Grundy coloring of \(K_t\vee P_4\) with \(t+3\) colors. Assign the four path vertices, in path order, colors \(1,2,3,1\). Assign the added clique vertices colors \(4,5,\ldots,t+3\). This coloring is proper. Every vertex carrying color \(i\) sees a neighbor of every color \(j<i\): on the path, the vertex of color two sees color one, the vertex of color three sees colors one and two; every clique vertex sees all three lower path colors and all lower clique colors. Hence the Grundy number satisfies
\[
\Gamma(K_t\vee P_4)\geq t+3.
\]
By [1, Theorem 3.3], stable chromatic number is at least Grundy number; by [1, Proposition 3.4], stable chromatic number is monotone under taking *any* subgraph, including edge-deleted subgraphs. Consequently,
\[
\chi_{\mathrm{stable}}(K_t\vee H)\geq
\chi_{\mathrm{stable}}(K_t\vee P_4)\geq t+3.
\]
This matches Step 2, proving all cases. In particular, the argument remains valid for \(C_4\), where deleting a cycle edge yields the requisite \(P_4\) subgraph.

## Verification
The bundled standalone `verify.py` reconstructs the clique joins and checks the explicit Grundy coloring for every integer \(1\leq t\leq15\). It independently enumerates all strict preference profiles and all proper colorings for the small cores \(P_1,P_2,P_3,P_4,C_3,C_4\), verifying the expected stable palette upper bounds. It likewise exhaustively checks the upper bounds for joins of one universal vertex with \(P_1,P_2,P_3\). Finally, it checks that a displayed strict-preference profile on the five-vertex fan \(K_1\vee P_4\) blocks each of its six proper three-colorings. The deterministic replay ends with `VERIFY_OK`.

Finite computation corroborates only the tested cases. The unrestricted claim rests on the proof above and the cited, mathematically established path/cycle and Grundy inequalities.

## Relationship to prior work
Koana, Oh and Yoneda [1] introduce this stability notion, determine the stable chromatic numbers of individual paths and cycles, and prove the Grundy lower bound and subgraph monotonicity used above. Those prior results are explicitly credited rather than presented as new. Their inspected original full text does not state a clique-join additivity result, the exact stable chromatic number of fans or wheels, or the full classification for joins with degree-two cores.

The new observation is that a clique can be colored first in preference order without creating outgoing envy to the core, and that a four-vertex path subgraph gives a uniform sharp lower bound after taking clique joins. The combination yields the all-parameter classification; it also includes cones over odd cycles, for which the reachability-oriented upper bound used in [1] is not sharp even on the base cycle.

Related work on the stable chromatic number of the complete tripartite graph \(K_{2,3,3}\) concerns a different graph class and does not imply the present theorem. Priority is based on accessible literature and remains subject to independent review.

## Limitations
The exact classification is restricted to nonempty cores of maximum degree at most two. The upper-bound lemma applies to arbitrary cores, but equality is not claimed for all graphs. The statement does not enumerate stable colorings for each preference profile, nor does it determine stable chromatic numbers for general tree cores or arbitrary joins. The mathematical review is not independent; historical priority against unindexed literature remains provisional.

## References
[1] Tomohiro Koana, Yeeseok Oh and Hirotaka Yoneda, *Graph Coloring with Color Preferences*, first public arXiv submission 1 September 2026, arXiv:2609.00569v1, Sections 2–3 (especially Theorem 3.3 and Propositions 3.4–3.6), https://arxiv.org/abs/2609.00569.
