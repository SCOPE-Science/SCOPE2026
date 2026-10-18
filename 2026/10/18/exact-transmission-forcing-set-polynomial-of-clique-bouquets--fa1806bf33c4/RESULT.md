# Exact transmission forcing-set polynomial of clique bouquets

## Finding

For integers \(k,m\ge2\), let \(W_{k,m}=K_1\vee(kK_m)\) be the graph of \(k\) disjoint cliques of \(m\) vertices joined to one common hub. Put \(N=km+1\). For transmission proportion \(0<\alpha\le1\) and filling threshold \(0<\beta\le1\), let \(\mathcal T_{\alpha,\beta}(W_{k,m};z)\) enumerate successful initial sets, with coefficient of \(z^s\) equal to the number of successful sets of \(s\) vertices. Define
\[
 L=(m-1)\alpha,\quad U=m\alpha,\quad H=km\alpha,\quad T=\min\{m(k-1)\alpha,\; (m-1)\alpha+m(k-1)\alpha^2\}.
\]
The **complete forcing-set polynomial** is
\[
\mathcal T_{\alpha,\beta}(W_{k,m};z)=
\begin{cases}
 z^{N-k-1}\big((1+z)(z+m)^k-m^k\big),&0<\beta\le L,\\
 z^N+\big(km\mathbf{1}_{\{\beta\le U\}}+\mathbf{1}_{\{\beta\le H\}}\big)z^{N-1}
 +km\mathbf{1}_{\{\beta\le T\}}z^{N-2},& L<\beta\le1.
\end{cases}
\]
Here each indicator is one when its condition holds and zero otherwise. In particular, the least exponent with nonzero coefficient, the transmission zero forcing number, is
\[
 Z_{\alpha,\beta}(W_{k,m})=
 \begin{cases}
 N-k,&\beta\le L,\\
 N-2,&L<\beta\le T,\\
 N-1,&T<\beta\le H,\\
 N,&H<\beta\le1.
 \end{cases}
\]
Empty parameter intervals are ignored. Since \(L<T\le H\), the boundaries are consistent. For \(k\ge3\), increasing the threshold across \(L\) can cause a jump of \(k-2\) in the minimum initial set size. For instance, choosing \(\alpha=1/(4mk)\) ensures \(L<T<1\) for every \(k,m\ge2\), so this jump occurs for arbitrarily large \(k\).

## Assumptions and scope

The graphs are finite, simple and undirected; \(k,m\ge2\). At time zero, vertices in an initial set have weight one and are *filled*; all other vertices have weight zero and are unfilled. In each simultaneous round, each filled vertex with exactly one unfilled neighbor transmits \(\alpha\) times its current weight to that neighbor. The received weights are summed, and precisely the previously unfilled vertices with total weight at least \(\beta\) become filled. Filled vertices stay filled. If a round fills no vertex the process stops. The result is for this synchronous transmission rule, not arbitrary asynchronous forcing or probability-based infection. All inequalities in the theorem include boundary equality as displayed. Every initial subset is counted once, with vertex labels distinguished.

## Proof

Write \(h\) for the common hub. The \(k\) peripheral \(m\)-cliques will be called *blades*. A necessary condition for any successful initial set is that each blade contain at most one initially unfilled vertex. Indeed, if two vertices in one blade are unfilled, then every filled vertex adjacent to either is adjacent to both: the hub and all other blade vertices see both unfilled vertices. Neither can be the unique unfilled neighbor of a filled vertex. By induction neither of these two vertices can ever become filled.

Assume from now on that exactly \(t\) blades have one unfilled vertex and the other \(k-t\) blades are completely filled initially. There are \(\binom kt m^t\) choices of which blades are incomplete and which of their vertices is unfilled.

**Case 1: the hub is initially filled.** If \(t=0\), all vertices are filled already. If \(t=1\), the unique unfilled blade vertex receives the amount \(\alpha\) from each of its \(m-1\) filled blade mates and another \(\alpha\) from the hub. It fills in the first round exactly when \(\beta\le U=m\alpha\). If \(t\ge2\), the hub has multiple unfilled neighbors and cannot transmit to any; each unfilled blade vertex receives exactly \(L=(m-1)\alpha\) from its own blade mates. Either all these vertices fill at once when \(\beta\le L\), or nothing fills and the process stops. The initial set size here is \(N-t\).

**Case 2: the hub is initially unfilled.** When \(t=k\), every initially filled vertex has the hub and its own incomplete-blade vertex as two unfilled neighbors, so no transmission occurs. When \(t\le k-1\), only vertices of the \(k-t\) completely filled blades can transmit to the hub in the first round. There are \(m(k-t)\) such vertices, each of weight one, so the hub fills precisely if \(\beta\le m(k-t)\alpha\); no incomplete blade vertex can fill in this first round. For \(t=0\) this condition is \(\beta\le H\), and once the hub fills every vertex is filled.

