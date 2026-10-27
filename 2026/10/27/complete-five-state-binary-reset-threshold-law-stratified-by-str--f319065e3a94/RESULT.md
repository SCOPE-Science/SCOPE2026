# Complete five-state binary reset-threshold law stratified by strong connectivity

## Finding

Consider the finite, uniform probability space of **all ordered pairs of deterministic maps on five labeled states**. It has exactly \(5^{10}=9,765,625\) members. Letters are distinguished even if their induced functions coincide; states are labeled; automata are not required to be initially connected, accessible from an initial state, or minimal.

Let \(\tau\) be the minimum length of a word mapping every state to a single state, or \(\infty\) when no such word exists. Let \(\mathsf{SC}\) denote strong connectivity of the directed multigraph formed by the two letter transitions. The **exact joint distribution** of \((\tau,\mathsf{SC})\) is:

| \(\tau\) | Not strongly connected | Strongly connected | Total |
|---:|---:|---:|---:|
| \(\infty\) | 1,582,216 | 120,024 | 1,702,240 |
| 1 | 30,025 | 1,200 | 31,225 |
| 2 | 1,393,160 | 210,000 | 1,603,160 |
| 3 | 2,245,800 | 641,520 | 2,887,320 |
| 4 | 1,120,800 | 627,840 | 1,748,640 |
| 5 | 482,640 | 361,680 | 844,320 |
| 6 | 208,560 | 235,200 | 443,760 |
| 7 | 87,360 | 148,080 | 235,440 |
| 8 | 41,040 | 90,960 | 132,000 |
| 9 | 16,800 | 53,760 | 70,560 |
| 10 | 2,880 | 33,360 | 36,240 |
| 11 | 0 | 11,040 | 11,040 |
| 12 | 0 | 10,320 | 10,320 |
| 13 | 0 | 5,520 | 5,520 |
| 14 | 0 | 2,640 | 2,640 |
| 15 | 0 | 960 | 960 |
| 16 | 0 | 240 | 240 |
| **Synchronizing subtotal** | **5,629,065** | **2,434,320** | **8,063,385** |
| **Entire space** | **7,211,281** | **2,554,344** | **9,765,625** |

Consequently, the exact means of finite reset thresholds, conditional on synchronizability, are
\[
\mathbb{E}[\tau\mid \tau<\infty] = \frac{5,970,397}{1,612,677},\qquad
\mathbb{E}[\tau\mid \tau<\infty,\mathsf{SC}]=\frac{45,961}{10,143},\qquad
\mathbb{E}[\tau\mid \tau<\infty,\neg\mathsf{SC}]=\frac{3,764,269}{1,125,813}.
\]
These are approximately \(3.7021654\), \(4.5313024\), and \(3.3436006\), respectively. Among the synchronizing automata that are not strongly connected, the maximal reset threshold is exactly \(10\), attained in exactly \(2,880\) cases; every threshold at least \(11\) forces strong connectivity. The overall maximum is \(16\), attained in \(240\) labeled ordered cases. The complete **joint** table, not either individual extreme, is the central finding.

## Assumptions and scope

Define \(Q=\{0,1,2,3,4\}\) and \(\Sigma=\{a,b\}\). Each of the two transition maps is an arbitrary function \(Q\to Q\), giving \((5^5)^2=5^{10}\) equally weighted automata. A word acts left to right. The reset threshold \(\tau(A)\) is the minimum nonnegative length of a word \(w\) for which \(\lvert Qw\rvert=1\), or \(\infty\). A five-state automaton has no reset word of length zero. The directed underlying graph is strongly connected when every state can reach every other state by following letter-labeled edges. Graph connectivity is independent of reachability from a distinguished initial state, which is not part of this model.

The tabulation uses **ordered letter maps and labeled states**, not the number of isomorphism classes, different transition monoids, minimal DFAs, or binary languages. The empirical frequencies have exact finite interpretations under this uniform model and do not imply asymptotic statements as the number of states increases.

## Proof

The numerical table is an exact exhaustive finite proof, with the full search code supplied in two separately implemented programs; no heuristic sampling or unproved bound on possible reset lengths is used.

**Complete sample-space bijection.** Encode a transition map \(f:Q\to Q\) uniquely by \(\sum_{i=0}^4 f(i)5^i\), an integer in \(\{0,\ldots,3124\}\). The outer double loop of each supplied program ranges over all \(3125^2\) ordered pairs without duplication. In particular, all repeated-map, constant-map, permutation-map, disconnected and nonsynchronizing cases are included.

**Exact subset transition.** For a nonempty subset \(S\subseteq Q\) use its five-bit indicator \(m(S)\in\{1,\ldots,31\}\). Given a map \(f\), the exact image mask is \(m(f(S))=\bigvee_{i\in S}2^{f(i)}\). The `image` table in `reset_enum.cpp` obtains this recurrence from the least significant set bit; the `ims` table in `reset_independent.cpp` instead inspects all five members of every mask. Both give the mathematical image of the subset, without approximation.

