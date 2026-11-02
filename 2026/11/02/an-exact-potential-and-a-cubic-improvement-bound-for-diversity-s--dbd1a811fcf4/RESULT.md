# An exact potential and a cubic improvement bound for diversity-seeking jumps on complete bipartite graphs

## Finding

For all integers \(a,b\geq 2\), all integers \(k\geq 2\), all populations of exactly \(a+b-1\) agents partitioned into \(k\) nonempty types, and every designation of strategic and immobile agents, consider the diversity-seeking jump game on \(K_{a,b}\) with exactly one vacant vertex. A strategic agent may move to the vacancy and receives the fraction of its *occupied neighbors* whose types differ from its own. Every permitted unilateral jump satisfies the **exact potential identity**

\[
 u_i(C')-u_i(C)=\Phi(C')-\Phi(C),\qquad
 \Phi(C)=\sum_{t=1}^{k}\left(\frac{\binom{A_t(C)}2}{a-1}+\frac{\binom{B_t(C)}2}{b-1}\right),
\]

where \(A_t(C)\) and \(B_t(C)\) count agents of type \(t\) in the respective bipartition classes. Consequently every improving-response path, under any choice of improving agent, terminates at a pure Nash equilibrium in at most

\[
 \left\lfloor\frac{a+b-2}{2}\operatorname{lcm}(a-1,b-1)\right\rfloor
 \leq \frac{(a+b-2)^3}{8}
\]

strict improving moves. In particular the improvement length is \(O((a+b)^3)\), uniformly in the numbers of types and immobile agents.

This conclusion includes the nonregular cyclic graph family \(K_{a,b}\) with \(a,b\geq2\) and \(a\ne b\), not covered by previously proved regular-graph or spider-graph sufficient conditions.

## Assumptions and scope

