# Exact reconfiguration distances for minimum zero forcing sets of crown graphs

## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n\) be the crown graph with bipartition \(\{a_i:i\in[n]\}\), \(\{b_i:i\in[n]\}\) and edges \(a_i b_j\) exactly when \(i\ne j\). A blue vertex with a unique white neighbor may force that neighbor blue. Let \(\mathcal R_n\) be the graph of *minimum* ordinary zero forcing sets of \(\operatorname{Cr}_n\), adjacent when exactly one chosen vertex is replaced by one unchosen vertex, with both configurations minimum zero forcing.

Put \(\mathcal P_n=\binom{[n]}2\), \(N=\binom n2\), \(k=2(n-2)\), and \(r=\binom{n-2}2\). Every minimum zero forcing set has complement
\[
\{a_i:i\in A\}\cup\{b_j:j\in B\},\qquad A,B\in\mathcal P_n,\quad A\ne B.
\]
Under this identification, \(\mathcal R_n\) is the induced subgraph of \(J(n,2)\square J(n,2)\) on ordered pairs \((A,B)\) with \(A\ne B\). Here \(J(n,2)\) has the two-subsets of \([n]\) as vertices, adjacent when they meet in exactly one element.

For two configurations \((A,B)\), \((C,D)\), set \(\epsilon=1\) exactly when \(C=B\), \(D=A\), and \(|A\cap B|=1\), and set \(\epsilon=0\) otherwise. **The exact shortest-path metric** is
\[
 d_{\mathcal R_n}((A,B),(C,D))
 =\bigl(2-|A\cap C|\bigr)+\bigl(2-|B\cap D|\bigr)+\epsilon.
\]
Thus there is precisely one type of collision detour: exchanging *adjacent* occupied Johnson vertices costs three moves rather than two. In particular, \(\mathcal R_n\) is connected; its diameter is \(3\) for \(n=3\) and \(4\) for every \(n\ge4\).

The **complete ordered all-pairs distance enumerator** is
\[
 D_n(q):=\sum_{X,Y\in V(\mathcal R_n)}q^{d_{\mathcal R_n}(X,Y)}
 =N\left[(N-2)(1+kq+rq^2)^2+(1+kq^2+rq^4)+k(q^3-q^2)\right].
\]
The vertex count is \(N(N-1)\), the edge count is \(Nk(N-2)\), and its Wiener index (sum of unordered pairwise distances) is
\[
 W(\mathcal R_n)
 =N\left[(N-1)^2(n-1)(n-2)+(n-2)\right].
\]
These metric and distance-distribution statements are the central result; the zero-forcing-number and minimum-set classification serve as an independently proved starting point, not a claimed new scalar invariant.

## Assumptions and scope
All graphs are finite and simple. Zero forcing uses only blue vertices and the unique-white-neighbor rule; it does not use skew or positive-semidefinite variants. A reconfiguration move replaces exactly one vertex of a minimum forcing set with another vertex, without a requirement that the exchanged vertices be adjacent in the crown graph. Distances are ordinary shortest-path lengths in this exchange graph, and the distance polynomial counts **ordered** pairs, including diagonal pairs.

## Proof
**1. Minimum forcing sets.** Let the initially white vertices be indexed by \(U\subseteq[n]\) on the first side and \(V\subseteq[n]\) on the second. If \(|V|\ge3\), each blue vertex on the first side sees at least two whites on the second, so no vertex of \(V\) can ever be forced: this remains true while \(V\) is unchanged. A symmetric argument applies to \(U\). Therefore every forcing set has \(|U|,|V|\le2\), giving at most four initially white vertices.

To attain four whites we must have \(|U|=|V|=2\). If \(U=V\), no initially blue vertex on either side has exactly one white neighbor, so forcing fails. If \(U\cap V=\varnothing\), an initially blue \(a_i\) with \(i\in V\) forces the opposite white vertex of the second part; analogously, initially blue vertices \(b_j\) with \(j\in U\) force the other white vertex of the first part. This can be done until both sides are blue. If \(U\cap V=\{x\}\), write \(U=\{x,u\}\), \(V=\{x,v\}\) with \(u\ne v\). Initially blue \(a_v\) forces \(b_x\), and initially blue \(b_u\) forces \(a_x\); now blue \(a_x\) and \(b_x\) can force the two remaining white vertices. Thus exactly the pairs \(U\ne V\) work, and the minimum forcing-set size is \(2n-4\).

**2. Reconfiguration graph.** All minimum sets omit exactly two vertices on each side. A one-vertex exchange between two such sets must remain within one side, thereby replacing one index of \(U\) or \(V\). Replacing one element in a two-subset is precisely a Johnson edge. The forbidden collision \(U=V\) removes the product diagonal, proving the graph identification.

**3. All-pairs metric.** Write \(d_J(E,F)=2-|E\cap F|\) for Johnson distances; the product distance \(d_J(A,C)+d_J(B,D)\) is always a lower bound. For any three distinct vertices \(E,F,H\) of \(J(n,2)\) with \(E\ne F\), there is an \(E\)-to-\(F\) Johnson geodesic avoiding \(H\): if the distance is one, use the edge; if it is two, the two disjoint two-subsets have four distinct common neighbors, at most one of which is \(H\).

