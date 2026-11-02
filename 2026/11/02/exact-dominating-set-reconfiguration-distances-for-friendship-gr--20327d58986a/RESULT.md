# Exact dominating-set reconfiguration distances for friendship graphs

## Finding
For every integer \(r\ge2\), let the friendship graph be \(F_r=K_1\vee rK_2\), with a universal vertex \(h\) and \(r\) disjoint pairs of outer vertices (called blades). Its upper domination number is \(\Gamma(F_r)=r\). Write \(\mathcal D_{r+1}(F_r)\) for the reconfiguration graph whose states are the dominating vertex subsets of cardinality at most \(r+1\), adjacent when exactly one vertex is inserted or deleted.

The following explicit state model determines **every geodesic distance** in \(\mathcal D_{r+1}(F_r)\). Write \(\delta(A,B)=|A\triangle B|\) for the symmetric-difference size of outer-vertex sets.

* \(H_X=\{h\}\cup X\) for any outer-vertex subset \(X\) with \(|X|\le r\).
* \(L_T=T\) for any transversal \(T\) choosing exactly one outer vertex per blade.
* \(U\) for any outer-vertex set occupying exactly one entire blade and exactly one vertex of every other blade. Let \(i(U)\) be the doubled blade and \(\mathscr T(U)\) the two transversals obtained by deleting one of the two vertices in its doubled blade.

These are all the states. For hub states, lower transversals and upper states, the exact symmetric distance formulas (with states distinct where specified) are

\[
\begin{aligned}
d(H_X,H_Y)&=\delta(X,Y),\\
d(H_X,L_T)&=1+\delta(X,T),\\
d(H_X,U)&=2+\min_{B\in\mathscr T(U)}\delta(X,B),\\
d(L_S,L_T)&=\delta(S,T),\\
d(L_T,U)&=1+\min_{B\in\mathscr T(U)}\delta(T,B),\\
d(U,V)&=\begin{cases}
0,&U=V,\\
\delta(U,V)+2,&U\ne V\text{ and }i(U)=i(V),\\
\delta(U,V),&i(U)\ne i(V).
\end{cases}
\end{aligned}
\]

For \(H_X\), let \(a\) be the number of blades containing exactly one member of \(X\), and \(b\) the number containing both. Its eccentricity is
\[
\operatorname{ecc}(H_X)=\begin{cases}
r+a+2,&b=0,\ a<r,\\
2r+1,&b=0,\ a=r,\\
r+a+2b,&b\ge1.
\end{cases}
\]
Every lower or upper state has eccentricity \(2r+1\). Thus
\[
\operatorname{rad}\mathcal D_{r+1}(F_r)=r+2,\qquad
\operatorname{diam}\mathcal D_{r+1}(F_r)=2r+1.
\]
The **center has exactly \(r+1\) states**: \(H_\varnothing\) and the \(r\) hub states whose outer part is one whole blade. The **periphery has exactly \((r+2)2^r\) states**.

The number of states and exchanges is exactly
\[
|V|=\sum_{j=0}^{r}\binom{2r}{j}+2^r+r2^{r-1},\qquad
|E|=2r\sum_{j=0}^{r-1}\binom{2r-1}{j}+(r+1)2^r.
\]
The threshold is sharp: \(\mathcal D_r(F_r)\) is disconnected, while \(\mathcal D_{r+1}(F_r)\) is connected. Connectivity at this threshold is consistent with the previously known chordal-graph theorem; the new claim concerns the explicit entire metric and eccentricity structure.

## Assumptions and scope
All graphs are finite, simple and undirected. The integer \(r\ge2\) is arbitrary. A dominating set meets or neighbours every vertex. The upper domination number is the maximum size of an inclusion-minimal dominating set. Reconfiguration moves add **or delete one** vertex, with all intermediate sets dominating and of size at most \(r+1\). The metric is the unweighted shortest-path metric in this graph. It is not a token-jumping, sliding, or fixed-cardinality metric.

The friendship graph's central vertex is \(h\). The outer vertices form \(r\) disjoint edges, called blades. The hub's presence automatically guarantees domination. Without the hub, domination requires at least one selected outer vertex in each blade. The cardinality cap therefore leaves only transversal sets of size \(r\) and one-doubled-blade sets of size \(r+1\). Every set with the hub and at most \(r\) other vertices is valid. The only minimal dominating sets are \(\{h\}\) and the \(2^r\) transversals; hence \(\Gamma(F_r)=r\).

