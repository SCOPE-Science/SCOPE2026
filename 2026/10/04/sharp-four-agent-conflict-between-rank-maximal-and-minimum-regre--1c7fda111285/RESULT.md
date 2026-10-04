# Sharp four-agent conflict between rank-maximal and minimum-regret stable roommates
## Finding
Consider the classical Stable Roommates problem with complete strict preferences. For a stable matching \(N\), write its **profile**
\[
p(N)=(p_1(N),p_2(N),\ldots),
\]
where \(p_k(N)\) is the number of agents assigned their \(k\)-th choice. A stable matching is **rank-maximal** when its profile is lexicographically maximal among all stable matchings.

The **regret** of \(N\) is
\[
r(N)=\max_i \operatorname{rank}_i(N(i)),
\]
and a stable matching is **minimum-regret** when it minimizes \(r(N)\).

Let \(R(I)\) and \(M(I)\) denote the complete sets of rank-maximal and minimum-regret stable matchings of an instance \(I\).

For two agents there is only one possible complete strict profile and one matching, so
\[
R(I)=M(I).
\]

For four agents there are
\[
6^4=1296
\]
labeled complete strict profiles. Their exact classification is
\[
\begin{array}{c|r}
\text{relation} & \text{profiles}\\ \hline
R(I)=M(I) & 1176\\
R(I)\subsetneq M(I) & 48\\
R(I)\cap M(I)=\varnothing & 24\\
\text{no stable matching} & 48
\end{array}
\]
and there are no profiles with
\[
M(I)\subsetneq R(I)
\]
or with nonempty nonnested overlap.

Thus four agents are the smallest Stable Roommates market in which rank-maximal and minimum-regret fairness can force incompatible stable choices. Unconditionally the disjoint-conflict incidence is
\[
\frac{24}{1296}=\frac1{54},
\]
and conditional on solvability it is
\[
\frac{24}{1248}=\frac1{52}.
\]

The \(72\) solvable disagreement profiles split into exactly three full orbits under simultaneous relabeling of the four agents. Each orbit has size \(24\): two satisfy \(R(I)\subsetneq M(I)\), and one has disjoint optimum sets.

A canonical representative of the disjoint orbit is
\[
\begin{aligned}
1&:2\succ3\succ4,\\
2&:3\succ4\succ1,\\
3&:1\succ4\succ2,\\
4&:3\succ2\succ1.
\end{aligned}
\]
It has exactly two stable matchings:
\[
N_R=\{\{1,2\},\{3,4\}\},
\qquad
N_M=\{\{1,3\},\{2,4\}\}.
\]
Their agent-rank vectors are respectively
\[
(1,3,2,1)
\quad\text{and}\quad
(2,2,1,2).
\]
Hence
\[
p(N_R)=(2,1,1),
\qquad
p(N_M)=(1,3,0).
\]
Therefore \(N_R\) is uniquely rank-maximal, because it gives one additional first choice, whereas \(N_M\) is uniquely minimum-regret, because it keeps every agent within rank \(2\):
\[
r(N_R)=3,
\qquad
r(N_M)=2.
\]
Both matchings have the same total partner-rank cost,
\[
1+3+2+1=2+2+1+2=7.
\]
So the first conflict is a clean trade-off between the lexicographic reward for an additional first choice and protection of the worst-off agent, not a difference in total rank welfare.

## Assumptions and scope
There are an even number of agents, every agent ranks all other agents strictly, and a matching is stable when it has no blocking pair.

The complete census concerns \(4\) labeled agents. The two-agent case supplies the sharp lower bound because no odd number of agents admits a perfect roommate matching in the classical formulation.

Rank-maximality is evaluated over stable matchings only and retains all ties. Minimum regret likewise retains every stable matching attaining the minimum worst partner rank.

No statement is made about incomplete lists, ties, stable partitions, or markets with six or more agents.

## Proof
For four labeled agents, each agent has \(3!=6\) possible preference orders, hence there are \(6^4=1296\) profiles. There are exactly three perfect matchings.

For each profile, the verifier checks every perfect matching for stability by testing every unmatched pair for mutual improvement. Two independent implementations are used: one based on precomputed rank maps and one based directly on positions in the preference lists.

