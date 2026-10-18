# Perfect edge domination of bicliques with a deleted matching: a one-edge instability

## Finding
For integers \(3\le m\le n\) and \(0\le t\le m\), let \(A=\{a_1,\ldots,a_m\}\), \(B=\{b_1,\ldots,b_n\}\), and define \(G_{m,n,t}\) by deleting the edges \(a_i b_i\), \(1\le i\le t\), from the complete bipartite graph. Let \(\mathcal P(G;z)=\sum_{F}z^{|F|}\), summing over all perfect edge dominating sets \(F\subseteq E(G)\). Then
\[
\mathcal P(G_{m,n,t};z)=(n-t)z^m+(m-t)z^n+z^{mn-t}
\]
except for \((m,n,t)=(3,3,3)\), where
\[
\mathcal P(G_{3,3,3};z)=3z^2+6z^4+z^6.
\]
In the nonexceptional case, the sets are precisely the full edge set and the full stars centered at the \(m+n-2t\) vertices not incident with the deleted matching.

In particular, for every \(n\ge4\), the graph \(G_{n,n,n-1}\) has exactly two minimum perfect edge dominating sets, each with \(n\) edges, whereas its one-edge deletion \(G_{n,n,n}\) has exactly one perfect edge dominating set, namely all its \(n(n-1)\) edges. The minimum jumps by the factor \(n-1\).

## Assumptions and scope
All graphs are finite, simple and undirected. A chosen edge dominates itself and each other edge with a common endpoint. A **perfect edge dominating set** \(F\) is a set of chosen edges such that **every edge outside \(F\)** is dominated by exactly one chosen edge. Chosen edges may be dominated multiply. All edges, vertices, stars and choices here are labelled. The range \(m\ge3\) is essential; no claim is made for smaller first part sizes or arbitrary edge-deletion patterns.

## Proof
Let \(F\) be a perfect edge dominating set, and put \(d_F(v)=|\{e\in F:v\in e\}|\). For every edge \(uv\notin F\), perfect domination says
\[
d_F(u)+d_F(v)=1. \tag{1}
\]
Let \(U=\{v:d_F(v)=0\}\). Equation (1) implies that \(U\) is independent (an edge with two endpoints in \(U\) violates it) and that every graph edge with both endpoints outside \(U\) belongs to \(F\). Every edge meeting \(U\) is unchosen. Hence
\[
F=E\bigl(G[V(G)\setminus U]\bigr),
\]
and (1) is equivalent to requiring that every neighbor of every vertex of \(U\) have \(F\)-degree exactly one. If \(U=\varnothing\), the only possibility is \(F=E(G)\), always valid.

Since the only cross-part nonedges of \(G\) are distinct matched pairs, every nonempty independent \(U\) is either contained entirely in \(A\), contained entirely in \(B\), or equals one deleted pair \(\{a_i,b_i\}\) with \(i\le t\).

First suppose \(U\subseteq A\). It cannot be all of \(A\), since \(G\) has edges and the degree-one requirement would fail. Write \(r=m-|U|\ge1\). If \(|U|\ge2\), choose distinct \(a_i,a_j\in U\). Because \(i\ne j\), the edge \(a_i b_j\) is present. Every one of the \(r\) selected vertices of \(A\) is also adjacent to \(b_j\): the only edge that might have been deleted at \(b_j\) is \(a_jb_j\), but \(a_j\) is white. Therefore \(d_F(b_j)=r\). As \(b_j\) neighbors the white vertex \(a_i\), the degree-one condition forces \(r=1\). Its single selected vertex \(a_k\) must be unmatched: if \(k\le t\), then \(b_k\) is adjacent to the other white vertices in \(A\) and has \(F\)-degree zero. Conversely, a full star at an unmatched \(a_k\) satisfies (1).

If \(U=\{a_i\}\) is a singleton, then \(r=m-1\). Every neighbor \(b_j\) of \(a_i\) has \(F\)-degree either \(m-1\) or \(m-2\). The degree-one requirement forces \(m=3\), all such neighbors to be matched to selected vertices of \(A\), and no unmatched \(b_j\). This entails \(n=t=m=3\). In that case \(U=\{a_i\}\) indeed produces a four-edge set. Exchanging \(A\) and \(B\) proves the symmetric classification for \(U\subseteq B\), including the three further four-edge sets in the exceptional case.

Finally, suppose \(U=\{a_i,b_i\}\) for \(i\le t\). For each \(j\ne i\), the vertex \(b_j\) is adjacent to the white vertex \(a_i\), and its \(F\)-degree is at least \(m-2\); similarly the neighbors of \(b_i\) have degree at least \(n-2\). The degree-one condition forces \(m=n=3\), and then every remaining vertex must have its deleted matching partner in the other part, forcing \(t=3\). For each of three matched pairs, deleting those two vertices from the induced selected subgraph leaves two chosen edges. All these cases satisfy the condition. Together with the full six-edge set and the six four-edge cases, this gives \(3z^2+6z^4+z^6\).

Thus all cases are exhausted. In the ordinary case, there are \(m-t\) unmatched centers in \(A\), each making a star of \(n\) edges, and \(n-t\) unmatched centers in \(B\), each making a star of \(m\) edges, plus the full edge set of \(mn-t\) edges. The polynomial follows. On a balanced \(n\)-by-\(n\) board with \(n\ge4\), the counts at \(t=n-1\) and \(t=n\) are \(2z^n+z^{n^2-n+1}\) and \(z^{n(n-1)}\), respectively. The claimed instability follows.

## Verification
The accompanying Python script `verify_ped.py` independently enumerates all labelled edge-subsets of 24 matched-deletion bicliques (1,147,328 candidate edge-subsets) and applies equation (1) directly. It separately enumerates independent white-vertex candidates for 197 further parameter triples and checks the predicted polynomial. Every comparison passed. It also verifies the one-edge deletion formula numerically for all \(4\le n\le44\). The printed output is reproduced in `verify_stdout.txt`. The infinite theorem is proved above, not inferred from finite experiments.

## Relationship to prior work
Grippo, Lin and Vera [1] establish the general perfect-edge-domination framework and give an algorithm to count all perfect edge dominating sets on \(P_6\)-free graphs. Their general counting algorithm is not claimed as new here. Grippo, Lin, Moyano and Vera [2] study extremal counts in trees, forests and chordal graphs and give counting algorithms on generalized series-parallel and chordal graphs. Those graph-class theorems do not cover the nonchordal dense bipartite family here (aside from small exceptions). The present claim is a **closed cardinality polynomial with an exact matching-deletion phase transition**, not a claim of improved counting complexity. Previous research on ordinary edge domination and efficient induced-matchings uses different domination constraints. Prior published classification of all matched-deletion biclique perfect-edge-dominating sets has not been established in the sources inspected; final bibliographic priority remains uncertain.

## Limitations
The first part size is at least three and the deleted edges form a matching. The exceptional six-cycle is isolated explicitly. Source [2]'s full primary text was inaccessible during the literature comparison; its abstract, bibliographic record and a secondary technical review were checked, creating a residual novelty risk. No independent mathematical audit has been performed.

## References
[1] L. N. Grippo, M. C. Lin and C. Vera, *Perfect Edge Domination in P6-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598, first posted 2025-09-04, version 2 posted 2026-03-05. https://arxiv.org/abs/2509.04598

[2] L. N. Grippo, M. C. Lin, V. Moyano and C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894, first posted 2026-07-04. https://arxiv.org/abs/2607.03894
