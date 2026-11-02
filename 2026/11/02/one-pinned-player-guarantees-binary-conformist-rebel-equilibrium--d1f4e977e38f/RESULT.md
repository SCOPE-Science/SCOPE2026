# One pinned player guarantees binary conformist–rebel equilibrium on a ring

## Finding

**Pinning theorem.** Every simple cycle with at least three vertices, binary actions, arbitrary conformist/rebel types at all nonfixed vertices and at least one stubborn vertex fixed to a prescribed action has a pure-strategy Nash equilibrium. The fixed actions may differ between stubborn vertices.

**Exact restoration law.** Start with an even cycle of \(n\ge4\) vertices whose original conformist and rebel types alternate, and replace exactly one vertex by a stubborn player fixed at either action. The number of pure Nash equilibrium action profiles is exactly
\[
K_n=\begin{cases}n/2,&n\equiv2\pmod 4,\\ n/2+1,&n\equiv0\pmod4.\end{cases}
\]
The formula is independent of which original type was replaced and of the chosen fixed action. In particular, the classical alternating cycles of length \(n\equiv2\pmod4\), which have no equilibrium without a stubborn player, acquire exactly \(n/2\) equilibria from one pinned vertex.

## Assumptions and scope

The underlying graph is an unweighted, undirected, simple cycle \(C_n\) with \(n\ge3\). Each action \(x_i\) belongs to \(\{0,1\}\). A conformist's payoff is the number of adjacent vertices using \(x_i\); a rebel's payoff is the number using the opposite action. A stubborn player is constrained to a specified \(0\) or \(1\) and has no permissible deviation. A pure Nash equilibrium requires every nonstubborn player's action to maximize their payoff given the two neighbors; payoff ties admit either action. The first assertion allows any nonempty set of stubborn vertices and arbitrary fixed values. The counting assertion is for a cycle of even length with exactly one stubborn vertex replacing a vertex of a formerly strictly alternating type pattern.

## Proof

**1. Local condition.** Consider a path between prescribed endpoint actions \(x_0=a\) and \(x_{L+1}=b\), with \(L\ge1\) interior conformists/rebels. Put \(t_i=0\) for conformists and \(t_i=1\) for rebels, and introduce the edge-disagreement bits \(y_j=x_j\oplus x_{j+1}\), indexed \(0\le j\le L\). For an interior vertex \(i\), if its two neighbors have different actions, both available actions give the same payoff. Otherwise the unique best response is to match both neighbors for a conformist or oppose both for a rebel. Thus, exactly,
\[
  \bigl(y_{i-1}\ne y_i\bigr)\quad\text{or}\quad
  \bigl(y_{i-1}=y_i=t_i\bigr). \tag{1}
\]
The endpoint constraint is \(\bigoplus_{j=0}^{L} y_j=a\oplus b\).

**2. A parity-state reachability lemma.** Process disagreement bits from left to right and track a pair \((p,v)\), where \(p\) is the XOR of all processed bits and \(v\) is the last one. After the first edge bit, both \((0,0)\) and \((1,1)\) are reachable. At a vertex of type \(t\), a successor bit \(w\) is legal precisely when \(w\ne v\) or \(w=v=t\), and the new state is \((p\oplus w,w)\). After the first interior vertex, exactly three of the four states are reachable, for either choice of \(t\).

Moreover any reachable state set of cardinality at least three yields at least three successors. Indeed, such a set contains both possible states ending in either \(v=t\) or \(v=1-t\). If it contains both states ending in \(v=t\), these two states can each append either bit, covering all four successor states. Otherwise it contains both states ending in \(v=1-t\), whose forced appended bit \(w=t\) gives both parity states ending in \(t\), while the remaining state ending in \(v=t\) can append \(w=1-t\), giving a third state. By induction, after all \(L\) interior vertices, at least three of the four states are reachable, so both parities \(p=0\) and \(p=1\) are reachable. Choose parity \(a\oplus b\), reconstruct the bits and then the unique actions from \(x_0=a\). This simultaneously satisfies the last endpoint and all interior best responses. If \(L=0\), there are no interior constraints.

**3. Pinned cycle.** Cut a cycle at every stubborn vertex. Each maximal consecutive block of nonstubborn vertices is a path whose two bordering stubborn actions are specified. With only one stubborn vertex, both endpoints of the single path are the same fixed action. By Step 2 every such block admits a best-response assignment for any given endpoint actions. The blocks share only stubborn endpoints and their interior incentive constraints are independent. Joining the assignments proves existence on every pinned cycle.

