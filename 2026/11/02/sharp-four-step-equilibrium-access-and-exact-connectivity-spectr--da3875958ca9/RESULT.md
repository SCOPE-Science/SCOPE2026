# Sharp four-step equilibrium access and exact connectivity spectrum in binary three-player games

## Finding

Consider three labeled players, each with two possible actions. Assume that for every player, at every fixed combination of opponents' actions, exactly one of that player's actions is the strict best response. Represent the resulting strict unilateral best-response graph by an orientation of the three-dimensional Boolean cube; different payoff arrays yielding the same oriented cube represent the same best-response pattern.

For every such graph with at least one pure Nash equilibrium (a sink), define the **equilibrium-access radius**
\[
L(G)=\max_{v\in\{0,1\}^3}\min_{z\in\operatorname{Sink}(G)}d_G(v,z),
\]
where \(d_G(v,z)\) is the minimum number of strict best-response edges from profile \(v\) to \(z\), with \(d_G(v,z)=+\infty\) if no path exists.

**Theorem.** Every strict three-player binary best-response graph possessing a sink has \(L(G)\le4\), and the bound is attained. Among the exactly \(2^{12}=4096\) equally weighted labeled best-response orientations, \(3134\) possess at least one sink, with the **complete exact distance distribution**
\[
\#\{G:L(G)=1,2,3,4\}=(258,644,1512,720).
\]
Exactly \(2492\) of those \(3134\) graphs are **connected** in the sense that every nonsink profile reaches every pure Nash equilibrium. Thus conditional on the existence of a pure equilibrium, the probability of connectivity under independently uniform orientation of the twelve cube edges is \(1246/1567\), and the probability of requiring four best-response changes from some initial profile is \(360/1567\). The remaining \(962\) orientations have no pure equilibrium.

## Assumptions and scope

A strategy profile is a bit vector \(v\in\{0,1\}^3\). For each player \(i\in\{1,2,3\}\) and each of the four opponent profiles, precisely one of the two actions is strictly preferable. A directed edge \(u\to v\) exists exactly when the profiles differ in one player's action and that player strictly prefers \(v\) given the other two actions. There are twelve independent binary comparisons, one per undirected cube edge; every orientation is realizable by a generic payoff array. In particular, with opponents' profile indexed by \(j\in\{0,1,2,3\}\), assign that player payoffs \(2j\) and \(2j+1\) within the corresponding pair, putting the larger number on the preferred action. All eight payoffs for that player are distinct.

The probability is defined on these \(4096\) best-response equivalence classes with each of the twelve orientations equally likely; independent continuous random payoffs induce exactly the same orientation distribution. It is not a claim about uniform cardinal payoff arrays or about fixed/cyclic activation schedules. Paths are *existential*: one can choose an improving player at each step.

## Proof

**1. Uniform sharp four-step bound.** Fix any sink \(z\) in an oriented three-cube and partition its vertices into Hamming-distance layers from \(z\). The three layer-one vertices each point directly to \(z\), so their shortest equilibrium-access distances are at most one. Let \(w\) be the unique layer-three vertex. If \(w\) is itself a sink its distance is zero. Otherwise it points to some layer-two vertex \(u\). If \(u\) has an outgoing edge to a layer-one vertex, then \(w\to u\to\text{layer one}\to z\) reaches equilibrium in three steps. If \(u\) has no outgoing edge to layer one, its only remaining neighbor is \(w\), and the edge \(w\to u\) points inward to \(u\); hence \(u\) has no outgoing edge and is itself a sink. In either case \(w\) reaches a sink within three steps.

Now take any layer-two vertex \(v\). If it points to either of its layer-one neighbors, it reaches \(z\) within two steps. Otherwise, if its third edge (to \(w\)) points inward, \(v\) is a sink. If its third edge points \(v\to w\), then the previous paragraph supplies an equilibrium path of at most three more steps. Thus every layer-two vertex reaches some sink within four steps; with the other layers this proves the bound.

**2. Sharpness.** Label vertices by integers \(0,\ldots,7\) using binary coordinates, and orient the twelve cube edges as

```text
0->2  0->4  1->0  2->3  3->1  5->4
5->1  6->4  6->2  7->6  7->5  7->3
```

These are exactly the twelve cube edges, oriented once each. Vertex \(4\) is the unique sink. Vertex \(2\) has its only outgoing edge to \(3\), which has its only outgoing edge to \(1\), which has its only outgoing edge to \(0\). From \(0\), the edge \(0\to4\) reaches the sink, while \(0\to2\) repeats the cycle. Therefore every shortest equilibrium path from \(2\) is \(2\to3\to1\to0\to4\), of length four. (For two binary players, the opposite-corner argument gives a universal bound of two, so four-step access first occurs with three players.)

