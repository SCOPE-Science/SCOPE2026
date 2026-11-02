# Seven goods are the sharp first EF1-failure horizon for strategic three-agent round-robin

## Finding

In the perfect-information round-robin draft with a fixed cyclic picking order, every pure subgame-perfect Nash equilibrium (SPNE) allocation is envy-free up to one good (EF1) whenever there are at most two complete rounds: for any number \(n\ge2\) of agents, any \(m\le 2n\) goods, and **arbitrary normalized monotone valuations**.

This bound is sharp at three agents: an explicit instance with seven goods and **strictly positive additive valuations with strict preferences between every two distinct bundles** has exactly two SPNE allocations, one of which fails EF1. Consequently, for three agents and additive goods, **seven is the smallest number of goods for which some pure SPNE allocation can violate EF1**. The claim concerns existence of an unfair equilibrium; it does not assert that every SPNE is unfair.

## Assumptions and scope

Let \(N=\{1,\ldots,n\}\) with \(n\ge2\), and let \(G\) contain \(m\) indivisible goods. Starting with agent 1, players choose one remaining good at a time, cyclically 1,2,...,\(n\),1,2,... until none remains. All picks are public; the game is finite and of perfect information. Each agent \(i\) values her final own bundle by \(v_i:2^G\to\mathbb R_{\ge0}\), with \(v_i(\varnothing)=0\) and \(v_i(S)\le v_i(T)\) for \(S\subseteq T\). Pure SPNE uses best responses in every subgame.

An allocation \(X=(X_1,\ldots,X_n)\) is EF1 if for every ordered pair \(i,j\), either \(X_j=\varnothing\) or some \(g\in X_j\) satisfies \(v_i(X_i)\ge v_i(X_j\setminus\{g\})\).

For the seven-good construction, number goods \(g_1,\ldots,g_7\), and use \(v_i(\{g_k\})=128b_{ik}+2^{k-1}\), extended additively, with the matrix \(B=(b_{ik})\):