The graph is the unweighted, undirected, complete bipartite graph with vertex classes \(A\) and \(B\) of cardinalities \(a\) and \(b\). There are exactly \(a+b-1\) agents, with one agent on every nonvacant vertex; each belongs to one of \(k\) types. Agent identities can be distinct within each type. Some agents may be immobile; a movable agent can jump only to the unique unoccupied vertex. There are no swaps, mutations, new vacancies, or nonlocal objectives. All occupied vertices have at least one occupied neighbor because \(a,b\geq2\) and there is only one vacancy. For the mover \(i\), utility is the number of occupied neighbors of a different type divided by the number of occupied neighbors. A strict improvement means \(u_i(C')>u_i(C)\).

## Proof

**Same-class jump.** If the moving agent changes vertices inside \(A\) (or inside \(B\)), then the occupied multiset of vertices in the opposite class is unchanged. Both the mover's neighborhood-type proportions and all type counts \(A_t,B_t\) are unchanged. Hence the utility difference and potential difference are both zero. Such a jump is not a strict improvement.

**Cross-class jump.** Suppose the vacancy is in \(A\) and an agent of type \(t\) moves from \(B\) to that vacancy. Write \(x=A_t(C)\) and \(y=B_t(C)\). Before the jump there are \(a-1\) occupied neighbors of the mover in \(A\); after the jump there are \(b-1\) occupied neighbors in \(B\). Therefore

\[
 u_i(C)=\frac{a-1-x}{a-1},\qquad
 u_i(C')=\frac{b-y}{b-1},\qquad
 u_i(C')-u_i(C)=\frac{x}{a-1}-\frac{y-1}{b-1}.
\]

Only type \(t\)'s within-class pair counts change. The identity \(\binom{x+1}2-\binom{x}2=x\) and the analogous deletion identity give

\[
 \Phi(C')-\Phi(C)=\frac{x}{a-1}-\frac{y-1}{b-1},
\]

which is exactly the mover's gain. The case of a vacancy in \(B\) and a move from \(A\) follows by exchanging the two bipartition classes. The identity holds for every feasible move, whether improving, neutral, or worsening. Prohibiting the moves of immobile agents only removes edges from the possible state-transition graph, and cannot affect the identity.

**Bound and termination.** At any state, the numbers of agents in the two classes are either \((a-1,b)\) or \((a,b-1)\). The nonnegative potential obeys

\[
 0\leq\Phi(C)\leq \frac{a+b-2}{2},
\]

because for a class with \(r\) occupants the sum of within-type unordered pair counts does not exceed \(\binom r2\). Put \(L=\operatorname{lcm}(a-1,b-1)\). Every value of \(\Phi\) is an integer multiple of \(1/L\). Under any strict improvement the exact identity implies a positive increase of at least \(1/L\); hence every improvement trajectory has length at most \(\lfloor (a+b-2)L/2\rfloor\). The terminal state has no permitted improving jump and therefore is a pure Nash equilibrium. Finally \(L\leq(a-1)(b-1)\leq(a+b-2)^2/4\), yielding the cubic upper bound.

## Verification

The included `verify.py` uses standard-library exact fractions. It exhaustively checks the utility/potential identity for **658,040** individual unilateral jumps across six parameter triples, including nonregular graphs, three types, multiple nonempty type counts, same-class jumps, and worsening as well as improving deviations. It detects **160,968** strict improvements, checks nonnegativity, the universal potential bound, and the minimum positive increment. Run `python3 verify.py` from the directory containing the file. These finite tests validate the implementation of the identity, not the all-size theorem; the proof above supplies the universal statement.

## Relationship to prior work

Narayanan, Sabbagh and Voudouris introduced the fraction-of-unlike-occupied-neighbors jump game. Their 2023 preprint and 2025 journal paper prove the finite improvement property for regular graphs with one vacancy and for spider graphs with one vacancy, and ask about further bipartite topologies. Neither of those covering hypotheses includes the nonregular complete bipartite graphs \(K_{a,b}\) when \(a,b\geq2\) and \(a\ne b\). The present result gives a simpler **exact**, rather than merely ordinal, potential and a uniform polynomial bound on the number of unilateral improving moves. The previously known regular results already cover the balanced case \(a=b\), and the spider results cover the star boundary \(\min\{a,b\}=1\); neither special case is claimed as new.

Variety-seeking jump games count distinct *types* of neighbors and thus have a different payoff. Diversity-seeking swap games allow two occupied vertices to exchange occupants and have no vacancy. General type-composition games evaluate composition among agents taking the *same action*, while here a mover values the composition of the **opposite** bipartition class under capacity constraints; the consulted theorem does not state the exact potential above. No reduction from that more general result is assumed. An unknown equivalent treatment under other nomenclature remains a publication-priority risk.

## Limitations

The exact identity uses **one** vacancy, the *complete* bipartite adjacency pattern, unweighted edges, and proportions of **occupied** neighbors. It is not a result about arbitrary bipartite graphs, multiple vacancies, nonuniform edge weights, two-agent swaps, continuous behavioral types, or stochastic convergence times. The cubic bound concerns the count of strict improving updates, not the overall cost of finding an improving move and not a tight worst-case lower bound. The result has received no independent audit or validation.

## References

1. L. Narayanan, Y. Sabbagh, A. A. Voudouris, *Diversity-Seeking Jump Games in Networks*, arXiv:2305.17757 (first posted 2023-05-28), also *Autonomous Agents and Multi-Agent Systems* 39, article 32 (2025), DOI:10.1007/s10458-025-09714-8.
2. L. Narayanan, J. Opatrny, S. Tummala, A. A. Voudouris, *Variety-Seeking Jump Games on Graphs*, IJCAI 2025, pp. 4005–4013, DOI:10.24963/ijcai.2025/446.
3. Y. Li, L. Narayanan, J. Opatrny, Y. T. Xu, *Diversity-Seeking Swap Games in Networks*, arXiv:2502.13375 (2025).
4. M. Alimi, M. de la Haye, P. Lenzner, Š. Schierreich, A. Skopalik, M. Wunderlich, *An Entropy Potential for Type-Composition Games*, arXiv:2606.14428 (2026).
