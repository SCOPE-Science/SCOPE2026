# An exact asymmetric-action limit for random game connectivity

## Finding

Consider the uniform ensemble of generic two-player ordinal games in which player 1 has exactly two actions and player 2 has exactly \(k\) actions, with \(k\ge 3\). At every opponent action, each player's strict ranking of their own actions is independently uniform. A game is called connected when it has at least one pure Nash equilibrium and every non-equilibrium action profile can reach every pure Nash equilibrium by a path of strict best-response moves.

The fraction of games in this ensemble that are connected, conditional on having at least one pure Nash equilibrium, is exactly

\[
\frac{2(k+1)}{3k+1}.
\]

Consequently, as \(k\to\infty\) with player 1's action count fixed at two, this conditional fraction tends to \(2/3\). This is an asymmetric-action regime; it is not the equal-action limit in the cited many-action theorem.

## Assumptions and scope

Write \(R(j)\in\{1,2\}\) for player 1's unique best response to player 2's action \(j\), and \(C(i)\in\{1,\ldots,k\}\) for player 2's unique best response to player 1's action \(i\). Under the uniform generic ordinal-game ensemble, the \(R(j)\) are independent fair choices, the \(C(i)\) are independent uniform choices, and the two families are independent. Define \(F(i)=R(C(i))\) for \(i\in\{1,2\}\).

The claim concerns the best-response graph with unilateral strict best-response edges. It does not concern convergence under a fixed sequential update schedule, mixed Nash equilibria, correlated payoff matrices, or games with ties. The conditional denominator is the set of games with at least one pure Nash equilibrium.

## Proof

A profile \((i,j)\) is a pure Nash equilibrium exactly when \(j=C(i)\) and \(F(i)=i\). Thus pure equilibria correspond exactly to fixed points of \(F\).

First, for \(k\ge3\), a game is connected if and only if \(F\) is constant. If \(F\) is constant with value \(c\), then \((c,C(c))\) is the unique pure equilibrium. From any profile, a player can first best-respond to the current opponent action, then the other player can best-respond, and after at most two further such moves the profile reaches \((c,C(c))\). Hence every non-equilibrium profile reaches the unique equilibrium, so the game is connected.

Conversely, if \(F(1)=2\) and \(F(2)=1\), then \(F\) has no fixed point and the game is not connected. The only remaining nonconstant map on a two-element set is the identity, which gives two pure equilibria \((1,C(1))\) and \((2,C(2))\). In that case \(C(1)\ne C(2)\), and \(R(C(1))=1\), \(R(C(2))=2\). Since \(k\ge3\), choose \(j\notin\{C(1),C(2)\}\). If \(R(j)=1\), profile \((1,j)\) has only one outgoing best-response edge, to \((1,C(1))\); it cannot reach the second equilibrium. If \(R(j)=2\), the symmetric argument applies to \((2,j)\). Therefore the identity case is not connected. This proves the equivalence.

Now calculate the probabilities. If \(C(1)=C(2)\), then \(F\) is constant automatically; this event has probability \(1/k\). If \(C(1)\ne C(2)\), the two sampled values of \(R\) are independent and agree with probability \(1/2\). Therefore

\[
\Pr(F\text{ is constant})=\frac1k+\left(1-\frac1k\right)\frac12=\frac{k+1}{2k}.
\]

The map \(F\) has no fixed point precisely when it is the swap \(1\mapsto2,\ 2\mapsto1\). This requires \(C(1)\ne C(2)\), then two independent specified values of \(R\), so

\[
\Pr(\text{no pure equilibrium})=\left(1-\frac1k\right)\frac14=\frac{k-1}{4k}.
\]

Hence \(\Pr(\text{at least one pure equilibrium})=(3k+1)/(4k)\). Since for \(k\ge3\) connectedness is equivalent to \(F\) being constant, and a constant map always has a fixed point, division gives

\[
\Pr(\text{connected}\mid\text{at least one pure equilibrium})
=\frac{(k+1)/(2k)}{(3k+1)/(4k)}
=\frac{2(k+1)}{3k+1}.
\]

Taking \(k\to\infty\) gives the limit \(2/3\). No asymptotic approximation is used in the finite-\(k\) formula.

## Verification

The proof reduces connectivity to a two-state best-response map and counts the map types exactly. A standalone exhaustive verifier enumerates every pair of response maps for \(3\le k\le7\), constructs the directed best-response graph, and checks the graph definition directly against the constant-map characterization and the exact counts. These finite checks are consistency checks only; the proof above establishes the result for every integer \(k\ge3\).

The formula predicts \(2(k+1)/(3k+1)\) for each finite \(k\ge3\), with limiting value \(2/3\). The case \(k=2\) is excluded because the identity map can then also be connected.

## Relationship to prior work

Johnston, Savery, Scott, and Tarbush study connectivity of best-response graphs in uniform generic ordinal games and give an asymptotic result when all players have the same number of actions. Their paper notes that unequal action counts can be accommodated by the framework but restricts the stated analysis to equal counts for simplicity. The theorem here treats the distinct regime with two actions for one player and an increasing number for the other.

Wiese and Heinrich compute frequencies of games convergent under a fixed sequential best-response dynamic, including exact equal-action two-player formulas. That convergence criterion is not the same as graph connectivity used here: this theorem asks whether every non-equilibrium profile can reach every pure equilibrium through available strict best-response edges, regardless of a prescribed update order. The exact rectangular-action conditional fraction above is not implied by their equal-action sequential-dynamics formula.

## Limitations

The result assumes independent uniform strict ordinal rankings at each opponent profile. It does not extend automatically to correlated payoffs, ties, nonuniform preference rankings, or a fixed update protocol. The result gives a conditional fraction, not the unconditional probability of connectivity: the latter is \((k+1)/(2k)\) for \(k\ge3\). The literature search did not establish a complete census of every rectangular-action random-game result; the exact asymmetric regime is compared with the closest inspected works, and broader priority remains a residual risk.

## References

1. T. Johnston, M. Savery, A. Scott, and B. Tarbush, “Game connectivity and adaptive dynamics in many-action games,” arXiv:2601.05965, first submitted 9 January 2026, revised 2 June 2026. https://arxiv.org/abs/2601.05965
2. S. C. Wiese and T. Heinrich, “The Frequency of Convergent Games under Best-Response Dynamics,” *Dynamic Games and Applications* 12 (2022), 689–700. https://doi.org/10.1007/s13235-021-00401-3
3. H. A. Mimun, M. Quattropani, and M. Scarsini, “Best-response dynamics in two-person random games with correlated payoffs,” *Games and Economic Behavior* 145 (2024), 239–262. https://doi.org/10.1016/j.geb.2024.03.011
