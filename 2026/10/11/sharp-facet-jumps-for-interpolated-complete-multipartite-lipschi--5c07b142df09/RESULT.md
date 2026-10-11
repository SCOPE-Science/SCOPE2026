# Sharp facet jumps for interpolated complete-multipartite Lipschitz-free balls

## Finding

Let \(k\ge3\), and let \(M=A_1\sqcup\cdots\sqcup A_k\) have \(|A_i|=m_i\ge1\). For \(1\le t\le2\) define the metric
\[
d_t(x,y)=\begin{cases}
0,&x=y,\\
t,&x\ne y\text{ and }x,y\in A_i\text{ for some }i,\\
1,&x\in A_i,\ y\in A_j,\ i\ne j.
\end{cases}
\]
Write \(N=\sum_i m_i\). The number of facets of the unit ball of the real Lipschitz-free space \(\mathcal F(M,d_t)\) is
\[
F(t)=\begin{cases}
2^N-2,&t=1,\\
2^N-2+\displaystyle\sum_{i=1}^{k}(2^{m_i}-2)(2^{N-m_i}-2),&1<t<2,\\
2^N-2-\displaystyle\sum_{i=1}^{k}(2^{m_i}-2),&t=2.
\end{cases}
\]
The newly established part is the interior formula and its exhaustive potential classification. The endpoint \(t=1\) is equilateral; the endpoint \(t=2\) is the previously solved complete-multipartite symmetric edge polytope. If some part has size at least two, the facet count rises strictly when entering \(1<t<2\) and drops at \(t=2\). For \((m_1,m_2,m_3)=(2,2,2)\), the respective counts are \(62\), \(146\), and \(56\).

## Assumptions and scope

All spaces and duality pairings are real. Each \(m_i\) is a positive integer, each of the \(k\ge3\) parts is nonempty, and \(1\le t\le2\). The triangle inequality follows from \(t\le2\); all distinct distances are positive. Fix any basepoint \(o\in M\). The Lipschitz dual ball is the full-dimensional polytope
\[
P_t=\{f:M\to\mathbb R:f(o)=0,\ |f(x)-f(y)|\le d_t(x,y)\text{ for all }x,y\in M\}.
\]
Its vertices correspond to the facets of the Lipschitz-free unit ball by polar duality in dimension \(N-1\). Potentials differing by an additive constant represent the same dual functional.

## Proof

**Tight-graph criterion.** Given \(f\in P_t\), join distinct vertices \(x,y\in M\) whenever \(|f(x)-f(y)|=d_t(x,y)\). Call the resulting graph \(H_f\). The row of the corresponding active linear constraint is, up to sign, the incidence vector of \(xy\). Incidence rows on \(N\) vertices span a space of rank \(N-c(H_f)\), where \(c(H_f)\) is the number of connected components. After fixing \(f(o)=0\), a feasible point is a vertex exactly when the active rows have rank \(N-1\). Consequently,
\[
f\in\operatorname{vert}(P_t)\quad\Longleftrightarrow\quad H_f\text{ is connected}.
\]
This criterion also verifies the strict endpoint cases: connectivity, rather than mere feasibility, controls extremality.

**Interior, type I: no tight pair inside a part.** Assume \(1<t<2\). If \(H_f\) is connected and has only cross-part edges, every tight edge has difference \(1\), so all potential values are integers after adding a common constant. Every pair of points has distance at most \(t<2\); hence the integer range is at most \(1\). Nonconstancy then forces, after subtracting the minimum, \(f(M)=\{0,1\}\). Conversely, for any binary potential the tight edges are precisely cross-part pairs of opposite values.

We claim that for \(k\ge3\), this binary tight graph is disconnected exactly when some part \(A_i\) is mixed (it contains both values) and every vertex outside \(A_i\) has one and the same value. To see necessity, if a vertex is isolated, all other parts have its value, and nonconstancy forces its own part to be mixed. If the tight graph has no isolated vertex, it is connected: two hypothetical nontrivial components each contain an edge between a zero and a one. Choose one tight edge between a zero in part \(A_i\) and a one in a distinct part \(A_j\) in the first component. If a second nontrivial component existed, each of its one-valued vertices would have to belong to \(A_i\), or it would connect to that zero; and each of its zero-valued vertices would have to belong to \(A_j\), or it would connect to that one. Choose a vertex in a third nonempty part. If its value is zero it connects to a one in each component; if its value is one it connects to a zero in each component. Either way, both components are joined, a contradiction. The stated mixed-part patterns plainly have isolated vertices. There are precisely \(2(2^{m_i}-2)\) excluded oriented patterns for each \(i\), and these are disjoint for distinct parts. The number of type-I vertices is therefore
\[
C_{\mathrm I}=2^N-2-2\sum_i(2^{m_i}-2).
\]

