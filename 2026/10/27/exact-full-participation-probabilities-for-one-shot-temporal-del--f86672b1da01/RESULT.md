# Exact full-participation probabilities for one-shot temporal delegation cycles

## Finding

Fix an integer \(n\ge 3\), a cycle \(C_n\) with one distinguished casting voter \(r\), and one independent approval time on each undirected cycle edge. Each noncasting cycle voter may delegate to either neighbor at that edge's unique approval time, provided that the resulting delegation is confluent and every chain reaches \(r\) at weakly decreasing times. Assume all \(n\) edge times are distinct and that their relative order is uniformly random. Let \(Z_n\) denote the number of valid full-participation delegation trees for the given order.

**Theorem.** For every integer \(n\ge 3\), \(Z_n\in\{0,1,2,3\}\). Its exact distribution, expressed as counts among the \(n!\) possible strict time orders, is

\[
\begin{aligned}
n!\Pr(Z_n=0)&=n!-(n-2)2^{n-1}-2,\\
n!\Pr(Z_n=1)&=(n-3)2^{n-1}+2,\\
n!\Pr(Z_n=2)&=2,\\
n!\Pr(Z_n=3)&=2^{n-1}-2.
\end{aligned}
\]

Consequently, the chance that all voters can be represented by the casting voter is exactly
\[
\Pr(Z_n>0)=\frac{(n-2)2^{n-1}+2}{n!}.
\]
Although the underlying static cycle has exactly \(n\) spanning trees, random one-shot approval times yield at most three time-conscious ones, and full participation becomes superexponentially rare as \(n\) increases. The three-tree count is attained precisely when the edge-time list is strictly unimodal with its peak away from the endpoints. Exactly two trees occur only for the two strictly monotone time orders.

## Assumptions and scope

Label vertices \(0,1,\ldots,n-1\) cyclically, with \(r=0\). Let \(e_i=\{i-1,i\}\) for \(1\le i<n\), and \(e_n=\{n-1,0\}\). Each edge \(e_i\) has a unique time \(t_i\); the \(t_i\) form a permutation of \(1,\ldots,n\). An approval from a nonroot voter across \(e_i\) may occur only at \(t_i\). Each nonroot voter chooses exactly one outgoing neighbor, and every resulting directed path must reach \(r\) without repeated vertices. Reading the chosen times from the delegating voter toward \(r\), they must be nonincreasing; distinctness makes these inequalities strict. The casting voter's terminal action is available at time \(1\), and retrospective trust permits every earlier or simultaneous downstream decision.

These conditions can be embedded literally in a temporal liquid-democracy election with \(n+1\) voters and \(n+1\) rounds: in addition to the \(n\) cycle voters, introduce an abstaining voter \(a\); at the last round each cycle noncasting voter approves only \(a\), making each a delegating voter under the final-round participation rule. The approvals to \(a\) cannot lie on a valid path to \(r\). The casting voter commits at round \(1\), and all noncasters use maximal retrospective trust \(\delta_v^t=t-1\). Thus exactly the cycle edges can occur in a full-participation, confluent and time-conscious outcome. No financial utilities, preferences among equally timed edges, or other constraints are assumed.

## Proof

Every connected spanning subgraph of a cycle that is a tree deletes exactly one edge. After deleting \(e_j\), there is a unique orientation of each retained edge toward \(r\). The arm using \(e_1,\ldots,e_{j-1}\) is time-conscious precisely when
\[
t_1<t_2<\cdots<t_{j-1},
\]
and the other arm using \(e_{j+1},\ldots,e_n\) is time-conscious precisely when
\[
t_{j+1}>t_{j+2}>\cdots>t_n.
\]
An empty or singleton block imposes no inequality. Denote this event by \(A_j\), so \(Z_n=\sum_{j=1}^{n}\mathbf 1_{A_j}\).

For fixed \(j\), the left and right blocks have lengths \(j-1\) and \(n-j\). Their internal orders are prescribed, and the omitted value is unconstrained. Hence
\[
|A_j|=\frac{n!}{(j-1)!(n-j)!}=n\binom{n-1}{j-1}.
\]
Summing over \(j\), the total incidence of individual events is \(F_1=n2^{n-1}\).

Suppose \(j<k\). If \(k\ge j+3\), event \(A_j\) forces \(t_{j+1}>t_{j+2}\), while \(A_k\) forces \(t_{j+1}<t_{j+2}\); their intersection is empty. Thus at most three deletions can be valid, and any simultaneous valid deletions must be consecutive.

