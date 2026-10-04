# Two witness parts for proper conflict-free choosability of complete multipartite graphs
## Finding
Every connected complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) with \(r\ge2\) is proper conflict-free \((\mathrm{degree}+2)\)-choosable. If \(r\ge3\), then \(G\) is proper conflict-free \((\mathrm{degree}+1)\)-choosable.

## Assumptions and scope
A proper conflict-free coloring is a proper vertex coloring in which every non-isolated vertex has a color appearing exactly once in its open neighborhood. A graph is proper conflict-free \((\mathrm{degree}+k)\)-choosable if every list assignment \(L\) satisfying \(|L(v)|\ge d_G(v)+k\) admits such a coloring from the lists.

Let \(G=K_{n_1,\ldots,n_r}\) be connected, so \(r\ge2\) and every part is nonempty. Write the parts as \(P_1,\ldots,P_r\), and let \(N=\sum_i n_i\).

## Proof
We use the same construction for the two asserted offsets. Let \(q=2\) when \(r\ge2\), and let \(q=1\) when \(r\ge3\). Assume \(|L(v)|\ge d_G(v)+q\) for every vertex.

Choose a vertex \(x\in P_1\) and a color \(\alpha\in L(x)\). Give \(x\) color \(\alpha\). Every other vertex \(u\in P_1\) has at least two available colors because \(d_G(u)\ge1\) and \(q\ge1\), so color \(u\) from \(L(u)\setminus\{\alpha\}\). Thus \(\alpha\) occurs exactly once on \(P_1\). Let \(C_1\) be the set of colors used on \(P_1\); then \(|C_1|\le n_1\).

Choose \(y\in P_2\). If \(q=2\), then
\[
|L(y)|\ge N-n_2+2\ge n_1+2.
\]
If \(q=1\), the hypothesis \(r\ge3\) gives at least one vertex outside \(P_1\cup P_2\), so
\[
|L(y)|\ge N-n_2+1\ge n_1+2.
\]
Hence there is a color \(\beta\in L(y)\setminus C_1\). Give \(y\) color \(\beta\). For each other \(u\in P_2\), the forbidden set \(C_1\cup\{\beta\}\) has size at most \(n_1+1\), while the same lower bound \(|L(u)|\ge n_1+2\) holds. Therefore \(u\) can be colored outside \(C_1\cup\{\beta\}\). Thus \(\beta\) occurs exactly once on \(P_2\), and the palettes of \(P_1\) and \(P_2\) are disjoint.

Now process \(P_3,P_4,\ldots,P_r\) in order. Before coloring \(P_i\), let \(C\) be the set of colors already used. The number of distinct colors in \(C\) is at most the number of already colored vertices, which is at most \(N-n_i\). Since
\[
|L(v)|\ge N-n_i+q\ge N-n_i+1>|C|
\]
for every \(v\in P_i\), each vertex of \(P_i\) can be colored from \(L(v)\setminus C\). Colors may repeat inside \(P_i\), because a part is independent. After the whole part is colored, add its colors to \(C\) and continue.

The resulting coloring is proper: different parts use disjoint palettes, and vertices inside one part are nonadjacent. Moreover, \(\alpha\) remains unique on \(P_1\) and \(\beta\) remains unique on \(P_2\). Every vertex of \(P_1\) sees \(\beta\) exactly once in its neighborhood, every vertex of \(P_2\) sees \(\alpha\) exactly once, and every vertex in any later part sees both \(\alpha\) and \(\beta\) exactly once. Hence the coloring is proper conflict-free. This proves both assertions.

## Verification
The proof is constructive and uses only the displayed list-size inequalities and the fact that different parts of a complete multipartite graph are completely adjacent. The accompanying `verify.py` implements the construction. It exhaustively checks all exact-size list assignments in five small multipartite instances and then performs deterministic seeded stress tests on larger bipartite and multipartite profiles. The replay output ends with `ALL CHECKS PASSED`.

The finite checks are only implementation tests; the theorem is established by the general proof above, not by finite enumeration.

## Relationship to prior work
Kashima, Škrekovski, and Xu introduced proper conflict-free degree-choosability and conjectured that every connected graph other than the 5-cycle is proper conflict-free \((\mathrm{degree}+2)\)-choosable. Their later sparse-graph paper records this as Conjecture 1.1 and proves, as an auxiliary result, that \(K_{2,r}\) is proper conflict-free \((\mathrm{degree}+2)\)-choosable. The present theorem extends that biclique slice to every connected complete multipartite graph.

The same later paper also conjectures proper conflict-free \((\mathrm{degree}+1)\)-choosability for connected graphs of minimum degree at least three. The second clause above proves the stronger list bound for every complete multipartite graph with at least three parts, without a minimum-degree assumption.

Targeted database and literature searches for the complete-multipartite \((\mathrm{degree}+2)\) theorem, the three-or-more-parts \((\mathrm{degree}+1)\) theorem, and their natural aliases found no prior statement implying either clause. The principal full texts inspected state the general conjectures, sparse-class results, and the \(K_{2,r}\) special case, but not the complete-multipartite theorem.

## Limitations
No optimality is claimed. In particular, the argument does not determine whether every complete bipartite graph is proper conflict-free \((\mathrm{degree}+1)\)-choosable, nor does it classify the smallest admissible offset for each multipartite part-size vector. The originality assessment is bibliographic rather than a formal novelty certificate; an unindexed or differently worded prior result remains possible.

## References
1. M. Kashima, R. Škrekovski, and R. Xu, “Remarks on proper conflict-free degree-choosability of graphs with prescribed degeneracy,” arXiv:2509.12560, first submitted 2025-09-16.
2. M. Kashima, R. Škrekovski, and R. Xu, “Degree-choosability of proper conflict-free list coloring of sparse graphs,” arXiv:2601.15611, first submitted 2026-01-22.
