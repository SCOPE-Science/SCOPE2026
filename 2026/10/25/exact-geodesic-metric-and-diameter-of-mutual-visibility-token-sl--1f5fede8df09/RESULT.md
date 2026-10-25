# Exact geodesic metric and diameter of mutual-visibility token-slide layers in complete bipartite graphs

## Finding

Let \(G=K_{m,n}\), \(m,n\ge3\), have partite classes \(A,B\) with \(|A|=m\), \(|B|=n\). A vertex subset is **mutually visible** when every two of its vertices have a shortest connecting path whose internal vertices lie outside the subset. The vertices of the size-\(k\) **token-slide reconfiguration layer** \(R_k(G)\) are the mutually visible \(k\)-subsets; an edge moves one selected vertex to an unselected adjacent vertex while preserving mutual visibility.

**Exact all-pairs metric.** For all \(S,T\in V(R_k(G))\) and every \(0\le k\le m+n-3\),
\[
d_{R_k(G)}(S,T)=\max\big\{|(S\triangle T)\cap A|,\ |(S\triangle T)\cap B|\big\}.
\]
The same formula holds for \(k=m+n-2\) whenever \(\min\{m,n\}=3\). In every stated case, \(R_k(G)\) is an isometric induced subgraph of the ordinary size-\(k\) token graph of \(G\).

**Sharp diameters.** Write \(N=m+n\) and \(P=\max\{m,n\}\). Then
\[
\operatorname{diam}(R_k(G))=\min\{2k,\ 2(N-k-1),\ P\},\qquad 0\le k\le N-3.
\]
If \(\min\{m,n\}=3\), then \(\operatorname{diam}(R_{N-2}(G))=3\). If \(m,n\ge4\), the top layer consists of \(mn\) isolated configurations; this disconnected boundary was previously established and is not part of the metric formula.

## Assumptions and scope

All graphs are finite, simple, undirected and vertex-labelled. A token slide changes a selected vertex into one unselected neighbor. Only mutually visible intermediate configurations are allowed. Set distance is the shortest number of slides, and the diameter is taken only for the connected layers specified above. The zero-token layer consists of one state and has diameter zero.

Write \(a=|S\cap A|\), \(b=k-a\). Mutual visibility is equivalent to
\[
(a\le1\ \mathrm{or}\ b<n)\qquad\mathrm{and}\qquad(b\le1\ \mathrm{or}\ a<m).
\]
Indeed, two selected vertices on one side require an unselected common neighbor on the opposite side for a selected-avoiding length-two geodesic; cross-side pairs are adjacent. Consequently, at each fixed \(k\) the feasible values of \(a\) form an integer interval \(I_k\): from \([\max\{0,k-n\},\min\{m,k\}]\), remove a lower endpoint if it has \(b=n,a\ge2\), and remove an upper endpoint if it has \(a=m,b\ge2\). For \(1\le k\le N-3\) this interval has at least two elements: for \(k\le2\), both levels zero and one are feasible; for larger \(k\), the initial interval has at least four elements and at most its two endpoints are excluded. At \(k=N-2\), \(I_k\) has multiple levels exactly when the smaller side has size three.

## Proof

**1. Exact lower bound.** Let
\[
u=|(S\setminus T)\cap A|,\quad v=|(S\setminus T)\cap B|,\quad w=|(T\setminus S)\cap A|,\quad x=|(T\setminus S)\cap B|.
\]
Since \(|S|=|T|\), \(u+v=w+x\). Every slide toggles selection at exactly one vertex of each part, so any walk from \(S\) to \(T\) has length at least
\[
L=\max\{u+w,v+x\}=\max\{|(S\triangle T)\cap A|,|(S\triangle T)\cap B|\}.
\]

