# Sub-quorum coloring number of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\) and all parts nonempty. Put \(L=\max_i n_i\). Then
\[
\psi_{sq}(G)=\max\{L,2\}.
\]

More structurally, take any sub-quorum coloring with at least three colors, let \(H\) be its colored induced subgraph, and let \(P\) be any largest occupied multipartite part of \(H\). Every color class meets \(P\). Hence the number of colors is at most \(|P|\le L\).

## Assumptions and scope
A sub-quorum coloring is an onto partial vertex coloring. For every colored vertex, at least half of the colored vertices in its closed neighborhood have its color. Equivalently, if the colored vertex set is \(S\), the color classes form a quorum coloring of the induced graph \(G[S]\). This equivalence is part of the initiating definition.

The theorem concerns finite simple complete multipartite graphs with at least two nonempty parts. Empty color classes are never counted. The two-color floor is needed exactly when \(L=1\), that is, when \(G\) is complete.

## Proof
Consider a sub-quorum coloring using \(q\) colors and let \(H=G[S]\) be its colored induced subgraph. The occupied parts of \(H\) have sizes \(a_1,\ldots,a_s\). Let \(P\) be one of largest occupied parts, write \(|P|=L_H\), and put
\[
M=|V(H)|-L_H.
\]
If \(s=1\), then \(H\) is edgeless, so \(q\le |V(H)|=L_H\le L\). We may therefore assume \(s\ge2\), so \(M\ge1\).

Suppose first that \(q\ge3\). Set
\[
h=\left\lceil\frac{M+1}{2}\right\rceil.
\]
For a color class \(C\) meeting \(P\), choose \(v\in C\cap P\). The colored closed neighborhood of \(v\) contains \(v\) together with every colored vertex outside \(P\), so it has size \(M+1\). If \(y=|C\setminus P|\), exactly \(y+1\) vertices of this closed neighborhood have the color of \(v\). The quorum inequality therefore gives
\[
y\ge h-1.
\]

Now let \(C\) be a color class disjoint from \(P\), and choose \(v\in C\) in an occupied part of size \(a\le L_H\). Its colored closed neighborhood has size \(|V(H)|-a+1\ge M+1\). The number of same-colored vertices visible there is at most \(|C|\). Hence
\[
|C|\ge h.
\]

Let \(u\) be the number of color classes meeting \(P\), and let \(w=q-u\) be the number disjoint from \(P\). If \(w\ge1\), then all vertices counted below lie outside \(P\), giving
\[
M\ge u(h-1)+wh.
\]
If \(M=2b\) is even, then \(b\ge1\) and \(h=b+1\), so the right-hand side is \(qb+w\ge3b+1>M\), impossible. If \(M=2b+1\ge3\), then \(b\ge1\) and \(h=b+1\), so the right-hand side is \(qb+w\ge3b+1>M\), again impossible.

The remaining case is \(M=1\). If a color class is disjoint from \(P\), it consists of the unique vertex \(z\) outside \(P\). The colored closed neighborhood of \(z\) has size \(L_H+1\), while only \(z\) itself has its color. The quorum inequality forces \(L_H\le1\), so \(|V(H)|=2\), contradicting \(q\ge3\). Thus \(w=0\) in every case.

Therefore every color class meets \(P\). Distinct color classes meet \(P\) in disjoint nonempty sets, and hence
\[
q\le |P|=L_H\le L.
\]
This proves the upper bound for all \(q\ge3\). Colorings with at most two colors automatically satisfy \(q\le\max\{L,2\}\), so
\[
\psi_{sq}(G)\le\max\{L,2\}.
\]

For the lower bound, if \(L\ge2\), choose a largest part and color each of its \(L\) vertices with a distinct color, leaving all other vertices uncolored. The colored induced graph is edgeless, so every colored closed neighborhood is a singleton and the coloring is sub-quorum. Thus \(\psi_{sq}(G)\ge L\). If \(L=1\), then \(G\) is a complete graph on at least two vertices. Color any two vertices with distinct colors and leave the rest uncolored. Each colored closed neighborhood then has two colored vertices, exactly one of its own color, so \(\psi_{sq}(G)\ge2\). The upper and lower bounds coincide.

## Verification
The standalone verifier enumerates every complete-multipartite isomorphism type through order \(7\), every nonempty colored vertex subset, and every unlabeled partition of that subset into color classes. It tests the sub-quorum condition directly from colored closed neighborhoods, compares the computed maximum with \(\max\{L,2\}\), and separately checks the structural assertion for every valid coloring with at least three colors.

The replay result is:

`ALL CHECKS PASSED; multipartite_profiles=37; partial_color_partitions=68154; structural_class_checks=7500; max_order=7`

This computation is only a finite stress test. The all-parameter theorem is established by the analytic counting argument above.

## Relationship to prior work
Sahbi, Belkina, and Bennadji introduced the first systematic study of sub-quorum coloring in arXiv:2609.39619v1, first public on 30 September 2026. Their full text defines a sub-quorum coloring exactly as a quorum coloring on a vertex-induced colored subgraph, proves general lower bounds including \(\psi_{sq}(G)\ge\beta_1(G)\) and \(\psi_{sq}(G)\ge\beta_2(G)\), and determines exact values for paths, stars, double stars, and several caterpillar families. A document-wide inspection found no complete-multipartite or complete-bipartite theorem. The lower construction for \(L\ge2\) is consistent with their independent-set lower bound; the new content here is the matching upper bound, the complete-graph boundary, and the structural obstruction for three or more colors.

Earlier quorum-coloring work does treat complete multipartite graphs, but for the ordinary invariant rather than the partial one. Sahbi's 2021 paper proves, for example, that an odd number of parts each of size three can have ordinary quorum number \(1\). Combining that published fact with the theorem above gives a sharp illustration of the point of the sub-quorum model: on the same graphs the sub-quorum number is \(3\).

Targeted semantic literature searches under sub-quorum, complete multipartite, complete bipartite, induced-subgraph, and maximum-part formulations returned only different coloring or domination invariants on the same graph family.

## Limitations
The proof uses the exact complete-multipartite neighborhood structure and does not automatically extend to arbitrary multipartite graphs with missing cross edges. The literature search cannot rule out an unindexed equivalent statement, especially under defensive-alliance terminology. The initiating sub-quorum paper is very recent, so concurrent-literature risk is nonzero. No independent audit has been performed.

## References
1. R. Sahbi, Y. Belkina, and A. Bennadji, *Sub-quorum colorings of some infinite families of caterpillars*, arXiv:2609.39619v1, first public version 2026-09-30.
2. R. Sahbi, *Solutions to four open problems on quorum colorings of graphs*, RAIRO Operations Research 55 (2021), 2385-2394, DOI:10.1051/ro/2021116.
3. S. M. Hedetniemi, S. T. Hedetniemi, R. Laskar, and H. M. Mulder, *Quorum colorings of graphs*, AKCE International Journal of Graphs and Combinatorics 10 (2013), 97-109.
