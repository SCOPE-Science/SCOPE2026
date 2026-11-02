# Removing anonymity from the credit-fairness incentive impossibility

## Finding

**Theorem (identity-independent obstruction).** Consider three labeled agents, each endowed with one unit of a homogeneous, divisible resource per round, over five rounds. Assume the online allocation mechanism observes current and past reported demands (not future reports), reports are nonnegative, allocations are nonnegative real quantities totaling at most three per round, utility is capped-linear, and credit fairness means precisely CF1–CF5 of Zahedi and Freeman. If the mechanism is Pareto efficient and credit fair on every report history, then it is not fully strategyproof, **without an anonymity assumption**. Indeed, one of the two profiles below has a one-round underreport increasing a single agent's five-round utility by at least \(1/2\).

The two profiles are obtained by exchanging two fixed agent labels. Rows are agents \(1,2,3\), columns are rounds \(1,2,3,4,5\):

\[
D^A=\begin{pmatrix}1&2&0&0&3\\3&0&1&1&2\\0&2&2&2&0\end{pmatrix},\qquad
D^B=\begin{pmatrix}0&2&2&2&0\\3&0&1&1&2\\1&2&0&0&3\end{pmatrix}.
\]

In profile \(A\), agent 1 reports zero instead of one in round 1 and is truthful thereafter; in profile \(B\), agent 3 does likewise. The same mechanism (with the same fixed identities and tie-breaking) must permit the two deviations to have respective utility gains \(x-1\) and \(2-x\), for a single shared parameter \(1\le x\le2\). Thus

\[
\max\{x-1,2-x\}\ge\tfrac12.
\]

## Assumptions and scope

A round has available supply \(E=3\) and endowments \(e_i=1\). Each agent's actual round utility from quantity \(a_{i,t}\) is \(u_{i,t}(a_{i,t})=\min\{d_{i,t},a_{i,t}\}\). For reported demands \(d'_{i,t}\), denote reported utility by \(u'_{i,t}=\min\{d'_{i,t},a_{i,t}\}\). Total utility is the sum over five rounds. Full strategyproofness is the absence of profitable misreports over the whole history; current-round (myopic) incentive compatibility is not at issue.

