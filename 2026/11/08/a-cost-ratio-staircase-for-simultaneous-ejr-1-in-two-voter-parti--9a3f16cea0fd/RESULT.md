# A cost-ratio staircase for simultaneous EJR-1 in two-voter participatory budgeting

## Finding

Fix an integer \(k\ge 3\) and real \(c>0\). There are two voters and \(2k+2\) distinct projects: two shared projects, each costing \(c\) and approved by both voters, and \(k\) private projects of cost \(1\) approved only by each respective voter. The total budget is \(2c\). An outcome is any subset of projects with total cost at most \(2c\), without any additional exhaustiveness requirement. Let \(N_k(c)\) denote the number of outcomes that satisfy extended justified representation up to one project (EJR-1) **simultaneously** for cost-based and cardinality-based additive satisfaction.

If \(0<c<3\), at least one simultaneous outcome exists: fund both shared projects. If \(c\ge3\), put \(m=\lfloor c\rfloor\). The **complete exact census** is

\[
N_k(c)=
\begin{cases}
2k^2,&2k-2\le c<2k-1,\\
2k(k+2),&2k-1\le c<2k,\\
2(k+1)^2,&c\ge2k,\\
2\binom{k}{m}\binom{k}{m+1},&3\le m\le k-1\text{ and }m+\tfrac12\le c<m+1,\\
0,&\text{otherwise, for }c\ge3.
\end{cases}
\]

The cases are mutually exclusive. More precisely, in the half-integer windows all simultaneous outcomes choose **no** shared project and choose \(m\) private projects on one side and \(m+1\) on the other. In the high-cost regime \(c\ge2k-2\), all simultaneous outcomes choose **exactly one** shared project and at least \(k-1\) private projects from each side. All the listed selections are indeed simultaneous outcomes.

For \(k=1,2\), both shared projects always form a simultaneous outcome for every \(c>0\); the displayed count formula is asserted only for \(k\ge3,c\ge3\). Within the specified family with positive **integer** shared-project costs, the first incompatible parameter is \(k=c=3\), giving eight projects; this is not a claim of global minimality over all approval-budgeting instances.

For example, when \(k=4\), \(N_4(7/2)=8\), \(N_4(4)=0\), and \(N_4(6)=32\). Hence compatibility may vanish and reappear as the shared-project cost increases.

## Assumptions and scope

