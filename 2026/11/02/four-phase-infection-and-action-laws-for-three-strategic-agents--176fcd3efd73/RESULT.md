# Four-phase infection and action laws for three strategic agents in the intermediate-immunity gap

## Finding
For the homogeneous stochastic virus-spread best-response process on the three-vertex complete graph, with one initially infected agent and common initial action \(a\), the previously untreated intermediate-immunity interval
\[
0<a<1,\qquad \frac a2<\tau<\min\{a,\frac12\}
\]
has an exact four-phase final-state law. Define
\[
\theta_0=\frac{\sqrt{1+8a}-1}{4},\qquad
\theta_1=\frac{a}{1+a},\qquad
\theta_2=\frac{\sqrt{a^2+8a}-a}{4}.
\]
These satisfy \(a/2<\theta_0<\theta_1<\theta_2<1/2\). Let \(K\) be the number of agents eventually infected. In the domain above,
\[
\begin{aligned}
\Pr(K=1)&=\tfrac13\mathbf 1_{\{\tau\ge\theta_1\}},\\
\Pr(K=2)&=\tfrac19\mathbf 1_{\{\tau\ge\theta_0\}}+
             \tfrac1{18}\mathbf 1_{\{\tau\ge\theta_2\}},\\
\Pr(K=3)&=1-\Pr(K=1)-\Pr(K=2).
\end{aligned}
\]
Equivalently, as \(\tau\) passes the three thresholds the ordered probabilities \((\Pr(K=1),\Pr(K=2),\Pr(K=3))\) are respectively
\[
(0,0,1),\quad (0,\tfrac19,\tfrac89),\quad
(\tfrac13,\tfrac19,\tfrac59),\quad
(\tfrac13,\tfrac16,\tfrac12).
\]
The first interval is \(a/2<\tau<\theta_0\), and each later interval begins *at* its left threshold; intervals outside \(\tau<\min\{a,1/2\}\) are empty. In particular, the final (fourth) phase is feasible precisely when \(a>1/3\).

The limiting action profile is determined by the limiting infection set: if only agent 1 is infected, it equals \((1,u,u)\) with \(u=\tau/(1-\tau)\); if exactly one susceptible agent \(i\) remains, its limiting action is \(\tau\) and both infected agents' actions are 1; if all are infected the profile is \((1,1,1)\). Conditional on \(K=2\), either of the initially susceptible agents has the same probability of being the unique survivor. Hence the displayed law also determines the joint limiting distribution of infections and actions.

## Assumptions and scope
There are exactly three agents and every pair is linked by the same positive edge weight, normalized to one. Agent 1 is infected at the start; agents 2 and 3 are susceptible. All initially choose action \(a\), and all have the same infection-immunity threshold \(\tau\), subject to the strict inequalities above. There is no recovery. Every epoch independently selects one of the three agents uniformly. Infected agents best respond with action 1. A susceptible with infected-neighbor total action \(W\) and all-neighbor total action \(Z>0\) chooses \(\min\{1,\tau Z/W\}\) if \(W>0\), and 1 otherwise. After the chosen agent updates, all susceptible agents whose own action multiplied by \(W/Z\) is **strictly greater** than \(\tau\) become infected simultaneously, using the infected set before this epoch. The process is exactly the rule of Karmakar, Podder, Roy and Sadhukhan, specialized to three agents; the infection check occurs after the action update. All limits in this theorem are almost sure limits under the independent uniform choices. No stochastic-contact transmission beyond this deterministic exposure test is assumed.

## Proof
First, \(a/2<\tau\) means the initial two susceptible agents are safe: each has exposure \(1/2\). Before the first update by agent 1, its action remains \(a\), and susceptible actions can only increase; an updated susceptible sets its own exposure at or below \(\tau\) and increasing the chosen action decreases the other's exposure. Therefore no infection occurs before agent 1 is first selected. The first selected susceptible, call it \(A\), changes its action from \(a\) to exactly \(2\tau\), as \(a<2\tau<1\), leaving the other susceptible, \(B\), at \(a\).

**Case 1: agent 1 is selected first.** This happens with probability \(1/3\). Both susceptible exposures immediately become \(a/(1+a)\). If \(\tau<\theta_1=a/(1+a)\), both are infected. If \(\tau\ge\theta_1\), both remain susceptible and safe. Thereafter each susceptible best response is \(x\mapsto\tau(1+y)\), where \(y\) is the other susceptible's action. The actions are nondecreasing from \(a\), remain safe because an opponent's increase lowers exposure, and tend to the unique fixed point \(u=\tau/(1-\tau)<1\); the asynchronous coordinate map is contractive with constant \(\tau<1/2\). Hence \(K=1\) exactly in the latter subcase.

**Case 2: a susceptible is selected first.** This happens with probability \(2/3\). Until agent 1 is selected, repeated updates of \(A\) alone do nothing, and the competition for the next first selection among agent 1 and \(B\) is a fair race.

**Case 2a: agent 1 wins this race**, conditional probability \(1/2\). On its update to 1, \(A\) is infected because \((2\tau)/(1+a)>\tau\). Agent \(B\), still at action \(a\), is infected simultaneously precisely if \(a/(1+2\tau)>\tau\), or \(\tau<\theta_0\), since \(\theta_0+2\theta_0^2=a\). If \(\tau\ge\theta_0\), \(B\) initially survives but, while both others are infected, has exposure 1. It survives indefinitely exactly if it is the very next agent selected, giving it the chance to decrease its action from \(a>\tau\) to \(\tau\); that event has probability \(1/3\). All other next choices cause immediate infection. This yields a contribution \((2/3)(1/2)(1/3)=1/9\) to \(\Pr(K=2)\) when \(\tau\ge\theta_0\).