An online mechanism's round-\(t\) allocation is determined by reported demands through round \(t\), fixed labeled agents, and other fixed publicly available parameters; it cannot condition on demands that have not yet been reported. It need not be anonymous, neutral, or symmetric. Credit balances start at \(c_{i,1}=0\). We use the published definition of credit fairness: for \(\Delta c_{i,t}=c_{i,t+1}-c_{i,t}\), (CF1) requires \(\min(0,1-u'_i)\le\Delta c_i\le\max(0,1-u'_i)\); (CF2) requires \(\Delta c_i\ge\sum_{j\ne i}u'_j-2\) when \(\sum_{j\ne i}u'_j>2\); (CF3) requires \(\sum_i\Delta c_i\le0\); (CF4) requires \(a_i\ge\min\{d'_i,1+\min(0,c_i)\}\); and (CF5) says that whenever any \(a_j>\max(0,1+c_j)\), every agent \(i\) receives either at least their reported demand \(d'_i\) or at least their credit-adjusted entitlement \(1+c_i\). Subscripts \(t\) are suppressed within each round.

Every reported round of both truthful and altered histories has total demand at least three. By Pareto efficiency, on such rounds all supply is assigned to agents with positive reported demand, with \(a_i\le d'_i\), so \(\sum_i a_i=3\) and \(u'_i=a_i\). This consequence uses the published PE definition, not anonymity.

## Proof

**1. Forced credit updates on these histories.** Whenever \(\sum_i d'_i\ge3\), PE makes \(\sum_i a_i=3\) and \(u'_i=a_i\). If \(a_i<1\), CF2 (the other agents get \(3-a_i>2\)) and CF1 together force \(\Delta c_i=1-a_i\). If \(a_i=1\), CF1 forces \(\Delta c_i=0\). If \(a_i>1\), CF1 provides \(\Delta c_i\ge1-a_i\). Since these lower bounds sum to zero, CF3 forces equality for every agent. Hence in all cases

\[
\Delta c_{i,t}=1-a_{i,t},\qquad
c_{i,t}=\sum_{s<t}(1-a_{i,s}).\tag{1}
\]

This rederives the source's forced-credit lemma for the present histories.

**2. Truthful profile \(A\) forces utility four for agent 1.** In round 1, demands \((1,3,0)\), PE and CF4 give \(a=(1,2,0)\), hence next credits \((0,-1,1)\). In round 2, demands \((2,0,2)\), CF4 requires agent 1 to receive at least one and agent 3 at least one. If agent 1 received more than one, CF5 would require agent 3 to receive at least \(\min\{d'_3,1+c_3\}=2\), which is impossible with supply three. Thus round 2 is \((1,0,2)\). In rounds 3 and 4, demands \((0,1,2)\) exhaust the supply, and PE forces \((0,1,2)\) in each. Applying (1) gives credits \((2,0,-2)\) at the start of round 5. With demands \((3,2,0)\), CF4 requires agent 2 to receive at least one. Were agent 2 allocated more than one, CF5 would require agent 1 to receive at least \(\min\{3,1+2\}=3\), contradicting the supply bound. Therefore round 5 must allocate \((2,1,0)\). The entire truthful allocation matrix is

\[
A^A=\begin{pmatrix}1&1&0&0&2\\2&0&1&1&1\\0&2&2&2&0\end{pmatrix}.
\]

Agent 1's true utility is \(1+1+2=4\). All forced allocations are derived from PE and CF alone, without any use of anonymity.

**3. Truthful profile \(B\).** The same argument with agents 1 and 3 exchanged forces

\[
A^B=\begin{pmatrix}0&2&2&2&0\\2&0&1&1&1\\1&1&0&0&2\end{pmatrix}.
\]

Agent 3's truthful utility is \(1+1+2=4\). This conclusion is a separate consequence of PE and CF for profile \(B\), not an assumption that the mechanism treats labels symmetrically.

**4. The two altered reports share a common prefix.** For profile \(A\), have agent 1 alone report zero instead of one in round 1; for profile \(B\), have agent 3 do so. Thereafter each agent reports truthfully. In both altered histories, the reported vectors for rounds 1 and 2 are exactly \((0,3,0)\) and \((2,0,2)\), with *the same fixed agent labels*. PE forces the first allocation \((0,3,0)\); (1) gives credits \((1,-2,1)\) entering round 2. CF4 gives at least one each to agents 1 and 3, while demand caps and PE exhaust all three units. Denote the common second-round allocation by

\[
(a_{1,2},a_{2,2},a_{3,2})=(x,0,3-x),\qquad 1\le x\le2.\tag{2}
\]

The same \(x\) must occur in both branches **by onlineness and identity of the entire reported history through round 2**. No symmetry of the mechanism is asserted or needed. Credits entering round 3 are \((2-x,-1,x-1)\).

**5. Continuations and the opposite incentive inequalities.** In altered profile \(A\), rounds 3 and 4 have reported demands \((0,1,2)\), so PE forces \((0,1,2)\) both times. Credits at the start of round 5 are \((4-x,-1,x-3)\). In round 5, demands are \((3,2,0)\). Since agent 2's adjusted entitlement is zero, any positive round-5 allocation to agent 2 would trigger CF5 and force agent 1 to receive at least \(\min\{3,1+(4-x)\}=3\), leaving no supply for agent 2. Thus agent 2 gets zero, agent 1 gets three, and the deviator's true total utility is \(x+3\). Relative to the truthful utility four, their gain is

\[
\Delta_A=x-1.\tag{3}
\]

In altered profile \(B\), rounds 3 and 4 instead have reported demands \((2,1,0)\), hence allocations \((2,1,0)\) both times. Credits at the start of round 5 are \((-x,-1,x+1)\). Reported demands in round 5 are \((0,2,3)\). Any positive allocation to agent 2 triggers CF5 and requires agent 3 to get at least \(\min\{3,1+(x+1)\}=3\), again impossible with positive allocation to agent 2. Thus agent 3 gets all three units, and the deviator's true total utility is \((3-x)+3=6-x\), for gain

\[
\Delta_B=2-x.\tag{4}
\]

By (2), \(\Delta_A,\Delta_B\ge0\) and \(\Delta_A+\Delta_B=1\). Consequently at least one is at least \(1/2\), violating full strategyproofness. The argument uses only the mechanism's response to a shared observable prefix, not anonymity. \(\square\)

## Verification

The self-contained `verify_credit_gadget.py` uses exact `fractions.Fraction` arithmetic. It checks all five CF axioms and reported-demand Pareto efficiency on the two truthful histories and on both altered histories for every \(x\) on the 101-point rational grid from one to two in increments of \(1/100\). It replays the resulting utilities, confirms \(\Delta_A+\Delta_B=1\) and the gain lower bound, and independently enumerates one-round feasible allocations on a tenth-unit grid for the critical second and fifth rounds. Run `python3 verify_credit_gadget.py`. The checker is finite corroboration; Steps 1–5 above are the universal proof.

## Relationship to prior work

Zahedi and Freeman, *Credit Fairness: Online Fairness in Shared Resource Pools*, arXiv:2601.17944v1 (January 25, 2026), arXiv:2601.17944v2 (August 16, 2026), and IJCAI 2026, introduced CF1–CF5, proved the forced-credit lemma, and showed incompatibility with strategyproofness and Pareto efficiency **under anonymity**. Their proof fixes a single truthful history and uses anonymity to set the deviator's second-round allocation to \(3/2\); their full v2 paper explicitly asks whether anonymity can be removed. Their v1 abstract states an apparently broader incompatibility informally, but its actual theorem and proof explicitly assume anonymity. Our two fixed-label demand profiles eliminate that assumption: their altered histories coincide through round 2 and force two opposite gains for *any* choice of \(x\). The quantitative \(1/2\) guarantee concerns this two-profile witness, not optimality among all possible demand profiles.

The relevant axioms and the source theorem are inspected in full in both preprint versions and in the accessible published conference presentation. We found no matching anonymity-free proof among targeted research-record and literature searches; that negative search does not certify priority.

## Limitations

This result concerns three agents, equal unit endowments, divisible allocations, capped-linear utilities, and a horizon of five rounds. It assumes the mechanism cannot anticipate future demand reports and uses the original CF1–CF5 definitions. It does **not** show impossibility of myopic online strategyproofness, does not address multi-resource utilities, and does not claim that the witness lower bound is optimal over all possible profiles. A human novelty and proof review has not been performed.

## References

- S. M. Zahedi and R. Freeman, *Credit Fairness: Online Fairness In Shared Resource Pools*, arXiv:2601.17944v1, first public January 25, 2026. https://arxiv.org/html/2601.17944v1
- S. M. Zahedi and R. Freeman, *Credit Fairness: Online Fairness in Shared Resource Pools*, arXiv:2601.17944v2, August 16, 2026. https://arxiv.org/html/2601.17944v2
- S. M. Zahedi and R. Freeman, *Credit Fairness: Online Fairness in Shared Resource Pools*, Proc. IJCAI 2026, pp. 446–453, DOI 10.24963/ijcai.2026/51. https://ijcai.org/proceedings/2026/51
