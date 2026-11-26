# Sharp four-step equilibrium access and exact connectivity spectrum in binary three-player games

## Finding and assumptions

There are three labeled players with two actions each. For each player's fixed opponents' actions exactly one action is strictly better. Profiles form the Boolean cube \(Q_3\); orient each edge toward the endpoint whose differing action is preferred by its player. A pure Nash equilibrium is a sink. When the sink set is nonempty, let
\[
L(G)=\max_v\min_{z\in\operatorname{Sink}(G)}d_G(v,z),
\]
where directed distance is \(+\infty\) if there is no path. One has \(L(G)\le4\), with equality possible. Of the \(2^{12}=4096\) labeled orientations, \(962\) have no sink and the remaining \(3134\) have the following exact distribution:
\[
\begin{array}{c|rrrr}
L & 1&2&3&4\\\hline
\# &258&644&1512&720
\end{array}
\]
Of the sink-positive orientations, \(2492\) are connected in the sense that every nonsink reaches every sink. For independent fair orientations of the twelve edges, the conditional connectivity probability is \(1246/1567\), and the conditional probability that \(L=4\) is \(360/1567\).

Each player has four pairs of payoff entries, one pair per opponents' profile. The pairs are disjoint, and each pair fixes a separate edge, so every orientation is realizable: for a given player and pair number \(j=0,1,2,3\), assign values \(2j\) and \(2j+1\), with the larger value on the preferred action. The uniform orientation law also arises from **independent identically distributed atomless payoff entries** (or independent comparisons each having probability one half of either outcome). Independence and continuity alone, without fairness of the within-pair comparisons, are not sufficient for the stated probabilities. The deterministic theorem and the labeled counts require no payoff distribution.

## Proof of the bound and sharpness

Fix a sink \(z\). Its Hamming-distance-one neighbors all point directly to it. Let \(w\) be the antipode. Either \(w\) is a sink or it points to some distance-two vertex \(u\). The other two incident edges of \(u\) join it to distance-one vertices. If either points out of \(u\), then \(w\) reaches \(z\) in three steps; if neither does, then \(u\) is itself a sink. Thus \(w\) has access distance at most three. A distance-two vertex can take an outgoing edge toward distance one and reach \(z\) within two steps. If there is no such edge, it is a sink or can go to \(w\), so its access distance is at most four. This proves the uniform bound.

Use binary labels \(0,\ldots,7\) and direct the twelve edges as follows:

```text
0->2  0->4  1->0  2->3  3->1  5->4
5->1  6->4  6->2  7->6  7->5  7->3
```

The only sink is \(4\) and the unique shortest route there from \(2\) is \(2\to3\to1\to0\to4\), so \(L=4\). In the two-player square with a sink, its neighbors enter it directly and its antipode is a sink or enters a neighbor, so the corresponding bound is at most two.

## Exact census

The sink events for adjacent vertices are incompatible. The cube is the bipartite graph \(K_{4,4}\) with the antipodal perfect matching removed; an independent set meeting both parts can have at most two vertices, and then must be an antipodal pair. The counts of independent sets of sizes \(1,2,3,4\) are respectively \(8,16,8,2\). Specifying \(k\) independent sinks fixes \(3k\) different edges and leaves the others free. Inclusion–exclusion therefore gives \(8\cdot2^9-16\cdot2^6+8\cdot2^3-2=3134\).

For the distance and connectivity counts, enumerate all twelve-bit orientation masks of the cube. For each mask, take the sinks to be the zero-outdegree vertices. A reverse breadth-first search from the sink set gives the distance to the nearest sink, and one reverse search from each individual sink checks whether every nonsink reaches it. The supplied `verify.py` performs the exhaustion with both reverse search and a separate Floyd–Warshall check of directed distances. An equivalent finite recurrence starts at each nonsink \(v\) with \(R_0(v)=\{v\}\), and sets \(R_{k+1}(v)=R_k(v)\cup N^+(R_k(v))\). The first \(k\) meeting the sink set gives the access distance, and containment of the full sink set in \(R_7(v)\) is exactly the all-sink test. No simple path can have more than seven edges. The nonzero classes are
\[
\begin{array}{r|r|r|r}
\text{sinks}&L&\text{not connected}&\text{connected}\\\hline
1&3&0&1512\\
1&4&0&720\\
2&1&248&8\\
2&2&336&252\\
3&2&56&0\\
4&1&2&0
\end{array}
\]
Summing the columns gives the stated census. Enumeration is exact because each of the twelve independently oriented edges has one bit, and every twelve-bit mask occurs once.

## Scope and relationship to prior work

The theorem concerns existentially chosen strict updates, not convergence under arbitrary activation sequences or an expected hitting time. Fabrikant, Jaggard and Schapira (*On the Structure of Weakly Acyclic Games*, arXiv:1108.2092, Lemma 4.6) already establish weak acyclicity of these games when a pure equilibrium exists. The focus here is sharp worst-case access length and the distribution of nearest-equilibrium distances, not existence of a finite path. Johnston, Savery, Scott and Tarbush (*Game Connectivity and Adaptive Dynamics*, arXiv:2309.10609, Appendix H) study the same notion of connectivity in a uniform model and give sample estimates. The Resultary record *Five-class connectivity census of three-player binary games* (2833bb8d55a9) gives the same exact counts of orientations with sinks and of connected orientations, as part of a broader classification of qualitative reachability, but does not give the nearest-equilibrium distance distribution. Heinrich et al. (*Best-response dynamics, playing sequences, and convergence to equilibrium in random games*, DOI 10.1007/s00182-023-00837-4) analyze playing sequences rather than existential shortest paths. The abstract of Bollobás, Gotsman and Shamir (*Connectivity and dynamics for random subgraphs of the directed cube*, DOI 10.1007/BF02784059) describes a directed-hypercube subgraph model, and a specialized finite tabulation in the unavailable full text cannot be ruled out. No absolute priority is claimed.
