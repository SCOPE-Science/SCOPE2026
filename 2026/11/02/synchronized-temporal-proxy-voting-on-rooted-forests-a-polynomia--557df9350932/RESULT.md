# Synchronized temporal proxy voting on rooted forests: a polynomial welfare rule and a sharp four-voter obstruction

## Finding

**Theorem.** Consider a finite temporal proxy-voting instance of lifetime \(L\geq1\) in which the undirected support of voter-to-voter approvals is a forest and each connected component contains exactly one committed ballot-caster. Every other voter must delegate, and each has at least one approval at the final time \(L\). Require each delegator to choose **one time-stamped approval action** for all ballots passing through that voter, rather than potentially different dates of the same approval for different constituents. The welfare-maximizing, time-conscious and action-synchronized delegation is computable, including its witnessing actions, in \(O(M+nL\log(L+1))\) time and \(O(nL+M)\) space, or infeasibility is detected; here \(n\) counts voters and \(M\) counts time-stamped available approvals. Trust horizons may vary arbitrarily by voter and by date.

This joint feasibility requirement has a sharp local obstruction: four voters suffice for every delegator to have an individually valid time-conscious route to the caster, and to approve someone in the final round, while no action-synchronized joint resolution exists. No such obstruction occurs in an instance with at most three voters and a single caster on a tree.

## Assumptions and scope

Fix a finite undirected tree \(T=(V,E)\) with designated caster \(r\), committed to voting starting at a fixed time \(\sigma\in\{1,\ldots,L\}\), and noncasting voters \(D=V\setminus\{r\}\). Each \(v\in D\) has a finite multiset \(A_v\) of triples \((u,t,w)\), where \(\{u,v\}\in E\), \(1\leq t\leq L\), and \(w\) is a positive integer score; at least one such triple per delegator has \(t=L\). For every \(v\in D\), a trust horizon \(h_v(t)\in\{0,\ldots,t-1\}\) is specified for each \(t\in\{1,\ldots,L\}\). A chosen resolution gives each \(v\) exactly one action \((p_v,t_v,w_v)\in A_v\), and its directed choices must terminate at the caster, without a directed cycle. Whenever \(p_v=u\in D\), require
\[
 t_v-h_v(t_v)\leq t_u\leq t_v.
\]
If \(p_v=r\), the persistent casting decision allows a time-conscious link exactly when \(t_v\geq\sigma\): the caster can then use the valid terminal time \(t_v\). Different children of the caster need not refer to the same time of its persistent casting decision. By contrast, each delegator's dated outgoing action is globally shared across all paths visiting that delegator. The objective is \(\sum_{v\in D}w_v\); failure to assign all delegators is infeasibility, not an allowed partial solution. This is the **action-synchronized** specialization, stated explicitly rather than silently identifying it with all possible interpretations of temporal confluence.

An undirected forest with one caster per component is handled independently on each component; its total optimum is the sum of component optima if every component is feasible. No source of approvals outside the displayed forest is permitted. The input can contain both directed approval orientations of a given undirected edge; they need not be used.

## Proof

**1. Unique direction.** Root the underlying tree at \(r\), with parent \(p(v)\) and children \(C(v)\). If a nonroot voter delegated to a child, the selected directed graph could not reach \(r\): the unique undirected route to \(r\) begins through \(p(v)\), and reversing the initial child edge would require revisiting \(v\). Therefore every feasible resolution uses an offered action toward \(p(v)\), and the only choices remaining are the dates and scores of those parent-directed actions.

**2. Exact subtree recurrence.** Write \(a_v(t)\) for the largest score of a parent-directed action of voter \(v\) available at date \(t\), setting \(a_v(t)=-\infty\) if absent. For each nonroot vertex and time \(t\), let \(F_v(t)\) be the maximum score from its entire rooted subtree, conditional on choosing \(v\)'s unique outgoing action at time \(t\), with \(-\infty\) for an impossible condition. A child \(c\) can be attached to a parent action at time \(t\) precisely when the child chooses some date \(s\) satisfying \(s-h_c(s)\leq t\leq s\). Define
\[
H_c(t)=\max_{\substack{1\leq s\leq L\\ s-h_c(s)\leq t\leq s}} F_c(s),
\qquad
F_v(t)=a_v(t)+\sum_{c\in C(v)}H_c(t).
\]
The maximum over the empty set and sums involving \(-\infty\) are \(-\infty\). At a leaf, the sum is zero. Conditional independence follows from the absence of edges between different child subtrees and from the single dated action at their common parent. Induction on subtree height proves the recurrence is both an upper bound for every admissible assignment and is attainable whenever finite.

**3. Persistent casting terminal.** The caster does not need to choose a new dated delegation. For each immediate child \(c\) an action at time \(s\geq\sigma\) can be linked to the caster by assigning the terminal casting edge the permissible time \(s\). Hence the exact optimum is
\[
\operatorname{OPT}(T)=\sum_{c\in C(r)}\max_{\sigma\leq s\leq L}F_c(s).
\]
If any summand is \(-\infty\), there is no solution. Keeping one attaining argument in every maximum reconstructs every dated approval action. If \(T\) has only the caster, the empty sum yields welfare zero.

