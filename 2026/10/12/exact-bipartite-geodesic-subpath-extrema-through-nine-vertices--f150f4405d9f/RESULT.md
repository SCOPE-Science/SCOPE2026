# Exact bipartite geodesic subpath extrema through nine vertices

## Finding

Let \(\operatorname{gpn}(G)\) denote the number of geodesics (shortest paths) between unordered distinct pairs of vertices in a finite connected simple graph, together with one zero-length geodesic at every vertex. Define
\[
M_n^{\mathrm{bip}}=\max\{\operatorname{gpn}(G):G\text{ is a connected simple bipartite graph on }n\text{ vertices}\}.
\]
**Theorem (complete small-order classification).** For \(n\in\{7,8,9\}\),
\[
\boxed{M_7^{\mathrm{bip}}=49,\quad M_8^{\mathrm{bip}}=74,\quad M_9^{\mathrm{bip}}=105.}
\]
Moreover all equality graphs, up to isomorphism, are as follows.

| Order | All maximum graphs (up to isomorphism) |
|---|---|
| \(7\) | \(K_{3,4}\), or \(K_{3,4}\) with exactly one edge removed. |
| \(8\) | \(K_{4,4}\) with a matching of size \(1\) or \(2\) removed. |
| \(9\) | \(K_{4,5}\) with a matching of size \(2\) or \(3\) removed; **or** \(K_{4,5}\) with the four edges of two vertex-disjoint \(K_{1,2}\) stars removed, both centers belonging to the five-vertex part. |

The third nine-vertex extremizer has diameter exactly \(4\); every nine-vertex matching-deletion extremizer has diameter \(3\). Thus the last equality case is structurally different from all matching-deletion graphs. For fixed named shores of the displayed sizes, the numbers of maximizing incidence matrices are \(13\), \(88\), and \(420\), respectively, distributed by the equality types as \((1,12)\), \((16,72)\), and \((120,240,60)\). These are counts **relative to fixed shore labels**, not counts of arbitrary fully labeled graphs.

## Assumptions and scope

All graphs are finite, simple, undirected, connected, and bipartite. For vertices \(u\ne v\), let \(\sigma_G(u,v)\) be the number of distinct unoriented shortest \(u\)-to-\(v\) paths. Then
\[
\operatorname{gpn}(G)=|V(G)|+\sum_{\{u,v\}\subseteq V(G)}\sigma_G(u,v).
\]
The extremum is over *all* bipartite graphs of the stated order, not merely complete bipartite graphs or their matching deletions. The result is finite and exact for the three orders \(7\), \(8\), \(9\) only.

## Proof

**Exhaustive reduction to bipartite incidence matrices.** A connected bipartite graph on \(n\ge2\) vertices has a proper two-coloring, unique up to interchanging colors. Write its two nonempty shore sizes as \(a\le b\), \(a+b=n\). Naming the shores, every such graph is encoded by a binary \(a\times b\) matrix \(A\), with \(A_{ij}=1\) exactly when its corresponding cross-edge exists. Conversely each matrix gives a simple bipartite graph, connected precisely when the resulting graph is connected. It follows that enumerating *every* integer mask in \(0\le m<2^{ab}\), separately for every \(1\le a\le\lfloor n/2\rfloor\), and discarding disconnected graphs, is exhaustive. Shore swaps and isomorphism repetitions do not affect maximality or completeness.

**Exact shortest-path recurrence.** For every source vertex \(s\), breadth-first search assigns distances \(d_s(v)\) and computes path counts using
\[
\sigma_s(s)=1,\qquad
\sigma_s(v)=\sum_{\substack{u\sim v\\d_s(u)=d_s(v)-1}}\sigma_s(u)
\quad (v\ne s).
\]
Induction on the integer BFS distance proves that \(\sigma_s(v)\) is exactly the number of shortest \(s\)-to-\(v\) paths: the penultimate vertex of each such path is a uniquely determined predecessor in the preceding BFS layer. Summing \(\sigma_s(v)\) only for vertex indices \(s<v\), then adding \(n\), counts every unoriented geodesic exactly once, including zero-length paths exactly once. Thus integer calculations in the exhaustive loops constitute a finite proof, not a sampling inference.

**Independently replayed enumeration.** The primary program `artifacts/census_bfs.cpp` enumerates every incidence mask and performs BFS with path counts. The independent program `artifacts/census_floyd.cpp` builds the distance matrix with Floyd--Warshall and counts geodesics by dynamic programming over the distance layers. All candidate matrices are processed by both programs. The following table reports, for each order and shore size, the maximum geodesic count over connected graphs; the two methods agree throughout.

| \(n\) | Shore profiles and corresponding maxima |
|---|---|
| \(7\) | \((1,6):28\); \((2,5):42\); \((3,4):49\). |
| \(8\) | \((1,7):36\); \((2,6):56\); \((3,5):69\); \((4,4):74\). |
| \(9\) | \((1,8):45\); \((2,7):72\); \((3,6):92\); \((4,5):105\). |