**2. Direct correction moves.** Execute \(\alpha=\min\{u,x\}\) slides from erroneous selected vertices of \(A\) to needed target vertices in \(B\), and \(\beta=\min\{v,w\}\) slides in the reverse direction. No endpoint is used twice. All cross-part slides exist because \(G\) is complete bipartite. Each such slide changes the level \(a\) by one. The starting and ending levels belong to the integer interval \(I_k\), so order the \(\alpha\) negative and \(\beta\) positive steps to stay within \(I_k\): when at its lower endpoint, take an available positive step; when at its upper endpoint, take an available negative step; elsewhere either step may be taken. If the only remaining step were outward at an endpoint, the prescribed endpoint would lie outside \(I_k\), a contradiction. Feasibility depends only on type, hence every intermediate state is valid.

**3. Two-slide same-side relays.** After these moves, all remaining mismatches are confined to a single part. Explicitly, the identity \(u-x=w-v\) shows that if \(u\ge x\), the residual demands comprise exactly \(r=u-x=w-v\) within-\(A\) exchanges; if \(u<x\), there are exactly \(r=x-u=v-w\) within-\(B\) exchanges. The current level is the target level, and every level of \(I_k\) has a neighboring feasible level.

For a residual \(A\)-exchange replacing selected \(p\in A\setminus T\) with unselected \(q\in T\cap A\): if the lower level is feasible, choose an empty \(z\in B\) and slide \(p\to z\to q\). If only the upper level is feasible, choose a selected \(z\in B\) and slide \(z\to q\), then \(p\to z\). The neighboring-level condition ensures the required intermediate empty or selected \(B\) vertex exists. For a residual \(B\)-exchange apply the symmetric construction. Each exchange takes exactly two valid slides, and leaves all previously corrected targets fixed.

The length of the resulting path is \(\alpha+\beta+2r=L\) by the two cases above. Hence the lower bound is attained. The same toggling argument lower-bounds distances in the unrestricted token graph, while our path is present there; therefore every connected visibility layer is isometric.

**4. Diameter upper bound.** Each symmetric difference within a part contains at most \(2k\) vertices and no more than that part's order, giving \(d\le\min\{2k,P\}\). Put \(t=N-k\), and assume \(k\le N-3\), so \(t\ge3\). Fix a part \(A\) of order \(m\). If both configurations omit at least one vertex of \(B\), then each omits at most \(t-1\) vertices of \(A\), giving \(|(S\triangle T)\cap A|\le2(t-1)\). If one contains all of \(B\), mutual visibility forces it to select at most one vertex of \(A\); hence \(t\ge m-1\). For \(m\ge4\), \(2(t-1)\ge2(m-2)\ge m\); for \(m=3\), \(t\ge3\) gives \(2(t-1)\ge4\ge m\). Either way \(|(S\triangle T)\cap A|\le2(t-1)\). The argument for \(B\) is symmetric. Thus \(d\le D:=\min\{2k,2(t-1),P\}\).

**5. Sharpness of the upper bound.** Relabel parts so \(n=P\ge m\); all witnesses below differ maximally on \(B\). If \(D=2k\), then \(n\ge2k\): select two disjoint \(k\)-subsets of \(B\), giving distance \(2k\). Otherwise, if \(D=2(t-1)\), then \(n\ge2(t-1)\): choose the same \((m-1)\)-subset of \(A\) in both configurations and disjoint omitted \((t-1)\)-subsets of \(B\), giving distance \(2(t-1)\). Both states are feasible because they leave at least one vertex unselected on each side. Finally, if \(D=n\), write \(n=2h\) or \(n=2h+1\). Partition \(B\) into two disjoint subsets of sizes \((h,h)\) or \((h,h+1)\), and make these the selected \(B\)-parts of the two configurations. The inequalities \(n\le2k\) and \(n\le2(t-1)\) ensure that the complementary selected \(A\)-part sizes needed to reach \(k\) both lie in \([0,m-1]\): for even \(n\), \(h\le k\le m+h-1\); for odd \(n\), \(h+1\le k\le m+h-1\). Both configurations are feasible, and their distance is \(n\). Equality cases in which several terms define \(D\) can use any corresponding construction.