If \(2\le t\le k-1\), after filling the hub still sees at least two unfilled blade vertices, so it cannot transmit. Each outstanding blade vertex receives exactly \(L\) in round two, from its \(m-1\) initially filled blade mates. Thus success requires \(\beta\le L\). Conversely, under this inequality the hub has already filled in round one because \(m(k-t)\alpha\ge m\alpha>L\), so the same condition suffices. Finally, if \(t=1\), the hub first receives \(m(k-1)\alpha\), after which it has exactly one unfilled neighbor. In round two that last vertex receives \(L\) from its blade mates together with the new hub's contribution \(m(k-1)\alpha^2\). Both rounds succeed precisely when
\[
\beta\le\min\{m(k-1)\alpha,\,L+m(k-1)\alpha^2\}=T.
\]
The size of a hub-absent initial set is \(N-1-t\). These cases exhaust all choices of initial set and all possible transmissions.

If \(\beta\le L\), the successful hub-present cases have \(0\le t\le k\); the successful hub-absent cases have \(0\le t\le k-1\). Their generating polynomial is
\[
\sum_{t=0}^k\binom kt m^tz^{N-t}
+\sum_{t=0}^{k-1}\binom kt m^tz^{N-1-t}
=z^{N-k-1}\big((1+z)(z+m)^k-m^k\big).
\]
If \(\beta>L\), the only successful hub-present cases are \(t=0\) (always) and \(t=1\) (when \(\beta\le U\)); the only hub-absent cases are \(t=0\) (when \(\beta\le H\)) and \(t=1\) (when \(\beta\le T\)). Each hub-present \(t=1\) or hub-absent \(t=1\) case has \(km\) labelled choices. This gives the second polynomial formula. Finally \(L<T\le H\) and \(U\le H\), so taking the smallest exponent gives all four cases of the zero forcing number formula. This proves the theorem.

## Verification

The companion standard-library-only program `verify_transmission_windmill.py` builds the graph explicitly, simulates simultaneous rounds with exact rational weights, exhaustively tests every labelled initial set and compares the full coefficient vector against the closed polynomial. It checked \(337\) graph/parameter pairs covering the graph sizes \((k,m)=(2,2),(3,2),(4,2),(2,3),(3,3),(2,4),(3,4)\), including boundary values and nearby rational thresholds; all matched. The program is a separate computational check of small instances, not an exhaustive verification over infinitely many sizes or real-valued parameters. The universal assertion is proved by the two-case argument above.

For example, with \(k=4\), \(m=2\), and \(\alpha=1/20\), the thresholds are \(L=1/20\), \(T=13/200\), \(U=1/10\), and \(H=2/5\). The minimum set sizes at \(\beta=1/25,3/50,2/25,1/5,7/10\) are respectively \(5,7,8,8,9\); the respective counts of minimum sets are \(48,8,9,1,1\).

There can be a successful initial set whose strict superset is not successful. For \(k=3,m=2,\alpha=3/10,\beta=63/100\), take all four nonhub vertices from two blades and just one vertex from the third blade, with the hub absent. In round one, the hub receives \(6/5\) and fills. The last blade vertex receives \(3/10+9/25=33/50\) in round two and fills. If the hub is added to the initial set instead, the last blade vertex receives only \(3/5<63/100\), so that larger seed set fails. The counterexample follows directly from the classification.

## Relationship to prior work

Berliner, Bozeman, Collins, Flagg, Furst and Hunnell introduced transmission zero forcing in 2026 and developed bounds and results for several standard graph families. Their maximum-degree criterion determines the high-threshold regime, but does not supply the full two-parameter forcing-set enumerator of clique bouquets. Published transmission-zero-forcing results for complete multipartite graphs concern graphs structurally different from \(K_1\vee(kK_m)\), which is not complete multipartite when \(k,m\ge2\). A published zero-forcing polynomial of friendship graphs concerns ordinary zero forcing and corresponds to the low-threshold specialization \(m=2\) of the first branch; it does not imply the novel threshold-dependent branch or the \(\alpha^2\) accumulation boundary. The novelty asserted here is the complete mixed-parameter polynomial on all clique bouquets, not the ordinary friendship-graph polynomial, the definition of transmission forcing, or the general maximum-degree bound.

## Limitations

This theorem is specific to a single common hub adjoining equal-sized cliques and synchronous transmission. It makes no assertion for arbitrary block graphs, unequal blade sizes, or asynchronous rules. Finite computation supports but does not replace the infinite proof. The comparison to existing indexed and accessible publications is not a proof of absolute priority: equivalent unindexed work remains possible, and the entire text of each adjacent published record was not necessarily accessible for comparison. The new polynomial counts successful labelled initial sets; it does not count forcing sequences or optimize the time to fill.

## References

- A. H. Berliner, C. Bozeman, K. L. Collins, M. Flagg, V. Furst and M. Hunnell, *Transmission Zero Forcing*, arXiv:2606.22246v1 (first public 2026-06-20), https://arxiv.org/abs/2606.22246.
- *Transmission zero forcing of complete multipartite graphs*, published mathematical research record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-transmission-zero-forcing-of-complete-multipartite-graphs--1247bfce37f4.
- *Zero forcing polynomial of friendship graphs*, published mathematical research record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-friendship-graphs--b77605779c1b.