## Proof
**1. States and exchanges.** The preceding domination observation proves the exhaustive \(H/L/U\) classification. Between hub states, moves toggle one outer vertex subject to the \(r\)-element cap. Each transversal \(L_T\) has an edge to \(H_T\), and edges to the \(r\) upper sets obtained by filling in one blade. Each upper state is incident to exactly its two contained transversals. There are no other edges: upper states are at capacity, lower transversals are inclusion-minimal in the no-hub sector, and the hub can be removed from a hub state only when its outer part is a transversal. These facts also prove connectedness: an upper state reaches a transversal, each transversal reaches its hub state, and all hub states connect to \(H_\varnothing\) by deletions.

**2. Distances involving a hub.** Within hub states, the distance is \(\delta(X,Y)\), attained by deleting the elements of \(X\setminus Y\) and then adding those of \(Y\setminus X\); all intermediate outer sets have at most \(r\) elements. Any path changes each differing element at least once, so the distance cannot be smaller. From \(H_X\) to \(L_T\), the hub must be deleted once, giving the lower bound \(1+\delta(X,T)\); the hub-only route attains it.

For an upper target \(U\), choose a floor \(B\in\mathscr T(U)\). The route \(H_X\to H_B\to L_B\to U\) has length \(\delta(X,B)+2\), giving the claimed upper bound. For the lower bound, take any route ending at \(U\). At the **last deletion of the hub** let its outer part be a transversal \(S\). Before that step the route changes at least \(\delta(X,S)\) outer vertices, and afterward it changes at least \(\delta(S,U)\) of them. Let \(B\in\mathscr T(U)\) agree with \(S\) at the doubled blade. Because \(S\) has one member there and \(U\) has both, \(\delta(S,U)=1+\delta(S,B)\). Thus the full route is at least \(\delta(X,S)+1+\delta(S,U)=2+\delta(X,S)+\delta(S,B)\ge2+\min_{B'\in\mathscr T(U)}\delta(X,B')\). This remains valid if the route visits hub states multiple times.

**3. Distances without a hub.** A transversal-to-transversal switch on a single blade takes two moves: add the missing outer vertex, then delete the old one. Repeating these switches gives \(d(L_S,L_T)=\delta(S,T)\), which also meets the universal symmetric-difference lower bound. For \(d(L_T,U)\), choose the closer contained transversal \(B\) of \(U\) and take the preceding switches followed by \(B\to U\), giving \(1+\min_B\delta(T,B)\). This equals \(\delta(T,U)\): on the doubled blade \(T\) meets exactly one of the two vertices, so the nearer floor agrees there. The universal symmetric-difference lower bound proves equality.

For two different upper states \(U,V\) with different doubled blades, delete from \(U\)'s doubled blade the vertex not belonging to \(V\), and likewise choose a floor of \(V\) agreeing with \(U\) on the doubled blade of \(V\). These floor choices reduce the symmetric difference by two; a sequence of transversal blade switches between the floors, bracketed by one deletion and one addition, has length exactly \(\delta(U,V)\). No path is shorter than its symmetric difference.

If two different upper states \(U,V\) have the *same* doubled blade, choose floors agreeing in that blade and switch the other differing blades. This gives \(\delta(U,V)+2\) steps. Conversely, the first move from \(U\) must delete a vertex of its doubled blade and the final move into \(V\) must add a vertex of that same blade. Neither blade vertex is in \(U\triangle V\), so these two operations are in addition to the at least \(\delta(U,V)\) required changes on other blades. This proves the sharp lower bound.

**4. Eccentricities.** Fix \(X\) with \(a\) singleton blades and \(b\) doubled blades, so \(|X|=a+2b\le r\). The farthest hub state is at distance \(r+|X|\): one may choose \(r\) outer vertices outside \(X\), and no state at the capped size has larger symmetric difference. The maximal distance to a lower transversal is \(r+a+1\): in each singleton blade choose the opposite vertex, while the \(b\) doubled blades contribute one forced overlap each. If \(X\) leaves any blade empty, doubling an empty blade and choosing opposite vertices on all singleton blades gives maximal hub-to-upper distance \(r+a+2\). This is also an upper bound because every upper state contains a floor transversal and every floor meets each of the \(b\) doubled blades of \(X\). When there is no empty blade, the size cap forces \(a=r,b=0\); any upper state then meets \(X\) in its doubled blade, and the maximum hub-to-upper distance is \(2r\). Taking the maximum of the three target classes gives the stated hub eccentricities.

