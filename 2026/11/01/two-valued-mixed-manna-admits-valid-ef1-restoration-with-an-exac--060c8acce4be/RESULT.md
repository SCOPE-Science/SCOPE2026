# Two-valued mixed manna admits valid EF1 restoration, with an exact unit-magnitude transfer distance

## Finding
For any finite number \(n\ge2\) of agents with the same additive value \(+a\) for each good and \(-b\) for each chore, where \(a,b>0\), every near-EF1 allocation can be restored to EF1 using at most \(m\) valid single-item transfers. The algorithm always transfers an own chore from the sole potentially unhappy agent to a current highest-utility other agent, if such a chore exists; otherwise it transfers a good in the opposite direction. No agent other than the designated one ever becomes EF1-unhappy, and **every** signed EF1-envy deficit of the designated agent toward each other agent is nonincreasing.

If \(a=b=t>0\), the algorithm uses the *minimum possible number* of item transfers, exactly
\[
T_{\min}=\left\lfloor\frac{\sum_{i=1}^{n}(g_i-c_i)}{n}\right\rfloor-(g_1-c_1),
\]
where \(g_i\) and \(c_i\) are the initial goods and chores counts of agent \(i\), and agent \(1\) is the only possibly EF1-unhappy agent. The formula includes the already-EF1 case only when the right-hand side is replaced by zero; the displayed equality is asserted when agent \(1\) is initially EF1-unhappy.

## Assumptions and scope
All items are indivisible and allocated, and all agents have an **identical additive valuation** taking exactly two possible signs and magnitudes: every good has value \(a>0\) and every chore has value \(-b<0\). Goods and chores may both occur; their counts and the real ratio \(a/b\) are arbitrary. There is no connectivity or eligibility constraint on transfers. Number the designated possibly unhappy agent \(1\); all other agents are initially EF1-happy.

For each current allocation, put \(s_i=a g_i-b c_i\) and, for distinct \(i,j\), define
\[
E_{ij}:=s_j-s_i-\max\{a\mathbf1_{g_j>0},\;b\mathbf1_{c_i>0}\}.
\]
This is the signed EF1 shortfall: \(E_{ij}>0\) means agent \(i\) still envies agent \(j\) even after either removing one good from \(j\)'s bundle or removing one chore from \(i\)'s own bundle. If neither operation is available, the maximum is zero. Agents with all \(E_{ij}\le0\) are EF1-happy. A transfer is *valid* when all agents \(2,\ldots,n\) stay EF1-happy and every \(E_{1j}\) is nonincreasing. This extends the signed mixed-manna convention in the cited primary source; it does **not** use the pure-chores convention in which the lone distinguished agent is the one being envied.

## Proof
**Greedy rule.** If every \(E_{1j}\le0\), stop. Otherwise choose \(h\in\{2,\ldots,n\}\) maximizing \(s_h=M\), with an arbitrary fixed tie rule. If \(c_1>0\), transfer one chore from \(1\) to \(h\); if \(c_1=0\), transfer one good from \(h\) to \(1\).

