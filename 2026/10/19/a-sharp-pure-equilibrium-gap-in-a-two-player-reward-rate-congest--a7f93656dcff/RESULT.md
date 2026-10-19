# A sharp pure-equilibrium gap in a two-player reward-rate congestion game

## Finding
An explicitly specified two-player, three-resource reward-rate congestion game has **no pure Nash equilibrium** throughout the sharp parameter interval \(5/4<\eta<2\), even though reward strictly decreases and execution time strictly increases with congestion on every resource. On that interval the game has a strict, four-step unilateral improvement cycle and a unique mixed equilibrium: player 1 selects the bundle \(\{B,C\}\) with probability \(\tfrac43(2-\eta)\), and player 2 selects the same bundle with probability \(2/5\). Outside the interval at least one pure Nash equilibrium exists. The absence of pure equilibrium is robust to sufficiently small joint perturbations of all positive resource rewards and times.

## Assumptions and scope
There are exactly two strategic players and three resources \(E=\{A,B,C\}\). Player 1's finite strategy set is \(\mathcal A_1=\{X,Y\}\), where \(X=\{B,C\}\) and \(Y=\{C\}\). Player 2's strategy set is \(\mathcal A_2=\{U,V\}\), where \(U=\{B,C\}\) and \(V=\{A\}\). Given actions, \(n_e\) is the number of players whose selected set contains resource \(e\). Each agent maximizes its **own** reward-per-time ratio
\[
J_i(a)=\frac{\sum_{e\in a_i} r_e(n_e(a))}{\sum_{e\in a_i}t_e(n_e(a))}.
\]
All resources have positive reward and strictly positive time; every feasible action is nonempty. Fix any \(\eta>0\). The resource data \((r_e(k),t_e(k))\), at occupancies \(k=1,2\), are

| Resource | \(k=1\) | \(k=2\) |
|---|---|---|
| \(A\) | \((2\eta,2)\) | \((\eta,3)\) |
| \(B\) | \((5,1)\) | \((4,2)\) |
| \(C\) | \((6,1)\) | \((1,2)\) |

For each resource \(r_e(1)>r_e(2)>0\) and \(0<t_e(1)<t_e(2)\). Resource \(A\) is never chosen by both players in the stipulated strategy sets, but its two-user parameters are defined consistently. No claim concerns other action sets or arbitrary reward-rate games.

## Proof
**Exact payoff table.** Evaluating both ratio payoffs at all four feasible profiles gives
\[
\begin{array}{c|cc}
 &U&V\\ \hline
X&(5/4,5/4)&(11/2,\eta)\\
Y&(1/2,2)&(6,\eta).
\end{array}
\]
For instance, under \((Y,U)\), resource \(C\) is used twice while \(B\) is used once. Therefore player 1's rate is \(1/2\) and player 2's is \((5+1)/(1+2)=2\). The other entries follow by the same direct substitutions. Entries are ordered (player 1 payoff, player 2 payoff).

**Best replies and parameter classification.** Against \(U\), player 1 uniquely prefers \(X\) because \(5/4>1/2\). Against \(V\), player 1 uniquely prefers \(Y\) because \(6>11/2\). Against \(X\), player 2 prefers \(V\) precisely when \(\eta>5/4\), with indifference at equality; against \(Y\), player 2 prefers \(U\) precisely when \(\eta<2\), with indifference at equality. The four profiles exhaust all pure choices. It follows that \((X,U)\) is a pure Nash equilibrium if and only if \(\eta\le5/4\), \((Y,V)\) is a pure Nash equilibrium if and only if \(\eta\ge2\), and neither \((X,V)\) nor \((Y,U)\) can be a pure Nash equilibrium for any positive \(\eta\). Hence the *exact* pure-equilibrium nonexistence region is \(5/4<\eta<2\).

**Strict improvement cycle.** For every \(\eta\) in this open interval, unilateral best replies follow
\[
(X,U)\ \xrightarrow{\,2\,}\ (X,V)\ \xrightarrow{\,1\,}\ (Y,V)\ \xrightarrow{\,2\,}\ (Y,U)\ \xrightarrow{\,1\,}\ (X,U).
\]
The successive improvement gains are exactly \(\eta-5/4\), \(1/2\), \(2-\eta\), and \(3/4\), all strictly positive. In particular the direct ratio game cannot admit a generalized ordinal potential (a scalar function strictly increasing on every strictly improving unilateral deviation) anywhere in the open interval. This observation is compatible with the fixed-parameter *transformed* additive game's Rosenthal potential: that is a different game.