**Interior, type II: at least one tight pair inside a part.** Let \(x,y\in A_i\) satisfy \(f(y)-f(x)=t\). Translate so \(f(x)=0\) and \(f(y)=t\). Every \(z\notin A_i\) obeys \(|f(z)|\le1\) and \(|f(z)-t|\le1\), hence
\[
t-1\le f(z)\le1.
\]
This interval has width \(2-t<1\), so no tight edge joins two vertices outside \(A_i\), even when they are in different parts. No other part can contain a tight same-part pair. Because \(H_f\) is connected, each outside vertex must have a tight edge into \(A_i\) and therefore takes value \(1\) or \(t-1\). Similarly, every vertex of \(A_i\) must take an endpoint value \(0\) or \(t\): a vertex with an intermediate value would have neither a same-part tight edge of length \(t\) nor a cross tight edge to one of the two possible outside values. Both endpoint values must appear in \(A_i\). Conversely, every such assignment has a connected tight graph: the two endpoint classes of \(A_i\) are joined by all their tight within-part pairs, and each outside vertex is joined to the opposite-distance endpoint. Thus type-II vertices are in one-to-one correspondence with choices of a unique mixed part \(i\), its nonconstant binary assignment \(\{0,t\}\), and an independent choice of \(\{t-1,1\}\) at each outside vertex. Their total is
\[
C_{\mathrm{II}}=\sum_{i=1}^{k}(2^{m_i}-2)2^{N-m_i}.
\]
The chosen part is unique because any other within-part tight pair is excluded. Type I and II are disjoint. Adding their counts yields
\[
F(t)=2^N-2+\sum_{i=1}^{k}(2^{m_i}-2)(2^{N-m_i}-2),\qquad1<t<2.
\]

**Endpoints.** At \(t=1\), all nonzero distances are one. A connected tight graph forces a nonconstant binary potential, and every nonconstant binary potential has a complete bipartite connected tight graph; hence \(F(1)=2^N-2\). At \(t=2\), the graph shortest-path metric of the complete multipartite graph, the endpoint formula in the statement follows from Proposition 3.5 of Higashitani–Jochemko–Michałek (2018), independently of the interior argument. The same tight-graph argument also recovers it: the binary potentials contribute \(2^N-2-2\sum_i(2^{m_i}-2)\), while potentials with an attained within-part difference \(2\) force all outside values to the midpoint and contribute \(\sum_i(2^{m_i}-2)\).

Finally, for \(k\ge3\), each \(N-m_i\ge2\). Consequently each nonzero summand \((2^{m_i}-2)(2^{N-m_i}-2)\) is positive. The strict changes at the endpoints follow if any \(m_i\ge2\); if all parts are singletons, every metric is simply equilateral, and the count is constant.

## Verification

The accompanying `check_facets.py` is a standard-library exact-arithmetic enumerator. It fixes a basepoint and tests every half-integer potential within distance two of it, accepting a potential precisely when its tight graph is connected. For \(t\in\{1,3/2,2\}\), spanning-tree tightness proves that this finite grid contains every possible vertex. The program agrees with the formula for each of the profiles \((2,1,1)\), \((2,2,1)\), \((2,2,2)\), and \((3,1,1)\), a total of twelve exact finite cases; its output ends `EXACT_SMALL_CASES_PASS: 12`.

The analytic tight-graph classification proves the formula for all part sizes and all real \(t\) in the stated intervals. The finite enumeration is an independent small-case check, not an extrapolated proof for arbitrary sizes.

## Relationship to prior work

Higashitani, Jochemko and Michałek (2018), Theorem 3.1 and Proposition 3.5, characterize facet-defining potentials for the symmetric edge polytope of a complete multipartite graph and establish exactly the \(t=2\) count given above. Mori, Mori and Ohsugi (2023 preprint; subsequent revision), Introduction, explicitly reproduce this known endpoint formula and study facets of join-graph symmetric edge polytopes. Neither graph setting varies positive intra-part distances over the strict interval \(1<t<2\). Cobollo, Guirao and Montesinos (2023) motivate metric-sensitive finite-dimensional geometry in Lipschitz-free spaces, but focus on numerical indices of three-point spaces rather than these higher-dimensional facet counts.

The two-part interpolation is a different, earlier studied case: its connected binary tight graphs are governed by a distinct combinatorial rule. The new theorem concerns every number of nonempty parts at least three and includes the new count contributed by mixed parts in the strict interior. The standard tight-edge rank criterion is not claimed as new.

## Limitations

No claim of novelty is made for either endpoint formula or for the general rank criterion. The theorem is restricted to real Lipschitz-free spaces, all cross-part distances equal to \(1\), and all distinct intra-part distances sharing one parameter \(t\). It does not classify arbitrary independently weighted multipartite metrics or higher-dimensional face vectors. Equivalent statements in less readily indexed weighted metric-polytope literature are a residual bibliographic risk. Independent mathematical validation has not been performed.

## References

1. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, 20 July 2018. Section 3.1, particularly Theorem 3.1 and Proposition 3.5. https://arxiv.org/abs/1807.07678
2. Ch. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1, 25 April 2023. https://arxiv.org/abs/2304.13183
3. A. Mori, K. Mori and H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287v1, 18 December 2023. Introduction and the known complete-multipartite endpoint expression; a later revised version is available. https://arxiv.org/abs/2312.11287
