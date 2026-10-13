# Exact k-tuple total dominator colorings of complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), part sizes \(n_i\ge1\), total order \(N=\sum_i n_i\), and largest part size \(L=\max_i n_i\). Let \(k\ge1\). A \(k\)-tuple total dominator coloring exists if and only if
\[
k\le N-L.
\]
For every feasible \(k\), define
\[
\tau=\min\left\{t\in\mathbb Z_{\ge1}: r\le k+t\le\sum_{i=1}^r\min\{n_i,t\}\right\}.
\]
Then
\[
\chi_{k,d}^t(G)=k+\tau.
\]
More precisely, every optimal coloring is obtained by choosing integers \(c_1,\ldots,c_r\) satisfying
\[
1\le c_i\le\min\{n_i,\tau\},\qquad \sum_{i=1}^r c_i=k+\tau,
\]
and partitioning the vertices of part \(i\) into exactly \(c_i\) nonempty color classes, with no color shared by two parts. Conversely, every such choice is optimal.

If colors are labeled by \([k+\tau]\), the exact number of optimal colorings is
\[
(k+\tau)!\sum_{\substack{1\le c_i\le\min\{n_i,\tau\}\\\sum_i c_i=k+\tau}}
\prod_{i=1}^r {n_i\brace c_i},
\]
where \({n\brace c}\) is a Stirling number of the second kind. Up to permutation of colors, the factor \((k+\tau)!\) is omitted.

Two useful specializations are immediate. If \(1\le k\le r-1\), then \(\tau=r-k\) and
\[
\chi_{k,d}^t(G)=r.
\]
If \(G=K_{m,n}\) with \(1\le m\le n\), then a \(k\)-tuple total dominator coloring exists exactly for \(1\le k\le m\), and throughout that range
\[
\chi_{k,d}^t(K_{m,n})=2k.
\]

## Assumptions and scope

All graphs are finite, simple, and undirected. A \(k\)-tuple total dominator coloring is a proper vertex coloring in which every vertex is adjacent to every vertex of at least \(k\) distinct color classes. The parameter \(\chi_{k,d}^t(G)\) is the minimum number of nonempty color classes in such a coloring.

The theorem concerns connected complete multipartite graphs, hence \(r\ge2\). It explicitly includes singleton parts and the boundary \(k=N-L\). When \(k>N-L\), no such coloring exists, so no finite value of \(\chi_{k,d}^t(G)\) is asserted.

## Proof

Let the multipartite parts be \(P_1,\ldots,P_r\). In any proper coloring of a complete multipartite graph, a color cannot occur in two different parts because every two vertices in different parts are adjacent. Thus every color class lies entirely inside a unique part. Let \(c_i\) be the number of nonempty color classes contained in \(P_i\), and let
\[
q=\sum_{i=1}^r c_i
\]
be the total number of colors.

Fix a vertex \(v\in P_i\). It is adjacent to every vertex outside \(P_i\) and to no vertex in \(P_i\). Therefore \(v\) is adjacent to every vertex of exactly the \(q-c_i\) color classes supported outside \(P_i\). Consequently, the coloring is a \(k\)-tuple total dominator coloring if and only if
\[
q-c_i\ge k\qquad(1\le i\le r).
\]
This reduces the entire problem to an integer occupancy condition.

First consider existence. Since each color class outside \(P_i\) contains at least one vertex, \(q-c_i\le N-n_i\). Hence existence forces \(k\le N-n_i\) for every \(i\), equivalently \(k\le N-L\). Conversely, if \(k\le N-L\), color every vertex differently. Then for each \(i\), a vertex in \(P_i\) totally dominates the \(N-n_i\ge k\) singleton color classes outside its part. This proves the feasibility criterion.

Assume now that \(k\le N-L\). For any feasible coloring put
\[
t=q-k.
\]
The inequalities \(q-c_i\ge k\) are equivalent to \(c_i\le t\). Since also \(1\le c_i\le n_i\), every feasible coloring with \(q=k+t\) colors satisfies
\[
r\le k+t=\sum_i c_i\le\sum_i\min\{n_i,t\}.
\]
Thus its value of \(t\) belongs to the set defining \(\tau\), and hence \(q\ge k+\tau\).

