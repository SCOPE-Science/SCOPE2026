# Linear-time coalition-count optimization with two consecutive approved sizes

## Finding

**Theorem.** For every integer \(n\ge1\), consider \(n\) labeled agents, each of whom approves either exactly one group size \(\{s\}\), or exactly two consecutive sizes \(\{s,s+1\}\), where approved sizes lie in \(\{1,\ldots,n\}\). There is a deterministic algorithm using \(O(n)\) time and \(O(n)\) space on a word-RAM with \(O(\log n)\)-bit arithmetic words that:

1. decides whether a *wonderful partition* (one where every agent approves the size of their group) exists;
2. if so, computes both the **minimum** and the **maximum** attainable number of groups in a wonderful partition; and
3. outputs a labeled wonderful partition attaining each extremum.

The time bound is optimal up to constants for an explicitly listed input and a constructed output. The restriction to consecutive sizes is substantive: the more general two-approved-sizes setting with no adjacency restriction is NP-complete [1, Appendix B; 2, Theorem 4]. The statement makes no claim about the set of *intermediate* attainable group counts.

## Assumptions and scope

Agents are distinct, groups have no graph, geographic or other composition restrictions, groups are nonempty, and an agent's preference depends **only** on the cardinality of their group. There are no exclusions. All interval endpoints are supplied as integers between \(1\) and \(n\). Each input approval interval has width at most one, in the precise sense \(r_i-\ell_i\in\{0,1\}\).

For each group size \(s\), let \(a_s\) be the number of agents accepting only size \(s\), and let \(b_s\) be the number accepting sizes \(s\) and \(s+1\). Thus \(b_n=0\) and \(\sum_{s=1}^n(a_s+b_s)=n\). A *wonderful partition* partitions the agents into nonempty groups and satisfies \(|\pi(i)|\in[\ell_i,r_i]\) for each agent.

## Proof

**1. Exact integer-flow equivalence.** For each \(s\) let \(t_s\) denote the number of the \(b_s\) flexible agents who are assigned size \(s+1\). Put \(t_0=t_n=0\). The number assigned to groups of size \(s\) must be

\[
N_s=a_s+b_s-t_s+t_{s-1}.
\]

It can be divided into size-\(s\) groups if and only if

\[
0\le t_s\le b_s,\qquad
N_s\equiv0\pmod s\quad(s=1,\ldots,n).

\]

Necessity follows by counting assignments. Conversely, choose arbitrary labeled flexible agents to forward according to the integers \(t_s\). By (1), the size-\(s\) assigned agents can be split into exactly \(g_s=N_s/s\) groups of size \(s\). Every member accepts that size. Nonnegativity of each \(N_s\) follows from \(0\le t_s\le b_s\) and nonnegative \(a_s,t_{s-1}\). Hence (1) is **equivalent**, not merely necessary, to existence of a wonderful partition. The total group count is exactly \(\sum_sg_s\).

**2. Exact extremal dynamic program.** Let \(R_s\) be all possible values of \(t_s\) for which constraints (1) can be satisfied through size \(s\). For reachable \(t\) define \(m_s(t)\) and \(M_s(t)\) as the minimum and maximum number of already completed groups of sizes at most \(s\). Initially \(R_0=\{0\}\) and \(m_0(0)=M_0(0)=0\). The transition from \(y=t_{s-1}\) to \(t=t_s\) is legal exactly when

\[
y\equiv t-a_s-b_s\pmod s.\]

For each legal transition add \((a_s+b_s-t+y)/s\) completed groups. Therefore

\[
 m_s(t)=\min_{\substack{y\in R_{s-1}\\y\equiv t-a_s-b_s\ (\mathrm{mod}\ s)}}
 \left(m_{s-1}(y)+\frac{a_s+b_s-t+y}{s}\right),
\]

with an analogous maximum formula for \(M_s(t)\); a state is unreachable if its candidate set is empty. This recurrence is exact by induction on \(s\), using the equivalence in Step 1 and the fact that only the integer \(t_{s-1}\) connects consecutive stages. The answer is unreachable if \(0\notin R_n\); otherwise the optimum group counts are \(m_n(0)\) and \(M_n(0)\).

