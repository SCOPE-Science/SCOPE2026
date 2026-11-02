# Short-distance sensor slides on circular ladders: complete mobility types and square counts

## Finding
For every integer \(n\ge 8\), let \(P_n=C_n\square K_2\) be the circular ladder with two rails and \(n\) columns. The *power-domination* process starts by marking selected vertices and their neighbors, then repeatedly marks the unique unmarked neighbor of any marked vertex when one exists. A minimum power-dominating set has size two. Define \(\mathcal R_n\) to have those minimum sets as vertices, joining two sets when exactly one selected vertex is slid across an edge of \(P_n\) and the new pair remains power-dominating.

Then \(\mathcal R_n\) is **connected and bipartite**, has \(11n\) vertices and \(24n\) edges, and has the full local degree enumerator
\[
D_n(t)=2nt^2+5nt^4+4nt^6.
\]
It has exactly **\(19n\) distinct unoriented four-cycles**. Because the reconfiguration graph is bipartite, every four-cycle is induced. Even for odd \(n\), when the original circular ladder is not bipartite, the reconfiguration graph remains bipartite. These are statements about *local sensor slides*, not the much less constrained token-jumping operation.

The complete mobility classification is as follows. Put \(S_d\) for a pair on one rail at cyclic column separation \(d\), and \(O_d\) for a pair on opposite rails at cyclic separation \(d\). There are exactly six possible types.

| Type | States | Slide degree | Four-cycles through each state | Types of neighbors (with multiplicities) |
| --- | ---: | ---: | ---: | --- |
| \(S_1\) | \(2n\) | 4 | 8 | \(2S_2+2O_1\) |
| \(S_2\) | \(2n\) | 6 | 7 | \(2S_1+2S_3+2O_2\) |
| \(S_3\) | \(2n\) | 2 | 1 | \(2S_2\) |
| \(O_0\) | \(n\) | 4 | 8 | \(4O_1\) |
| \(O_1\) | \(2n\) | 6 | 12 | \(2O_0+2O_2+2S_1\) |
| \(O_2\) | \(2n\) | 4 | 6 | \(2O_1+2S_2\) |

## Assumptions and scope
Columns are elements of \(\mathbb Z/n\mathbb Z\); the vertex set is \(\{(r,i):r\in\{0,1\},\ i\in\mathbb Z/n\mathbb Z\}\). Two vertices are adjacent if they have the same row and consecutive columns, or the same column and different rows. The cyclic column separation is \(\min\{|i-j|,n-|i-j|\}\) using representatives \(0\le i,j<n\). The graph distance in \(P_n\) equals this separation plus one if the rows differ.

Girish and Somasundaram, Lemma 2 (2024), establish that a pair of vertices power dominates \(GP(n,1)\cong P_n\) precisely when its graph distance is at most three. This is an existing *static* classification, not a contribution of this theorem. A single selected vertex cannot power dominate \(P_n\) for \(n\ge8\): after its closed neighborhood is marked, each marked neighbor has at least two unmarked neighbors, so propagation cannot start. Hence the applicable states are precisely the pairs at distance one, two, or three.

## Proof
**1. Exhaustive state types.** For \(n\ge8\), no unordered same-rail pair at cyclic separation \(d\in\{1,2,3\}\) is duplicated by choosing its opposite oriented gap, so there are \(n\) such pairs on each rail, or \(2n\) of each type \(S_d\). For opposite rails the choices of gap \(0\), \(\pm1\), and \(\pm2\) give \(n,2n,2n\) pairs of types \(O_0,O_1,O_2\). Their sum is \(11n\).

**2. All legal slides.** Let \(N_P(v)\) denote a neighborhood in the original prism, and \(N_R(X)\) the neighbors of a two-vertex configuration. The complete rule, using the earlier distance criterion, is
\[
N_R(\{a,b\})=\big\{\{w,b\}:w\in N_P(a)\setminus\{b\},\ d_P(w,b)\le3\big\}\cup\big\{\{a,w\}:w\in N_P(b)\setminus\{a\},\ d_P(a,w)\le3\big\}.
\]
Applying this expression to representatives \(S_d=\{(0,0),(0,d)\}\) and \(O_d=\{(0,0),(1,d)\}\), with both signs of the gap for the latter when \(d>0\), gives exactly the neighbor-type counts in the table. This is a finite enumeration of at most six candidate moves per representative and is independently reproduced by the attached `verify_symbolic.py`. In particular,
\[
|E(\mathcal R_n)|=\tfrac12(2n\cdot4+2n\cdot6+2n\cdot2+n\cdot4+2n\cdot6+2n\cdot4)=24n.
\]
The table gives the asserted degree polynomial.

**3. Bipartiteness.** In every row of the neighbor-type table, the type \(S_2\) or \(O_1\), corresponding to a base distance of two, is adjacent only to a type with base distance one or three, and conversely. Thus the partition into the \(4n\) distance-two pairs and the \(7n\) distance-one-or-three pairs is a proper bipartition. This holds irrespective of the parity of \(n\).

