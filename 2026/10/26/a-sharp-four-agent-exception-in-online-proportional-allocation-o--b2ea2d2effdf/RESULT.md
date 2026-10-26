# A sharp four-agent exception in online proportional allocation of unit chores

## Finding

Let \(n\geq1\) be the number of agents, let unit-size indivisible chores arrive sequentially, and suppose that each arriving chore has a nonempty publicly observed subset of agents eligible to receive it. A deterministic online allocator must irrevocably assign each chore immediately to an eligible agent. An adaptive adversary may select each later eligibility set after observing earlier assignments, and may stop after any arrival. Proportional shares are eligibility-aware: each unit chore contributes \(1/|S|\) to the share of each agent in its eligibility set \(S\).

Let \(\tau(n)\) denote the least positive number of arrivals by which some adaptive adversary can force violation of proportionality up to one chore (Prop1) at a prefix against every deterministic online rule; set \(\tau(n)=\infty\) if no such number exists. Then
\[
\boxed{\tau(n)=\begin{cases}
\infty,&1\leq n\leq3,\\
5,&n=4,\\
3,&n\geq5.
\end{cases}}
\]
For at most three agents, assigning each nonsingleton-eligibility chore to an eligible agent with smallest current excess load over eligibility-aware proportional share maintains Prop1 at *every* prefix, for arbitrarily long sequences. At four agents, the same greedy rule handles every prefix of length at most four; a five-chore adaptive adversary defeats **every** deterministic allocator. At least five agents admit a three-chore adversary. The four-agent five-chore obstruction is the nontrivial exceptional cell of the exact frontier.

## Assumptions and scope

There are \(n\) labeled agents and finitely many indivisible chores, each with identical unit cost for all eligible agents. Every eligible set \(S_t\subseteq\{1,\ldots,n\}\) is nonempty; an agent not in \(S_t\) cannot receive chore \(t\). Write \(L_i(t)\) for agent \(i\)'s number of assigned chores after \(t\) arrivals and
\[
P_i(t)=\sum_{s=1}^{t}\frac{\mathbf{1}\{i\in S_s\}}{|S_s|}.
\]
Prop1 at prefix \(t\) means \(L_i(t)-\mathbf{1}\{L_i(t)>0\}\leq P_i(t)\) for every agent \(i\). Equivalently, because \(P_i(t)\geq0\), it means \(L_i(t)-P_i(t)\leq1\) for every agent, including recipients with empty bundles. The adversary is adaptive, and the guarantee is deterministic and holds at every prefix, not merely at a prespecified terminal horizon. The number \(n\), but not future eligibility sets, is known to the allocator. This result does not concern variable processing times, general agent-specific costs, randomization against an oblivious adversary, or the usual unrestricted-agent proportional share.

## Proof

**Scaled discrepancy dynamics.** Let \(Q\) be a positive common multiple of \(1,\ldots,n\), and put \(d_i=Q(L_i-P_i)\). These integers always sum to zero. A chore with eligible set \(S\) of cardinality \(k\), assigned to \(r\in S\), changes the discrepancy by
\[
d'_i=d_i-\frac{Q}{k}\mathbf{1}\{i\in S\}+Q\mathbf{1}\{i=r\}.
\]
Thus singleton-eligibility chores change no discrepancy, and Prop1 is equivalent to \(\max_i d_i\leq Q\). The *minimum-discrepancy rule* selects an \(r\in S\) minimizing \(d_r\), with arbitrary deterministic tie-breaking.

**One, two, and three agents.** The first case is immediate. With two agents, every nontrivial chore is eligible for both, and selecting a minimum-discrepancy agent alternates the scaled difference between \((0,0)\) and a permutation of \((-1,1)\) for \(Q=2\). No prefix can violate Prop1.

