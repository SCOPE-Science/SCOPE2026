# A sharp switch potential for mixed imitation and best response on complete coordination networks

## Finding

**Theorem.** In the homogeneous, opponent-coordinating, two-strategy complete-network process defined below, put
\[
a=R-T>0,\quad b=P-S>0,\quad t=\frac{(n-1)b}{a+b},\quad h=\lfloor t\rfloor+1.
\]
If \(k\) is the number of agents playing \(A\), the integer-valued function \(\Phi(k)=|k-h|\) **increases strictly after every actual strategy switch**, independently of the activated agent and of the fixed mixture of best responders and imitators. Consequently every trajectory has at most \(n-1\) strategy switches; this bound is sharp even when both behavioral types are present. Every activation sequence that activates each agent infinitely often eventually reaches an absorbing strategy profile. If at least one agent is a best responder, that profile is always unanimous.

When all agents imitate, the only possible additional absorbing profiles have \(2\le k\le n-2\) and satisfy the exact earnings equality
\[
(k-1)R+(n-k)S=kT+(n-k-1)P.
\]
There is at most one admissible mixed value of \(k\); when it exists, all \(\binom nk\) profiles with that many \(A\)-players are absorbing. For \(n=4\) and \((R,S,T,P)=(4,-1,0,2)\), all six profiles with two players on each strategy are absorbing, showing that the best-responder qualification in the consensus statement is necessary.

## Assumptions and scope

Fix an integer \(n\ge2\) and the simple complete graph on \(n\) labeled players. At every discrete step exactly one player is activated. Each player has a fixed type, either an *imitator* or a *best responder*. Both strategies \(A,B\) are available and every player uses the **same** payoff matrix
\[
\begin{array}{c|cc}&A&B\\\hline A&R&S\\ B&T&P\end{array},\qquad \min\{R,P\}>\max\{S,T\}.
\]
Each player's *current earnings* sum its matrix payoffs against the other \(n-1\) players; self-interactions are excluded. A best responder selects the strategy maximizing its counterfactual earnings against the other players' current choices and retains its choice at an exact tie. An imitator examines the **other** \(n-1\) players' current earnings and copies the strategy of a highest-earning neighbor; when both strategies occur among highest earners, it retains its own strategy. Types do not change. A persistently activating schedule visits every player infinitely often; no bound on the gap between visits is assumed.

An *actual switch* is an update changing the active player's strategy. An *absorbing profile* is one from which no activation produces an actual switch. The statement bounds switches, not the total number of activation events, since a fair activation schedule may insert arbitrarily many no-change steps.

## Proof

Write \(a=R-T\), \(b=P-S\), \(c=R-S\), and \(d=P-T\). All four are strictly positive by assumption, and \(a+b=c+d\). Thus
\[
0<t=\frac{(n-1)b}{a+b}<n-1,\qquad 1\le h=\lfloor t\rfloor+1\le n-1.
\]
For an activated player currently playing \(A\), the counterfactual advantage of playing \(A\) over \(B\) is
\[
(k-1)a-(n-k)b=(a+b)(k-1-t).
\]
For one currently playing \(B\), the advantage is
\[
ka-(n-k-1)b=(a+b)(k-t).
\]
In particular, when \(k<h\), an \(A\)-best-responder can change only to \(B\) and a \(B\)-best-responder cannot change to \(A\). When \(k>h\), the reverse holds: only \(B\)-to-\(A\) best-response switches are possible.

Suppose that both strategies are represented. Every \(A\)-player earns
\[
U_A(k)=(k-1)R+(n-k)S,
\]
whereas every \(B\)-player earns
\[
U_B(k)=kT+(n-k-1)P.
\]
Their difference is
\[
U_A(k)-U_B(k)=(a+b)(k-w),\quad
w=t+\frac{c}{a+b},\quad t<w<t+1.
\]
When \(k<h\) we have \(k\le t<w\). Any \(A\)-imitator therefore switches to \(B\) upon activation, while any \(B\)-imitator stays \(B\): the latter has another \(B\) neighbor because \(k<h\le n-1\) entails at least two \(B\)-players. Hence every switch for \(k<h\) decreases \(k\) by one. Similarly, when \(k>h\) we have \(k>t+1>w\); there are at least two \(A\)-players, so every switch increases \(k\) by one. At \(k=h\), either sign of switch can occur but any switch changes \(|k-h|\) from zero to one. Unanimous profiles do not switch: best response prefers coordination, and all neighbors of an imitator choose the same strategy. Therefore every actual switch strictly increases \(\Phi(k)=|k-h|\).

Since \(0\le\Phi(k)\le\max\{h,n-h\}\le n-1\), there can be at most \(n-1\) actual switches. After the last switch the state is fixed. If it were not absorbing, at least one player would have a different response when activated; persistence would eventually activate that player and create another switch, a contradiction. Hence all persistent schedules eventually reach an absorbing profile.

