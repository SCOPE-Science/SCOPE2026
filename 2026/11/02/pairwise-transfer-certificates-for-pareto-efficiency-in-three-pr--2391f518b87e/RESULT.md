# Pairwise-transfer certificates for Pareto efficiency in three-project portioning

## Finding

For any finite nonempty set of agents with normalized nonnegative three-project budget reports and any proposed normalized budget, the budget is Pareto efficient under \(\ell_1\) distance **if and only if** no positive transfer of budget between two projects weakly improves every agent and strictly improves at least one agent. This gives an exact \(O(n)\) Pareto test for \(n\) agents. The three-project boundary is sharp: for four projects there are five-agent profiles with a strict global Pareto improvement but no improving single-pair transfer.

## Assumptions and scope

Let \(n\geq1\), \(\Delta_3=\{x\in\mathbb R_{\geq0}^3:\sum_{j=1}^3x_j=1\}\), and let reports \(p^{(1)},\ldots,p^{(n)}\in\Delta_3\) be arbitrary. An outcome \(x\in\Delta_3\) gives agent \(i\) disutility \(D_i(x)=\sum_{j=1}^3|x_j-p^{(i)}_j|\). A budget \(y\) dominates \(x\) if \(D_i(y)\leq D_i(x)\) for every \(i\), with strict inequality for at least one agent. A single-pair transfer has the form \(x+\varepsilon(e_k-e_j)\in\Delta_3\), for distinct project indices \(j,k\) and \(\varepsilon>0\). The claim does not require symmetric agents, rational reports, or use of a particular aggregation mechanism.

## Proof

**Common non-worsening box.** For every zero-sum triple \(z\in\mathbb R^3\), \(\|z\|_1=2\|z\|_\infty\). Indeed, if \(z\neq0\), the sum of positive coordinates equals the absolute sum of negative coordinates, and one of the two sign classes has a single nonzero coordinate. Thus put \(r_i=\|x-p^{(i)}\|_\infty\). For every \(y\in\Delta_3\), the inequalities \(D_i(y)\leq D_i(x)\) for all agents are equivalent to
\[
L_j\leq y_j\leq U_j\quad(j=1,2,3),
\qquad L_j=\max\{0,\max_i(p^{(i)}_j-r_i)\},
\qquad U_j=\min\{1,\min_i(p^{(i)}_j+r_i)\}.
\]
Call this common non-worsening box \(B\). In particular, \(x\in B\).

**From a global improvement to a pair transfer.** Suppose \(y\in B\cap\Delta_3\) strictly improves agent \(i\). Then \(r_i>0\), and \(q=y-x\) is a nonzero zero-sum triple. Let \(A_i=\{j:|x_j-p^{(i)}_j|=r_i\}\) be agent \(i\)'s active coordinates. Every active coordinate must be moved strictly toward its reported value: if \(x_j>p^{(i)}_j\), then \(q_j<0\), and if \(x_j<p^{(i)}_j\), then \(q_j>0\). Because \(x-p^{(i)}\) is a zero-sum triple and \(r_i>0\), there are either exactly one or exactly two active coordinates; when there are two, their signs are opposite.

If there are two active coordinates, choose the elementary transfer from the active coordinate with negative \(q_j\) to the active coordinate with positive \(q_k\). If there is one active coordinate, choose that coordinate and any other coordinate with the opposite nonzero sign of \(q\), which exists by \(\sum_jq_j=0\). In both cases the chosen transfer has the same direction of motion as \(q\) on its two affected coordinates. Since \(x,y\in B\), for a sufficiently small positive \(\varepsilon\), the transferred outcome remains in \(B\cap\Delta_3\): the box coordinate margins used by \(q\) are positive. All active coordinates of the strictly improved agent move toward its report, and each inactive coordinate has slack below \(r_i\); hence, after shrinking \(\varepsilon\) if needed, every absolute coordinate deviation of this agent is strictly smaller than \(r_i\). Its \(\ell_1\) cost strictly decreases, while all others weakly decrease by membership in \(B\). Conversely, any such transfer is itself a global Pareto improvement. This proves the equivalence, including boundary reports and outcomes. If an agent has \(r_i=0\), the common box contains only \(x\), and both improvement conditions are false.