**4. Exact enumeration following one pin.** Suppose \(n\) is even and the original types alternate. Label the newly fixed vertex by \(0\), and let \(t_0,t_1,\ldots,t_{n-1}\) denote the **original** alternating binary type indicators, including the superseded original value at vertex \(0\). Put \(y_i=x_i\oplus x_{i+1}\) (cyclic indices), and \(z_i=y_i\oplus t_i\). For each remaining strategic vertex \(1\le i\le n-1\), the neighboring original types differ: \(t_{i-1}=1\oplus t_i\). By (1), the **only** forbidden adjacent pair is \((z_{i-1},z_i)=(0,1)\). Consequently all admissible \(z\)-sequences are uniquely
\[
 z_0z_1\cdots z_{n-1}=1^\ell0^{n-\ell},\qquad 0\le\ell\le n.
\]
Such a disagreement vector comes from a cyclic binary action profile precisely when \(\bigoplus_i y_i=0\). Since \(\bigoplus_i t_i\equiv n/2\pmod2\), this closure condition reads \(\ell\equiv n/2\pmod2\). Among the integers from \(0\) through \(n\), exactly \(n/2\) satisfy this congruence if \(n/2\) is odd, and exactly \(n/2+1\) do so if \(n/2\) is even. Every admissible difference vector lifts to exactly one action profile after specifying the pinned action \(x_0\); this establishes the formula. The old no-pin obstruction for alternating \(n\equiv2\pmod4\) rings is the classical Theorem 4 of Cao and Yang (2014), not a newly asserted result here.

## Verification

The accompanying standalone C++17 source `verify_cycle.cpp` directly evaluates every player's direct payoff at every candidate binary action profile. It exhausts all four player types (conformist, rebel, stubborn at zero, stubborn at one) for every cycle size \(3\le n\le8\): 87,360 type assignments, of which 86,856 contain a stubborn player. Across all type assignments only the two unpinned alternating cycles of length six have no equilibrium. It also checks the exact one-pin count for both original alternating patterns, every pin location and both fixed actions on every even size from four through sixteen, totaling 280 cases. A separate seeded test covers 7,000 pinned cycles of sizes nine through fifteen. Finally, a direct three-action search finds no pure equilibrium in the four-ring whose ordered player types are rebel, conformist, rebel, stubborn-at-zero, showing why the binary restriction matters.

To reproduce, compile with a C++17 compiler and run:

```sh
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_cycle.cpp -o verify_cycle
./verify_cycle
```

The executable prints `VERIFY_OK checks=94641` on success. Computational checks test finite instances only. Steps 1–4 provide the universal proofs and complete unbounded counting arguments.

## Relationship to prior work

Cao and Yang (2014, Theorem 4) precisely classify **unpinned**, binary conformist–rebel rings, including nonexistence for alternating lengths congruent to two modulo four. Cao, Qin, Yang and Zhang (2019) study dynamics on conformist–rebel graphs, again without stubborn types. Cao, Sanchez and Zhang (2026, arXiv:2607.05932, first public July 7) formulate binary conformist–rebel–stubborn games and prove three general sufficient equilibrium criteria, but do not supply the unconditional pinned-cycle theorem or the one-pin equilibrium count. Pei, Cao and Zhang (2026, arXiv:2607.10997, first public July 13) characterize rings with **at least three actions**, subject to the condition that every conformist has a conformist or stubborn neighbor; their criterion does not apply to the binary case and is not equivalent to the present theorem. The new contribution is unconditional equilibrium restoration by pinning any nonempty subset of a binary ring, together with the sharp exact count when a single vertex of an alternating ring is fixed.

## Limitations

The existence theorem assumes exactly two actions, equal nonnegative unit weights on an undirected simple cycle and neutral treatment of ties. It makes no claim about synchronous or asynchronous learning convergence, arbitrarily weighted edges, arbitrary graphs, or games with at least three actions. The exact equilibrium formula requires a *single* pinned vertex replacing a vertex of a fully alternating even ring; it is not a count for arbitrary types or multiple pins. No independent external audit has been performed; precedence against unindexed equivalent results remains uncertain.

## References

1. W. Cao, A. Sanchez and B. Zhang, *Network games with heterogeneous players*, arXiv:2607.05932, first posted July 7, 2026, https://arxiv.org/abs/2607.05932.
2. S. Pei, W. Cao and B. Zhang, *Network games with three types of players*, arXiv:2607.10997, first posted July 13, 2026, https://arxiv.org/abs/2607.10997.
3. Z. Cao and X. Yang, *The fashion game: Network extension of Matching Pennies*, Theoretical Computer Science 540–541 (2014), 169–181, https://doi.org/10.1016/j.tcs.2014.05.009.
4. Z. Cao, C.-Z. Qin, X. Yang and B. Zhang, *Dynamic matching pennies on networks*, International Journal of Game Theory 48 (2019), 887–920, https://doi.org/10.1007/s00182-019-00665-5.
