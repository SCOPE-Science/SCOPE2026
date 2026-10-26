# An approval-responsive, online-strategyproof completion of temporal equal shares

## Finding

For any finite horizon \(T\ge 1\), any number \(n\ge 1\) of voters, and any nonempty finite set of available candidates in each round, a **complete, semi-online Method of Equal Shares (MES)** can be implemented as follows: before the first unaffordable round, run the standard minimum-price MES; at the first unaffordable round and in all remaining rounds, elect a candidate maximizing the total *remaining MES budget of its current approvers*, using a fixed candidate priority to break ties. Do not charge voter budgets after this switch.

**Theorem.** For every sequence of approval profiles (including those with nonempty ballots), this rule (i) chooses exactly one candidate in every round, (ii) satisfies **online strategyproofness** (OSP: a single voter cannot increase their approval satisfaction in the current round by changing only that round's report while the past is fixed), and (iii) retains **weak extended justified representation** (wEJR). Moreover, it satisfies the published stronger axiom wEJR+ under the definitions of Phillips–Elkind–Teh–Wąs [3]. The theorem holds with any frozen nonnegative fallback voter weights, not only residual budgets; the balance-weighted choice is a natural approval-responsive instance. The extra theorem contribution is simultaneous complete output and OSP; fairness inheritance uses the established MES proportionality results [2,3].

This is not the assertion that completed MES is globally strategyproof across all \(T\) rounds. OSP concerns one round's immediate approval satisfaction with its preceding history fixed.

## Assumptions and scope

Let \(N=\{1,\ldots,n\}\), and in round \(t\in\{1,\ldots,T\}\) let \(C_t\) be a nonempty finite candidate set and \(A_t(i)\subseteq C_t\) the approval set of voter \(i\). For consistency with [1], all sincere ballots may be required nonempty; the present one-round OSP argument also tolerates empty reports. Fix a total order on all candidate labels, independent of submitted approvals. Put the per-round accounting price \(p=n/T\). Each voter starts with budget \(b_i=1\).

For candidate \(c\), write \(S_t(c)=\{i:c\in A_t(i)\}\). A candidate is *affordable* if \(\sum_{i\in S_t(c)}b_i\ge p\). For each affordable candidate define
\[
\rho_t(c)=\min\left\{r\ge0:\sum_{i\in S_t(c)}\min(b_i,r)\ge p\right\}.
\]
While at least one candidate is affordable, elect an affordable candidate of minimum \(\rho_t(c)\), with the fixed priority for ties, and subtract \(\min(b_i,\rho_t(c))\) from the budget of each approving voter. At the **first** round without an affordable candidate, enter permanent fallback mode. In that round and every later round, elect a candidate maximizing
\[
W_t(c)=\sum_{i\in S_t(c)}b_i,
\]
with the same fixed tie order, and leave budgets frozen. All comparisons are exact, and the fixed priority is independent of ballots. More generally, after switching one may freeze any nonnegative history-measurable weights \(w_i\) and maximize \(\sum_{i\in S_t(c)}w_i\) in the fallback rounds.

For a voter, satisfaction means the number of selected rounds whose winning candidate they sincerely approve. A group \(G\subseteq N\) is *fully cohesive* if in each round all members approve at least one common candidate. wEJR means that for each integer \(\ell\ge1\) and fully cohesive \(G\) with \(|G|\ge \ell n/T\), some member approves at least \(\ell\) elected outcomes. This agrees with the weak temporal EJR convention used in [1,2].

## Proof

**1. Candidate-separable monotone priorities.** Fix the past, hence all current budgets and the Boolean condition indicating whether fallback mode has started. Before fallback, assign every currently affordable candidate the priority pair \((1,-\rho_t(c))\); assign every unaffordable candidate the pair \((0,W_t(c))\). Order pairs lexicographically, breaking exact ties by the fixed candidate priority. The algorithm chooses the candidate with highest pair. After fallback begins, it chooses the candidate with highest frozen-weight approval score.

The priority of each candidate depends on the current approvals **only through that candidate's own supporter set**. Enlarging a supporter set cannot reduce its priority: \(W_t(c)\) cannot decrease; affordability can change only from false to true; and the minimum solution \(\rho_t(c)\) of the payment inequality cannot increase, since the left side grows pointwise in \(r\). The same monotonicity holds for nonnegative frozen fallback weights. Therefore shrinking a supporter set cannot improve the candidate's priority. None of these observations relies on the support sets of other candidates.

**2. Online strategyproofness.** Fix a current round, the entire past, all other voters' reports, and one voter's true current approval set \(A\). Let \(c\) be the winning candidate under truthful reporting. If \(c\in A\), the voter is already satisfied in that round, so no deviation can improve the binary payoff. Otherwise, consider any alternative current report. Every candidate \(a\in A\) has either the same or *lower* priority than under truth (because the voter already supported it and can only remove that support). The unapproved winner \(c\notin A\) has either the same or *higher* priority than under truth (because the voter can only add support). Consequently no \(a\in A\) can overtake \(c\), including under the fixed tie order. No deviation can change current dissatisfaction into satisfaction. This proves OSP in both MES and fallback modes, including the switching round. It also proves online independence of irrelevant alternatives: deleting approval for a losing candidate cannot change the current winner.

**3. Full output and efficiency.** Each round selects from its nonempty \(C_t\). Finite candidate sets and the fixed tie rule make the rule deterministic. Given rational budgets, the minimum affordable price can be computed by sorting the approving budgets and solving a piecewise-linear equation; the procedure is polynomial in the natural input size. All payments are nonnegative and no budget becomes negative. Fallback is a weighted-approval score calculation. If at least one voter has positive remaining budget and every voter approves a nonempty set, a candidate with positive fallback support exists.

**4. Fairness.** Up to its first unaffordable round, the rule makes exactly the same choices and payments as standard temporal MES. If no unaffordable round occurs, the outcomes coincide completely. Otherwise, the tail consists of additional actual winners where the noncompleted MES of [1] would make no decision; therefore every voter's total satisfaction weakly increases, preserving every lower-bound satisfaction guarantee already established for the unfinished MES.

For completeness, one may recover the wEJR lower bound directly by the standard budget argument of [2]. Suppose a fully cohesive group \(G\) of size \(g\ge\ell p\) has every voter satisfied in at most \(\ell-1\) rounds of the full completed sequence. At an early MES halt, \(\sum_{i\in G}b_i<p\), since otherwise the group's common approved candidate would be affordable. If MES never halts, all \(n\) initial budget units have been spent in \(T\) rounds at price \(p\), so every budget is zero. In either case, some member \(i\in G\) has remaining budget \(b_i<p/g\le1/\ell\), and hence paid more than \(1-1/\ell\) in at most \(\ell-1\) approving MES rounds. There must be a payment strictly exceeding \(1/\ell\). Choose the earliest such payment made by *any* member of \(G\). Before that round every member has paid at most \(1/\ell\) in each of at most \(\ell-1\) approving rounds, so each has at least \(1/\ell\) budget left. The group's common approved candidate is then affordable at the rate \(1/\ell\), since \(g/\ell\ge p\). But the MES winner charges some voter more than \(1/\ell\), requiring a strictly larger price, contrary to the minimum-price selection rule. This contradiction proves wEJR. The stronger wEJR+ assertion is inherited from the proved arbitrary-completion theorem of [3, Theorem 3.14], where the accounting normalization \(e_i=T/n\) and unit candidate cost are equivalent to the present \(b_i=1\) and cost \(p=n/T\) by multiplication by \(n/T\).

**5. A real completion, not a fixed candidate.** For \(n=T=2\), first-round ballots \(\{a\},\{a\}\) select \(a\), reducing both balances to \(1/2\). With second-round ballots \(\{a\},\{b\}\), neither alternative can pay the price \(p=1\); standard MES stops, while the completion elects \(a\) or \(b\) according to the fixed tie order. If the second-round balances are unequal in another history, the fallback responds to current approvals and their remaining weights rather than choosing a ballot-independent constant. The score monotonicity is essential, not merely decorative: at this same reachable second-round state, an *anti*-approval completion electing a minimum-weight-support candidate would choose \(a\) on the sincere disjoint ballots (fixed tie order \(a\) first). Voter 2, who sincerely approves only \(b\), could then submit \(\{a,b\}\): the anti-approval scores become \(1\) for \(a\) and \(1/2\) for \(b\), so \(b\) wins and the voter profits. Thus arbitrary ballot-responsive completions do not automatically inherit OSP.

## Verification

The standalone file `verify.py` uses rational arithmetic and reconstructs the minimum-price rule by sorting supporter balances. It checks 66,288 fixed-state combinations; 184,734 one-approval loser-deletion cases; 1,187,136 unilateral current-report strategyproofness comparisons; and 22,894 full two-/three-round trajectories with direct wEJR tests, as well as a concrete premature-stop example. Run `python verify.py` with Python 3. No third-party dependencies are required. These exhaustive finite checks do not prove the general quantified theorem; Parts 1–4 provide the analytic proof.

## Relationship to prior work

Borodin and Lueger [1, Section 4.3] prove OSP for MES **without** completion and explicitly ask whether a completion can preserve OSP. Their OIIA-to-OSP implication is an established supporting principle, not claimed here. Chandak, Goel, and Peters [2, Theorem 4.3] establish wEJR for semi-online MES; the present argument recovers that budget bound and shows it survives a complete, ballot-responsive tail. Phillips, Elkind, Teh, and Wąs [3, Definition 3.13 and Theorem 3.14] permit **arbitrary** decisions in the post-termination tail and prove wEJR+; that prior result covers the fairness inheritance but does **not** show that arbitrary or budget-sensitive completions preserve OSP. Approval-based score monotonicity and fixed tie-breaking are classical ideas; the nontrivial assertion here is their compatible use with the affordability-based switching boundary of temporal MES.

## Limitations

This is an existence/construction theorem, not a characterization of every possible completion. No full-horizon strategyproofness, PJR/EJR in their strong temporal forms, welfare optimum, or protection against strategic earlier-round manipulation is asserted. The fairness proof assumes the standard proportionality model and its identical publicly specified MES rule; no claim is made for variants charging fictitious budgets during fallback or with approval-dependent tie-breaking. Mathematical priority remains uncertain outside the inspected primary literature and searched published-record corpus; absence of a matching search result does not certify novelty.

## References

[1] A. Borodin and T. Lueger, *Online Temporal Voting: Strategyproofness, Proportionality and Asymptotic Analysis*, arXiv:2603.26504, first submitted 2026-03-27, Sections 2 and 4.3, https://arxiv.org/abs/2603.26504.

[2] N. Chandak, S. Goel, and D. Peters, *Proportional Aggregation of Preferences for Sequential Decision Making*, arXiv:2306.14858, first submitted 2023-06-26, Section 4.2 and Theorem 4.3, https://arxiv.org/abs/2306.14858.

[3] B. Phillips, E. Elkind, N. Teh, and T. Wąs, *Strengthening Proportionality in Temporal Voting*, arXiv:2505.22513, first submitted 2025-05-28; AAMAS 2026, Definition 3.13 and Theorem 3.14, https://arxiv.org/abs/2505.22513.

[4] E. Elkind, T. Y. Neoh, and N. Teh, *Temporal Elections: Welfare, Strategyproofness, and Proportionality*, arXiv:2408.13637, first submitted 2024-08-24, https://arxiv.org/abs/2408.13637.
