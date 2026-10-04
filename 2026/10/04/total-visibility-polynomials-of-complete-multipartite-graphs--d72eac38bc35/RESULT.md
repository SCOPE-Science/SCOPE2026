# Total visibility polynomials of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph, \(r\ge2\), with \(N=\sum_i n_i\), \(I=\{i:n_i\ge2\}\), \(q=|I|\), and \(s=|\{i:n_i=1\}|\). Its total visibility polynomial is \((1+x)^N\) when \(q=0\), and for \(q\ge1\) it is \[\mathcal V_t(G;x)=(1+x)^N-\sum_{i\in I}x^{N-n_i}(1+x)^{n_i}+(q-1)x^N.\] Moreover, the maximal total mutual-visibility sets are exactly: \(V(G)\) if \(q=0\); the sets \(V(G)\setminus\{u\}\) with \(u\) in a singleton part if \(q=1\); and, if \(q\ge2\), the sets whose complements are either one singleton-part vertex or two vertices from two distinct non-singleton parts. Consequently, \[\mu_t^-(G)=\begin{cases}N,&q=0,\\N-1,&q=1,\\N-2,&q\ge2,\end{cases}\] and the number of maximal total mutual-visibility sets is \(1\), \(s\), or \(s+\sum_{i<j,\ i,j\in I}n_i n_j\), respectively.

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. For a graph \(G\), a set \(X\subseteq V(G)\) is a total mutual-visibility set if every two vertices of \(G\) have a shortest path whose internal vertices avoid \(X\). The total visibility polynomial \(\mathcal V_t(G;x)\) counts such sets by cardinality. A maximal total mutual-visibility set is maximal under inclusion, and \(\mu_t^-(G)\) is the minimum cardinality of such a maximal set.

Write the partite classes of \(G=K_{n_1,\ldots,n_r}\) as \(V_1,\ldots,V_r\), put \(N=\sum_i n_i\), and let \(I=\{i:n_i\ge2}\), \(q=|I|\), and \(s=|\{i:n_i=1}|\).

## Proof
Let \(X\subseteq V(G)\) and write \(Y=V(G)\setminus X\). Vertices in different partite classes are adjacent. The only pairs at distance two are pairs of distinct vertices in the same non-singleton class \(V_i\), and every shortest path between such a pair has exactly one internal vertex in \(V(G)\setminus V_i\). Therefore
\[
X	ext{ is total mutual-visible}
\quad\Longleftrightarrow\quad
Y\capigl(V(G)\setminus V_iigr)
earnothing\ 	ext{ for every }i\in I.
	ag{1}
\]
Equivalently, \(Y
ot\subseteq V_i\) for every \(i\in I\).

If \(q=0\), then \(G\) is complete, every vertex set is total mutual-visible, and hence
\[
\mathcal V_t(G;x)=(1+x)^N.
\]
Assume \(q\ge1\). In the complement description, the forbidden sets \(Y\) are exactly those belonging to \(\mathcal P(V_i)\) for at least one \(i\in I\). Their weighted contribution to \(\sum_Y x^{N-|Y|}\) is
\[
x^{N-n_i}(1+x)^{n_i}
\]
for class \(V_i\). Since distinct partite classes are disjoint, the families \(\mathcal P(V_i)\) and \(\mathcal P(V_j)\) intersect only in \(\{arnothing}\). Thus weighted inclusion-exclusion gives
\[
\mathcal V_t(G;x)
=(1+x)^N-
\sum_{i\in I}x^{N-n_i}(1+x)^{n_i}+(q-1)x^N.
	ag{2}
\]

It remains to classify maximal sets. By monotonicity, \(X\) is maximal total mutual-visible exactly when its complement \(Y\) is inclusion-minimal subject to (1).

If \(q=0\), the unique minimal complement is \(Y=arnothing\), so the unique maximal set is \(V(G)\).

If \(q=1\), say \(I=\{1}\), condition (1) requires \(Y\) to contain a vertex outside \(V_1\). Every class outside \(V_1\) is a singleton. Hence the minimal admissible complements are exactly the one-element sets consisting of a singleton-part vertex. There are \(s\) of them, and every maximal set has size \(N-1\).

