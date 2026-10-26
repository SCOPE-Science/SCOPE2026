# Three item types already defeat deterministic online temporal EF1

## Finding

Consider a stream of indivisible goods allocated immediately and irrevocably among three agents with nonnegative additive valuations. There are only three distinct item types, whose valuation vectors, in agent order, are
\[
A=(0,1,2),\qquad B=(0,2,1),\qquad C=(1,2,2).
\]
For this fixed valuation system, **no deterministic online allocation rule can maintain envy-freeness up to one good (EF1) after every arrival for all arrival sequences**. More precisely, an adaptive choice of types forces a violation by the seventh item, even if the rule knows the type vectors and the seven-item horizon in advance. For this same valuation system, the adversary cannot force a violation within six arrivals.

In contrast, **every individual fixed sequence of at most seven arrivals from these three types admits an allocation that is EF1 after each arrival**, if the entire sequence is known in advance. Thus the obstruction is genuinely to irrevocable online decisions, not to temporal EF1 feasibility for any particular short sequence.

A previously established positive theorem guarantees online temporal EF1 whenever there are at most two item types. Together, that established theorem and the present three-type example give the exact type-count threshold for a universal deterministic online guarantee in this model: two types always suffice; three need not.

## Assumptions and scope

There are precisely three agents, fixed throughout, with utilities additive across items. Type \(t\in\{A,B,C\}\) has the stated valuation vector. Items arrive singly. After observing the current type, an allocator selects one recipient without transferring any previously assigned item. The incoming type may be selected by an adversary who observes all preceding recipients, but the valuation vectors, set of possible types, and seven-item horizon are public before the process. No randomization is assumed. For a cumulative allocation \((S_1,S_2,S_3)\), EF1 means that for every ordered pair of distinct agents \((i,j)\), there exists an item \(g\in S_j\) with \(v_i(S_i)\ge v_i(S_j\setminus\{g\})\), or there is no envy to begin with. Zero-valued goods are permitted.

## Proof

**Count-state reduction.** Let \(s_{t,i}\in\mathbb Z_{\ge0}\) be the number of goods of type \(t\) assigned to agent \(i\). These nine counts encode all relevant information: item identities and chronological order within a type have no further effect on additive EF1. Write \(s\) for the flattened count vector with each type's three recipients consecutive. Let \(V_{t,i}\) be the integer entries of the displayed valuation vectors. For each ordered pair of distinct agents, define
\[
U_i(s)=\sum_t s_{t,i}V_{t,i},\quad
R_{ij}(s)=\sum_t s_{t,j}V_{t,i},\quad
M_{ij}(s)=\max\bigl(\{0\}\cup\{V_{t,i}:s_{t,j}>0\}\bigr).
\]
Then the state is EF1 exactly when
\[
U_i(s)+M_{ij}(s)\ge R_{ij}(s)\quad\text{for all }i\ne j.
\]
This is a finite integer test, including the empty-bundle boundary.

**Adversarial game.** Put \(W_0(s)=\mathrm{false}\) for EF1 states and, for integer \(h\ge1\), define
\[
W_h(s)=\bigvee_{t\in\{A,B,C\}}\ \bigwedge_{i=1}^{3}
\left[\neg\mathrm{EF1}(s+e_{t,i})\ \lor\ W_{h-1}(s+e_{t,i})\right].
\]
Here \(e_{t,i}\) adds exactly one item of type \(t\) to recipient \(i\). This recurrence is exact by backward induction: the adversary chooses a type, then the allocator chooses its recipient; fairness failure ends the game immediately. It contains every possible deterministic history-dependent allocator, since counts are sufficient for future fairness.

**Finite exact certificate.** The attached `STRATEGY.json` lists one adversarial next type for every fair state reachable when following a particular winning adversarial policy from the empty state for seven turns. It contains \(42\) distinct count states. For each displayed state, the standalone `verify_strategy.py` checks all three recipient choices: the resulting state either violates the integer EF1 inequalities immediately or, with positive time remaining, is another listed state. There are \(126\) checked responses, of which \(74\) violate EF1 immediately; there is no fair seventh-item terminal branch. Induction over the strictly increasing item count therefore proves that every allocator loses by turn seven. The same checker independently evaluates the full exact Boolean recurrence and obtains \(W_7(0)=\mathrm{true}\) and \(W_6(0)=\mathrm{false}\).

**Hindsight contrast.** The checker separately performs exhaustive exact dynamic programming over all \(3^\ell\) fixed type sequences for each \(1\le\ell\le7\), retaining every EF1-feasible recipient-count state at every prefix. Every sequence has a nonempty set at the final prefix. This establishes the asserted \(3279\) separate existence claims without replacing the universally quantified online statement by a claim about a fixed adversarial sequence.

## Verification

Run `python verify_strategy.py` from the same directory as `STRATEGY.json` (Python standard library only). The program confirms the valuation data, nonnegative integer states, graph reachability and closure of all certificate branches, the exact six-/seven-turn minimax outcomes, and temporal feasibility of all \(3279\) fixed sequences of lengths one through seven. The certificate is a finite exhaustive proof object for the specific seven-turn instance; neither floating-point approximation nor random sampling is used. A separate implementation with explicit per-agent item bundles also reproduced the six-/seven-turn minimax distinction.

## Relationship to prior work

Choi, Li and Teh (2026), Theorem 3.1, provide an online cyclic rule guaranteeing temporal EF1 for at most two item types (indeed for mixed items); that positive guarantee is **not new here**. Their three-type discussion illustrates that the particular cyclic rule need not achieve EF1, whereas the present result rules out **every** deterministic online rule on one concrete three-type all-goods instance. Elkind et al. (2024) and He et al. (2019) established more general temporal-fairness obstructions, including a 23-good example for which a temporal EF1 allocation does not exist even with complete foresight. This finding instead separates online and clairvoyant feasibility at three types and seven items. Cohen, Teh and Wooldridge (2026) prove randomized online EF1 lower bounds against oblivious adversaries for different scaling regimes; those do not directly determine this fixed-three-agent, fixed-three-type adaptive minimax threshold.

## Limitations

The seven-item bound is verified for the **specified valuation vectors**; no claim is made that seven is the smallest universal adversarial horizon over every three-type valuation system. The positive two-type side comes from cited literature, not an independent reproof here. The obstruction concerns deterministic allocators against an adaptive type adversary. It is not a lower bound on the success probability of randomized rules against an oblivious arrival stream. The short-sequence hindsight statement is a separate finite exhaustive result; it does not establish hindsight feasibility for longer streams. Historical priority of the exact three-type witness remains uncertain despite targeted comparisons.

## References

- Kui-Wang Choi, Minming Li, Nicholas Teh, *Temporal Fair Division of Indivisible Mixed Manna: Tractable Settings* (first submitted 2026-08-20), arXiv:2608.20033, https://arxiv.org/abs/2608.20033 .
- Edith Elkind, Alexander Lam, Mohamad Latifian, Tzeh Yuan Neoh, Nicholas Teh, *Temporal Fair Division of Indivisible Items* (first submitted 2024-10-18), arXiv:2410.14593, https://arxiv.org/abs/2410.14593 .
- Jiafan He, Ariel D. Procaccia, Alexandros Psomas, David Zeng, *Achieving a Fairer Future by Changing the Past*, IJCAI 2019, https://www.ijcai.org/Proceedings/2019/49 .
- Cohen, Teh and Wooldridge, *Online Fair Division Against an Oblivious Adversary* (2026), arXiv:2609.28333, https://arxiv.org/abs/2609.28333 .
