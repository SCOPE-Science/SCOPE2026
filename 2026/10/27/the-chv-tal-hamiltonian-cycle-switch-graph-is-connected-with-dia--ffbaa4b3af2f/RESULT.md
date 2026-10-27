# The Chvátal Hamiltonian-cycle switch graph is connected with diameter nine

## Finding
Let \(G\) be the twelve-vertex Chvátal graph specified by the 24-edge list below. Its Hamiltonian-cycle two-edge-switch graph \(\mathcal H(G)\) has **185 vertices and 382 edges**, is **connected**, has **diameter nine** and **radius six**. A switch removes two edges of an undirected Hamiltonian cycle and inserts two other edges of \(G\), with the result again one undirected Hamiltonian cycle.

The exact degree distribution, stated as (switch degree, number of cycles), is \((2,21),(3,48),(4,60),(5,28),(6,6),(7,18),(9,4)\). The eccentricity distribution is \((6,12),(7,104),(8,53),(9,16)\). The number of unordered cycle pairs at distances one through nine is respectively \(382,1129,2694,4116,4876,2992,713,110,8\). In particular eight pairs of Hamiltonian cycles require nine optimum-preserving two-edge switches, and all pairs can be connected with at most nine.

## Assumptions and scope
Work with simple undirected graphs and labelled vertices \(0,1,\ldots,11\). The entire graph \(G\) is specified by its unordered edges:

```
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7)
(2,3) (2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8)
(5,10) (5,11) (6,10) (6,11) (7,8) (7,11)
(8,10) (9,10) (9,11)
```

These 24 pairs specify one labelled presentation of the standard Chvátal graph, which has 12 vertices, is 4-regular, triangle-free, and 4-chromatic. A Hamiltonian cycle is an unoriented edge set visiting each vertex exactly once; cyclic rotations and orientation reversal do **not** make distinct vertices of \(\mathcal H(G)\). Both inserted edges must be edges of \(G\), and every intermediate state must itself be a Hamiltonian cycle. No assertion is made for Hamiltonian paths, vertex recolourings, or arbitrary graphs.

## Proof
An exhaustive finite enumeration is an exact proof because every object belongs to a finite, explicitly enumerated universe and all loops and tests are given in the two complete verifier sources.

**Completeness of the first enumeration.** Fix the first vertex of each directed traversal to be \(0\). The `enumerate` recursion in `verify.cpp` visits every simple path rooted at \(0\) by recursively taking each unused graph-neighbor. At depth twelve it accepts precisely when the last vertex is adjacent to \(0\) and the second vertex label is smaller than the last vertex label. Every undirected Hamiltonian cycle has exactly two rooted traversals, which differ by reversal, so exactly one survives that strict ordering. The resulting accepted edge subsets are stored as 24-bit masks, one bit per displayed edge. The calculation returns exactly 185 distinct masks, each with twelve set bits. This agrees with the previously reported count of 370 oriented Hamiltonian cycles when orientations are distinguished.

**Correctness of the exchange test.** Any two Hamiltonian cycles each contain twelve graph edges. Their edge-set symmetric difference has cardinality four if and only if each cycle loses exactly two edges and gains exactly two edges in comparison with the other. Hence those and only those pairs are adjacent in the stipulated switch graph. The verifier examines each unordered pair of the 185 masks, creates precisely these adjacencies, and counts 382 exchange edges. There is no reliance on geometric adjacency of tours or on a heuristic 2-opt procedure.

**Complete distance calculation.** From every one of the 185 states, breadth-first search explores all reachable states through the exact exchange adjacency. All 185 states are reached from every source; hence the graph is connected. BFS gives shortest-path distances in an unweighted graph, so taking maxima gives the exact diameter nine and radius six. Counting vertex degrees, the maximum distance from each source, and all unordered source-target distances produces the distributions stated under Finding. The distance-nine count of eight supplies a sharp lower-bound witness for the diameter; reachability with all distances at most nine gives the upper bound.

**Independent completeness cross-check.** `verify_independent.py` does not enumerate rooted paths. Instead, it decides independently for every one of the 24 edges whether to include it, pruning only when a vertex already has degree above two or cannot reach degree two using its remaining incident edges. Consequently all and only spanning 2-regular subgraphs are generated. There are 278 such two-factors. Exactly 185 are connected, and a connected spanning 2-regular graph is precisely a Hamiltonian cycle. This second enumeration independently derives the same 185 masks, switch graph size, connectivity, degree distribution and eccentricity bounds. The independent construction checks the search universe rather than merely rerunning the same DFS code.

## Verification
The two files `verify.cpp` (standard C++17) and `verify_independent.py` (Python 3 standard library) are complete and require no external packages or other files. In a directory containing them, run:

```
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify
./verify
python3 verify_independent.py
```

The C++ run prints `HAMILTONIAN_OK undirected_cycles=185 directed_oriented_cycles=370`, `SWITCH_OK vertices=185 edges=382 connected=1 diameter=9 radius=6`, exact distribution lines, and `ALL_VERIFY_OK`. The independent Python run prints `TWO_FACTORS_TOTAL 278` and `INDEPENDENT_VERIFY_OK ...`. Both were executed on the supplied source files. These tests establish a finite exhaustive claim and are not statistical extrapolations.

## Relationship to prior work
Chvátal's 1970 article introduces the twelve-vertex graph as a minimal triangle-free 4-regular 4-chromatic construction. Its Hamiltonian-cycle count, 370 oriented or 185 unoriented tours, is known in graph catalogues and is **not** proposed as a new numerical invariant here. Takaoka (2018) studies exactly the two-edge Hamiltonian-cycle reconfiguration operation and shows both complexity hardness and connectivity in certain restricted graph classes. The Chvátal graph is not one of the covered connected classes (in particular it is non-bipartite and non-chordal). Kleer–Patel–Stroh (2020) study switch connectivity and sampling in dense graphs; their high-minimum-degree conditions do not hold here, where the order is twelve and minimum degree is four. The exact 185-state switch-graph adjacency, component, diameter, radius, and degree and distance profiles are the distinct claim.

## Limitations
This is a finite computational proof for one graph, not an infinite-family theorem or a mixing-time estimate. The conclusion depends on the given undirected edge list and on *two-edge* rather than one-edge or unrestricted multi-edge changes. Originality comparisons cannot exclude every unindexed article or database; no independent expert audit is asserted. The first-public date identifies the earliest verified archival graph-defining source, not a date for this result.

## References
1. V. Chvátal, “The smallest triangle-free 4-chromatic 4-regular graph,” *Journal of Combinatorial Theory* **9** (1970), 93–94. The 1970-07 issue is the archival first-known source; the source transcription's entire prose was inspected. DOI: 10.1016/S0021-9800(70)80057-6.
2. A. Takaoka, “Complexity of Hamiltonian Cycle Reconfiguration,” *Algorithms* **11** (2018), article 140, DOI: 10.3390/a11090140. Primary open-access PDF inspected for the switch definition and connectivity statements.
3. P. Kleer, V. Patel and F. Stroh, “Switch-based Markov Chains for Sampling Hamiltonian Cycles in Dense Graphs,” arXiv:2011.09726v1 (2020). Primary preprint inspected for density hypotheses and switch regime.
4. *Chvátal graph*, MathWorld / standard graph catalogues, for the previously known oriented Hamiltonian-cycle count (370).