**Shortest-word invariant.** Starting from \(m(Q)=31\), for every word \(w\) the path obtained by following its letters in the nonempty-subset graph ends at \(m(Qw)\), and conversely every path labels a word. A reset word exists exactly when a singleton mask \(1,2,4,8,16\) is reachable. Breadth-first search in `reset_enum.cpp` returns precisely the length of the shortest such path, or declares it unreachable after exploring the complete reachable set. There are just \(31\) nonempty masks; any shortest path is simple, so no possible shortest reset word exceeds \(30\) letters. The second implementation independently evolves entire frontiers by exact word length, removes previously seen masks, and stops upon the first singleton or exhaustion. Its fixed \(31\)-layer loop is therefore mathematically exhaustive.

**Strong-connectivity invariant.** In `reset_enum.cpp`, a vertex can reach all other vertices exactly when forward reachability from state \(0\) covers all five states and reverse reachability to state \(0\) also covers all five. Each reachability closure stabilizes after at most four edge additions along a simple path, so five relaxation passes suffice. `reset_independent.cpp` instead takes the reflexive-transitive closure of the five-state adjacency relation by Floyd–Warshall's recurrence, then requires every row to equal the full state set. The two implementations thus use different connectivity tests as well as different shortest-path enumeration mechanisms.

**Certified arithmetic.** Both complete traversals return the displayed \(17\)-row joint table, counting \(\tau=\infty\) as one category, and separately return the first-moment sums \(18,821,345\) (not strongly connected) and \(11,030,640\) (strongly connected) over synchronizing automata. The count check \(1,582,216+120,024+5,629,065+2,434,320=9,765,625\) exhausts the sample space. Dividing these integer moment sums by their respective synchronizing sample counts, and by their total, gives the three displayed rational means. The other assertions follow by examining the proven table's support and its extremal entries.

## Verification

The standalone files `reset_enum.cpp` and `reset_independent.cpp` are complete, dependency-free C++17 programs and have no inputs. On a C++17 compiler, execute:

```sh
g++ -O3 -std=c++17 -o reset_enum reset_enum.cpp
./reset_enum > counts_bfs.txt
g++ -O3 -std=c++17 -o reset_independent reset_independent.cpp
./reset_independent > counts_layers.txt
```

The two programs were compiled and run from the supplied sources. Their reported `H[k]` bins, nonsynchronizing subtotals, and integer moments match exactly (the first implementation uses queue-based BFS and root reachability, the second full-frontier propagation and transitive closure). The corresponding outputs are embedded as `counts_bfs.txt` and `counts_layers.txt`. `joint_counts.csv` reproduces the entire exact table, not an estimate. Independently of those runs, the published high-tail isomorphism-class count \((46,43,23,11,4,1)\) at lengths \(11\) through \(16\), ordered ascending, becomes \((11,040,10,320,5,520,2,640,960,240)\) when multiplied by \(240\), agreeing with the new enumeration's high-tail marginal.

## Relationship to prior work

The most directly covering **partial** result is Don–Zantema–de Bondt [2], Section 4.4, whose two-letter five-state row enumerates the six high-threshold isomorphism-class counts at reset lengths \(11\)–\(16\). Those marginal high-tail values are **already known** and are cited as an external cross-check, not claimed as a discovery. That table does **not** supply the reset-threshold frequency distribution at lengths \(1\)–\(10\), its non-synchronizing mass, the bivariate strong-connectivity split, or the exact conditional means for the full ordered labeled map space.

The extensive small-state experiments of Kisielewicz–Kowalski–Szykuła [3] establish verification ranges and difficult extremizers, rather than the particular joint distribution here. Dżyga–Ferens–Gusev–Szykuła [4] establish attainable reset-threshold sets and existence intervals, which do not imply multiplicities under uniform random labeling. Chapuy–Perarnau [5] analyze a uniformly random two-letter automaton asymptotically and provide no exact five-state finite probability table in the inspected main results. The more recent survey [1] identifies average reset threshold as a substantive research topic and motivates the exact finite benchmark.

## Limitations

The claim is confined to five labeled states and two distinguished letters, with **all** maps allowed. No formula for other state sizes, no limiting law, and no classification of transition semigroups is asserted. This is a finite exhaustive computational theorem, not a symbolic all-\(n\) theorem. The prior high-tail marginal was established previously [2]. Unindexed earlier computational data or an unexamined equivalent presentation may still match some or all of the full joint table. The complete text of the motivating 2026 survey was not available for inspection; the accessible introductory material and abstract were read, so no negative full-document novelty claim is made for that source.

## References

[1] M. Szykuła, “Synchronizing Automata: Open Problems,” *EPTCS* 451 (2026), 33–47, arXiv:2608.24245, doi:10.4204/EPTCS.451.3. Initial public release 2026-08-25.
[2] H. Don, H. Zantema, and M. de Bondt, “Slowly synchronizing automata with fixed alphabet size,” arXiv:1609.06853, Section 4.4 and the five-state table, p. 16. Journal version: *Information and Computation* 279 (2021), 104614.
[3] A. Kisielewicz, J. Kowalski, and M. Szykuła, “Experiments with Synchronizing Automata,” arXiv:1607.04025, Section 3 and Table 2.
[4] M. Dżyga, R. Ferens, V. V. Gusev, and M. Szykuła, “Attainable Values of Reset Thresholds,” *LIPIcs* 83 (MFCS 2017), 40:1–40:14, doi:10.4230/LIPIcs.MFCS.2017.40.
[5] G. Chapuy and G. Perarnau, “Short Synchronizing Words for Random Automata,” arXiv:2207.14108v2; SODA 2023, doi:10.1137/1.9781611977554.ch26.