It remains to classify absorbing profiles. For \(0<k<h\), every \(A\)-player, whatever its type, switches to \(B\) when activated; likewise for \(h<k<n\), every \(B\)-player switches to \(A\). Thus only \(k=h\) can support a mixed absorbing profile. At \(k=h\), set \(F=U_A(h)-U_B(h)\). If \(F>0\), every \(B\)-imitator changes to \(A\); if \(F<0\), every \(A\)-imitator changes to \(B\). If \(F=0\), then \(h=w\) and consequently \(t<h<t+1\), so **every best responder** switches when activated (both best-response advantages are strict and point opposite to its current choice). Hence, with at least one best responder no mixed profile is absorbing: when \(F\ne0\), any member of the disfavored strategy who is a best responder also changes, except possibly at a best-response tie. At the sole possible tie \(t=h-1\), one has \(F=(a+b)(h-w)>0\), and every \(B\)-player, whether best responder or imitator, changes to \(A\); in the generic case \(h-1<t<h\), both best-responder types change. Thus consensus is forced.

If all agents imitate, \(F=0\) is necessary for a mixed absorbing profile. If \(k=1\) or \(k=n-1\), the lone player of the minority strategy has **no same-strategy neighbor** and therefore changes even when the two types have equal earnings; hence these states are not absorbing. If \(2\le k\le n-2\) and \(F=0\), every player sees both strategies among its neighbors, sees them earn equally, and retains its choice by the tie rule. Finally \(F(k)=(a+b)(k-w)\) is strictly increasing, so at most one integer \(k\) satisfies \(F(k)=0\); if so it must be \(h\). This proves the claimed classification.

For sharpness at each \(n\ge2\), take \((R,S,T,P)=(n,0,0,1)\), one initial \(A\)-imitator and \(n-1\) initial \(B\)-best-responders. Here \(t=(n-1)/(n+1)<1\), so \(h=1\). Activate the \(B\)-best-responders one by one: each strictly prefers \(A\) and changes, and the sequence makes exactly \(n-1\) switches before unanimity. Extend the finite activation prefix by repeating all agents to obtain a persistent sequence. For the nonconsensus example \((n,R,S,T,P)=(4,4,-1,0,2)\), the condition \(\min\{R,P\}>\max\{S,T\}\) holds and \(U_A(2)=U_B(2)=2\), proving the six absorbing profiles.

## Verification

The standalone file `verify.py` independently implements one-step current-earnings imitation (neighbors only) and counterfactual best response (excluding self), both with exact tie-retention rules. It exhaustively enumerates all strategies and individual activations for \(5700\) finite parameter-and-type cases, encompassing \(171120\) states and \(945888\) one-player activations, checking monotonicity, all equilibria, and longest switching paths by dynamic programming. It also checks sharp examples through \(n=14\). This extensive finite test is a regression check **not** a proof of the theorem for arbitrary \(n\); the preceding symbolic inequalities are the proof.

To reproduce, run `python3 verify.py` with a standard Python 3 interpreter; no external packages are required.

## Relationship to prior work

Hasheminejad and Ramazi (2023, arXiv:2306.03243; IEEE Control Systems Letters) study mixed best-response and imitation dynamics on coordination networks and establish convergence on paths and several sparse-tree families using a *section-count* potential. Their general-network potential question motivates investigating a very different dense topology. The complete-graph argument here requires homogeneous payoffs and the stated strict opponent-coordination inequalities; it does **not** imply their heterogeneous-payoff general-network conjecture.

Le, Rajaee, and Ramazi (2022, arXiv:2202.04782) study mixed coordination/anticoordination/imitator populations in a different aggregate-population convention. Fu and Ramazi (2020, arXiv:2006.03438) investigate heterogeneous imitation dynamics, while Ramazi, Riehl, and Cao (2016, PNAS) address best responders. None of the inspected statements was found to supply the present neighboring-payoff, single-switch, sharply bounded mixed-update potential. This is a **qualified literature comparison**, not a claim of definitive global publication priority.

## Limitations

The proof covers **complete graphs, identical payoffs, binary strategies, strict opponent-coordination, fixed behavioral types, single-player sequential activation, and specified deterministic ties**. It does not cover heterogeneous payoff matrices, general dense graphs, simultaneous activation, randomized response rules, or every plausible convention for imitation ties. Persistent activation entails finite-time absorption but gives no uniform upper bound on the number of *activation steps* before absorption. Relevant broader convergence results or unpublished work may limit novelty; independent scientific verification has not been performed.

## References

1. N. Hasheminejad and P. Ramazi, *Equilibration of Coordinating Imitation and Best-Response Dynamics* (2023), arXiv:2306.03243, https://arxiv.org/abs/2306.03243 .
2. H. Le, A. Rajaee, and P. Ramazi, *Heterogeneous Mixed Populations of Coordinating, Anticoordinating, and Imitating Individuals* (2022), arXiv:2202.04782, https://arxiv.org/abs/2202.04782 .
3. H. Fu and P. Ramazi, *Evolutionary Matrix-Game Dynamics Under Imitation in Heterogeneous Populations* (2020), arXiv:2006.03438, https://arxiv.org/abs/2006.03438 .
4. P. Ramazi, J. R. Riehl, and M. Cao, *Networks of conforming or nonconforming individuals tend to reach satisfactory decisions* (2016), PNAS, https://doi.org/10.1073/pnas.1610244113 .
5. T. Raducha and M. San Miguel, *Coordination and equilibrium selection in games: the role of local effects* (2021), arXiv:2110.10036, https://arxiv.org/abs/2110.10036 .