For adjacent cuts \(j,j+1\), the entire first block of length \(j\) must increase and the remaining block of length \(n-j\) must decrease. We obtain
\[
|A_j\cap A_{j+1}|=\binom{n}{j}.
\]
For distance-two cuts \(j,j+2\), the time list must increase strictly through \(t_{j+1}\) and decrease strictly afterward. In particular its global maximum is at position \(j+1\), and
\[
|A_j\cap A_{j+2}|=\binom{n-1}{j}.
\]
This distance-two intersection automatically satisfies \(A_{j+1}\), so it is exactly the triple intersection \(A_j\cap A_{j+1}\cap A_{j+2}\). There are no other nonempty pair or triple intersections and no fourfold intersection.

Therefore the total pair-incidence and triple-incidence are
\[
F_2=\sum_{j=1}^{n-1}\binom n j+\sum_{j=1}^{n-2}\binom{n-1}{j}=3\cdot2^{n-1}-4,
\quad
F_3=\sum_{j=1}^{n-2}\binom{n-1}{j}=2^{n-1}-2.
\]
Write \(B_k\) for the number of orders with exactly \(k\) valid cuts. Since \(Z_n\le3\), elementary counting of incidences gives
\[
B_3=F_3,\qquad B_2=F_2-3F_3=2,\qquad B_1=F_1-2B_2-3B_3=(n-3)2^{n-1}+2,
\]
and \(B_0=n!-B_1-B_2-B_3\). This is the claimed distribution. The \(B_3\) family is the strict unimodal family with an interior maximum; both strictly increasing and strictly decreasing orders each have two valid cuts, exhausting \(B_2=2\). The claimed probability follows by dividing \(B_1+B_2+B_3\) by \(n!\). Finally, \(n2^{n-1}/n!\to0\) faster than any geometric rate by the factorial ratio test. \(\square\)

## Verification

The standalone Python 3 file `check_cycle.py` constructs every possible deleted-edge orientation and traces the actual delegation paths to the root, checking every time inequality. It enumerates all \(n!\) edge-time orders for every \(3\le n\le8\), using no formula-specific shortcuts in the path test, and compares its exact histograms to the theorem. The cases \(n=4\) and \(n=6\) yield histograms \((6,10,2,6)\) and \((590,98,2,30)\), indexed by \(Z_n=0,1,2,3\). The finite test corroborates but is not used to prove the all-\(n\) theorem.

## Relationship to prior work

Markakis and Papasotiropoulos (2023, arXiv:2307.12898) formalize time-conscious and confluent delegations, including retrospective trust; their primary results concern feasibility and optimization complexity, not a random strict-order cycle census. Casteigts, Raskin, Renken, and Zamaraev (arXiv:2011.03738) study random edge-time permutations in temporal graphs with Erdős–Rényi footprints and connectivity thresholds, rather than a fixed cycle's exact rooted delegation-tree distribution. Casteigts and Corsini (arXiv:2312.06260) study temporal connectivity-preserving spanning trees and bidirectional structures, which require different reachability quantifiers. Enright, Meeks, and Molter (arXiv:2202.12055) count individual temporal paths; they do not give the present simultaneous arborescence distribution. A prior static cycle delegation enumeration with at least two casting voters concerns random valid outgoing edge choices with no temporal constraints and does not imply this fixed-one-guru random-time count. Standard counts of unimodal permutations underlie one part of the proof but do not alone establish the four-way tree-count distribution.

## Limitations

Only one casting cycle voter, one approval time per cycle edge, strict distinct times, full retrospective trust and confluence are considered. The stated distribution is over relative timestamp orders, not uniform random choices of final delegation trees. Repeated approvals, tied times, multiple casting voters, independent edge-presence failures, alternative horizon constraints and other network topologies are not classified. The explicit final-round abstainer embedding is an exact specialization of the cited temporal election model, but no claim is made about empirical voting rates. A literature search cannot exclude equivalent formulations in unindexed work on edge-ordered graphs or permutation statistics. The result is not independently certified.

## References

1. E. Markakis and G. Papasotiropoulos, *As Time Goes By: Adding a Temporal Dimension Towards Resolving Delegations in Liquid Democracy*, arXiv:2307.12898, first available 2023-07-24. https://arxiv.org/abs/2307.12898
2. A. Casteigts, M. Raskin, M. Renken, V. Zamaraev, *Sharp Thresholds in Random Simple Temporal Graphs*, arXiv:2011.03738, 2020. https://arxiv.org/html/2011.03738v4
3. A. Casteigts and T. Corsini, *In Search of the Lost Tree: Hardness and Relaxation of Spanning Trees in Temporal Graphs*, arXiv:2312.06260, 2023. https://arxiv.org/abs/2312.06260
4. J. Enright, K. Meeks, H. Molter, *Counting Temporal Paths*, arXiv:2202.12055, 2022. https://arxiv.org/abs/2202.12055
5. E. C. Akrida and P. G. Spirakis, *Moving in Temporal Graphs with Very Sparse Random Availability of Edges*, arXiv:1310.7898, 2013. https://arxiv.org/html/1310.7898v1
