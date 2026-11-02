# Sparse-approval collapse of integral and fractional Pareto optimality

## Finding

For every finite approval-based committee election in which each voter approves **at most two candidates**, every Pareto-optimal committee is fractionally Pareto-optimal. The reverse implication holds for arbitrary additive utilities. Thus, on this entire sparse-approval domain, integral and fractional Pareto optimality coincide for every committee size. The bound two is sharp in the size of an approval ballot: a five-candidate, two-seat election with some three-candidate approval ballots has a Pareto-optimal committee that is fractionally Pareto dominated.

## Assumptions and scope

Let \(C\) be a finite set of \(m\) candidates, \(1\le k\le m\), and let \(N\) be a finite set of voters, each with an approval set \(A_i\subseteq C\) of cardinality at most \(2\). Empty ballots and repeated ballots are permitted. For an integral committee \(W\subseteq C\) of cardinality \(k\), the additive approval utility of voter \(i\) is \(u_i(W)=|A_i\cap W|\). A fractional committee is a vector \(x\in[0,1]^C\) satisfying \(\sum_{c\in C}x_c=k\), with utility \(u_i(x)=\sum_{c\in A_i}x_c\). A feasible alternative Pareto dominates \(W\) if each voter has utility at least \(u_i(W)\) and at least one voter has strictly greater utility. PO and fPO prohibit, respectively, integral and fractional feasible dominators.

The theorem is universal over the number of candidates and voters, committee sizes, the ballot multiset, and all real fractional committees. It assumes unit additive approval utilities, not arbitrary positive valuations.

## Proof

**A threshold exchange lemma.** Fix an integral committee \(W\), and write \(T=C\setminus W\). Suppose that at least one candidate in \(T\) is approved by a voter. Let \(P\subseteq W\) and \(Q\subseteq T\) satisfy these three conditions: (i) no voter whose approvals are entirely contained in \(W\) approves a member of \(P\); (ii) for every voter approving one candidate \(c\in W\) and one candidate \(d\in T\), inclusion \(c\in P\) implies \(d\in Q\); (iii) \(|P|>|Q|\). Then \(W\) has a strictly Pareto-dominating integral committee.

Indeed, put \(Z=(W\setminus P)\cup Q\). The first two conditions show that \(u_i(Z)\ge u_i(W)\) for every voter; voters approving no member of \(W\) cannot lose utility either. Also, \(|Z|=k-r\) where \(r=|P|-|Q|\ge1\). If some voter already strictly improves at \(Z\), append any \(r\) unselected candidates to reach size \(k\). Otherwise, pick an approved candidate \(d\in T\). If \(d\notin Q\), a voter approving \(d\) must be strictly improved by adding \(d\): a singleton or a voter without selected approvals gains, while a crossing voter has its old approved candidate still in \(Z\), because condition (ii) forbids removing that candidate when \(d\notin Q\). If instead every approved candidate of \(T\) is in \(Q\), choose an approved \(d\in Q\). Since \(Z\) causes no strict improvement, every supporter of \(d\) must also approve some \(c\in P\) (otherwise this voter would have strictly gained). Restoring \(c\) produces utility \(2\), strictly greater than the original utility \(1\), for that voter. In either case, fill the remaining at most \(r-1\) vacancies arbitrarily; adding candidates never lowers utilities. The resulting committee has size \(k\) and strictly Pareto dominates \(W\). This proves the lemma.

**Threshold decomposition.** Assume that \(W\) is PO but not fPO, and let a fractional committee \(x\) dominate \(W\), strictly for at least one voter. For \(c\in W\) put \(a_c=1-x_c\), and for \(d\in T\) put \(b_d=x_d\). Each belongs to \([0,1]\), and the fractional seat constraint gives
\[
\sum_{c\in W}a_c=\sum_{d\in T}b_d.
\]
A voter whose approvals are entirely inside \(W\) forces every one of those approved candidates to have \(a_c=0\), because fractional coordinates are at most one. For any crossing ballot \(\{c,d\}\) with \(c\in W\), \(d\in T\), dominance forces \(b_d\ge a_c\).