Conversely, let \(t=\tau\). Put \(b_i=\min\{n_i,\tau\}\). The defining inequalities for \(\tau\) say
\[
r\le k+\tau\le\sum_i b_i.
\]
Starting with \(c_i=1\) for all \(i\) and distributing the remaining \(k+\tau-r\) units among the parts without exceeding \(b_i\), one obtains integers \(c_i\) with \(1\le c_i\le b_i\) and \(\sum_i c_i=k+\tau\). Partition \(P_i\) into \(c_i\) nonempty classes and give all resulting classes distinct colors. Then
\[
(k+\tau)-c_i\ge k,
\]
so this is a valid \(k\)-tuple total dominator coloring. Therefore \(\chi_{k,d}^t(G)=k+\tau\). The same argument shows that the displayed conditions on \((c_i)\) characterize all optimal colorings.

For the enumeration, fix an admissible optimal vector \((c_i)\) and put \(q=k+\tau\). There are
\[
\frac{q!}{\prod_i c_i!}
\]
ways to allocate the \(q\) labeled colors among the parts. For part \(P_i\), the number of surjections from its \(n_i\) labeled vertices onto its prescribed \(c_i\) labeled colors is
\[
c_i!{n_i\brace c_i}.
\]
Multiplying and cancelling the factors \(c_i!\) gives \(q!\prod_i{n_i\brace c_i}\). Summing over all admissible vectors proves the counting formula.

If \(k\le r-1\), any proper coloring already uses at least \(r\) colors, while the one-color-per-part coloring is \(k\)-tuple total dominator, proving \(\chi_{k,d}^t(G)=r\). For \(K_{m,n}\), feasibility is \(k\le m\). In any feasible coloring each shore must contain at least \(k\) color classes because a vertex can totally dominate only classes on the opposite shore; splitting each shore into exactly \(k\) nonempty classes attains \(2k\).

## Verification

The accompanying executable checker independently enumerates all color-count vectors for complete multipartite profiles with two through four parts and part sizes at most five, comparing the resulting minimum directly with the formula for \(\tau\). It separately enumerates labeled vertex colorings for every ordered multipartite profile of total order at most six, verifies the minimum and the Stirling-number count of optimal colorings, and checks the complete-bipartite specialization throughout \(1\le m\le n\le50\) and \(1\le k\le m\).

These finite computations are stress tests only. The infinite theorem, the feasibility boundary, and the enumeration formula are proved analytically above.

## Relationship to prior work

Beggas and Marweni introduced the general \(k\)-tuple total dominator coloring framework studied here and published a broad study of bounds, corona constructions, edge-corona constructions, and graph modifications. The publisher metadata lists Mathematics Subject Classification 05C15 and 05C69. The accessible abstract and indexed metadata do not state a complete-multipartite exact formula. The full article was not available in the lawful public sources inspected, so possible hidden overlap in that article is retained as a residual literature risk rather than treated as disproved.

The case \(k=1\) is the established total dominator coloring invariant and is not claimed as new. The case \(k=2\) is the previously introduced double total dominator coloring. Targeted searches of those names, of complete bipartite and complete multipartite variants, and of the general \(k\)-tuple terminology found no statement implying the all-\(k\) water-filling formula, the complete-bipartite law \(2k\), or the optimal-coloring enumeration above. The accepted content is therefore the simultaneous arbitrary-\(k\) structural classification and enumeration, not the already-known definitions or the \(k=1\) specialization.

## Limitations

The theorem relies essentially on the complete multipartite adjacency pattern. It does not extend verbatim to multipartite graphs with missing cross edges or added within-part edges. The result counts only minimum-color \(k\)-tuple total dominator colorings; it does not enumerate valid colorings using more colors. A residual originality risk remains because the full text of the 2025 initiating article was not accessible in the public sources inspected, although its abstract, metadata, references, targeted web searches, and dedicated database searches did not expose a covering complete-multipartite theorem.

## References

1. F. Beggas and W. Marweni, “An extensive study on the k-tuple total dominator chromatic number of graphs,” *Computational and Applied Mathematics* 45, 74 (2026), published online 15 October 2025. DOI: 10.1007/s40314-025-03466-7.
2. F. Beggas, H. Kheddouci, and W. Marweni, “On the double total dominator chromatic number of graphs,” *Discrete Mathematics, Algorithms and Applications* 14 (2022), 2150154. DOI: 10.1142/S1793830921501548.
3. A. P. Kazemi, “Total dominator chromatic number in graphs,” *Transactions on Combinatorics* 4 (2015), 57–68. DOI: 10.22108/TOC.2015.6171.