**4. Connectivity.** A configuration of type \(S_3\) can slide to \(S_2\), then \(S_1\). Every \(O_2\) configuration can slide to \(O_1\), which can slide to \(S_1\); \(O_0\) slides to \(O_1\). Hence every vertex has a path to some \(S_1\) vertex. On a fixed rail, successive \(S_1\) pairs \(\{(r,i),(r,i+1)\}\) and \(\{(r,i+1),(r,i+2)\}\) are joined by the two-slide route through \(\{(r,i),(r,i+2)\}\) of type \(S_2\). This transports the adjacent pair around the complete rail. A pair \(\{(0,i),(0,i+1)\}\) can switch to \(\{(1,i),(1,i+1)\}\) through the valid opposite-rail intermediate \(\{(0,i),(1,i+1)\}\) of type \(O_1\). Therefore the \(S_1\) states, and hence the entire graph, form one connected component.

**5. Four-cycles.** For each state \(X\), the number of unoriented four-cycles containing it is the exact finite expression
\[
q(X)=\sum_{\{Y,Z\}\in\binom{N_R(X)}2}\bigl(|N_R(Y)\cap N_R(Z)|-1\bigr).
\]
Indeed \(X\) itself is a common neighbor of \(Y,Z\); each different common neighbor supplies exactly one four-cycle through \(X\), and each such four-cycle has exactly one unordered pair of the two neighbors of \(X\) that it uses. Evaluate the expression using the explicit neighbor rule from step 2. It gives \(q(S_1),q(S_2),q(S_3),q(O_0),q(O_1),q(O_2)=(8,7,1,8,12,6)\), as shown in the table. The finite check is fully reproducible by `verify_symbolic.py`, which enumerates the six types and this common-neighbor expression without performing the power-domination process.

The local table is uniform for every \(n\ge8\): all allowed pair separations are at most three and each local slide changes a single vertex by one original-graph edge, so the six candidate moves and the distance-three admissibility test are independent of the distant remaining columns. At separation three, moving outward produces forbidden separation four before any wraparound alternative becomes available. The same observation applied to the two consecutive slides defining the common-neighbor intersections prevents any extra local square from appearing at the cyclic seam. In particular, the largest relevant distance-four exclusion is valid also at \(n=8\). This establishes the displayed local counts for the entire infinite range, not just tested lengths.

Each square has four vertices, so summing square incidences gives
\[
4c_4(\mathcal R_n)=2n(8+7+1)+n(8)+2n(12+6)=76n,
\qquad c_4(\mathcal R_n)=19n.
\]

## Verification
Run `python verify_direct.py` and `python verify_symbolic.py` with Python 3.9 or later, no third-party dependencies. The former independently implements the original power-domination propagation, enumerates all one- and two-vertex sets and all physical slides for \(8\le n\le20\), and checks the vertex count, all degrees, connectedness, bipartiteness and squares. The latter directly generates the six permitted pair families, computes the complete neighbor lists, and checks the six-type degree and four-cycle-incidence table for lengths \(8,9,10,11,12,13,14,15,16,17,19,23,31\). Both scripts passed after extraction from the completed record. These finite executions support the exact local calculation; the proof of uniformity and the known static criterion extend the result to all \(n\ge8\).

## Relationship to prior work
The concept of power domination was introduced by Haynes, Hedetniemi, Hedetniemi, and Henning (2002). Xu and Kang (2011) studied power domination in generalized Petersen graphs as an archival structural problem; its accessible abstract concerns optimal cardinality and does not settle adjacent relocation. Girish and Somasundaram (2024), Lemma 2, already establish the precise two-vertex power-domination criterion for prisms. Hence neither the optimum cardinality two nor the count of \(11n\) feasible pairs (which follows immediately from their lemma) is claimed as original here. Bjorkman and coauthors' power-domination reconfiguration work (first arXiv posting 2022; journal publication 2026) develops token addition/removal and token jumping, with an illustrative token-sliding example; its inspected text contains no circular-ladder theorem. The proposed addition is the entire physically adjacent token-sliding *local mobility structure*, connectivity and bipartition, plus the exact four-cycle count \(19n\). The static distance criterion does not itself assert these reconfiguration properties.

## Limitations
The theorem covers only the ordinary prism \(C_n\square K_2\), only optimal two-sensor configurations, only one-edge token slides, and only \(n\ge8\). It does not determine the diameter or all-pairs shortest-path distribution. The four-cycle formula counts unoriented simple cycles, not arbitrary four-step closed walks. No independent scholarly audit is claimed. Literature searched by both ``power domination'' and ``reconfiguration'' terminology may miss a historical equivalent in the language of adjacent token motion or graph configuration spaces.

## References
1. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi, M. A. Henning. *Domination in Graphs Applied to Electric Power Networks*. SIAM J. Discrete Math. 15 (2002), 519–529. DOI: 10.1137/S0895480100375831. The original full-text imprint records electronic publication on 10 September 2002.
2. L. Girish and K. Somasundaram. *Bound for the k-Fault-Tolerant Power-Domination Number*. Symmetry 16 (2024), 781. DOI: 10.3390/sym16070781; especially Lemma 2, published 21 June 2024.
3. G. Xu and L. Kang. *On the power domination number of the generalized Petersen graphs*. Journal of Combinatorial Optimization 22 (2011), 282–291. DOI: 10.1007/s10878-010-9293-y. The full text was not accessible; the archival connection is based on its abstract.
4. B. Bjorkman et al. *Power Domination Reconfiguration*. La Matematica 5 (2026), article 8. DOI: 10.1007/s44007-025-00187-5; published 13 January 2026. Preprint arXiv:2201.01798.