**3. Linear-time residue compression.** For a fixed next state \(t\), all eligible predecessors lie in one residue class modulo \(s\). Their comparison for the minimum is exactly the comparison of the integers

\[
s\,m_{s-1}(y)+y,\]

and for the maximum of \(s\,M_{s-1}(y)+y\); the term \(a_s+b_s-t\) does not depend on \(y\). Scan the reachable predecessors once and retain the minimum and maximum representative for each observed residue modulo \(s\). Then scan the \(b_s+1\) possible current values, consulting only one representative per residue. A length-\(n+1\) timestamp array avoids clearing a length-\(s\) table between stages. As \(|R_s|\le b_s+1\), the total work is bounded by

\[
 O\!\left(\sum_{s=1}^n (|R_{s-1}|+b_s+1)\right)
 =O\!\left(n+\sum_{s=1}^n b_s\right)=O(n).
\]

All integer scores have magnitude at most \(O(n^2)\), so a constant number of ordinary \(O(\log n)\)-bit RAM words suffices for each operation. Storing an optimizing predecessor for each reachable state costs \(O(n)\) total space. Reverse traversal reconstructs both optimal vectors \((t_s)\), and distributing labeled agents by their accepted sizes and dividing size buckets into equal groups takes \(O(n)\) more time and space. This completes the proof.

**Small instance.** Four agents with approved-size intervals \([1,2],[2,3],[2,2],[1,2]\) have a wonderful two-group partition \(\{\{1,4\},\{2,3\}\}\), and a wonderful three-group partition \(\{\{1\},\{4\},\{2,3\}\}\). Both extrema are computed by the algorithm; labels here are one-based.

## Verification

The standalone `verify.py` implements the residue-compressed two-extrema algorithm, constructs both labeled witnesses, and compares results to an independent exhaustive set-partition enumerator for all \(2536\) admissible profiles with \(n\le4\), as well as \(5000\) seeded profiles with \(5\le n\le8\). It also compares against independent enumeration of flexible-agent split counts on \(1250\) seeded instances for sizes \(9,10,11,12,15\). These tests passed. They corroborate but do not replace the all-\(n\) proof above. Execute `python verify.py` using Python's standard library.

## Relationship to prior work

Constantinescu, Lenzner, Reiffenhäuser, Schmand and Varricchio [1] prove an \(O(n^5)\) wonderful-partition algorithm for arbitrary interval approvals. Their model and Appendix B also explain the equivalence of general two-size approvals to a modular-indegree graph orientation problem. The present size-adjacent class corresponds to a path of size labels (with parallel edges), and its single one-step carry admits a strictly linear-time computation of **both extremal group counts and witnesses**. The general algorithm solves feasibility for this subclass but does not imply the claimed linear complexity bound. Darmann et al. [2] establish NP-completeness when two allowed sizes need not be consecutive; that hardness is not asserted for the present subclass.

## Limitations

This theorem does not solve more general intervals of width at least two, arbitrary disconnected two-size approval sets, additional social-network constraints, weighted group preferences, enumeration of all wonderful partitions, or whether every intermediate group count is achievable. The \(O(n)\) bound assumes word-RAM arithmetic on input-sized integers, rather than a bit-operation cost model. An equivalent linear-time result under modular graph-orientation or consecutive-choice terminology could exist outside the literature identified below; priority is not independently adjudicated.

## References

1. A. Constantinescu, P. Lenzner, R. Reiffenhäuser, D. Schmand, G. Varricchio, *Solving Woeginger's Hiking Problem: Wonderful Partitions in Anonymous Hedonic Games*, arXiv:2311.02067v1 (first posted 2023-11-03), https://arxiv.org/abs/2311.02067 . In particular Section 1.3, Theorem 2.5 and Appendix B.
2. A. Darmann, E. Elkind, S. Kurz, J. Lang, J. Schauer, G. Woeginger, *Group activity selection problem with approval preferences*, International Journal of Game Theory 47 (2018), 767–796, first online 2017-10-14, https://doi.org/10.1007/s00182-017-0596-4 . In particular Theorem 4.