**Case 2b: \(B\) wins the race**, conditional probability \(1/2\). Its first response is
\[
b=\min\{1,\tau(a+2\tau)/a\}.
\]
The equality \(b=1\) is equivalent to \(2\tau^2+a\tau\ge a\), or \(\tau\ge\theta_2\). Before agent 1's selection the two susceptible actions never decrease and no one is newly infected. At the moment agent 1 switches from \(a\) to 1, \(B\) becomes infected: after its first update \(b>2\tau\), while the other susceptible action is at most 1, so \(b>\tau(1+x_A)\). For \(A\), infection follows too unless its action remains exactly \(2\tau\) while \(B\) has action 1. Indeed, if \(x_A>2\tau\), then \(x_A>\tau(1+x_B)\) since \(x_B\le1\). If \(x_A=2\tau\), \(B\) has not changed after its initial response, so \(A\) is infected iff \(b<1\), and is exactly safe when \(b=1\).

Thus an additional survivor arises only when \(\tau\ge\theta_2\), when \(B\) reaches 1 on its first selection and agent 1 is selected before \(A\)'s next nontrivial update, a further fair race with probability \(1/2\). In that exceptional state \(B\) is infected and \(A\), at action \(2\tau>\tau\), is safe at exact exposure \(\tau\). To avoid infection after both others are infected, \(A\) must be the next selected agent (probability \(1/3\)) and reduce its action to \(\tau\). This contributes \((2/3)(1/2)(1/2)(1/3)=1/18\) to \(\Pr(K=2)\). Otherwise everyone is infected. All these events are determined by finitely many first-appearance races, each completed almost surely. Together with Case 1 and Case 2a, this proves the distribution.

For thresholds, \(\theta_0\) is the positive root of \(t+2t^2=a\), \(\theta_1\) is the root of \(t(1+a)=a\), and \(\theta_2\) the positive root of \(2t^2+at=a\). At \(t=a/2\) the first polynomial is below \(a\); at \(t=\theta_1\) it exceeds \(a\) by \(a^2(1-a)/(1+a)^2\). At \(t=\theta_1\), the third polynomial is below \(a\) by \(a(1-a)/(1+a)^2\); at \(t=1/2\) it exceeds \(a\) by \((1-a)/2\). The three roots thus have the claimed strict order. Finally \(\theta_2<a\) iff \(a>1/3\). At equality in each threshold test, infection does not occur because infection requires a strict inequality, so the claimed weak threshold signs are exact.

Once there is one remaining susceptible with both other agents infected, its optimal response is \(\tau\), and an updated action \(\tau\) remains safe forever. When all agents are infected, every agent eventually updates to 1. In the single-infection case the contractive response map gives \((1,u,u)\). Both initially susceptible labels are exchangeable, so conditional \(K=2\) survivor labels have equal probability. This establishes the joint limit.

## Verification
The standalone program `check_three_agent.py` implements the epoch rule with exact rational arithmetic, independently of the race decomposition. It propagates every possible uniform-choice outcome for 24 epochs and collapses only states whose ultimate infection count is justified by an absorbing inequality. For 96 distinct rational \((a,\tau)\) pairs spanning all four phases and three exact jump boundaries, it verifies 288 probability enclosures of the form \(P_{\mathrm{settled},k}\le P_k\le P_{\mathrm{settled},k}+P_{\mathrm{unresolved}}\). The worst unresolved mass in these tests is less than \(0.00006\). The verification includes the boundary triples \((a,\tau)=(18/25,2/5),(2/3,2/5),(8/15,2/5)\). These finite-horizon enclosures are consistency tests, **not** an exhaustive proof of infinite-time convergence or of uniqueness in the literature; the proof above supplies the infinite-time argument.

## Relationship to prior work
Karmakar, Podder, Roy and Sadhukhan introduced this exact action/infection process in their 2023 preprint, later published in 2025. In the revised full text, Theorems 7–8 cover \(1/(n-1)\le\tau<a<1\), and Theorems 9–10 cover \(\tau\le a/(n-1)\) for \(\tau<a<1\). They do not determine the interval \(a/(n-1)<\tau<1/(n-1)\), whose \(n=3\) specialization is precisely the present domain. Their different \(a=0\), \(a=1\), and \(a\le\tau\) cases are also not implications of the present statement. This note gives a complete exact law for the smallest nontrivial population within that omitted interval, including the corresponding action limits. Other network epidemic games and compartmental models have different state transitions; their thresholds do not directly imply these four probabilities. An equivalent result could exist in unindexed specialist work, and no absolute priority claim is made.

## Limitations
The theorem assumes exactly three agents, homogeneous initial actions and immunity, equal positive interaction weights, independently uniform sequential updates, irreversible infection, and strict infection above the threshold. It does **not** classify larger populations, heterogeneous immunity, recovery, arbitrary graphs, or alternative infection timing. The four phase regions are understood after intersection with the stated open domain; the fourth is empty when \(a\le1/3\). The finite verifier is not an infinite proof, and publication-priority assessment is limited to the sources explicitly compared.

## References
- S. Karmakar, M. Podder, S. Roy, and S. Sadhukhan, *The spread of an epidemic: a game-theoretic approach*, arXiv:2303.09771, first released 17 March 2023. https://arxiv.org/abs/2303.09771
- Same authors, revised open-access manuscript, Sections 2 and 3.4 and Appendix B. https://sayarkarmakar.github.io/publications/AAP_revision.pdf
- Same authors, *Advances in Applied Probability* 57 (2025), 749–810, DOI:10.1017/apr.2024.64. https://doi.org/10.1017/apr.2024.64