**3. Analytic equilibrium denominator.** An orientation with \(k\) specified sinks is possible only if those \(k\) vertices are pairwise nonadjacent; fixing those sinks orients \(3k\) distinct edges inward and leaves \(12-3k\) free. The independent-set counts of the three-cube at sizes \(k=1,2,3,4\) are \(8,16,8,2\). Inclusion–exclusion gives
\[
\#\{G:\operatorname{Sink}(G)\ne\varnothing\}
=8\cdot2^9-16\cdot2^6+8\cdot2^3-2=3134.
\]

**4. Exhaustive exact distance and connectivity certificate.** `verify.py` iterates exactly all \(2^{12}\) edge-orientation bit strings in lexicographic edge order. For each, it computes every sink as an out-degree-zero vertex; multi-source reverse breadth-first search computes all shortest distances to the sink set. In addition, a separate Floyd–Warshall all-pairs distance computation agrees on every state in every orientation. The maximum distances over the \(3134\) nonempty-sink orientations yield counts \(258,644,1512,720\) at radii \(1,2,3,4\). For every sink the script separately checks reachability from each nonsink by reverse breadth-first search, corroborated by Floyd–Warshall; exactly \(2492\) graphs pass the every-nonsink-to-every-sink connectivity test. The script separately checks the inclusion–exclusion total and the twelve arcs of the sharpness witness.

This is a complete finite certificate because the twelve edge comparisons are all independent, the bit strings run through every orientation exactly once, and all graph searches terminate on eight vertices. It does not replace the analytic proof of the universal four-step bound.

## Verification

Run with standard Python 3:

```sh
python3 verify.py
```

The program must print `VERIFY_OK` and the exact orientation totals. It has no external dependencies or random input; all integer counts and path lengths are exact. The independently implemented Floyd–Warshall and reverse-BFS algorithms verify the full census; the independent-set inclusion–exclusion formula verifies the pure-equilibrium denominator. The twelve-arc witness is checked against the full undirected cube edge set, its sole sink, and its four-step source distance.

## Relationship to prior work

Johnston, Savery, Scott, and Tarbush, *Game Connectivity and Adaptive Dynamics* (first public version September 19, 2023, arXiv:2309.10609), establish connectivity results mainly in large games. Their Appendix H reports sampling of 10,000 games for each small parameter combination; it does not provide the exact \(4096\)-orientation distance/connection spectrum or the sharp universal four-step access cutoff.

Fabrikant, Jaggard, and Schapira, *On the Structure of Weakly Acyclic Games* (arXiv:1108.2092, Lemma 4.6), **already prove** that any strict two-by-two-by-two game with a pure Nash equilibrium is weakly acyclic. Consequently, the existence of some finite improvement path is **not claimed as new** here. The contribution is the sharp length-four bound and the complete conditional distance/connectivity census, neither of which follows quantitatively from existence alone.

Heinrich and coauthors, *Best-response dynamics, playing sequences, and convergence to equilibrium in random games* (2023), examine random and clockwork playing sequences and asymptotic convergence; they do not provide the stated finite existential shortest-distance spectrum. Bollobás, Gotsman, and Shamir (1993) treat a different random directed-hypercube-subgraph model in the accessible abstract, but could not be excluded by a full-text comparison; see the limitation below.

## Limitations

This establishes *existence of a suitably chosen sequence* of at most four strict updates, not convergence under every fair, synchronous, random, or cyclic activation rule, and not an expected hitting time under a chosen stochastic dynamic. The exact enumeration covers three labeled binary players only. The known underlying weak-acyclicity theorem is expressly not a novelty claim. The closest 1993 directed-hypercube-subgraph article was available only through its abstract, so any earlier specialized finite-cube tabulation remains an originality risk. No independent validation has been performed.

## References

1. T. Johnston, M. Savery, A. Scott, B. Tarbush, *Game Connectivity and Adaptive Dynamics*, arXiv:2309.10609, first posted 2023-09-19. https://arxiv.org/abs/2309.10609 ; full openly accessible version: https://arxiv.org/html/2309.10609v6 .
2. A. Fabrikant, A. D. Jaggard, M. Schapira, *On the Structure of Weakly Acyclic Games*, arXiv:1108.2092, Lemma 4.6. https://arxiv.org/abs/1108.2092 .
3. T. Heinrich et al., *Best-response dynamics, playing sequences, and convergence to equilibrium in random games*, International Journal of Game Theory 52 (2023), 703–735. https://doi.org/10.1007/s00182-023-00837-4 .
4. B. Bollobás, C. Gotsman, E. Shamir, *Connectivity and dynamics for random subgraphs of the directed cube*, Israel Journal of Mathematics 83 (1993), 321–328. https://doi.org/10.1007/BF02784059 .