**6. Connected maximum layer.** If \(\min\{m,n\}=3\) and \(k=N-2\), all feasible states have at most three mismatches on each side, hence distance at most three. With \(|A|=3\), take one configuration of type \((1,n)\) and one of type \((2,n-1)\) whose selected \(A\)-parts are disjoint. Their \(A\)-symmetric difference has size three, attaining the bound. This also covers \(m=n=3\).

## Verification

The standalone `verifier.py` directly constructs the token-slide layer using the **original pairwise geodesic definition** of mutual visibility; exhaustive breadth-first searches verify every connected-state distance against the formula and the stated diameters for tested small hosts. It separately enumerates all feasible pairs of occupancy types and intersection sizes across larger parameters to verify the sharp diameter expression without enumerating vertex-labelled configurations.

Run `python verifier.py` from a Python 3 environment. The observed result is `VERIFY_OK bfs_cases=68 bfs_pairs=617027 bfs_configurations=4392 type_extrema=2175`. The breadth-first checks cover every tested host with \(3\le m\le n\le7\) and \(m+n\le10\); the type-extrema checks cover all \(3\le m\le n\le17\) and all admissible layers. These are finite consistency checks; the unlimited-parameter result is proved above.

## Relationship to prior work

Fresán-Figueroa, Goldfeder and Lozano-Piña, *Reconfiguration graphs of mutual-visibility sets* (arXiv:2610.24324v1, first public 2026-10-16), introduced the fixed-cardinality mutual-visibility token-slide layers. Their Theorem 4.2 gives the occupancy-type characterization, Theorem 4.6 classifies connectivity, and Proposition 4.7 proves an upper bound \(d(S,T)\le|S\triangle T|-||S\cap A|-|T\cap A||\) and a diameter bound \(2\min\{k,N-k\}\). These are prior results, not new claims here. They do not state the exact all-pairs distance or sharp diameter; our geodesic routing proof strengthens these bounds. In particular, for disjoint balanced configurations of type \((2,2)\) in \(K_{4,4}\), the prior generic bound is eight, whereas the exact metric gives four.

Fabila-Monroy and Trujillo-Negrete, *On the Automorphism Group of Token Graphs of Complete Bipartite Graphs* (arXiv:2302.07914v4), determine symmetries of the unrestricted token graph, not shortest paths under mutual-visibility constraints. *On some metric properties of supertoken graphs* (Utilitas Mathematica 123, 2025, DOI:10.61091/um123-02) treats a related token model that allows multiplicities and therefore does not establish the required visibility-preserving shortest paths. No equivalent exact visibility-layer metric or all-parameter diameter was located in the consulted references; literature search non-detection does not certify priority.

## Limitations

The distance formula is confined to finite complete bipartite hosts with both sides of order at least three and to connected mutual-visibility layers. The maximum layer is disconnected when both sides have at least four vertices. No claim is made for arbitrary host graphs, non-geodesic token moves, other visibility notions, or the connectivity/metric of every component in disconnected layers. The mathematical proof and finite checks are not an independent audit. Historical-priority uncertainty remains.

## References

1. J. A. Fresán-Figueroa, I. A. Goldfeder and A. Lozano-Piña, *Reconfiguration graphs of mutual-visibility sets*, arXiv:2610.24324v1 (2026-10-16). https://arxiv.org/html/2610.24324v1
2. R. Fabila-Monroy and A. L. Trujillo-Negrete, *On the Automorphism Group of Token Graphs of Complete Bipartite Graphs*, arXiv:2302.07914v4 (2025). https://arxiv.org/html/2302.07914v4
3. *On some metric properties of supertoken graphs*, Utilitas Mathematica 123 (2025), 19–33. DOI:10.61091/um123-02. https://combinatorialpress.com/um-articles/vol-123/on-some-metric-properties-of-supertoken-graphs/