**The chore transfer is available and keeps all other agents happy.** Since agent \(1\) is unhappy, some \(k\ne1\) has \(E_{1k}>0\), hence
\[
s_k-s_1>\max\{a\mathbf1_{g_k>0},b\}\ge b.
\]
Consequently \(s'_1=s_1+b<s_k\le M\). Agent \(h\) changes utility from \(M\) to \(M-b\), receives an own removable chore, and can compare to any bundle by removing this chore, since every other agent has utility at most \(M\), including the changed agent \(1\). Thus \(h\) is EF1-happy.

For a different agent \(j\notin\{1,h\}\), comparisons with all bundles except \(1\) or \(h\) are unchanged, and \(h\)'s utility decreases. If \(c_j>0\), its previous happiness toward \(k\) gives
\[
s_k-s_j\le\max\{a\mathbf1_{g_k>0},b\}<s_k-s_1,
\]
so \(s_j>s_1\) and \(s'_1-s_j<b\); removing one of \(j\)'s own chores resolves any new envy toward \(1\).

If \(c_j=0\), then \(s_j=a g_j\ge0\). When \(g_1=0\), \(s'_1\le0\), so there is no envy. When \(g_1>0\) but \(g_k=0\), the preceding strict inequality gives \(s'_1<s_k\le0\), again no envy. In the remaining case \(g_1,g_k>0\), \(j\)'s original happiness toward \(k\) implies \(s_k-s_j\le a\), whereas \(1\)'s unhappiness toward \(k\) implies \(s_k-s_1>\max\{a,b\}\). Hence
\[
s'_1-s_j<a+b-\max\{a,b\}\le a.
\]
Because \(1\) still has a good, agent \(j\) can remove one good from \(1\)'s bundle to eliminate that envy. Thus all agents other than \(1\) remain happy.

The chore transfer raises \(s_1\) by \(b\), lowers only \(s_h\) by \(b\), and leaves the goods indicators unchanged. For any \(j\), the possible loss in the own-chore-removal threshold of \(E_{1j}\) is at most \(b\). Consequently no \(E_{1j}\) rises, even when \(1\) gives away its final chore.

**The good transfer is available and keeps all other agents happy.** Now \(c_1=0\), hence \(s_1\ge0\). Unhappiness to some \(k\) forces \(g_k>0\) and \(s_k-s_1>a\): if \(g_k=0\), then \(s_k\le0\le s_1\), which is impossible. Thus \(M>s_1+a\) and \(h\) has a good. After moving one good from \(h\) to \(1\),
\[
s'_1=s_1+a<M,\qquad s'_h=M-a>s_1\ge0.
\]
For any bundle of a third agent \(j\), if \(g_j>0\), deleting one of \(j\)'s goods makes its utility at most \(M-a=s'_h\); if \(g_j=0\), then \(s_j\le0<s'_h\). For the new bundle of \(1\), deleting its newly received good leaves utility \(s_1<s'_h\). Thus \(h\) stays happy.

For any other \(j\notin\{1,h\}\), its prior happiness toward \(h\) and \(g_h>0\) imply
\[
M-s_j\le\max\{a,b\mathbf1_{c_j>0}\}.
\]
Since \(s'_1<M\) and agent \(1\) now owns a good, this same remedy establishes \(j\)'s happiness toward \(1\). Its happiness toward \(h\) only improves because \(h\)'s utility falls; all remaining comparisons are unchanged. Finally, \(s_1\) rises by \(a\) and the only affected other utility falls by \(a\). Even if \(h\)'s final good disappears, the corresponding threshold in \(E_{1h}\) can fall by only \(a\), so all \(E_{1j}\) are nonincreasing.

**Termination.** Each step strictly raises \(s_1\). More concretely, chore transfers consume one of \(1\)'s initial chores, and after its chore supply becomes empty it never receives another chore. Each subsequent good transfer moves an as-yet-unmoved good from outside \(1\) into its bundle. The number of steps is thus at most \(c_1^{(0)}+\sum_{j\ne1}g_j^{(0)}\le m\). If still unhappy, one of the two proved branches is available, so stopping must yield EF1.

**Exact shortest distance for equal magnitudes.** Set \(a=b=t\) and \(z_i=s_i/t=g_i-c_i\in\mathbb Z\). For every pair \(i\ne j\), if \(z_j>z_i\), either \(i\) owns a chore or \(j\) owns a good (otherwise \(z_i\ge0\ge z_j\), contradiction). Hence their mixed EF1 comparison is equivalent to \(z_j-z_i\le1\). An allocation is therefore EF1 precisely when all integer scores differ by at most one. The happiness of agents \(2,\ldots,n\) among themselves implies their scores are \(M\) or \(M-1\) for some integer \(M\). Unhappiness of agent \(1\) implies \(z_1\le M-2\), so \(1\) is a minimum-score agent. Every greedy step raises \(z_1\) by one and lowers a maximum other score by one; because \(z_1+1\le M-1\), the distinguished agent remains a minimum-score agent after the step. This invariant repeats until the allocation is EF1. Conservation of \(Z=\sum_i z_i\) means every EF1 allocation consists of scores \(\lfloor Z/n\rfloor\) and \(\lceil Z/n\rceil\); the greedy terminal score of agent \(1\), being a minimum, is \(\lfloor Z/n\rfloor\). Therefore the greedy number of steps is exactly \(\lfloor Z/n\rfloor-z_1^{(0)}\). Any one-item transfer can raise \(z_1\) by at most one, while every EF1 target must give it a score at least \(\lfloor Z/n\rfloor\), so no transfer sequence, even one allowed to pass through non-near-EF1 states, can use fewer steps. This proves sharp optimality.

## Verification
Run the standalone standard-library-only script `python3 verify_restoration.py`. It exhaustively evaluates all near-EF1 count-vector states with \(2\le n\le4\), \(2\le m\le8\), both signs present, and \((a,b)\) in \(\{(1,1),(1,2),(2,1),(2,3),(3,2),(1,5),(5,1)\}\). It checks the exact signed shortfalls, validity of every greedy transition, termination bounds, and the sharp equal-magnitude transfer count. Observed output: `PASS: all finite states tested; near-EF1 cases 8331 total verified transfers 14259 both-direction candidates 608`. This finite exhaustion is a consistency test, not the proof of the general theorem.

For an example requiring both kinds of transfers under the rule, let \((a,b)=(2,1)\) and the three agents initially have count pairs \((g_i,c_i)=(0,1),(3,0),(2,0)\). The utilities begin as \((-1,6,4)\), then become \((0,5,4)\) after sending agent \(1\)'s chore to agent \(2\), then become \((2,3,4)\) after sending one good from agent \(2\) to agent \(1\). The last allocation is EF1.

## Relationship to prior work
Chandramouleeswaran, Nimbhorkar, and Rathi establish valid EF1 restoration separately for monotone all-goods and all-chores settings and exhibit a *mixed-manna obstruction* using heterogeneous item values (arXiv:2410.14421v1, Sections 3–4 and Appendix B.1, and arXiv:2410.14421v4, Section 4.3 and Table 1). The revised Table 1 explicitly leaves the general mixed-manna feasibility and optimization problems open. That obstruction has goods of distinct magnitudes and chores of distinct magnitudes; it does not satisfy the two-valued hypothesis here. The result above identifies an unrestricted-population, unrestricted-ratio positive mixed-sign class, including a transition between chore removal and good receipt not covered by either homogeneous-sign argument. Igarashi, Kamiyama, Suksompong, and Yuen study the different problem of reconfiguring one already EF1 *goods* allocation into another via EF1-preserving exchanges; that does not establish repair from a near-EF1 signed allocation or monotonicity of signed shortfalls. These comparisons establish separation from inspected statements, not comprehensive publication priority.

## Limitations
The theorem requires identical values \(+a,-b\) across items of the same sign, identical agents, unrestricted single-item transfers, and initially at most one unhappy agent. It does not apply to heterogeneous goods/chores magnitudes (where counterexamples are known), to agent-specific valuations, or to paths between prescribed EF1 endpoints. The upper bound \(m\) is not claimed globally optimal for \(a\ne b\); the shortest-path formula applies only when \(a=b\) and initially \(1\) is unhappy. Publication priority against inaccessible or unindexed specialist work remains a residual uncertainty. No independent audit has been performed.

## References
1. H. Chandramouleeswaran, P. Nimbhorkar, N. Rathi, *Fair Division in a Variable Setting*, arXiv:2410.14421v1 (first public 2024-10-18), https://arxiv.org/html/2410.14421v1, especially Definitions 3.1–3.3, Theorem 3.5, Appendix B.1.
2. H. Chandramouleeswaran, P. Nimbhorkar, N. Rathi, *Fair Division in a Variable Setting*, arXiv:2410.14421v4 (revised 2026-04-26), https://arxiv.org/html/2410.14421v4, especially Table 1 and Section 4.3.
3. A. Igarashi, N. Kamiyama, W. Suksompong, S. M. Yuen, *Reachability of Fair Allocations via Sequential Exchanges*, Algorithmica 86 (2024), https://doi.org/10.1007/s00453-024-01271-y, Sections 1–4 and Appendix A.
