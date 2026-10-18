# Preference-stable chromatic number of the one-apex complete bipartite graphs

## Finding

For all integers \(a\ge b\ge1\), the complete tripartite graph with parts of sizes \(a,b,1\) has preference-stable chromatic number
\[
\chi_{\mathrm{stable}}(K_{a,b,1})=b+2.
\]
In particular, adding one universal vertex to \(K_{a,b}\) increases its preference-stable chromatic number by exactly one. For \(b\ge2\), an explicit adversarial preference profile certifies the lower bound for the entire infinite two-parameter family.

## Assumptions and scope

All graphs are finite, simple, and undirected. A strict preference profile on a palette \([k]=\{1,\ldots,k\}\) assigns to each vertex a strict total order of the colors. A coloring \(c:V(G)\to[k]\) is proper when adjacent vertices have different colors. Its *envy digraph* has an arc \(v\to w\) when \(v\) strictly prefers the color \(c(w)\) to its own color \(c(v)\). A proper coloring is *stable* if this digraph is acyclic. The preference-stable chromatic number is the smallest \(k\) such that every strict preference profile on \([k]\) admits a stable proper coloring. This is the blocking-cycle notion introduced by Koana, Oh, and Yoneda; a hypothetical exchange need not preserve properness.

Write the partite classes of \(K_{a,b,1}\) as \(A\), \(B\), and \(\{u\}\), with \(|A|=a\), \(|B|=b\). Thus \(u\) is universal, both \(A\) and \(B\) are independent, and every edge between \(A\) and \(B\) exists. The labeling of colors is arbitrary. The proof treats \(b=1\) separately.

## Proof

**Upper bound.** Let \(k=b+2\), and consider *any* preference profile. Give the universal vertex \(u\) its favorite color. Next, process the \(b\) vertices of \(B\) in any order, giving each its favorite color among those not yet taken by \(u\) or earlier vertices of \(B\). Exactly one color remains after these \(b+1\) choices; give that color to every vertex of \(A\). This is proper because colors used on distinct partite classes are disjoint, and \(B\) may have distinct colors within itself.

There is no envy arc from \(u\) to another vertex: its color was its favorite. Each processed vertex of \(B\) has no envy arc to a later vertex of \(B\) or to a vertex of \(A\), since all their colors were available when that vertex of \(B\) chose. A vertex of \(A\) cannot envy another vertex of \(A\), since all receive one color. Hence every envy arc points backward in the ordering consisting of \(u\), the processed \(B\) vertices, then the vertices of \(A\). The envy digraph is acyclic. This proves \(\chi_{\mathrm{stable}}(K_{a,b,1})\le b+2\).

**Lower bound for \(b=1\).** The graph contains a triangle on \(u\), one vertex of \(A\), and the sole vertex of \(B\); any proper coloring therefore needs at least three colors, and the upper bound is three.

**Lower bound for \(b\ge2\).** Put \(k=b+1\). In each of \(A\) and \(B\), distinguish \(b\) vertices indexed by \(i\in\{1,\ldots,b\}\); this is possible because \(a\ge b\). In both classes, the indexed vertex \(i\) ranks color \(i\) first and the extra color \(k\) second, with all remaining colors in arbitrary strict order. Give any remaining vertices of \(A\) and the universal vertex \(u\) arbitrary strict preferences.

Consider any proper coloring using the palette \([k]\). Let \(z\) be the color of \(u\); no vertex in \(A\cup B\) may have color \(z\). For each side \(X\in\{A,B\}\) and every color \(t\in[k]\setminus\{z\}\), there is a distinguished vertex of \(X\) whose favorite color *among the remaining palette* \([k]\setminus\{z\}\) is \(t\): if \(z=k\), the distinguished vertices still favor their respective indexed colors, while if \(z=i\le b\), the distinguished vertex \(i\) now favors \(k\) and every other distinguished vertex retains its indexed favorite.

Let \(S_A\) and \(S_B\) be the nonempty sets of colors actually used in \(A\) and \(B\), respectively. Properness makes these sets disjoint. For each \(s\in S_A\), choose a vertex \(v_s\in B\) whose favorite remaining color is \(s\); let \(f(s)\in S_B\) be its assigned color. Since its assigned color differs from \(s\), vertex \(v_s\) strictly prefers \(s\) to \(f(s)\). Similarly, for each \(t\in S_B\), choose \(w_t\in A\) whose favorite remaining color is \(t\), and write \(g(t)\in S_A\) for its assigned color. Again \(w_t\) strictly prefers \(t\) to \(g(t)\).

