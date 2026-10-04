# Dominant edge metric bases of lollipop graphs
## Finding
For integers \(m\ge3\) and \(\ell\ge2\), let \(L_{m,\ell}\) be the lollipop graph obtained from \(K_m\) and \(P_\ell=p_1\cdots p_\ell\) by adding the bridge \(cp_1\), where \(c\in V(K_m)\). Every vertex cover of \(L_{m,\ell}\) is an edge metric generator. Consequently the dominant edge metric dimension equals the vertex-cover number, \[\operatorname{Ddim}_e(L_{m,\ell})=m-1+\left\lfloor\frac{\ell}{2}\right\rfloor.\] Moreover, the dominant edge metric bases are exactly the minimum vertex covers. If \(\ell=2r+1\), their number is \(m-1\); if \(\ell=2r\), their number is \((m-1)(r+1)+1\).

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. For integers \(m\ge3\) and \(\ell\ge2\), the lollipop graph \(L_{m,\ell}\) is formed from a clique \(K_m\) with distinguished attachment vertex \(c\), a path
\[
P_\ell=p_1p_2\cdots p_\ell,
\]
and the bridge \(cp_1\).

For a vertex \(s\) and an edge \(xy\), write
\[
d(s,xy)=\min\{d(s,x),d(s,y)\}.
\]
A set \(S\) is an edge metric generator if all edges have pairwise distinct vectors of distances to \(S\). A dominant edge metric generator is simultaneously an edge metric generator and a vertex cover.

## Proof
Let \(S\) be an arbitrary vertex cover and put \(T=V(L_{m,\ell})\setminus S\). Then \(T\) is independent.

For an edge \(e\), the coordinates of its edge-distance vector that are zero are exactly the selected endpoints:
\[
\{s\in S:d(s,e)=0\}=e\cap S.
\]
Hence two edges with different intersections with \(S\) are already distinguished. Suppose two distinct edges \(e,f\) have the same intersection with \(S\). Since \(S\) covers every edge, that common intersection must be a singleton \(\{s\}\), and
\[
e=sx,\qquad f=sy
\]
for distinct \(x,y\in T\).

If \(s\) is a nonattachment clique vertex, then it has at most one neighbor in \(T\): the clique contributes at most one unselected vertex, and such a vertex has no path neighbors. Thus this case cannot occur.

If \(s=c\), the only way to have two neighbors of \(c\) in \(T\) is to have one omitted nonattachment clique vertex and \(p_1\) both outside \(S\). Because \(T\) is independent and \(\ell\ge2\), one then has \(p_2\in S\). If \(u\) is the omitted clique vertex, then
\[
d(p_2,cu)=2,\qquad d(p_2,cp_1)=1,
\]
so the two edges are distinguished.

Finally suppose \(s=p_i\). If both path neighbors of \(p_i\) lie in \(T\), choose a selected nonattachment clique vertex \(z\). Such a \(z\) always exists because \(m\ge3\) and at most one clique vertex lies in \(T\). For \(i\ge2\),
\[
d(z,p_{i-1}p_i)=i,\qquad d(z,p_ip_{i+1})=i+1.
\]
For \(i=1\), the analogous possible pair is \(cp_1\) and \(p_1p_2\), and
\[
d(z,cp_1)=1,\qquad d(z,p_1p_2)=2.
\]
Thus no two distinct edges have the same edge-distance representation. Every vertex cover is therefore a dominant edge metric generator.

It remains to compute the minimum vertex covers. If \(c\in S\), then a minimum cover contains exactly \(m-2\) of the other clique vertices and a minimum vertex cover of \(P_\ell\). Its size is
\[
(m-1)+\left\lfloor\frac{\ell}{2}\right\rfloor.
\]
If \(c\notin S\), all other clique vertices and \(p_1\) are forced, after which the residual path \(p_2\cdots p_\ell\) requires \(\lfloor(\ell-1)/2\rfloor\) further vertices. This gives
\[
m+\left\lfloor\frac{\ell-1}{2}\right\rfloor.
\]
The two values coincide exactly when \(\ell\) is even; for odd \(\ell\) the first is smaller. Therefore
\[
\operatorname{Ddim}_e(L_{m,\ell})
=
m-1+\left\lfloor\frac{\ell}{2}\right\rfloor.
\]

For \(\ell=2r+1\), the path \(P_{2r+1}\) has the unique minimum vertex cover
\[
\{p_2,p_4,\ldots,p_{2r}\}.
\]
The attachment vertex \(c\) must be selected and exactly one of the other \(m-1\) clique vertices is omitted, yielding \(m-1\) bases.

For \(\ell=2r\), the path \(P_{2r}\) has exactly \(r+1\) minimum vertex covers. With \(c\) selected, each may be combined with any choice of one omitted nonattachment clique vertex, giving \((m-1)(r+1)\) bases. There is one additional minimum cover with \(c\) omitted: all other clique vertices are selected together with
\[
\{p_1,p_3,\ldots,p_{2r-1}\}.
\]
Hence the total number of bases is
\[
(m-1)(r+1)+1.
\]

## Verification
The included checker constructs every \(L_{m,\ell}\) for \(3\le m\le7\) and \(2\le\ell\le9\). It computes all-pairs distances, enumerates every vertex subset, tests the vertex-cover condition, and independently checks edge-distance representations.

It verifies directly that every vertex cover edge-resolves, and then checks the stated dimension, parity-dependent basis counts, and structural descriptions of all minimum bases.

## Relationship to prior work
The 2023 paper introducing dominant edge metric dimension defines the parameter as the minimum size of a set that is both a vertex cover and an edge metric generator. Its primary full text gives exact values for complete graphs, complete bipartite graphs, cycles, paths, and wheels, and gives formulas for corona, iterated corona, edge-corona, and join products. It does not state a lollipop, kite, or clique-path coalescence formula in the inspected text.

Lollipop graphs themselves have been studied for other distance parameters. A 2017 paper determines their local metric dimension as \(m-1\), and another 2017 paper determines their strong metric dimension as \(m-1\). Those scalar vertex-resolving results do not imply the dominant edge metric statement here: the latter requires a vertex cover, distinguishes edges rather than vertices, and its value depends on the path length.

## Limitations
The result is for the standard lollipop \(K_m\) joined by one bridge to \(P_\ell\), with \(m\ge3\) and \(\ell\ge2\). The proof does not assert that every vertex cover edge-resolves in arbitrary block graphs or arbitrary clique-path coalescences. The finite computation is corroborative only; the all-parameter theorem follows from the proof. A differently named or non-indexed treatment of the same family may exist.

## References
1. M. Tavakoli, M. Korivand, A. Erfanian, G. Abrishami, E. T. Baskoro, “The dominant edge metric dimension of graphs,” Electronic Journal of Graph Theory and Applications 11(1) (2023), 197–208, DOI 10.5614/ejgta.2023.11.1.16.
2. A. N. Cahyabudi, T. A. Kusmayadi, “On the local metric dimension of a lollipop graph, a web graph, and a friendship graph,” Journal of Physics: Conference Series 909 (2017), 012039, DOI 10.1088/1742-6596/909/1/012039.
3. T. A. Putri, T. A. Kusmayadi, “On The Strong Metric Dimension of Lollipop Graph and Generalized Web Graph,” Proceeding ICMETA 1(1) (2017).