The stable-matching count marginal is
\[
1098\text{ profiles with one stable matching},\qquad
150\text{ with two},\qquad
48\text{ with none}.
\]

For every solvable profile, rank-maximality is computed in two independent ways. First, profiles are compared lexicographically. Second, each rank vector is given a steep-base exact integer score with base \(5\); one extra assignment at any rank then outweighs all possible lower-rank contributions.

Minimum regret is also computed twice: directly from the maximum partner rank and independently by increasing the admissible rank threshold until a stable matching exists.

The resulting relation histogram is exactly
\[
1176,\quad48,\quad24,\quad48
\]
for equality, strict rank-maximal containment in the minimum-regret set, disjointness, and unsolvability.

For every solvable disagreement profile, all \(24\) simultaneous agent relabelings are generated. Canonicalization yields exactly three orbits, each of full size \(24\). The unique disjoint orbit has the canonical representative displayed above.

Direct evaluation of its two stable matchings gives rank vectors
\[
(1,3,2,1)
\quad\text{and}\quad
(2,2,1,2),
\]
hence signatures \((2,1,1)\) and \((1,3,0)\), regrets \(3\) and \(2\), and common total cost \(7\). This proves both uniqueness statements and disjointness.

## Verification
The embedded `verify_rankmax_minreg_stable_roommates.py` uses only the Python standard library.

It verifies:
- the two-agent base case;
- all \(1296\) complete strict four-agent profiles;
- all three perfect matchings in every profile;
- equality of two independent stability tests;
- equality of two independent rank-maximal computations;
- equality of two independent minimum-regret computations;
- the stable-count marginal \(1098,150,48\);
- the relation histogram \(1176,48,24,48\);
- the three disagreement orbits of size \(24\);
- the canonical disjoint witness, its two stable matchings, profiles, regrets, and equal total cost.

Run:

`python3 verify_rankmax_minreg_stable_roommates.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Teo and Sethuraman study optimal Stable Roommates matchings by linear programming. Their 2000 paper explicitly defines minimum-regret stable roommates as minimizing the rank of the worst-off assigned agent and contrasts this individual-welfare criterion with egalitarian total welfare.

Abraham, Levavi, Manlove, and O'Malley study a non-bipartite globally-ranked-pairs restriction. They explicitly define rank-maximality by lexicographic maximization of a rank signature and discuss egalitarian and minimum-regret stable roommate matchings in the same optimality framework.

Simola and Manlove later formulate rank-maximal Stable Roommates with Incomplete lists directly in terms of the profile of assigned ranks and also formalize minimum-regret stable matchings. Their paper shows that rank-maximal optimization can be computationally hard even with short lists, while minimum-regret optimization is polynomial-time solvable in the classical model.

These sources establish the two fairness criteria and show that they are genuinely different optimization concepts. The contribution here is the sharp smallest-market conflict and its exact complete four-agent classification. Targeted searches did not locate the \(1176/48/24/48\) table, the three-orbit decomposition, or the unique disjoint orbit described above.

## Limitations
The theorem is a complete finite classification for four agents, not a formula for larger Stable Roommates markets.

The result compares optimum sets, not algorithms or computational complexity. It does not imply that one fairness criterion is normatively preferable to the other.

The exact four-agent table and orbit statement were not located in the inspected literature, but an unindexed exercise, thesis, software table, or supplementary computation could contain an equivalent classification.

## References
1. C.-P. Teo and J. Sethuraman, “On a cutting plane heuristic for the stable roommates problem and its applications,” *European Journal of Operational Research* 123 (2000), 195–205. DOI: 10.1016/S0377-2217(99)00049-1.
2. D. J. Abraham, A. Levavi, D. F. Manlove, and G. O'Malley, “The Stable Roommates Problem With Globally-Ranked Pairs,” *WINE 2007*, pp. 431–444. DOI: 10.1007/978-3-540-77105-0_48.
3. S. Simola and D. Manlove, “Profile-based optimal stable matchings in the Roommates problem,” arXiv:2110.02555, 2021.