For each lower transversal \(T\), its opposite transversal \(S\) gives \(d(L_T,H_S)=2r+1\). For each upper \(U\), choose a hub state \(H_X\) whose outer set consists of the vertices **opposite to \(U\)** in all \(r-1\) singleton blades and contains neither vertex of \(U\)'s doubled blade; then \(d(U,H_X)=2r+1\). The distance formulas show no pair exceeds \(2r+1\). Hence all lower and upper states are peripheral. The hub formula is minimized exactly at \(X=\varnothing\) or \(X\) equal to one full blade. It is maximized exactly at the hub states consisting of one outer vertex in every blade, or one outer vertex in all but one blade. Counting these plus the no-hub states gives the center and periphery cardinalities claimed.

**5. Enumerators and sharp threshold.** There are \(\sum_{j=0}^r\binom{2r}{j}\) hub states, \(2^r\) lower transversals, and \(r2^{r-1}\) upper states. The hub-subgraph edges number \(2r\sum_{j=0}^{r-1}\binom{2r-1}{j}\) by choosing the toggled outer vertex and an allowed set of other vertices. There are \(2^r\) hub-to-lower edges and \(r2^r\) lower-to-upper edges. These yield the formulas. At cap \(r\), every transversal is isolated, because it is inclusion-minimal without the hub and every feasible addition exceeds the cap. At cap \(r+1\), connectivity was proved in Step 1. Thus \(r+1\) is the first connected cap.

## Verification
Two standalone Python 3 standard-library verifiers accompany this result:

- Run `python3 verify_direct.py` to build the friendship graph from its vertex adjacency, examine every vertex subset for domination, and construct the reconfiguration graph directly from one-vertex toggles. It checks exact state and edge counts, connectedness, and all eccentricities for \(2\le r\le5\), and every state-type symmetry representative for \(6\le r\le8\).
- Run `python3 verify_metric.py` to construct the abstract hub/transversal/upper graph independently and compare every exact distance formula to breadth-first search on all ordered pairs for \(2\le r\le5\), then compare representative-origin distances against all destinations at \(r=6\).

The proof applies to **all integers \(r\ge2\)**. These finite programs corroborate the theorem but do not establish the unrestricted quantifier by finite extrapolation. There is no stochastic computation or external package dependency.

## Relationship to prior work
Haas and Seyffarth introduced \(k\)-dominating graphs and established sufficient connectivity conditions, including their chordal-graph case; the fact that the critical friendship-graph reconfiguration is connected follows from that general framework. Suzuki, Mouawad and Nishimura studied broader connectivity and diameter behavior of domination reconfiguration and provided general counterexamples and bounds, not a friendship-graph all-pairs metric. Alikhani, Brown and Jahari previously determined the friendship graph's ordinary domination polynomial, which implies the counts of dominating sets but says nothing directly about adjacency or shortest reconfiguration routes. Messinger and Porter addressed Eulerian rather than geodesic properties of \(k\)-dominating graphs. Their general definitions, connectivity conclusions, and enumeration of dominating sets are not presented as new here.

The claimed contribution is the complete all-pairs shortest-path formula, its eccentricity classification, sharp radius/diameter, and exact centers and periphery at \(k=r+1\). Accessible prior results and related searchable research records were compared by the mathematical statements they imply, not just by keywords; no equivalence or stronger result covering this claim was identified.

## Limitations
This result concerns friendship graphs with \(r\ge2\) and addition/deletion moves under the specific size cap \(r+1\). No formula is asserted for general windmill graphs with larger complete blades, other caps, fixed-cardinality exchange moves, reconfiguration mixing times, or arbitrary chordal graphs. The argument is self-contained for the specified family, but absolute originality against all older unindexed literature is not established. Independent audit has not been performed.

## References
1. R. Haas and K. Seyffarth, *The k-Dominating Graph*, arXiv:1209.5138 (first posted 2012-09-24). https://arxiv.org/abs/1209.5138
2. S. Alikhani, J. Brown and S. Jahari, *On the Domination Polynomials of Friendship Graphs*, arXiv:1401.2092 (first posted 2014-01-08). https://arxiv.org/abs/1401.2092
3. A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714 (first posted 2014-01-22). https://arxiv.org/abs/1401.5714
4. M. E. Messinger and A. Porter, *Eulerian k-dominating reconfiguration graphs*, arXiv:2404.10962 (first posted 2024-04-17). https://arxiv.org/abs/2404.10962