Suppose \(q\ge2\). A one-element complement \(\{u}\) is admissible exactly when \(u\) lies in a singleton part, because then \(u
otin V_i\) for every \(i\in I\). Also, if \(u\in V_i\) and \(v\in V_j\) for distinct \(i,j\in I\), then \(Y=\{u,v}\) is admissible and is minimal: deleting \(u\) leaves a singleton subset of \(V_j\), and deleting \(v\) leaves a singleton subset of \(V_i\). Conversely, let \(Y\) be a minimal admissible complement. If it contains a singleton-part vertex, that vertex alone is admissible, so minimality forces \(|Y|=1\). Otherwise every vertex of \(Y\) lies in a non-singleton part. Admissibility forces \(Y\) to meet at least two such parts. If \(|Y|\ge3\), one can delete a vertex while retaining vertices in at least two non-singleton parts, contradicting minimality. Hence \(Y\) consists of exactly two vertices in two distinct non-singleton parts.

The stated lower total mutual-visibility number follows by subtracting the maximum size of a minimal admissible complement from \(N\). The number of maximal sets is \(1\) when \(q=0\), is \(s\) when \(q=1\), and for \(q\ge2\) equals
\[
s+\sum_{i<j,\ i,j\in I}n_i n_j,
\]
because the second type of minimal complement is determined by an unordered pair of non-singleton parts and one chosen vertex in each.

## Verification
The accompanying `verify.py` constructs each complete multipartite graph directly, computes graph distances by breadth-first search, and tests the defining total mutual-visibility condition by deleting the proposed internal blockers and checking whether every pair retains its original distance. It exhaustively checks all vertex subsets for all \(87\) complete multipartite isomorphism types of orders \(2\) through \(9\). For each graph it independently compares the full coefficient vector of \(\mathcal V_t(G;x)\), the number of maximal total mutual-visibility sets, and \(\mu_t^-(G)\) with the formulas above.

The archived output is:
`VERIFY_OK`
`checked 87 complete multipartite isomorphism types of orders 2..9`
`verified the full total-visibility polynomial, maximal-set count, and lower total mutual-visibility formula`
`the all-orders theorem rests on the accompanying structural proof`

The finite computation is corroborative only; the theorem for arbitrary part sizes follows from the structural proof.

## Relationship to prior work
Brešar and Yero introduced the lower total mutual-visibility number in 2023/2024 and proved general bounds, complexity results, and several product formulas. Their full text contains no complete-multipartite treatment of \(\mu_t^-\); its complete-bipartite proposition concerns the different invariant \(\mu^-\).

Bujtás, Klavžar, and Tian introduced visibility polynomials and proved a general distance-two characterization of total mutual-visibility sets. They explicitly computed the total visibility polynomial of balanced complete bipartite graphs, obtaining
\[
\mathcal V_t(K_{n,n};x)=igl((1+x)^n-x^nigr)^2,
\]
and noted that general complete bipartite graphs can be handled similarly. Formula (2) specializes to that result and extends the enumeration to arbitrary complete multipartite graphs, including singleton parts. Their full text contains no occurrence of “multipartite.”

A later Builder-Blocker study treats complete multipartite graphs for the ordinary mutual-visibility game and describes maximal ordinary mutual-visibility sets used by that game. It does not state a total visibility polynomial or the lower total mutual-visibility classification above.

## Limitations
Originality is a best-of-knowledge conclusion based on exact-phrase, alias, implication, and full-text comparisons with the defining lower-total paper, the visibility-polynomial paper, and later complete-multipartite mutual-visibility work. The 2025 distance-two theorem supplies a general criterion from which condition (1) can be derived, so the main originality risk is that an unlocated source may already have carried out the resulting weighted enumeration or maximal-complement classification.

The result concerns complete multipartite graphs only. It does not determine lower total mutual-visibility numbers or visibility polynomials for arbitrary cographs or arbitrary diameter-two graphs. No independent audit, expert attestation, or formal proof-assistant verification has been performed.

## References
1. B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv `2307.02951`; Applied Mathematics and Computation 465 (2024), 128411, DOI `10.1016/j.amc.2023.128411`.
2. C. Bujtás, S. Klavžar, and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv `2412.03066`; Aequationes Mathematicae 99 (2025), 1883–1901, DOI `10.1007/s00010-025-01197-y`.
3. V. Iršič Chenoweth, S. Klavžar, G. Rus, E. Tan, and J. Tian, *Builder-Blocker Mutual-Visibility Game*, Bulletin of the Malaysian Mathematical Sciences Society (2026), DOI `10.1007/s40840-026-02083-9`.