The map \(g\circ f:S_A\to S_A\) has a directed cycle, since \(S_A\) is finite and nonempty. Write its distinct cyclic colors as \(s_1,\ldots,s_m\), with \(g(f(s_j))=s_{j+1}\), taking indices cyclically. Set \(t_j=f(s_j)\). Then \(v_{s_j}\) has color \(t_j\) and prefers \(s_j\), while \(w_{t_j}\) has color \(s_{j+1}\) and prefers \(t_j\). Consequently
\[
v_{s_j}\longrightarrow w_{t_{j-1}}\longrightarrow v_{s_{j-1}}\longrightarrow\cdots\longrightarrow v_{s_j}
\]
is a blocking cycle, when its vertices are traversed with the obvious alternating cyclic indexing. More explicitly, every \(v_{s_j}\to w_{t_{j-1}}\) exists because \(w_{t_{j-1}}\) has color \(s_j\), and every \(w_{t_j}\to v_{s_j}\) exists because \(v_{s_j}\) has color \(t_j\). The selected vertices on a cyclic orbit are distinct: the \(s_j\) are distinct, and if two \(t_j\) were equal then the corresponding successors \(g(t_j)\) would be equal, contradicting distinctness on that orbit.

Thus *every* proper \(k\)-coloring has a blocking cycle. No stable proper \((b+1)\)-coloring exists for the displayed preference profile, proving \(\chi_{\mathrm{stable}}(K_{a,b,1})\ge b+2\). Together with the upper bound, this proves the claim for every \(a\ge b\ge1\).

## Verification

The standalone program `artifacts/verify.py` exhaustively enumerates every proper coloring on the adversarial palette for the six parameter pairs \((a,b)=(2,2),(3,2),(4,2),(3,3),(4,3),(5,3)\), confirming that every envy digraph contains a directed cycle. It also tests the constructive upper-bound coloring on 700 deterministic randomized preference profiles across seven parameter pairs, including \(b=1\). Separate direct enumeration of all palette maps for \((2,2),(3,2),(3,3)\) agreed with the structured enumeration. Execute from the package root with `python3 artifacts/verify.py` using the Python standard library. These checks are finite corroboration only; the proof above establishes the full infinite family.

## Relationship to prior work

Koana, Oh, and Yoneda (arXiv:2609.00569v1, first public 1 September 2026) introduced the stable chromatic number and proved the exact complete-bipartite formula \(\chi_{\mathrm{stable}}(K_{a,b})=b+1\) when \(a\ge b\). Their acyclic-orientation technique also yields the upper bound here. The new ingredient is a preference profile in which the indexed witnesses retain a complete set of favorite colors after **any one** color is reserved for the universal vertex. This converts the known complete-bipartite obstruction into a *strict apex increment*, which does not follow from subgraph monotonicity or the orientation bound alone.

An independently published exact computation gives \(\chi_{\mathrm{stable}}(K_{2,3,3})=6\), but it concerns three non-singleton parts and is not a formula for the present two-parameter family. A separate exact classification for complete graphs with a deleted matching covers a small boundary instance, \(K_{2,2,1}\cong K_5-M_2\), but does not imply the general case. These statements are acknowledged rather than presented as new.

## Limitations

The statement concerns complete tripartite graphs with **exactly one singleton part** and two other nonempty parts. It does not determine the stable chromatic number for arbitrary complete multipartite graphs or for several universal apex vertices. The motivating preprint's accessible abstract and detailed secondary technical synopsis, and the accessible full text of the related published \(K_{2,3,3}\) result, were checked; a complete first-hand reading of the motivating preprint was not possible through the available access route. This leaves a residual literature-coverage risk, as does unindexed independent work.

## References

1. T. Koana, Y. Oh, and H. Yoneda, *Graph Coloring with Color Preferences*, arXiv:2609.00569v1, posted 1 September 2026. https://arxiv.org/abs/2609.00569
2. *Stable chromatic number of the complete tripartite graph* \(K_{2,3,3}\), publicly accessible mathematical result and verification package, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-stable-chromatic-number-of-the-complete-tripartite-graph-k-2-3-3--b34a81e3d305
