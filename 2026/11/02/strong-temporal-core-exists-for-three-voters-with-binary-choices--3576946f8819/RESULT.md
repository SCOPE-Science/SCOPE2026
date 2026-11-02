# Strong temporal core exists for three voters with binary choices

## Finding

**Theorem.** Fix any integer \(\ell\ge1\). Consider three voters \(N=\{1,2,3\}\), the same two alternatives \(a,b\) in each of \(\ell\) rounds, and arbitrary nonempty approval sets \(A_{i,r}\subseteq\{a,b\}\). One alternative is chosen per round. Write \(u_i(o)=\lvert\{r:o_r\in A_{i,r}\}\rvert\).

There is an outcome \(o\) that is strongly core-stable under Definition 6.1 of Phillips et al. (2025). Moreover, it can be constructed in time \(O(\ell^4)\). A stronger, explicit sufficient property holds: \(o\) is Pareto efficient, every voter satisfies \(u_i(o)\ge\lfloor\ell/3\rfloor\), and at least two voters satisfy \(u_i(o)\ge\lfloor2\ell/3\rfloor\).

## Assumptions and scope

The horizon is arbitrary and known. Every voter approves at least one of the two alternatives in each round, but may approve both and may change approvals between rounds. We use integer, additive per-round approval satisfaction. A proposed coalition deviation controls only its selected rounds; satisfaction from such a deviation counts only approved choices on those controlled rounds, as in the original definition.

In detail, an outcome is strongly core-stable when for every nonempty coalition \(S\subseteq N\), every round subset \(R\subseteq[\ell]\) of size \(\lvert R\rvert=\lfloor\ell\lvert S\rvert/3\rfloor\), and every two-alternative selection \(y_R\) on \(R\), at least one \(i\in S\) satisfies \(u_i(o)\ge u_i(y_R)\). Equivalently, no coalition can make **every** member strictly better off using its quota of controlled rounds.

## Proof

**1. Singleton-ballot reduction.** First suppose every voter approves exactly one option in every round. Let \(v\) be the number of unanimous rounds and \(d=\ell-v\) the number of contested rounds. In a contested round, exactly one voter is in the minority. Let \(c_i\) count the contested rounds in which voter \(i\) is the minority, and relabel the voters so \(c_1\ge c_2\ge c_3\), with \(c_1+c_2+c_3=d\). Set

\[
\alpha=\lfloor d/3\rfloor,\quad
\beta=\lfloor2d/3\rfloor,\quad
h=d-\beta=\lceil d/3\rceil.
\]

In unanimous rounds choose the unanimous favorite. Initially choose the majority favorite in every contested round. Switch exactly \(t\) rounds of the \(c_1\) rounds in which voter 1 was in the minority, so that those rounds instead choose voter 1's favorite, where

\[
t=\begin{cases}
\max\{0,c_1-(d-\alpha)\},&c_2\le h,\\
c_1-h,&c_2>h.
\end{cases}
\]

This switch is feasible: in the first case \(0\le t\le c_1\) since \(d-\alpha\ge0\); in the second \(0<t\le c_1\) since \(c_1\ge c_2>h\). The resulting satisfaction counts **from the contested rounds alone** are

\[
(s_1,s_2,s_3)=(d-c_1+t,\;d-c_2-t,\;d-c_3-t).
\]

If \(c_2\le h\), then \(s_1\ge\alpha\) by the definition of \(t\). Also \(t\le h-c_2\): this is immediate if \(t=0\), and otherwise follows from \(c_1+c_2\le d\) and \(h\ge\alpha\). Therefore \(s_2,s_3\ge d-h=\beta\).

If \(c_2>h\), take \(t=c_1-h\). Then

\[
(s_1,s_2,s_3)=(d-h,\;c_3+h,\;c_2+h).
\]

Thus \(s_1=\beta\) and \(s_2\ge h\ge\alpha\). Since \(d\le3h\) and \(c_2>h\), we have \(c_2+h\ge d-h=\beta\), so \(s_3\ge\beta\). Both cases give every voter at least \(\alpha\) and two voters at least \(\beta\).

Each unanimously approved round adds one to every voter's satisfaction. For \(q\in\{1,2\}\), the elementary inequality

\[
v+\lfloor qd/3\rfloor\ge\lfloor q(d+v)/3\rfloor
\]

therefore gives every voter at least \(\lfloor\ell/3\rfloor\) and at least two voters at least \(\lfloor2\ell/3\rfloor\) over the entire horizon.

