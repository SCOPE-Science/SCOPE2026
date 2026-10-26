# Exact two-marker refinement trajectories and an antipodal discontinuity on cycles
## Finding
Let \(C_n\), \(n\ge3\), be the simple cycle with vertex set \(\mathbb Z/n\mathbb Z\), and distinguish the vertices \(0\) and \(t\) in different initial singleton colours, where \(1\le t\le\lfloor n/2\rfloor\). Give all remaining vertices one common colour. For each vertex \(x\), define \(d_0(x)=d_{C_n}(x,0)\) and \(d_t(x)=d_{C_n}(x,t)\). The round-\(r\) partition of ordinary synchronous counting colour refinement is exactly the fibre partition of
\[
F_r(x)=\bigl(\min\{d_0(x),r+1\},\min\{d_t(x),r+1\}\bigr),\qquad r\ge0.
\]
The **first stable round** (the first round whose partition equals the next round's) is
\[
\rho(n,t)=\begin{cases}
\max\bigl\{t-1,\lfloor(n-t-1)/2\rfloor\bigr\},&2t<n,\\
\lfloor(n-2)/4\rfloor,&2t=n.
\end{cases}
\]
If \(2t<n\), the final partition has \(n\) singleton cells. If \(2t=n\), it has exactly \(n/2+1\) cells, indexed by distance from vertex \(0\); these are the orbits of the reflection fixing both landmarks. The depth is not monotone in marker separation: for example, on \(C_{20}\) the depths at separations \(t=7,8,9,10\) are \(6,7,8,4\), respectively.

## Assumptions and scope
The graph is finite, simple and undirected; for \(n=3\), it is the three-vertex triangle. Colour refinement retains a vertex's current colour and replaces its colour with an injective encoding of that colour together with the **multiset** of its two neighbours' colours. Round zero is the stipulated initial colouring. A stable round is indexed by partitions rather than arbitrary numerical colour names. Marker colours are distinct and ordered; neither marker is recoloured to the other's colour. Graph distance is shortest-path distance. No edge labels or external vertex order is used by the refinement algorithm.

## Proof
**1. Refinement and truncated distances.** A standard induction on \(r\) characterizes the round-\(r\) colour of a vertex by the isomorphism type of its depth-\(r\) rooted, initially-coloured **walk-unfolding tree**: the two children at each node correspond to the graph neighbours, with repeated visits represented by separate tree nodes. This is exactly the retained-colour/multiset recurrence. The earliest occurrence of either uniquely coloured marker in this unfolding is at its graph distance, if that distance is at most \(r\). Hence equality of round-\(r\) colours implies equality of \(F_r\): marker occurrence at depths at most \(r\) determines the exact distance, whereas nonoccurrence determines the truncated value \(r+1\).

For the converse, suppose two vertices have equal \(F_r\). If neither marker is visible within distance \(r\), both unfoldings have only the common initial colour throughout, so coincide. If exactly one marker, say \(0\), is visible, the two vertices have the same exact distance from \(0\); the cycle reflection fixing \(0\) interchanges them (or each is fixed). Their rooted radius-\(r\) unfoldings contain no occurrence of the other marker \(t\), so the reflection identifies their coloured unfoldings. If both markers are visible, equality of \(F_r\) is equality of both exact distances. Two nonantipodal marked vertices form a resolving set of the cycle: the distance pair determines a vertex uniquely. In the even-cycle antipodal case it determines the vertex up to the unique reflection fixing both markers, which is an automorphism preserving the initial colours. Thus the unfoldings agree also in this case. This proves the partition identity at every \(r\ge0\).

**2. Nonantipodal threshold.** Assume \(2t<n\), write \(L=n-t>t\), and put \(c=r+1\). The pair of untruncated distances resolves every vertex, so the refinement is stable as soon as the truncation map is injective. We prove that injectivity holds exactly when
\[
c\ge\max\bigl\{t,\lceil L/2\rceil\bigr\}.
\]
If \(c<t\), the two neighbours of marker \(0\) (which are distinct from the other marker as \(t\ge2\)) both have truncated pair \((1,c)\) for \(c\ge2\), and when \(c=1\) both have \((1,1)\); thus injectivity fails. If \(c\ge t\) but \(2c<L\), choose two consecutive internal vertices on the longer \(0\)-to-\(t\) arc at positions \(c\) and \(c+1\) measured from \(0\). Both are at distance at least \(c\) from *each* marker, even allowing the shorter alternative route around the cycle, and hence share \((c,c)\). Thus \(c\ge\lceil L/2\rceil\) is necessary.

Conversely suppose \(c\ge t\) and \(2c\ge L\). If neither component of the truncated pair is saturated, it is the untruncated resolving pair and is unique. If both are saturated, their vertex lies on the longer arc and its longer-arc position \(j\) obeys \(c\le j\le L-c\); this contains at most one integer. Finally, suppose exactly one component is saturated. For each fixed unsaturated distance \(1\le j<c\) from marker \(0\), there are at most two candidate vertices. The candidate reached by proceeding from \(0\) toward \(t\) has distance at most \(|j-t|<c\) from \(t\), so cannot have its second component saturated; at most the opposite candidate can. The argument is symmetric when only the distance from \(t\) is unsaturated. The distance-zero case has only one candidate. Hence every truncated pair is unique and the stable partition is discrete, first attained at \(r=\max\{t-1,\lceil L/2\rceil-1\}\), as claimed. Stability cannot precede discreteness because whenever a truncated pair is still duplicated, the preceding necessity argument applies at the corresponding cap and the next cap either splits a pair or, if the cap is below the final threshold, the global partition cannot yet be stable: a stable 1-WL partition is unchanged at all later rounds, whereas the final distance-pair partition is discrete.

**3. Antipodal threshold.** Now \(n=2t\). For every vertex the two untruncated distances sum to \(t\), and the distance pairs distinguish precisely the reflection orbits indexed by \(j=d_0(x)\), \(0\le j\le t\). Thus the partition at cap \(c=r+1\) is the fibre partition of \(j\mapsto(\min\{j,c\},\min\{t-j,c\})\). This map is injective on \(\{0,\ldots,t\}\) exactly when \(2c\ge t\): if \(2c<t\), the central consecutive indices have identical pair \((c,c)\); if \(2c\ge t\), the saturated central interval contains at most one integer and the remaining indices are distinguished by an unsaturated coordinate. Consequently the first stable round is \(\lceil t/2\rceil-1=\lfloor(t-1)/2\rfloor=\lfloor(n-2)/4\rfloor\), with \(t+1\) orbit cells. This includes the smallest even cycle \(C_4\), where the initial colouring is already stable.

## Verification
The accompanying standalone `verify.py` implements synchronous refinement directly from neighbours and initial colours, without using the proposed partition or threshold to generate the refinement. It separately constructs the proposed truncated-distance partitions and checks equality at every round. For all \(3\le n\le90\) and \(1\le t\le\lfloor n/2\rfloor\), it checks the first stable round and final cell count as well as every partition identity. The saved output records 2,024 configurations and 124,542 round-partition comparisons. The finite tests corroborate, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work
Arvind–Köbler–Rattan–Verbitsky establish broad structural links between colour refinement and graph-isomorphism properties, rather than the two-marked cyclic round-by-round partitions or exact stopping-depth function [1]. Kluge develops group-algebra methods for colour refinement on circulants and proves the Tinhofer property for prime-order circulants: in that setting, at most two suitably individualized vertices yield a discrete partition [2, Theorem 4]. Therefore the **discreteness** conclusion on odd prime cycles is already covered by a stronger general result and is not claimed as novel. The exact pair-truncation formula for **every round**, its all-length classification (including composite cycles), the separation-dependent sharp stopping depth, and the exceptional antipodal orbit count are the additional results here. The full relevant sections of both papers were compared; no matching exact stopping-depth result was located. This is a literature comparison, not proof that no other publication contains an equivalent statement.

## Limitations
The claim is restricted to simple cycles with **two distinct, separately coloured** markers and ordinary synchronous counting refinement; it does not give corresponding formulas for graph powers, arbitrary circulants, or higher-dimensional WL. Neither the enumeration nor the finite checks establish originality against unindexed literature. No independent audit is represented as completed.

## References
[1] V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, first public arXiv submission 2015-02-04, arXiv:1502.01255 (https://arxiv.org/abs/1502.01255).

[2] L. Kluge, *Combinatorial refinement on circulant graphs*, first public arXiv submission 2022-04-03, arXiv:2204.01054 (https://arxiv.org/abs/2204.01054), especially Section 4.2 and Theorem 4.
