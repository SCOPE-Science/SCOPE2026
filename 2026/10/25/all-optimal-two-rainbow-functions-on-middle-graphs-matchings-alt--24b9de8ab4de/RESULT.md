# All optimal two-rainbow functions on middle graphs: matchings, alternating cycles, and residual colorings

## Finding

For every finite simple graph \(G=(V,E)\), let \(M(G)\) denote its middle graph and let \(N(G)\) count its minimum-weight two-rainbow dominating functions, distinguishing both the vertices and the two colors. A *configuration* consists of (i) a matching \(Q\subseteq E\); (ii) a collection \(\mathcal C\) of pairwise vertex-disjoint, undirected simple even cycles of \(G\) that avoid every endpoint of \(Q\); and (iii) a proper assignment of colors 1 and 2 to the vertices of
\[
 U=V\setminus\bigl(V(Q)\cup\textstyle\bigcup_{C\in\mathcal C}V(C)\bigr).
\]
Each chosen cycle additionally admits exactly two alternating assignments of its edge-vertices to the singleton labels \(\{1\}\) and \(\{2\}\). A chosen matching edge-vertex receives \(\{1,2\}\). Every remaining edge-vertex receives the empty label, and every original vertex outside \(U\) receives the empty label.

**Theorem.** These and only these are the minimum-weight two-rainbow functions of \(M(G)\); their common weight is \(|V|\). In particular,
\[
 N(G)=\sum_{\substack{Q\ \mathrm{matching},\;\mathcal C\ \text{vertex-disjoint even cycles}\\V(Q)\cap V(\mathcal C)=\varnothing}} 2^{|\mathcal C|}\,\chi_{G[U]}(2),
\]
where \(\chi_H(2)\) means the number of proper two-colorings of \(H\). A graph with no vertices has one proper coloring; for a nonempty graph, \(\chi_H(2)=0\) if it is not bipartite and \(\chi_H(2)=2^{c(H)}\) otherwise.

For any forest \(F\), the cycle family is necessarily empty, so
\[
 N(F)=\sum_{Q\text{ a matching of }F}2^{c(F[V\setminus V(Q)])}.
\]
For a path on \(n\ge0\) original vertices, writing \(a_n=N(P_n)\),
\[
 \sum_{n\ge0}a_nz^n=\frac{1+z}{1-z-z^2-z^3},\qquad (a_0,a_1,a_2,a_3,a_4,a_5)=(1,2,3,6,11,20).
\]
For the star with one center and \(m\ge1\) leaves, \(N(K_{1,m})=2+m2^{m-1}\).

## Assumptions and scope

All graphs are finite, undirected and simple; disconnected graphs and isolated vertices are allowed. The middle graph has vertex set the disjoint union \(V(G)\sqcup E(G)\). An original vertex is adjacent precisely to its incident edge-vertices; two edge-vertices are adjacent when the underlying edges share an endpoint. A two-rainbow function assigns each middle-graph vertex one of \(\varnothing,\{1\},\{2\},\{1,2\}\) and is feasible if every empty-labeled vertex has all of \(\{1,2\}\) in the union of its neighbors' labels. Its weight is the total number of assigned color tokens. Distinct matchings and undirected cycle edge sets are counted separately; cycle orientations are not counted, whereas the two alternating color assignments are counted. No quotient by automorphisms is taken.

## Proof

**Step 1 (a local charge).** For each original vertex \(v\), define
\[
 q(v)=|f(v)|+\frac12\sum_{e\ni v}|f(e)|.
\]
Every edge has two endpoints, hence \(\sum_{v\in V}q(v)=w(f)\). If \(f(v)\ne\varnothing\), then \(q(v)\ge1\). If \(f(v)=\varnothing\), its only neighbors in \(M(G)\) are its incident edge-vertices; by the two-rainbow condition these edge labels jointly contain both colors, so their total cardinality is at least two and again \(q(v)\ge1\). Thus \(w(f)\ge |V|\).

To attain the bound, take a maximal matching of \(G\), assign \(\{1,2\}\) to its edge-vertices, and assign \(\{1\}\) to every unmatched original vertex; set all other labels empty. Every empty original vertex is incident to a chosen edge and sees both colors. Every empty edge-vertex meets an edge of the maximal matching (otherwise the matching could be enlarged), so also sees both colors. An unmatched original vertex is not empty. This function has weight \(2|Q|+(|V|-2|Q|)=|V|\), proving the optimum is exactly \(|V|\). For edgeless graphs the matching is empty and the same construction works.

**Step 2 (all equality cases).** If \(w(f)=|V|\), all charges \(q(v)\) equal one. An original vertex bearing a nonempty label therefore has exactly one singleton color and no nonempty incident edge label. Every empty original vertex has incident edge-label cardinalities totaling exactly two. Because it must see both colors, either exactly one incident edge has label \(\{1,2\}\), or exactly two incident edges have opposite singleton labels.