**4. Running time.** For each child \(c\), every finite state \(F_c(s)\) contributes the interval \([s-h_c(s),s]\) with weight \(F_c(s)\). All values \(H_c(t)\) are interval-stabbing maxima. Bucket the intervals by their integer left endpoint. Sweep \(t=1,\ldots,L\), inserting newly active intervals into a max-heap and expiring those with right endpoint below \(t\). The top live heap entry yields the maximum and its attaining date. This takes \(O(L\log(L+1))\) time and \(O(L)\) working memory for each child, plus \(O(L)\) time per vertex to combine its children and \(O(M)\) to aggregate offers. The total is \(O(M+nL\log(L+1))\) time and \(O(nL+M)\) space including backpointers and the input. The score arithmetic is exact over integers; bounds count arithmetic operations, not integer-bit costs.

**5. Sharp four-voter obstruction.** Let the voter tree have edges \(av,bv,vr\), with \(r\) casting from round \(1\), horizon \(L=3\), every delegator's horizon identically zero, and all offered scores one. The complete approvals are
\[
 A_a=\{(v,1,1),(v,3,1)\},\quad
 A_b=\{(v,2,1),(v,3,1)\},\quad
 A_v=\{(r,1,1),(r,2,1),(a,3,1)\}.
\]
Each delegator approves someone at round \(3\). Alone, \(a\) can choose its time-\(1\) action followed by \(v\)'s time-\(1\) action; \(b\) similarly uses time \(2\); \(v\) can itself use either time \(1\) or \(2\). Jointly, both \(a\) and \(b\) must delegate toward \(v\). As their horizons vanish, their only viable parent-directed actions demand \(t_v=1\) and \(t_v=2\) respectively. The time-\(3\) action of \(v\) points toward \(a\), which cannot reach the caster without a cycle. Consequently no joint solution exists. For at most three voters, the rooted tree is either a star, in which the separate leaf routes are independently compatible with the persistent caster, or a path with the caster at an endpoint, in which the far leaf's feasible route already supplies a compatible action for the unique intermediate voter. This establishes minimality.

## Verification

The standalone `VERIFY.py` implements the interval-sweep dynamic program, constructive recovery, and a separately written brute-force enumeration over **all** directed offered actions, including the wrong-way ones, with independent terminal casting times. It checks the four-voter witness and 3,900 seeded instances with sizes \(2\leq n\leq6\), lifetimes \(2\leq L\leq4\), arbitrarily variable trust horizons, nonuniform scores and possible final-round backward approvals. Of these, 2,510 admit a synchronized solution. For every test it checks exact agreement between optimal objective values and independently verifies the recovered witness. Run `python3 VERIFY.py` with Python 3 standard library only. These finite checks supplement, and do not replace, the general inductive proof.

## Relationship to prior work

Markakis and Papasotiropoulos (2023, arXiv:2307.12898) define time-conscious paths, temporal confluence and welfare maximization; they prove general hardness and present algorithms for relaxed requirements or retrospective trust, but not this one-caster-forest, arbitrary-horizon, action-synchronized optimization and its sharp feasibility obstruction. Escoffier, Gilbert and Pass-Lanneau (2019, arXiv:1904.05775), Section 5, use tree dynamic programming for equilibria of **static** guru-preference delegation games, not time-stamped shared actions. Casteigts, Himmel, Molter and Zschoche (2019, arXiv:1909.06437), Section 5, study one temporal path with waiting limits and forest supports, not the joint welfare of multiple synchronized paths. Ge et al. (2023, DOI:10.1155/2023/1974161), Sections 2–3, optimize a group-Steiner objective on directed temporal networks under different edge travel-time conditions rather than the displayed per-voter trust-horizon recurrence. The familiar general principle of dynamic programming on trees is not claimed as new; the exact constrained objective, sharp obstruction, and near-input-time implementation are the delimited contribution.

## Limitations

The theorem does not address arbitrary networks with cycles, multiple casting voters in one connected component, abstaining voters, or original temporal-path semantics if the same delegator is allowed to take different dated actions for different ballots. Restricting each voter to one dated action matters for the obstruction and recurrence. A separately selected persistent casting timestamp is **not** required. Priority is assessed against the specified inspected literature, not guaranteed universally; broader unpublished or unindexed results could subsume the observation. The random experiments do not establish asymptotic properties beyond the proof.

## References

1. E. Markakis and G. Papasotiropoulos, *As Time Goes By: Adding a Temporal Dimension Towards Resolving Delegations in Liquid Democracy*, arXiv:2307.12898, first posted July 24, 2023. https://arxiv.org/abs/2307.12898
2. B. Escoffier, H. Gilbert, and A. Pass-Lanneau, *The Convergence of Iterative Delegations in Liquid Democracy in a Social Network*, arXiv:1904.05775, first posted April 10, 2019. https://arxiv.org/html/1904.05775v2
3. A. Casteigts, A.-S. Himmel, H. Molter, and P. Zschoche, *The Computational Complexity of Finding Temporal Paths under Waiting Time Constraints*, arXiv:1909.06437, first posted September 13, 2019. https://arxiv.org/html/1909.06437v5
4. Y. Ge et al., *An Efficient Dynamic Programming Algorithm for Finding Group Steiner Trees in Temporal Graphs*, International Journal of Intelligent Systems (2023), DOI:10.1155/2023/1974161. https://onlinelibrary.wiley.com/doi/10.1155/2023/1974161