An approval-based budgeting instance has projects \(P\), positive costs \(d(p)\), budget \(b\), approval sets \(A_i\), and additive satisfaction functions \(\mu^\#(X)=|X|\) and \(\mu^d(X)=\sum_{p\in X}d(p)\). Voter \(i\)'s satisfaction in outcome \(W\) is \(\mu(W\cap A_i)\). A nonempty group \(S\) is \(T\)-cohesive when \(T\subseteq\bigcap_{i\in S}A_i\) and \(d(T)\le |S|b/2\). We use the EJR-1 definition of Brill et al.: for every such \(S,T\), either \(T\subseteq W\), or there are \(i\in S\) and \(p\in P\setminus W\) for which \(\mu_i(W\cup\{p\})>\mu(T)\). The two satisfaction functions are checked independently against this same requirement. Missing-project choices can lie outside \(T\), as permitted by the stated EJR-1 definition.

The count is over subsets of **labeled** projects, not over voter symmetry classes. Real costs are permitted; only the number \(k\) of private projects is integral. When \(k\le2\), only existence, not counting, is asserted.

## Proof

Let \(s\in\{0,1,2\}\) be the number of selected shared projects and let \(x_1,x_2\in\{0,1,\ldots,k\}\) count the selected private projects in the respective groups. Feasibility is equivalent to

\[sc+x_1+x_2\le2c.\]

For \(k\ge3,c\ge3\), set \(m=\lfloor c\rfloor\) and \(L=\min\{k,m\}\ge3\). A singleton voter has budget entitlement \(c\) and can afford a set of \(L\) private unit projects. If \(s+x_i<L\), this cohesive set cannot be contained in \(W\), and adding one unselected project raises the voter's cardinality satisfaction by at most one, never **strictly above** \(L\). Thus cardinality EJR-1 entails

\[s+x_i\ge L\qquad(i=1,2).\tag{1}\]

Conversely, (1) implies cardinality EJR-1: any singleton-cohesive set is either a set of at most \(L\) private projects or one shared project, and the shared two-voter group only has subsets of the two shared projects. If a cohesive set is not already selected, a missing member of that set raises an approved voter's cardinality score strictly beyond its size, because each voter's current cardinality score is at least \(L\ge3\). Hence (1) is an exact cardinality criterion.

When \(s=2\), the budget leaves no room for private projects, and the cardinality score of each voter is two, contradicting (1). When \(s=1\), criterion (1) says \(x_1,x_2\ge L-1\). For these choices the cost-based EJR-1 condition holds automatically: every singleton-cohesive set costs at most \(c\), while each voter's funded approved-project cost is \(c+x_i\ge c+2\); the largest common-group cohesive set is the pair of shared projects, of cost \(2c\), and either voter can add the unselected shared project to obtain cost satisfaction \(2c+x_i>2c\). Therefore, in this case simultaneous satisfaction is equivalent to

\[x_1,x_2\ge L-1,\qquad x_1+x_2\le c.\tag{2}\]

If \(k>m\), then \(L=m\), and \(2(L-1)=2m-2\ge m+1>c\) because \(m\ge3\); thus (2) is impossible. If \(k\le m\), condition (2) is feasible exactly for \(c\ge2(k-1)\), which already implies \(c\ge k\). In that regime \(x_i\in\{k-1,k\}\). For each of the two choices of the shared project, selecting the private subsets gives \(k^2\) configurations at total private count \(2k-2\), another \(2k\) at \(2k-1\), and one at \(2k\), yielding the first three branches of the displayed census.

When \(s=0\), the cardinality constraint requires \(x_i\ge L\). Applying cost-based EJR-1 to the two-voter group and the cohesive set of both shared projects (total cost \(2c\)), both of which are missing, requires

\[\max\{x_1,x_2\}+c>2c,\qquad\text{i.e. }\max\{x_1,x_2\}>c.\tag{3}\]

This is also sufficient for cost-based EJR-1: the unselected shared project can be added for every singleton-cohesive set, giving cost satisfaction \(x_i+c>c\), and for the common group a voter satisfying (3) can add an unselected shared project and exceed \(2c\). If \(k\le m\), (3) cannot hold. If \(k>m\), then \(L=m\), \(x_i\ge m\), and (3) requires at least one \(x_i\ge m+1\). Writing \(c=m+\delta\) with \(0\le\delta<1\), feasibility then forces

\[x_1+x_2\ge2m+1,\qquad x_1+x_2\le2m+2\delta,\]

which holds precisely when \(\delta\ge1/2\). The integer sum must be exactly \(2m+1\), so \((x_1,x_2)\) is either \((m,m+1)\) or \((m+1,m)\). The number of labeled selections is therefore \(2\binom{k}{m}\binom{k}{m+1}\), proving the fourth branch and exhaustiveness of the fifth.

Finally, for \(0<c<3\), selecting both shared projects exhausts the budget and makes the common group's every cohesive set selected. A singleton group can afford at most two unit private projects (or one shared project), while the funded outcome provides both shared approvals and cardinality satisfaction two; every missing cohesive set can be improved past its cardinality using one missing approved project, and its cost is at most \(c\) versus the funded cost satisfaction \(2c\). Both EJR-1 properties hold. For \(k\le2\) the same argument works for all \(c>0\), since a singleton can afford at most two private projects. This completes the proof.

## Verification

Run `python3 verify_ejr.py` with Python 3 (standard library only). The verifier separately enumerates every budget-feasible labeled outcome and every cohesive pair \((S,T)\) for all three nonempty voter groups, implementing EJR-1 directly with exact rational arithmetic rather than using the theorem's intermediary inequalities. It tests \(72\) rational parameter cells for \(k=3,4,5\), and additional cells at \(k=6\). Every checked count agrees with the asserted formula, with a positive count below \(c=3\). Examples include \(k=4,c=7/2\) giving eight, \(k=4,c=4\) giving zero, and \(k=4,c=6\) giving 32. These finite checks do not replace the general proof.

## Relationship to prior work

Brill, Forster, Lackner, Maly, and Peters (2023), Proposition 3.6, already prove that cost-based and cardinality-based EJR-1 can be incompatible, with two voters, two shared projects of cost five, and five unit private projects per voter (the \(k=c=5\) instance of the present family). The incompatibility phenomenon and this witness are **not** claimed as new. The present theorem instead resolves the exact dependence on arbitrary real shared-project cost, including repeated fractional-cost compatibility windows, a high-cost recovery threshold, and a complete labeled-outcome census in the nontrivial regime \(c\ge3\). None of these general statements follows from that one witness alone. Peters, Pierczyński, and Skowron (2020/2021) introduce proportional-budgeting EJR and the Method of Equal Shares; Kraiczy and Elkind (2023) study adaptive EJR verification for one approval-based satisfaction measure. These results do not state the present two-measure parameter classification.

## Limitations

The theorem assumes two equally entitled voters, precisely two shared costly projects, two symmetric sets of \(k\) private unit-cost projects, and total budget twice the shared-project cost. It does not classify arbitrary approval profiles, unequal budgets, simultaneous stronger EJR-x, or the number of compatible outcomes for \(0<c<3\). Mathematical priority remains subject to any unindexed equivalent analysis. No independent external audit has been performed.

## References

1. M. Brill, S. Forster, M. Lackner, J. Maly, and J. Peters, *Proportionality in Approval-Based Participatory Budgeting*, arXiv:2302.03672 (first publicly released 2023-02-07), especially Definition 3.5 and Proposition 3.6. https://arxiv.org/abs/2302.03672
2. D. Peters, G. Pierczyński, and P. Skowron, *Proportional Participatory Budgeting with Additive Utilities*, arXiv:2008.13276 (first publicly released 2020-08-30). https://arxiv.org/abs/2008.13276
3. S. Kraiczy and E. Elkind, *An Adaptive and Verifiably Proportional Method for Participatory Budgeting*, arXiv:2310.10215 (first publicly released 2023-10-16). https://arxiv.org/abs/2310.10215
