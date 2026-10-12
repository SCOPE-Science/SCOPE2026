# Exact color-refinement depth and orbit recovery on equal-cycle dumbbell graphs
## Finding
For integers \(m\ge 3\) and \(k\ge 0\), let \(D_{m,k,m}\) be the dumbbell graph obtained from two vertex-disjoint cycles \(C_m\) and a path \(P_{k+2}\) by identifying the two path endpoints with one vertex of each cycle. Thus the connector path has \(k\) internal vertices. Let \(\operatorname{Stab}(G)\) be the least round at which ordinary color refinement from the uniform coloring stops changing the vertex partition.

Then
\[
\operatorname{Stab}(D_{m,k,m})=
\begin{cases}
\left\lfloor m/2\right\rfloor,&k+1=m,\\
\max\!\left\{\left\lfloor m/2\right\rfloor,\left\lceil k/2\right\rceil,\min\{m,k+1\}\right\},&k+1\ne m.
\end{cases}
\]

The equality \(k+1=m\) is a genuine resonance. If the connector length equals the cycle length, the stable color partition is strictly coarser than the automorphism-orbit partition: corresponding positions on the connector and on the two cycles remain color-equivalent forever. For every \(k+1\ne m\), the stable color partition is exactly the automorphism-orbit partition.

## Assumptions and scope
All graphs are finite, simple, undirected, and initially uncolored. The dumbbell convention is the one used in the spectral-graph literature: \(D_{p,k,q}\) consists of cycles \(C_p,C_q\) joined by a path \(P_{k+2}\) whose only vertices on the cycles are its endpoints.

Round \(0\) is the uniform coloring. In each later round, a vertex receives a color determined by its previous color and the multiset of previous colors on its neighbors. Stabilization refers to equality of induced partitions, not literal equality of color labels.

## Proof
Let \(u,v\) be the two degree-three attachment vertices. Every other vertex has degree two. The graph has an automorphism interchanging the two cycles and reversing the connector, so \(u\) and \(v\) have the same color in every refinement round.

View each maximal degree-two chain between degree-three vertices in the universal cover as a thread. There are only two thread lengths: the cycle thread length \(m\), and the connector thread length \(p=k+1\). The two endpoints of every lifted thread always have the same color, namely the color of \(u,v\).

For a degree-two vertex at distance \(x\) from one endpoint of a thread of length \(L\), an induction on the round gives the exact color invariant
\[
\left\{\min\{x,r\},\min\{L-x,r\}\right\}
\]
at round \(r\ge1\), together with the common endpoint color. Indeed, round \(1\) only sees that both neighbors have degree two or degree three, and each subsequent round extends the visible distance by one edge from both ends. Because the endpoint colors agree, the two distances are unordered.

Inside one thread of length \(L\), these clipped pairs stop refining exactly at round \(\lfloor L/2\rfloor\). Hence the cycle threads contribute \(\lfloor m/2\rfloor\), while the connector contributes
\[
\left\lfloor\frac{k+1}{2}\right\rfloor=\left\lceil\frac{k}{2}\right\rceil.
\]

It remains to analyze collisions between a cycle-thread vertex and a connector-thread vertex. If the two thread lengths differ, say \(L_1<L_2\), then the vertices one edge from an endpoint have equal clipped pairs through round \(L_1-1\), but at round \(L_1\) they become \(\{1,L_1-1\}\) and \(\{1,L_1\}\). No cross-thread collision can survive longer, because equality of the two clipped-distance pairs through round \(L_1\) would force equality of the full endpoint-distance sums and hence \(L_1=L_2\). Thus unequal thread lengths contribute the additional term \(\min\{m,k+1\}\).

If \(k+1=m\), the two thread lengths are equal, so corresponding positions have identical clipped-distance pairs in every round. There is therefore no cross-thread splitting term, giving exactly \(\lfloor m/2\rfloor\).

For the orbit statement, when \(k+1\ne m\), the stable colors first distinguish thread type and then distinguish position up to reversal. These are exactly the automorphism orbits: cycle positions are grouped by distance from the attachment vertex across the two cycles, and connector positions are grouped by reflection across the midpoint. When \(k+1=m\), stable colors merge corresponding cycle and connector positions. Such vertices cannot be automorphic because every internal connector vertex is a cut vertex, whereas no cycle vertex is. Hence the stable partition is strictly coarser than the orbit partition precisely in the resonant case.

## Verification
The accompanying standalone checker constructs the graphs directly and recomputes ordinary color refinement. It verifies both the depth formula and the orbit-partition criterion for every
\[
3\le m\le30,\qquad 0\le k\le100.
\]
It returns:

`VERIFY_OK depth_checks=2828 orbit_checks=2828 m=3..30 k=0..100`

The computation is corroborative only; the proof above establishes the result for all stated parameters.

## Relationship to prior work
Wang, Belardo, Huang, and Li Marzi use the same dumbbell family \(D_{a,b,c}\) in their 2010 spectral characterization work. Liu and Lu later use the notation \(D_{p,k,q}\) and define it explicitly as two cycles joined by \(P_{k+2}\). These papers study adjacency, signless-Laplacian, and Laplacian spectra rather than color refinement.

Krebs and Verbitsky formalize color-refinement stabilization and relate refinement rounds to truncated universal covers. That local-view principle explains why the present proof reduces to clipped endpoint distances on subdivided threads. Targeted searches over dumbbell/handcuff terminology, color refinement, \(1\)-WL, Weisfeiler--Leman iteration number, equitable partitions, and orbit recovery did not locate the formula above or the resonance \(k+1=m\).

## Limitations
The theorem treats equal cycle lengths. Unequal dumbbells \(D_{p,k,q}\) can have additional interactions among three distinct thread lengths and are not covered here. The literature search was targeted rather than exhaustive, so an unindexed equivalent computation remains a residual priority risk. The finite checker is not used as a substitute for the all-parameter proof.

## References
1. J. Wang, F. Belardo, Q. Huang, and E. M. Li Marzi, *Spectral Characterizations of Dumbbell Graphs*, Electronic Journal of Combinatorics 17(1), R42, 2010, DOI: 10.37236/314.
2. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014.
3. X. Liu and P. Lu, *Laplacian spectral characterization of dumbbell graphs and theta graphs*, arXiv:1407.5255, first posted 20 July 2014.