**Exact algorithm.** Compute \(r_i,L_j,U_j\). Examine the six ordered donor/receiver pairs \((j,k)\). A pair can move nontrivially within \(B\cap\Delta_3\) precisely when \(x_j>L_j\) and \(x_k<U_k\). Among those pairs, a transfer strictly improves some agent precisely when there is an agent \(i\) with \(r_i>0\) whose active coordinate set \(A_i\) lies entirely in the pair and such that active donor coordinates satisfy \(x_j>p^{(i)}_j\) and active receiver coordinates satisfy \(x_k<p^{(i)}_k\). For this agent, the transfer can be chosen small enough that inactive deviations remain below \(r_i\). Checking six pairs and all agents is \(O(n)\) after constant-size arithmetic on the three coordinates. Absence of such a pair certifies Pareto efficiency.

**Four-project obstruction.** Consider \(x=(1/4,1/4,1/4,1/4)\) and five ideal budgets
\[
\begin{aligned}
p^{(1)}&=(3/10,3/10,3/10,1/10),\\
p^{(2)}&=(3/10,3/10,1/5,1/5),\\
p^{(3)}&=(3/10,1/5,3/10,1/5),\\
p^{(4)}&=(1/5,3/10,1/5,3/10),\\
p^{(5)}&=(1/5,1/5,3/10,3/10).
\end{aligned}
\]
The allocation \(y=(6/25,13/50,13/50,6/25)\) improves the first agent's \(\ell_1\) cost from \(3/10\) to \(7/25\), while leaving the remaining four costs exactly \(1/5\). Yet, for every ordered pair of distinct coordinates \((j,k)\), at least one of the five agents has \(p^{(i)}_j>x_j\) and \(p^{(i)}_k<x_k\). That agent is already below their target on the proposed donor and above their target on the proposed receiver, so any feasible positive donor-to-receiver transfer strictly raises their \(\ell_1\) cost. All twelve elementary transfers are blocked. Therefore the three-project local-to-global equivalence fails already at four projects.

## Verification

The standalone exact-rational script `verify.py` checks the closed-form common-box minimum-radius criterion against the six-transfer test for all three-agent report multisets and outcomes on the denominator-\(2,3,4,5\) rational grids: \(49{,}927\) profile/outcome cases. For every positively detected pair, it constructs an exact rational strictly dominating transfer and independently checks all agents' \(\ell_1\) costs. It also checks all twelve blocking directions in the four-project example and the exact costs of its Pareto improvement. A separate floating-point linear-programming comparison was performed for the \(12{,}736\) grid cases with denominators \(2,3,4\). These finite computations are supplementary tests; the all-real, all-agent theorem is proved above, not inferred from enumerations.

## Relationship to prior work

Freeman, Pennock, Peters and Vaughan (2019), *Truthful Aggregation of Budget Proposals*, introduce the divisible-budget \(\ell_1\) model, characterize Pareto-efficient moving-phantom mechanisms, and explain that utilitarian minimizers are Pareto optimal. Elkind, Greger, Lederer, Suksompong and Teh (2023), *Settling the Score: Portioning with Cardinal Preferences*, study axiomatic properties of such aggregation rules, including Pareto efficiency and range respect. The finding here instead concerns arbitrary given outcomes, not a selected social choice rule: it provides an exact all-profile local-to-global test for three projects, and shows why the same test fails at four. No uniqueness claim is made for the technique or for earlier Pareto results.

## Limitations

The positive equivalence relies on exactly three projects, normalized reports, and \(\ell_1\) preferences. The four-project witness rules out this specific pairwise criterion in higher dimensions, but does not classify all larger-dimensional certificates. It does not establish strategyproofness or other fairness axioms. Publication priority remains subject to specialist-literature checks; no independent external audit has been performed.

## References

- R. Freeman, D. M. Pennock, D. Peters, and J. W. Vaughan, *Truthful Aggregation of Budget Proposals*, arXiv:1905.00457 (first publicly posted 2019-05-01), https://arxiv.org/abs/1905.00457.
- E. Elkind, M. Greger, P. Lederer, W. Suksompong, and N. Teh, *Settling the Score: Portioning with Cardinal Preferences*, arXiv:2307.15586 (first publicly posted 2023-07-28), https://arxiv.org/abs/2307.15586.
- I. Caragiannis, G. Christodoulou, and N. Protopapas, *Truthful Aggregation of Budget Proposals with Proportionality Guarantees*, arXiv:2203.09971 (2022), https://arxiv.org/abs/2203.09971.