With three agents set \(Q=6\). Sort the three discrepancies after every arrival. The following eight triples form a forward-invariant family under all nontrivial eligibility sets and **all** minimum-discrepancy tie choices:
\[
\begin{aligned}
T_1&=(-5,1,4), & T_2&=(-4,-1,5),\\
T_3&=(-4,2,2), & T_4&=(-3,0,3),\\
T_5&=(-2,-2,4), & T_6&=(-2,1,1),\\
T_7&=(-1,-1,2), & T_8&=(0,0,0).
\end{aligned}
\]
Here a pair of indices refers to positions in the *sorted* triple, rather than fixed agent names. Applying the displayed integer update and sorting gives the complete transition table below; columns list eligibility-position sets \(\{1,2\}\), \(\{1,3\}\), \(\{2,3\}\), and \(\{1,2,3\}\), respectively:

| From | 12 | 13 | 23 | 123 |
|---|---|---|---|---|
| \(T_1\) | \(T_5\) | \(T_6\) | \(T_1\) | \(T_7\) |
| \(T_2\) | \(T_2\) | \(T_7\) | \(T_3\) | \(T_4\) |
| \(T_3\) | \(T_7\) | \(T_7\) | \(T_2\) | \(T_8\) |
| \(T_4\) | \(T_4\) | \(T_8\) | \(T_4\) | \(T_6\) |
| \(T_5\) | \(T_1\) | \(T_6\) | \(T_6\) | \(T_3\) |
| \(T_6\) | \(T_6\) | \(T_6\) | \(T_5\) | \(T_7\) |
| \(T_7\) | \(T_3\) | \(T_7\) | \(T_7\) | \(T_4\) |
| \(T_8\) | \(T_4\) | \(T_4\) | \(T_4\) | \(T_5\) |

The initial triple is \(T_8\). Every possible transition stays in this family; singleton chores leave the state unchanged. Since every listed triple has maximum component at most \(5<6\), induction proves the all-horizon Prop1 guarantee for three agents.

**Four-agent safety for the first four chores.** Set \(Q=12\) and use the same greedy rule. Singleton chores again leave discrepancies unchanged. Let \(\mathcal R_0=\{(0,0,0,0)\}\); recursively form \(\mathcal R_{t+1}\) by applying the displayed update to every vector in \(\mathcal R_t\), each of the eleven eligible subsets of size two, three, or four, and *each* eligible recipient tied for minimum discrepancy. This is an exact, finite, fully specified enumeration of every possible greedy outcome. Direct integer enumeration gives
\[
(|\mathcal R_0|,|\mathcal R_1|,|\mathcal R_2|,|\mathcal R_3|,|\mathcal R_4|)
=(1,28,187,617,1405).
\]
Every vector in every one of these five sets satisfies \(\max_i d_i\leq12\). The complete recurrence and its exhaustive verification are implemented in the attached dependency-free `verify.py`. Because the recurrence includes all eleven nonsingleton sets and every tie response, this finite certificate establishes the lower bound \(\tau(4)\geq5\), not just a sample of arrival strings.

**Four-agent five-chore adaptive obstruction.** Express each discrepancy vector in sorted order, allowing the adversary to identify agents by their current discrepancy values. Start at \((0,0,0,0)\). First release a chore eligible for all four agents. Whatever its recipient, the sorted state becomes \((-3,-3,-3,9)\). Second, release a chore eligible for exactly the three agents at discrepancy \(-3\); the state becomes \((-7,-7,5,9)\).

Third, release a chore eligible for the two agents with discrepancy \(-7\) and the agent with discrepancy \(5\). If assigned to the latter, the new state is \((-11,-11,9,13)\), already violating Prop1. Otherwise the state is \((-11,1,1,9)\). In that surviving branch, release a fourth chore eligible for the two agents at discrepancy \(1\), obtaining \((-11,-5,7,9)\). Fifth, release a chore eligible for the two agents at discrepancies \(7\) and \(9\). The two possible sorted outcomes are
\[
(-11,-5,3,13)\quad\text{and}\quad(-11,-5,1,15).
\]
Both have maximum discrepancy greater than \(12\). This exhausts every recipient response and establishes \(\tau(4)\leq5\).