For additional boundary checks, the programs recover maximum values \(20\) and \(33\) for orders \(5\) and \(6\), with unique equality graphs \(K_{2,3}\) and \(K_{3,3}\). The nine-vertex enumeration includes all \(2^{20}=1,048,576\) incidence matrices for shores \((4,5)\), and in particular does **not** restrict to deletion patterns in advance.

**Complete equality classification.** The second program records the number of missing edges and the sorted missing-edge degrees on each shore of every maximizing matrix. Its complete output is reproduced in `artifacts/floyd_output.txt`. The only equality profiles are:

| \(n\) and shores | Missing edges | Missing-degree sequences on the two shores | Number of matrices |
|---|---:|---|---:|
| \(7:(3,4)\) | \(0\) | \((0,0,0):(0,0,0,0)\) | \(1\) |
| \(7:(3,4)\) | \(1\) | \((0,0,1):(0,0,0,1)\) | \(12\) |
| \(8:(4,4)\) | \(1\) | \((0,0,0,1):(0,0,0,1)\) | \(16\) |
| \(8:(4,4)\) | \(2\) | \((0,0,1,1):(0,0,1,1)\) | \(72\) |
| \(9:(4,5)\) | \(2\) | \((0,0,1,1):(0,0,0,1,1)\) | \(120\) |
| \(9:(4,5)\) | \(3\) | \((0,1,1,1):(0,0,1,1,1)\) | \(240\) |
| \(9:(4,5)\) | \(4\) | \((1,1,1,1):(0,0,0,2,2)\) | \(60\) |

A profile with degrees all \(0\) and \(1\) is precisely a deleted matching. The final profile forces two distinct vertices in the five-vertex shore to be incident with two deleted edges each, and each of the four vertices in the opposite shore to be incident with one. Therefore the four deleted edges are **exactly two vertex-disjoint two-edge stars**. This exhausts all possible isomorphism types of maximum graphs. The third program, `artifacts/check_nine_profiles.cpp`, independently reproduces the three nine-vertex profiles using the BFS counter.

**Explicit value of the exceptional graph.** In the two-star deletion graph on shores \((4,5)\), there are \(9\) zero-length paths and \(16\) edges. Shortest paths between two vertices of the four-vertex shore contribute \(20\), between two vertices of the five-vertex shore contribute \(36\), and between endpoints of the \(4\) deleted cross edges contribute \(24\). Hence
\[
\operatorname{gpn}(G)=9+16+20+36+24=105.
\]
The two star centers have disjoint neighborhoods and are at distance four via any of the other three vertices of their shore. Precisely \(12\) four-edge geodesics connect the two centers (choose one of two neighbors at each center and one of three intermediate vertices). This explains both the graph's diameter and why its global optimum is invisible to a search restricted to matching deletions.

## Verification

The six files in `artifacts/` comprise three complete C++17 sources and their corresponding reference outputs. With a C++17 compiler, compile and run each source without arguments; compare standard output exactly to its included output file. Both general programs enumerate orders \(5\) through \(9\) and exhaustively treat every shore split, all \(2^{ab}\) masks, connectivity and shortest-path multiplicities. A third program independently classifies all \(105\)-geodesic graphs with shore sizes \((4,5)\). There are no external datasets, solvers, timeouts, or heuristic filters; every possible mask is visited. This is a **finite exhaustive certificate** and has no implication that any assertion is proved for arbitrarily large \(n\).

## Relationship to prior work

Knor, Sedlar, Škrekovski, and Zhang introduced this invariant and explicitly posed their Problem 15, the classification of bipartite graphs that maximize it at fixed order; their April 2026 paper gives general bounds and several families but does not determine the exhaustive global small-order equality types established here. A published diameter-two extremal theorem identifies balanced complete bipartite graphs as optimal among graphs of diameter two, but cannot control our diameter-three and diameter-four maximizers. A different published construction of path blow-ups improves large-order lower bounds and does not give complete unrestricted bipartite classification at orders seven, eight, or nine. Exact formulas for the matching-deletion *subfamily*, even when available, do not imply a global bound over all incidence matrices and cannot detect the diameter-four two-star coextremizer. The present finding claims the global finite classification, not an original general matching-deletion formula.

## Limitations

The theorem is exactly for orders seven through nine and connected simple bipartite graphs. It does not classify maximizers for order ten or above, or over nonbipartite graphs. The correctness certificate is exhaustive over the stated finite orders; it is not an asymptotic proof. The three verification sources share standard combinatorial definitions but use distinct shortest-path counting algorithms. Similar unindexed or unpublished enumerations remain an originality risk.

## References

1. M. Knor, J. Sedlar, R. Škrekovski, and X.-D. Zhang, *Counting Geodesic Paths in Graphs*, arXiv:2604.04907v1, first publicly posted April 6, 2026; https://arxiv.org/html/2604.04907v1; DOI:10.1007/s00009-026-03159-3. In particular, Section 4, Problem 15.
2. *Balanced complete bipartite graphs uniquely maximize geodesic subpaths at diameter two*, 2026 public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-diameter-two-geodesic-subpath-extremum--d8fd04cc9d21.
3. *Boundary-tapered path blow-ups improve the geodesic-subpath lower bound*, 2026 public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-boundary-tapered-geodesic-path-blowups--26120b82068c.
