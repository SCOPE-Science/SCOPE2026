# The first non-Eulerian totally simple synchronization obstructions: a complete five-state census

## Finding

A primitive directed multigraph with two outgoing edges at each vertex is **totally simple** when no partition with at least two and fewer than the total number of blocks is strongly lumpable, and **totally synchronizing** when every two-letter edge coloring admits a reset word. The smallest number of vertices in a primitive binary two-out graph that is totally simple, non-Eulerian and not totally synchronizing is **five**.

Exactly **four** five-vertex directed multigraph isomorphism classes have these three properties, each representing 120 labeled graphs, or **480 labeled graphs in all**. Their primitive integer left stationary vectors and counts of synchronizing edge colorings are:

| Unordered stationary-vector entries | Number of graph classes | Synchronizing colorings out of 32 |
|---|---:|---:|
| \((1,1,1,1,2)\) | 2 | 28 |
| \((1,1,2,2,3)\) | 2 | 30 |

There are no such non-Eulerian examples on two, three or four vertices. The broader primitive five-state census consists of **1,220** isomorphism classes, of which **890** are totally synchronizing, **470** are totally simple, and **448** have both properties. Of the remaining 22 totally simple but not totally synchronizing types, **18** are Eulerian and the four above are non-Eulerian. The Eulerian remainder has synchronizing-coloring frequencies 24 (four types), 28 (eight types), and 30 (six types).

## Assumptions and scope

Graphs are finite directed **multigraphs**, allow loops and parallel arcs, and have exactly two outgoing arc slots per vertex. Graph isomorphisms preserve directed arc multiplicities; outgoing slots themselves are unordered. For each vertex, independently assigning the two outgoing arcs to letters \(a,b\) gives \(2^n\) edge colorings on \(n\) vertices; parallel arcs count as distinct edge slots when counting these colorings. Graphs are primitive if strongly connected and their cycle-length gcd is one. Eulerian means in-degree two at every vertex.

For a partition \(\mathcal P\) of the vertex set, strong lumpability means that for every pair of vertices in the same block and every target block, their outgoing arc counts into that target block coincide. A nontrivial partition has between two and \(n-1\) blocks. By the standard graph congruence/lumpability correspondence, absence of such partitions is total simplicity. For a coloring, a reset word maps all vertices to one state. The stationary vector \(\pi\) is the coprime positive integer row solution of \(\pi A=2\pi\), where \(A\) is the multigraph adjacency matrix.

## Proof

The claim is a finite exhaustive theorem. At order \(n\), each vertex has an unordered pair of targets, giving \(\binom{n+1}{2}^n\) completely specified labeled graphs. Encode that pair by its lexicographic rank and encode all vertex pairs in base \(\binom{n+1}{2}\). For each graph test strong connectivity in both directions and calculate the period by a spanning-tree distance gcd. Retain precisely the least code in each vertex-permutation orbit, and independently calculate its orbit size as \(n!/|\operatorname{Aut}(G)|\). These rules cover each primitive isomorphism class once and only once.

For each representative enumerate every set partition into \(2,\ldots,n-1\) blocks; compare the two outgoing neighbor-count vectors of vertices in each block. This exactly decides total simplicity, not just a necessary condition. For each of the \(2^n\) edge colorings, breadth-first-search the finite nonempty-subset transition graph starting at the full vertex set; a reset word exists if and only if some singleton is reachable. Thus testing every coloring exactly decides total synchronization. Compute the stationary vector with signed integer cofactors of \(2I-A^\top\), normalized by gcd. The integral enumeration uses no floating-point comparisons.

The program `scripts/enumerate.cpp` implements these steps for \(n=2,3,4,5\). Its resulting four canonical order-five codes and exact data are:

| Code | Outgoing unordered target pairs, vertices 0–4 | \(\pi\) | Resetting colorings | One nonresetting coloring mask |
|---:|---|---|---:|---:|
| 3928 | `3:4;1:2;0:2;0:1;0:0` | `2:1:1:1:1` | 28 | 6 |
| 11226 | `1:2;3:4;0:4;0:3;0:0` | `2:1:1:1:1` | 28 | 6 |
| 58372 | `1:3;1:2;0:4;0:2;0:1` | `2:3:2:1:1` | 30 | 13 |
| 58879 | `0:4;2:3;1:2;0:2;0:1` | `2:2:3:1:1` | 30 | 8 |