**At least five agents: exact three-chore boundary.** For \(n\geq5\), release two chores eligible for all \(n\) agents. If both go to the self-review, her load after removing one is \(1\), whereas her proportional share is \(2/n<1\): failure after the second chore. Otherwise the two recipients differ. Release a third chore eligible exactly for those two recipients. Whichever receives it has load two but proportional share \(2/n+1/2<1\), so Prop1 fails at the third chore.

Conversely, for every \(n\), no adversary can force failure within two chores: on the second arrival assign its chore to an eligible agent not holding the first chore, whenever possible. If no such agent is eligible, its eligibility set consists only of the first recipient. That recipient's proportional share then includes a full unit from the singleton chore, and her final load minus one is exactly one. Every other agent has at most one chore and hence satisfies Prop1. Thus \(\tau(n)=3\) for \(n\geq5\), completing the proof.

## Verification

Run `python3 verify.py` using Python 3 and no external dependencies. Its integer implementation independently tests closure of the eight three-agent states for every eligibility choice and every greedy tie; enumerates all four-agent greedy outcomes for the first four jobs; verifies every response branch of the explicit adaptive five-job adversary; and separately solves the finite four-agent horizon game by exact minimax recursion. On the actual packaged source, the assertions pass and the reported four-agent counts are \((1,28,187,617,1405)\). The unbounded three-agent statement follows from the finite-state inductive closure, **not** from treating a bounded experiment as infinite evidence. The four-agent exhaustive portion is finite and covers precisely the four-job horizon claimed.

## Relationship to prior work

Biburger, Megow, and Shahkarami (arXiv:2610.08064, first public October 6, 2026) introduced and analyzed the same eligibility-aware online Prop1 model, establishing asymptotically tight \(\Theta(\sqrt m)\) deterministic approximation for chores, where \(m\) is the number of arriving chores, including unit-size chores. Their lower-bound construction targets previously loaded agents and is related to the simple large-\(n\) third-chore obstruction here. Their inspected theorem, proof, and appendices do not supply the all-horizon three-agent positive result or the exact exceptional four-agent five-chore horizon.

Sun, Wang, and Li (arXiv:2602.18098, first public February 20, 2026) investigate eligibility-aware proportionality and its offline existence/computation; those offline conclusions do not resolve adaptive irrevocable allocation. Classical online discrepancy and rounding results address different allowable vector choices and guarantees; no theorem in the inspected relevant sources implies this complete \(n=3,4,\geq5\) exact frontier. The two larger-literature connections should not be mistaken for a proof of absolute historical novelty.

## Limitations

The theorem is for identical **unit-size** chores and an **adaptive** adversary. It does not imply exact Prop1 for three agents with arbitrary processing times, or impossibility with three arrivals against a fixed oblivious input at five agents. Historical-priority uncertainty remains; finite database searches do not certify uniqueness or independence. The four-job four-agent lower bound rests on a transparent exhaustive finite recurrence verified by runnable integer code, not an unevaluated assertion about all possible algorithms.

## References

1. J. Biburger, N. Megow, and G. Shahkarami, *Online Fair Division under Eligibility Constraints*, arXiv:2610.08064, first submitted October 6, 2026, https://arxiv.org/abs/2610.08064. See especially Sections 2–3 and Appendix B.
2. A. Sun, R. Wang, and B. Li, *Fair Orientations: Proportionality and Equitability*, arXiv:2602.18098, first submitted February 20, 2026, https://arxiv.org/abs/2602.18098. See Sections 1–3 and its proofs.
3. N. Bansal, H. Jiang, R. Meka, S. Singla, and M. Sinha, *Online Discrepancy Minimization for Stochastic Arrivals*, SODA 2021. Different stochastic vector-balancing model; cited for methodological context, not for this deterministic theorem.