The first kind of empty vertex is an endpoint of precisely one doubly labeled edge. Consequently the doubly labeled edges form a matching \(Q\). All remaining nonempty edge labels are singletons, each incident to an empty original vertex of the second kind at both endpoints. Therefore the graph formed by these singleton-labeled edges has degree two at every one of its nonisolated vertices and its incident edge colors differ at each vertex. Its components are simple even cycles with alternating edge colors. Those cycle vertices are disjoint from matching endpoints. Every original vertex outside these parts has one singleton color.

**Step 3 (the residual condition).** Consider any edge-vertex not selected in either \(Q\) or a cycle. If one of its endpoints lies on a matching edge, it sees the chosen doubly labeled edge-vertex and hence both colors. If one endpoint lies on an alternating cycle, it sees both cycle colors on the two other incident edge-vertices. Otherwise both endpoints lie in \(U\); its only possible nonempty neighbors are those two original vertices, and its rainbow condition is equivalent to their singleton colors being distinct. Thus the labels on \(U\) form a proper two-coloring of \(G[U]\). Conversely, every configuration of the theorem meets the rainbow requirement at every empty vertex by this same case distinction. The extraction and reconstruction are inverses, yielding the bijection and enumeration formula.

**Step 4 (path and star).** In a path there are no cycles, so configurations are tilings of the path by chosen matching edges (dominoes) and remaining singleton vertices (monomers); any two consecutive monomers have distinct colors. Let \(D(z)\) count allowed suffixes when the preceding tile is a domino or there is no preceding tile, and \(S(z)\) count them when the preceding tile is a fixed-color monomer. Empty suffixes contribute one. A domino of length two can always be followed by a \(D\)-suffix, whereas a monomer following a fixed-color monomer has one choice and a monomer following a domino has two. Hence
\[
 S=1+zS+z^2D,\qquad D=1+2zS+z^2D.
\]
Solving gives \(D=(1+z)/(1-z-z^2-z^3)\). For \(K_{1,m}\), the empty matching contributes two proper two-colorings, and choosing any one of the \(m\) matching edges leaves \(m-1\) isolated vertices and hence \(2^{m-1}\) two-colorings. No even cycle is present. This proves the stated specialization.

## Verification

The standalone file `verify.py` tests the original middle-graph adjacency and two-rainbow condition by exhaustive assignment of all color tokens of total weight at most \(|V|\). It then independently enumerates graph matchings, undirected simple even cycles, compatible cycle packs, and residual proper two-colorings. The two counts agree in 86 test graphs, including all simple labeled graphs of orders at most four; all checked functions of weight below \(|V|\) are infeasible. This includes 1,671,091 candidate token assignments and graphs with up to 15 middle-graph vertices. The script separately tests path terms, stars, and the instances \(N(K_4)=21\), \(N(C_4)=14\), and \(N(C_5)=20\). Run with `python verify.py` using only Python's standard library. The printed output is in `verification_output.txt`. Finite tests are checks of premises and special cases, not a substitute for the preceding all-order proof.

## Relationship to prior work

Kim introduced the study of rainbow domination in middle graphs in a paper publicly deposited on 17 November 2020 (reference [1], primary 05C69); the results there principally treat three-rainbow domination. In a later full article, Kim proved \(\gamma_{r2}(M(G))=|V(G)|\) for every graph (reference [2], Theorem 1.3), and characterized optimum **Roman** functions, which are a strictly more restrictive labeling class than two-rainbow functions. The minimum value is therefore prior work and not claimed here. The present theorem classifies and enumerates *every* two-rainbow minimum function, including alternating-cycle solutions that cannot arise as Roman functions. The path sequence agrees with OEIS A047081 (reference [3]), which records its recurrence but not this middle-graph combinatorial interpretation. Searches did not locate a direct published equivalent classification; lack of an indexed match is not a proof of priority.

## Limitations

The theorem concerns the ordinary two-rainbow domination rule and the middle-graph construction, not Italian domination, Roman domination or higher rainbow cardinalities. The graph-wide formula is a structural sum, not a polynomial-time evaluation algorithm for arbitrary graphs. It distinguishes named colors and labeled graph vertices and does not count classes under automorphisms. No claim is made that the path recurrence is a new integer sequence. Exhaustive bibliographic priority confirmation and independent scientific validation have not been performed.

## References

[1] K. Kim, *On k-rainbow domination in middle graphs*, arXiv:2011.08635v1 (public 2020-11-17); published in RAIRO Operations Research 55 (2021), 3447–3458, DOI 10.1051/ro/2021163. https://arxiv.org/abs/2011.08635

[2] K. Kim, *Italian, 2-rainbow and Roman domination numbers in middle graphs*, RAIRO Operations Research 58 (2024), 2045–2053, DOI 10.1051/ro/2024072. https://doi.org/10.1051/ro/2024072

[3] OEIS Foundation, A047081 (classical order-three recurrence and generating function). https://oeis.org/A047081
