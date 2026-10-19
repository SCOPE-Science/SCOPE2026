# The ten-switch diameter and inverse antipodes of the nine-pair crown graph

## Finding

For every integer \(4\le n\le9\), let \(C_n=K_{n,n}-\{i i':1\le i\le n\}\) be the crown graph, and let \(F_n\) have as vertices the perfect matchings of \(C_n\). Two vertices are adjacent if their symmetric difference is one alternating four-cycle. Then \(F_n\) is connected, with the exact orders, sizes, radii, and diameters in the table below.

| \(n\) | \(|V(F_n)|\) | \(|E(F_n)|\) | radius | diameter |
|:---:|---:|---:|---:|---:|
| 4 | 9 | 12 | 3 | 3 |
| 5 | 44 | 120 | 4 | 4 |
| 6 | 265 | 1,260 | 5 | 6 |
| 7 | 1,854 | 13,440 | 6 | 7 |
| 8 | 14,833 | 152,040 | 7 | 8 |
| 9 | 133,496 | 1,835,568 | 8 | **10** |

Thus \(n=9\) is the **first value \(n\ge4\)** for which a connected crown-graph four-cycle-switch graph has diameter strictly greater than \(n\). The exact diameter-ten pairs admit a unique description: under the identification of perfect matchings with derangements \(\pi\in S_9\), they are exactly the unordered pairs
\[
\{\pi,\pi^{-1}\},\qquad\text{where the cycle type of }\pi\text{ is }(3,3,3).
\]
There are exactly \(1,120\) such pairs. Each of the \(2,240\) derangements of this cycle type has the unique antipode \(\pi^{-1}\); every derangement of another cycle type has eccentricity at most nine.

For completeness, the eight conjugacy classes of derangements have the following exact eccentricities:

| cycle type | class size | eccentricity | farthest vertices per source |
|---|---:|---:|---:|
| \((2,2,2,3)\) | 2,520 | 9 | 32 |
| \((2,2,5)\) | 9,072 | 8 | 12,760 |
| \((2,3,4)\) | 15,120 | 9 | 36 |
| \((2,7)\) | 25,920 | 8 | 12,978 |
| \((3,3,3)\) | 2,240 | 10 | 1 |
| \((3,6)\) | 20,160 | 9 | 36 |
| \((4,5)\) | 18,144 | 8 | 13,200 |
| \((9)\) | 40,320 | 8 | 13,208 |

The eccentricity multiplicities of \(F_9\) are \(93,456\) at eight, \(37,800\) at nine, and \(2,240\) at ten.

## Assumptions and scope

All graph vertices on both sides of \(C_n\) are individually labelled. A perfect matching corresponds to a bijection \(\pi:[n]\to[n]\) with \(\pi(i)\ne i\) for every \(i\), hence a derangement. A switch exchanges \((i,\pi(i)')\) and \((j,\pi(j)')\) with \((i,\pi(j)')\) and \((j,\pi(i)')\), requiring both new edges to exist. Distances refer to the ordinary unweighted simple reconfiguration graph; no vertex relabelling is allowed **during** a path. Only the finite parameter interval \(4\le n\le9\) is asserted; there is no diameter assertion for larger crowns.

## Proof

**Exact reduction.** The switch above is permitted precisely when \(i<j\), \(\pi(i)\ne j\), and \(\pi(j)\ne i\). It yields the derangement \(\pi\circ(i\ j)\), where the transposition acts on the input positions. These inequalities are sufficient and necessary, and every possible alternating four-cycle in the crown graph exchanges exactly two matching edges. This gives a complete finite adjacency rule without extraneous edges.

**Conjugation symmetry.** Every \(\sigma\in S_n\) induces a graph automorphism \(\pi\mapsto\sigma\pi\sigma^{-1}\) of this derangement-switch graph: relabelling rows and their matching columns simultaneously preserves the forbidden diagonal and alternating four-cycles. Therefore the distance histogram from a vertex, its eccentricity, and its number of farthest vertices depend only on its cycle type. Derangements of \(n\) are partitioned by all integer partitions of \(n\) having no part one. It is therefore sufficient, for each \(n\), to enumerate **every derangement** and conduct a complete breadth-first search from one representative of **every** such cycle type.

**Exhaustive finite step.** The self-contained files `verify_python.py` and `verify_cpp.cpp` independently generate the entire state spaces for \(4\le n\le9\). The former enumerates permutations, builds adjacency explicitly, and searches it. The latter recursively constructs row-to-column bijections and generates neighbors on demand from packed assignments. In both cases each BFS visits all configurations, and the exact distance histograms for representatives of all cycle types agree. The complete \(n=9\) cycle-type histograms are retained in `verify_python.out` and `verify_cpp.out`; their sums are each \(133,496\). The table follows by minimizing and maximizing eccentricity across the exhaustive list of classes. Each undirected edge is generated from two endpoints and counted once, giving the edge counts.

**Exceptional antipodes.** At \(n=9\) the only cycle type of eccentricity ten is \((3,3,3)\). In both independent BFS computations a representative of this class has precisely one vertex at distance ten, and an explicit inverse-permutation test identifies it with the representative's inverse. Since inversion commutes with conjugation, this statement holds for every vertex of that cycle type. No other vertex has eccentricity ten. Inversion has no fixed point within this class, because each constituent three-cycle is replaced by its different inverse. Hence the unordered diameter-ten pairs number \(2,240/2=1,120\). This establishes both existence and exhaustive uniqueness of the claimed antipodes.

The finite results for \(n=4,5,6,7,8\) show diameter at most \(n\), while the nine-pair result shows diameter ten. Therefore nine is the first failing size among all \(n\ge4\) not exceeding nine, which suffices for the stated first-occurrence conclusion.

## Verification

Run `python3 verify_python.py` and compile the other independent checker with `g++ -std=c++17 -O2 verify_cpp.cpp -o crown_check && ./crown_check`. Both programs require no downloaded libraries or datasets. Compare their `small_n`/`results` fields and every cycle-type record: class size, eccentricity, reachable count, complete BFS distance histogram, farthest count, and inverse test. Both report all six graphs connected and the exact table. In particular the \((3,3,3)\) distance histogram on \(F_9\) is
\[
(1,27,324,2259,9777,26442,43059,37899,13590,117,1),
\]
where the final entry counts its unique distance-ten antipode. The BFS certificates are exhaustive finite computations, **not** an extrapolation beyond \(n=9\). A third-party independent scientific audit has not been performed.

## Relationship to prior work

Dyer, Jerrum, and Müller [1, Lemma 2] prove that four-cycle-switch graphs are connected with diameter at most \(n\) for the class of **chordal bipartite** graphs with two vertex classes of size \(n\). Their bound does not apply here: for every \(n\ge3\), choosing any three corresponding left/right index pairs in \(C_n\) induces a chordless six-cycle. The new value ten at \(n=9\) is a concrete obstruction to extending this particular diameter bound without its graph-class hypothesis. The same primary paper does not calculate the crown-graph derangement-switch distances.

Bonamy and coauthors [2] study connectivity and computational complexity of perfect-matching four-cycle reconfiguration on general graph classes, without the exact distance and antipode classification established here. The classical enumeration of derangements gives the number of vertices but no switch distances. Separately, adjacent-*position* derangement swaps are a strictly more restrictive graph and must not be conflated with the arbitrary-position swaps corresponding to four-cycles in a crown graph.

## Limitations

The diameter and antipode assertions are limited to \(4\le n\le9\), with the exceptionally strong classification only at \(n=9\). A complete graph search, even when independently reproduced, does not establish a theorem for all \(n\). No mixing-time or Markov-chain convergence estimate follows from the diameter computation alone. Research into unindexed computational archives could reveal prior equivalent calculations; publication priority and independent scientific validation are not claimed.

## References

[1] M. Dyer, M. Jerrum and H. Müller, *On the switch Markov chain for perfect matchings*, arXiv:1501.07725, first public version 30 January 2015; Lemma 2, pp. 4–5. https://arxiv.org/abs/1501.07725

[2] M. Bonamy, N. Bousquet, M. Heinrich, T. Ito, Y. Kobayashi, A. Mary, M. Mühlenthaler and K. Wasa, *The Perfect Matching Reconfiguration Problem*, MFCS 2019, LIPIcs 138, paper 80; preprint arXiv:1904.06184. https://doi.org/10.4230/LIPIcs.MFCS.2019.80