For a mask, its bit for vertex \(i\) selects which of that vertex's sorted two arcs receives letter \(a\); the other receives \(b\). Each displayed coloring fails to synchronize by the same exhaustive subset criterion. Distinct canonical codes prove the four are pairwise nonisomorphic. The four have permutation orbits of size 120.

Across \(n=2,3,4,5\), the numbers of primitive types are respectively \(2,12,100,1220\), and numbers of totally simple but not totally synchronizing types are \(1,1,2,22\). A separate in-degree test shows that each of the first four (orders at most four) is Eulerian; at order five 18 are Eulerian and four are not. This proves minimality and completeness.

## Verification

An independent Python verifier (`scripts/check.py`) reads the included canonical graph data, independently rechecks graph primitivity, isomorphism-orbit sizes, stationary eigenvectors, all proper set partitions, and all colorings. Unlike the forward full-subset breadth-first search of the C++ implementation, its synchronization test uses backward reachability of mergeable unordered state pairs. Synchronization holds exactly when every state pair can be merged by some word, so the two approaches are logically equivalent but computationally independent. Running `python3 scripts/check.py --data-dir data` prints `INDEPENDENT_CHECK_PASS` and the five-vertex obstruction spectrum.

To regenerate the data from all labeled graph encodings, compile `g++ -std=c++17 -O2 scripts/enumerate.cpp -o enumerate`, then execute `./enumerate 2`, `./enumerate 3`, `./enumerate 4`, and `./enumerate 5`, redirecting standard output to their respective `data/graph_N.csv` files. Standard error contains the class counts and color-spectrum summaries; compare them to `data/stats_N.txt`. Regeneration checks the full candidate universe; reading the stored representatives alone is not an exhaustive proof without the enumerator and canonicality argument.

## Relationship to prior work

Gusev and Szykuła (2015) already obtained the five-vertex marginal totals 1,220 primitive types and 890 totally synchronizing types; these numbers are reproduced as checks, not asserted as new. D'Angeli and Rodaro (2026) define total simplicity through lumpability, study its relation to synchronization, pose the structural classification question, and exhibit both Eulerian and non-Eulerian nonlumpable nonsynchronizing examples. In particular their non-Eulerian example already has stationary entries \((1,1,2,2,3)\) up to permutation. That existence is **not** claimed here. The present result adds the exact smallest non-Eulerian order, four-type classification, complete stationary-vector and coloring-frequency spectrum, and joint counts. The proof uses direct enumeration, not a proposed eigenvector sufficiency criterion. Both non-Eulerian stationary types admit multiple proper equal-weight partitions, so no at-most-one-equipartition shortcut is used to infer their behavior.

## Limitations

The classification concerns only outdegree two and at most five vertices, with loops and parallel arcs allowed; it is not a characterization for all state counts. Numerically different presentations may have the same isomorphism class and are counted only once. The conclusion about 480 labeled graphs uses the computed size of each corresponding permutation orbit. Computational verification is reproducible but has not undergone independent external audit. The historical-priority comparison is limited to the inspected works and indexed searches; an unindexed equivalent enumeration cannot be ruled out.

## References

1. D. D'Angeli and E. Rodaro, *On totally synchronizing graphs*, arXiv:2607.17335, first posted 19 July 2026, especially Section 4 and Open Problem 4.11. https://arxiv.org/abs/2607.17335
2. V. V. Gusev and M. Szykuła, *On the Number of Synchronizing Colorings of Digraphs*, arXiv:1508.02133, 2015, especially Table 2. https://arxiv.org/abs/1508.02133
3. V. V. Gusev and E. V. Pribavkina, *On synchronizing colorings and the eigenvectors of digraphs*, arXiv:1511.09079, first posted 2015. https://arxiv.org/abs/1511.09079