**2. Nonempty multiapproval ballots.** For each ballot \(\{a,b\}\), temporarily retain only \(a\); leave singleton ballots unchanged. This creates a valid singleton-ballot election. Apply step 1 and retain its outcome \(o^0\). Restoring the original approvals can only increase each voter's satisfaction for any fixed outcome. Consequently, \(o^0\) satisfies the same lower bounds in the original election.

**3. Pareto completion.** Among outcomes \(y\) with \(u_i(y)\ge u_i(o^0)\) for every \(i\), choose one maximizing \(u_1(y)+u_2(y)+u_3(y)\). This set is nonempty and its maximum exists. A strict coordinatewise Pareto improvement over the selected outcome would also dominate \(o^0\) and have larger total welfare, a contradiction. Hence the selected \(o\) is globally Pareto efficient and retains the two threshold guarantees.

For a polynomial construction, use dynamic programming over rounds and achievable satisfaction triples \((x_1,x_2,x_3)\) with each coordinate in \(\{0,\ldots,\ell\}\). The two decisions in each round give at most two transitions per state. There are at most \(O(\ell^3)\) states per layer and \(\ell\) layers; store predecessors, then choose a final triple dominating \(u(o^0)\) and maximizing total satisfaction. The running time and stored certificate size are at most \(O(\ell^4)\).

**4. Excluding every coalition deviation.** For a singleton coalition, its controlled-round quota is \(\lfloor\ell/3\rfloor\). Any deviation can satisfy that voter in at most that many controlled rounds, while \(u_i(o)\) is at least the quota. For a two-voter coalition, the quota is \(\lfloor2\ell/3\rfloor\). Every pair of voters contains at least one of the two high-satisfaction voters constructed above, whose satisfaction is already at least the pair's quota. Finally, the grand coalition controls all \(\ell\) rounds; a deviation strictly improving all three would be a Pareto improvement over \(o\), impossible by step 3. These are every possible nonempty coalition. Therefore \(o\) satisfies the stated strong core axiom. \(\square\)

## Verification

Run the standalone Python 3 script `verify_three_core.py`. It computes a threshold-feasible outcome via the construction, independently performs a complete exact-integer satisfaction-vector dynamic program to choose a Pareto completion, and then enumerates all coalitions and all quota-sized suboutcomes to check strong core directly. The script checks all \(31{,}464\) unordered round-multisets of all \(27\) full-ballot types through horizon four, another \(1{,}715\) seven-type structural profiles through horizon six, and \(900\) deterministic randomized full-ballot profiles through horizon seven. These finite tests are consistency checks, not the proof of the all-horizon statement.

## Relationship to prior work

Phillips, Elkind, Teh, and Wąs (2025) define the strong temporal core and show that it can be empty in general; their Section 6 and relevant appendix examples do not give this all-horizon positive theorem for three voters and two alternatives. Their Proposition 6.2 establishes implications **from** strong core, not an existence guarantee **for** strong core. Masařík, Pierczyński, and Skowron (2023) formulate proportionality for constrained public decisions and discuss the distinction from core stability; their satisfiable proportionality conditions are not equivalent to the quantified strong-core condition here. Chandak, Goel, and Peters (2023) study temporal JR/PJR-style proportionality rather than this coalition-deviation notion.

## Limitations

This result requires three voters, exactly two available alternatives, additive dichotomous satisfaction, and nonempty approval ballots in every round. It does not establish strong-core existence outside that domain, characterize every strongly core-stable outcome, or improve the general-case impossibility result. The finite verifier is not an infinite certificate, and full external priority searches cannot rule out unindexed earlier special-case results. Independent scientific audit has not been performed.

## References

- Bradley Phillips, Edith Elkind, Nicholas Teh, and Tomasz Wąs. *Strengthening Proportionality in Temporal Voting*. arXiv:2505.22513v1, May 28, 2025. Definition 6.1 and Proposition 6.2. https://arxiv.org/abs/2505.22513
- Tomáš Masařík, Grzegorz Pierczyński, and Piotr Skowron. *A Generalised Theory of Proportionality in Collective Decision Making*. arXiv:2307.06077, 2023. https://arxiv.org/abs/2307.06077
- Nikhil Chandak, Shashwat Goel, and Dominik Peters. *Proportional Aggregation of Preferences for Sequential Decision Making*. arXiv:2306.14858, 2023. https://arxiv.org/abs/2306.14858