If \(C\ne B\), first move \(A\) to \(C\) along a geodesic avoiding \(B\), then move \(B\) to \(D\) along a geodesic avoiding \(C\). This reaches the product lower bound. If \(C=B\) but \(D\ne A\), perform the second-coordinate geodesic first, avoiding \(A\), followed by the first-coordinate geodesic, avoiding \(D\). The only remaining case is \((C,D)=(B,A)\). If \(|A\cap B|=1\), the product lower bound is two, but each possible first step to a target coordinate would create a collision. Choose the third two-subset \(H\) of \(A\cup B\). The legal route \((A,B)\to(H,B)\to(H,A)\to(B,A)\) has length three. If \(A\cap B=\varnothing\), write \(A=\{a_1,a_2\}\), \(B=\{b_1,b_2\}\); set \(H=\{a_1,b_1\}\), \(K=\{a_2,b_2\}\). The four-step route \((A,B)\to(H,B)\to(H,K)\to(B,K)\to(B,A)\) attains the product lower bound of four. This proves the metric for every \(n\ge3\), without finite extrapolation.

**4. Distance distribution.** The distance enumerator from any vertex of \(J(n,2)\) is \(B(q)=1+kq+rq^2\), with \(k=2(n-2)\) neighbors and \(r=\binom{n-2}2\) vertices at distance two. For all ordered pairs of product configurations before excluding collisions, the distance polynomial is \(N^2B(q)^2\). Inclusion-exclusion for \(A=B\) and \(C=D\) subtracts \(2NB(q)^2\) and adds \(NB(q^2)\), leaving \(N[(N-2)B(q)^2+B(q^2)]\). Finally, the \(Nk\) ordered adjacent-swaps increase distance from two to three, contributing \(Nk(q^3-q^2)\). This is exactly the stated \(D_n(q)\).

The degree-four term is nonzero precisely for \(n\ge4\), and the degree-three term is nonzero for \(n=3\), giving the diameter values. The number of vertices and edges follows from the diagonal deletion and the two degree classes. Differentiating \(D_n(q)\) at \(q=1\), halving for unordered pairs, and using \(k+1+r=N\) yields the Wiener formula.

## Verification
The accompanying `verify_primary.py` independently enumerates every four-white configuration of \(\operatorname{Cr}_n\), applies the ordinary forcing closure, builds the actual one-vertex exchange graph, and exhaustively checks graph distances, degree classes, all distance counts, and Wiener indices for \(3\le n\le8\). `verify_alt.cpp` independently builds the Johnson-pair graph using bit masks, recomputes every shortest distance and distance-histogram coefficient, and checks the all-parameter formulas on the same finite range. Execute `python3 verify_primary.py`, then `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt`. All assertions passed in the recorded checks. These computations corroborate, rather than replace, the symbolic proof for unrestricted \(n\).

## Relationship to prior work
Barioli and collaborators developed classical zero forcing in the minimum-rank setting, and Geneson, Haas and Hogben introduced the graph of minimum zero forcing sets under single-vertex replacements; their 2020 work asks for efficient shortest-distance determination. A previous all-size classification of zero forcing sets for complete bipartite graphs with a matching deleted already includes the crown-graph **minimum-set count and characterization** as a specialization. Those structural inputs, and the scalar zero forcing number, are not asserted as original. The new contribution claimed here is the all-pairs shortest-path formula, its unique adjacent-swap obstruction, and the complete distance enumerator and Wiener formula on the induced diagonal-deleted Johnson square. Neither the inspected primary reconfiguration article nor the compared earlier zero-forcing-set classification states or directly supplies those metric identities.

## Limitations
No statement is made about forcing sets of nonminimum cardinality, moves requiring adjacency in the original crown graph, or other forcing rules. The proof does not assert that the graph metric of arbitrary diagonal-deleted Cartesian squares has this form; it uses the special geodesic redundancy and triangles of \(J(n,2)\). Prior results cover the minimum configurations, and equivalent metric identities may exist in unindexed literature or follow from an independently published general configuration-space theorem. No independent scholarly audit has been performed.

## References
1. F. Barioli et al., “Zero forcing parameters and minimum rank problems,” arXiv:1003.2028v1 (first public version, 2010-03-10), https://arxiv.org/abs/1003.2028.
2. L. Hogben et al., “Propagation time for zero forcing on a graph,” arXiv:1410.4191v1 (2014-10-15), https://arxiv.org/abs/1410.4191.
3. J. Geneson, R. Haas and L. Hogben, “Reconfiguration graphs of zero forcing sets,” arXiv:2009.00220v1 (2020-09-01), https://arxiv.org/html/2009.00220v1.
4. Earlier exact zero-forcing-set classification for complete bipartite graphs with a matching deleted, mathematical record `8a368cb2-e9c6-47c0-8103-80090f2907c4` (for logical comparison of claims; no additional provenance asserted).