| Agent | \(g_1\) | \(g_2\) | \(g_3\) | \(g_4\) | \(g_5\) | \(g_6\) | \(g_7\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 6 | 0 | 3 | 4 | 0 | 5 | 2 |
| B | 4 | 3 | 3 | 5 | 2 | 6 | 5 |
| C | 1 | 2 | 1 | 2 | 5 | 3 | 3 |

Because the binary contribution for any bundle lies in \(\{0,\ldots,127\}\) and uniquely encodes that bundle, all \(2^7\) bundle values are distinct for each agent, and every singleton value is strictly positive.

## Proof

**Universal lower horizon.** If \(m<n\), each bundle has at most one item, so EF1 is immediate. Otherwise \(n\le m\le2n\), and every player has a first pick. Fix agents \(i,j\). At player \(i\)'s first turn, every then-available good \(g\) can be secured by choosing \(g\) at that turn. Since valuations are monotone, the resulting final value after such a unilateral deviation is at least \(v_i(\{g\})\), irrespective of subsequent play. Equilibrium optimality of \(i\)'s strategy therefore implies \(v_i(X_i)\ge v_i(\{g\})\) for every good available at this first turn.

Player \(j\) takes at most two goods. At most one of them, her first-round pick, can precede \(i\)'s first turn. If \(X_j\ne\varnothing\), remove a good \(h\in X_j\) picked before \(i\)'s first turn when one exists; otherwise remove any \(h\in X_j\). The residual \(X_j\setminus\{h\}\) is either empty or a singleton available at \(i\)'s first turn. Monotonicity and the preceding deviation guarantee then give \(v_i(X_i)\ge v_i(X_j\setminus\{h\})\). This proves EF1 for every ordered pair. In fact this argument uses only root Nash optimality, not subgame perfection.

**Complete finite SPNE characterization for the witness.** For an additive draft, previous acquisitions add constants to the players' future payoffs, so equilibrium continuation choices depend only on the set \(S\) of goods still available and the fixed turn index. Let \(E(S)\) be all bundles-partitions of \(S\) achievable by pure SPNE in the subgame on \(S\); \(E(\varnothing)\) contains the all-empty allocation. If the current player is \(i\), for each \(g\in S\) let \(E_g(S)\) consist of allocations obtained from \(E(S\setminus\{g\})\) by adding \(g\) to player \(i\). Define

\[
T(S)=\max_{g\in S}\ \min_{Y\in E_g(S)}v_i(Y_i),
\qquad
E(S)=\bigcup_{g\in S}\bigl\{Y\in E_g(S):v_i(Y_i)\ge T(S)\bigr\}.
\]

For necessity, at a pure SPNE the chosen continuation is itself subgame-perfect; for any alternative move \(g\), its continuation payoff is at least the minimum across \(E_g(S)\), so the chosen outcome meets \(T(S)\). For sufficiency, choose the qualifying outcome on the prescribed move and, after every alternative move, select a subgame-perfect continuation minimizing this player's payoff from that move. The threshold guarantees no profitable deviation, and induction guarantees equilibrium in every continuation. This establishes the recurrence exactly, with no sampling assumption.

With seven goods, each subgame has a remaining mask \(S\in\{0,\ldots,127\}\), and current player index \((7-|S|)\bmod3\). Exact integer evaluation of all 128 states yields precisely the following two complete root SPNE allocations:

\[
X^{(1)}=(\{g_1,g_3,g_4\},\{g_6,g_7\},\{g_2,g_5\}),
\qquad
X^{(2)}=(\{g_1,g_4,g_6\},\{g_3,g_7\},\{g_2,g_5\}).
\]

For \(X^{(2)}\), agent B has utility \(v_B(\{g_3,g_7\})=1092\), but assesses A's three goods at \(513,648,800\); deleting any one leaves value at least \(513+648=1161>1092\). Thus \(X^{(2)}\) fails EF1. It is a genuine SPNE outcome, not merely an allocation exhibiting envy.

## Verification

Run `python3 verify.py certificate.json` using Python 3 with no third-party dependencies. The checker independently recomputes the complete state sets via memoized and bottom-up recurrences, verifies their agreement over all 128 subgames, checks strict ranking of all bundles, and constructs an explicit perfect-information strategy tree producing \(X^{(2)}\). It checks every one-shot deviation at 13,700 strategy-tree nodes, exactly two root SPNE outcomes, and the envy gap of 69. The included `certificate.json` stores the state counts and root allocations for deterministic reproduction.

The lower-horizon theorem holds for **all** normalized monotone valuations; exhaustive computation is used only for the finite seven-good upper witness, not to infer the universal bound.

## Relationship to prior work

Goldberg, Hollender and Tyrovolas (2026), Theorem 17, already prove that online strategic round-robin can fail EF1 for three additive agents. Their exhibited instance uses nine goods and has a **unique** unfair SPNE allocation. This result identifies the sharp earlier threshold for existence of *some* unfair SPNE, with seven goods; it does not replace their unique-equilibrium claim. Their proofs of proportionality up to one good (PROP1) and two-agent EF1 do not imply the present two-round result for arbitrary monotone valuations.

Amanatidis et al. (2026) independently examine **pure Nash equilibria of an offline direct-revelation round-robin mechanism** and give an eight-good EF1 counterexample in that distinct strategic game. Their agents submit fixed bid rankings in advance rather than choosing adaptively at each subgame; their Nash results do not entail the present online SPNE boundary.

## Limitations

The seven-good witness has two distinct SPNE allocations, only one of which is unfair. The result does not show that all equilibria must fail at seven goods, nor does it classify all seven-good preference profiles. The two-round protection assumes monotone valuations and one-item irreversible picks in a fixed cyclic order; it does not apply directly to chores, nonmonotone preferences, or other picking sequences. Priority remains subject to publications or equivalent results not identified in the cited literature.

## References

- P. W. Goldberg, A. Hollender, and G. Tyrovolas, *Equilibria of Round-Robin: Computational Hardness and Fairness for Few Subadditive Agents*, arXiv:2609.18309v1, first publicly posted 2026-09-16. https://arxiv.org/html/2609.18309v1
- G. Amanatidis, H. Aziz, G. Birmpas, F. Fusco, S. Leonardi, and R. Reiffenhäuser, *Revisiting the Fairness of Pure Nash Equilibria of Round-Robin*, arXiv:2610.23686v1, first publicly posted 2026-10-16. https://arxiv.org/abs/2610.23686
