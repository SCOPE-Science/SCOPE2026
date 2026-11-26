# Total simplicity and total synchronization in primitive binary two-out graphs on five vertices

## Finding

Among the 1,220 isomorphism classes of primitive directed two-out multigraphs on five vertices, the joint classification by total simplicity and total synchronization is:

| | Totally synchronizing | Not totally synchronizing | Total |
|---|---:|---:|---:|
| Totally simple | 448 | 22 | 470 |
| Not totally simple | 442 | 308 | 750 |
| Total | 890 | 330 | 1,220 |

Exactly 18 of the 22 totally simple but not totally synchronizing classes are Eulerian. Of these 18, four have 24 synchronizing colorings, eight have 28, and six have 30 (out of 32). Thus the known total-synchronization marginals can be resolved by a structural condition, and the Eulerian obstructions admit three different synchronizing-coloring counts. The previously covered four non-Eulerian classes are included for completeness in the joint census, not claimed as new.

## Assumptions and scope

The graphs are finite directed multigraphs with loops and parallel arcs allowed and exactly two outgoing arcs per vertex. Isomorphism preserves directed arc multiplicity, but there is no fixed ordering of outgoing arcs. For coloring counts, the two named letters are assigned bijectively to the two outgoing arc slots at each vertex, including separate choices for parallel slots. The one-step transition of a letter maps each vertex to the target of its assigned arc. A coloring is synchronizing if some word in the letters takes all vertices to one vertex; a graph is totally synchronizing if all its colorings are synchronizing.

A graph is primitive if strongly connected and its directed cycle-length gcd is one. It is Eulerian if every in-degree is two. A partition is strongly lumpable if every two vertices in the same block have identical outgoing arc counts into every target block. Total simplicity is the absence of such a partition with between two and four blocks. This is equivalent to simplicity of every coloring: a congruence for one coloring gives equal outgoing arc counts into every block, and given lumpable counts one can order the two target blocks consistently for each source block to obtain a coloring preserving the partition.

## Proof

An ordered list of five unordered target pairs, each chosen from the 15 pairs with repetition on the vertex set, specifies a labeled graph. Order the pairs lexicographically and encode each list by its base-15 integer with vertex 0 least significant. All \(15^5=759{,}375\) codes are considered. Keep the least code in each vertex-permutation orbit. Thus two representatives cannot be isomorphic and every orbit contributes precisely one representative.

For each candidate, test reachability from vertex 0 and toward vertex 0. If all vertices are reachable in both tests, take shortest distances \(d(v)\) from vertex 0. The gcd of the integers \(d(u)+1-d(v)\) over all arcs \(u\to v\) is the period: these integers sum along any closed walk to its length; conversely, appending a fixed return walk from \(v\) to 0 to each of the two paths of lengths \(d(u)+1\) and \(d(v)\) shows that their difference is divisible by the period. Keep the candidates of period one.

Enumerate all proper nontrivial partitions by successively placing each vertex in an existing or a new block, and test the outgoing arc-count equalities block by block. This test distinguishes total simplicity exactly. For each of the 32 colorings, follow the finite subset transition graph starting at the full set. A singleton is reachable exactly when the coloring has a reset word. The exact results from the resulting four-way tabulation are the displayed entries \(448,22,442,308\). The in-degree-two filter on the 22 simple obstructions gives the Eulerian frequency table:

| Synchronizing colorings | Eulerian classes |
|---:|---:|
| 24 | 4 |
| 28 | 8 |
| 30 | 6 |

In fact, no Eulerian binary two-out graph on more than one vertex is totally synchronizing. Split the vertices into source and target copies and treat arcs as edges of the resulting 2-regular bipartite multigraph. Alternating colors along each even cycle, including cycles of length two from double edges, gives a coloring in which both letters are permutations. All its words are permutations, so it cannot synchronize. This observation explains why the 18 Eulerian entries above are also exactly the simple Eulerian classes in the primitive census. It does not count the simple graphs or determine the frequency table without examining their graph structure.

## Reproduction

The accompanying enumerator `scripts/enumerate.cpp` implements the finite code search and tests described above. Compile with `g++ -std=c++17 -O2 scripts/enumerate.cpp -o enumerate` and run `./enumerate 5` into a separate output directory. The representative rows match `data/graph_5.csv` and the summary matches `data/stats_5.txt`. The four joint counts come from `total_classes`, `simple_classes`, `simple_and_total` and `simple_non_total`. In the representative file, select rows of simplicity flag 1 and coloring count below 32; count the target multiplicities of each row and tabulate the sync-count column when all target multiplicities are two.

The accompanying `scripts/check.py --data-dir data` rechecks the stored representatives at orders 2–5, using a backward pair-merger test instead of forward full-subset reachability. Every pair can be merged if and only if a reset word exists: one can successively merge pairs in the current image to reduce its size to one. A stored-row recheck is a consistency test; exhaustive generation gives coverage of the candidate universe.

## Relationship to prior work and limitations

Gusev and Szykuła (2015), Table 2, already report 1,220 primitive classes and 890 totally synchronizing classes for these parameters. They are reproduced marginals. D’Angeli and Rodaro (2026), §4.1 and Figure 5, relate total simplicity to lumpability and give examples illustrating that the two graph properties differ; Open Problem 4.11 asks for a structural characterization. Their Proposition 2.7 and Lemma 5.8 relate nonsynchronizing colorings to permutations at prime Eulerian order and permutation colorings to bipartite factorizations, respectively. Those results explain the Eulerian mechanism, not the total-simplicity split or this class-count distribution.

The earlier October 13 census of binary automata uses primitivity in the distinct sense of having no common proper congruence. A totally simple graph forces this property in every coloring, and for a non-Eulerian graph at least one letter is not a permutation. Forgetting the letters in that census and filtering for graph primitivity, total simplicity and non-Eulerian status recovers the four non-Eulerian classes (from its representatives 1, 2, 3 and 11), including their coloring counts when parallel-slot assignments are restored. In particular their minimum order and exact four-type classification are not contributions of this result. That automaton census omits all synchronizing colorings and pairs of permutations, so it does not supply the present joint census or list of Eulerian simple graph types.

The classification is finite, for order five and two outgoing arcs, not a general characterization. The exact results are computational, with a complete finite candidate universe and integer tests. No claim about unseen work or formal verification is made.

## References

1. V. V. Gusev and M. Szykuła, *On the Number of Synchronizing Colorings of Digraphs*, arXiv:1508.02133, Table 2. https://arxiv.org/abs/1508.02133
2. D. D’Angeli and E. Rodaro, *On totally synchronizing graphs*, arXiv:2607.17335, Proposition 2.7, §4.1, Figure 5 and Lemma 5.8. https://arxiv.org/abs/2607.17335
3. *The smallest binary primitive nonsynchronizing nonpermutation boundary*, 2026-10-13. https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-the-smallest-binary-primitive-nonsynchronizing-nonpermutation-bo--7f7c2dad36ac