**Unique mixed equilibrium.** Let \(p\) be the probability that player 1 chooses \(X\), and let \(q\) be the probability that player 2 chooses \(U\). Player 1 is indifferent exactly when
\[
q(5/4-1/2)+(1-q)(11/2-6)=0,
\qquad q=2/5.
\]
Player 2 is indifferent exactly when
\[
p(5/4-\eta)+(1-p)(2-\eta)=0,
\qquad p=\tfrac43(2-\eta).
\]
For \(5/4<\eta<2\) both probabilities lie strictly between zero and one. Consequently these mixtures form a Nash equilibrium. No pure equilibrium exists in this region. In any non-pure equilibrium of a nondegenerate two-by-two game, both players must mix (otherwise an opponent's unique strict best reply and then the remaining player's unique strict best reply imply a pure equilibrium). Each indifference condition has a unique solution; therefore the mixed equilibrium is unique. At the interior benchmark \(\eta=3/2\), it is \((p,q)=(2/3,2/5)\).

**Robustness.** At \(\eta=3/2\), the four strict cycle gains equal \(1/4\), \(1/2\), \(1/2\), and \(3/4\). Payoff ratios are continuous in each resource reward and strictly positive resource time. Thus there is an open neighborhood of the specified finite reward/time vector within the positive, strictly congestion-monotone data in which these four strict inequalities persist. All such games lack a pure Nash equilibrium. This is a topological continuity assertion, not a claim of a universal numerical perturbation radius.

## Verification
The standalone, standard-library Python program `verify.py` computes the four payoffs using exact rational arithmetic from resource occupancy, checks all specified positive/congestion-monotone inequalities at six representative \(\eta\)-values including both boundaries, verifies the strict cycle and mixed indifference at \(\eta=3/2\), and checks 400 additional nearby rational perturbations. Run `python verify.py` from the directory containing that program. The proof of the full infinite continuum of \(\eta\)-values is the symbolic inequality argument above; finite program samples are illustrative checks rather than a substitute for it.

## Relationship to prior work
Abdelraouf, Srivastava and Gupta (2026) introduce finite reward-rate congestion games with **exactly this form of individual ratio payoff** and prove that, at each fixed Dinkelbach multiplier, the *additive transformed* game is an exact potential game (their Proposition 1). They note the direct quotient need not be an exact potential but do not, in their analyzed statements and examples, classify pure-equilibrium failure for a concrete quotient game. The result here separates nonexistence of *any* direct pure equilibrium from the weaker statement that an exact potential is absent, and gives a full phase boundary and unique mixed equilibrium. It does not contradict the transformed potential existence theorem.

Classical Rosenthal games guarantee pure equilibria for additive congestion payoffs, whereas congestion-averse games and non-matroid strategy families allow more general aggregation and nonexistence phenomena (Byde, Polukarov and Jennings 2009; Voice, Polukarov, Byde and Jennings 2009). Those broad works reduce a general claim of novel nonexistence to a *model-specific* claim: the explicit positive, strictly congestion-monotone **ratio representation**, the full exact parameter interval and the mixed-equilibrium formula are the contributions asserted here. None of the primary material inspected supplied this exact construction or parameter classification; uninspected variants remain a genuine priority risk.

## Limitations
This is an exact result about a particular asymmetric two-player, three-resource, finite-action family. It is not a proof that three resources are minimal, that all reward-rate games lack pure equilibria, or that mixed strategies are dynamically selected. Resource \(A\) is a singleton option, so some resource/occupancy entries are latent. Generic game theory already guarantees mixed equilibria in all finite games; the contribution is their explicit dependence on congestion parameters and the sharp breakdown of the transformed game's pure-equilibrium guarantee in the direct ratio game. Existing general results for nonlinear congestion-averse games may imply generic possibilities of missing pure equilibria without covering the exact representation and bifurcation interval. Independent scientific validation has not been performed.

## References
1. H. Abdelraouf, V. Srivastava, V. Gupta, *Reward-Rate Congestion Games and Replicator–Dinkelbach Dynamics*, arXiv:2609.28240v1 (publicly submitted September 23, 2026), https://arxiv.org/html/2609.28240v1 . Section II, Proposition 1, and the task-allocation example.
2. R. W. Rosenthal, *A class of games possessing pure-strategy Nash equilibria*, International Journal of Game Theory 2 (1973), 65–67.
3. A. Byde, M. Polukarov, N. R. Jennings, *Games with Congestion-Averse Utilities*, SAGT (2009), 220–232.
4. T. Voice, M. Polukarov, A. Byde, N. R. Jennings, *On the Impact of Strategy and Utility Structures on Congestion-Averse Games*, WINE (2009), 600–607, DOI:10.1007/978-3-642-10841-9_61.
5. M. Feldotto, L. Leder, A. Skopalik, *Congestion Games with Mixed Objectives*, Journal of Combinatorial Optimization 36 (2018), 1145–1167, DOI:10.1007/s10878-017-0189-y (abstract consulted).