For each threshold \(t\in(0,1)\), define
\[
P_t=\{c\in W:a_c\ge t\},\qquad Q_t=\{d\in T:b_d\ge t\},\qquad Z_t=(W\setminus P_t)\cup Q_t.
\]
The two dominance restrictions are exactly conditions (i) and (ii) of the lemma. The existence of strict improvement also implies that some candidate in \(T\) is approved: if no one approves any unselected candidate, fractional reduction of selected coordinates cannot improve a voter. Hence, by PO and the lemma, \(|P_t|\le |Q_t|\) at every threshold. Yet the layer-cake identity yields
\[
\int_0^1(|P_t|-|Q_t|)\,dt=\sum_{c\in W}a_c-\sum_{d\in T}b_d=0.
\]
Therefore \(|P_t|=|Q_t|\) for almost every threshold. The threshold committees \(Z_t\) weakly improve every voter, and for each voter
\[
 u_i(x)-u_i(W)=\int_0^1\bigl(u_i(Z_t)-u_i(W)\bigr)\,dt.
\]
For the voter strictly improved by \(x\), the integral is strictly positive, so a threshold exists where \(|P_t|=|Q_t|\) and \(u_i(Z_t)>u_i(W)\). This \(Z_t\) is an integral committee of exactly \(k\) candidates which Pareto dominates \(W\), contradicting PO. Thus PO implies fPO; the converse is immediate because every integral committee is a fractional committee.

**Sharpness of the ballot-size restriction.** Let \(C=\{a,b,c,d,e\}\) and \(k=2\). The seven approval ballots are
\[
\{a,c,d\},\ \{a,c,e\},\ \{a,d,e\},\ \{b,c\},\ \{b,d\},\ \{b,e\},\ \{c,d\}.
\]
The committee \(W=\{a,b\}\) yields utilities \((1,1,1,1,1,1,0)\). The fractional committee with coordinates \(x_a=0\) and \(x_b=x_c=x_d=x_e=1/2\) yields \((1,1,1,1,1,1,1)\). Hence \(W\) is not fPO. It is nevertheless PO: each alternative two-candidate committee containing \(a\) loses a voter who approves \(b\) and an unselected candidate; each containing \(b\) loses a voter who approves \(a\) and two of the other candidates; and each committee contained in \(\{c,d,e\}\) loses at least one voter with ballot \(\{b,t\}\), where \(t\) is not selected. Thus no alternative integral committee weakly improves all voters.

## Verification

The included dependency-free `verify.py` checks the exact three-approval witness against all \(\binom{5}{2}=10\) integral committees and against its rational fractional dominator. It also exhaustively considers the \(2^{10}=1024\) possible supports of distinct singleton and doubleton approval ballots over four candidates, all nontrivial committee sizes and PO committees, and every denominator-two or denominator-three fractional committee from the specified grids. It tests \(10{,}544\) Pareto-optimal committees and \(460{,}068\) fractional comparisons without finding a counterexample. These finite checks corroborate the theorem but **do not prove the arbitrary-size result**, which follows from the threshold exchange argument above.

## Relationship to prior work

Becker, Boehmer, Frank and Glessen [1] define fractional Pareto optimality, characterize it through positive-weight welfare maximization and prove PO–fPO equivalence on specific structured approval domains under single-dominance and cloning hypotheses. The at-most-two-approvals domain is not generally single-dominance-only: for ballots \(\{a,c\},\{a,d\},\{b,c\},\{b,d\},\{c,d\}\) with \(k=2\), committee \(\{a,b\}\) is dominated by \(\{c,d\}\), but none of its four one-candidate swaps is a Pareto improvement. Thus their single-dominance theorem does not directly imply this sparse-ballot theorem. The general unrestricted-domain PO–fPO separation, including a three-approval-style example, is already part of the prior literature; the contribution here is the universal positive domain boundary, not the mere existence of a separation.

Schünke [2] develops single-dominance reasoning for candidate- and voter-interval domains. Aziz, Lang and Monnot [3] study computing and testing integral Pareto-optimal committees under set preference extensions, rather than this fractional equivalence in the sparse-approval domain.

## Limitations

The assertion concerns unit additive approvals and fixed-size committees. It does not extend to arbitrary cardinal utilities or assert equivalence for approval ballots of size three. The accompanying enumeration is finite; the mathematical proof handles arbitrary finite sizes. The literature comparison cannot rule out unindexed or inaccessible equivalent results, and independent scientific verification has not been performed.

## References

[1] P. Becker, N. Boehmer, F. Frank and L. Glessen, *Fractional Pareto-Optimality in Multiwinner Voting*, arXiv:2606.11160, first public 2026-06-09. https://arxiv.org/abs/2606.11160

[2] J. Schünke, *Pareto Optimality in Approval-Based Multiwinner Voting*, arXiv:2605.30490, first public 2026-05-28. https://arxiv.org/abs/2605.30490

[3] H. Aziz, J. Lang and J. Monnot, *Computing and Testing Pareto Optimal Committees*, arXiv:1803.06644, first public arXiv 2018-03-18. https://arxiv.org/abs/1803.06644
