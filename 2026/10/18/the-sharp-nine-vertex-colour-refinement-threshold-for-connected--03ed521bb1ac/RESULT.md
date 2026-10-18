# The sharp nine-vertex colour-refinement threshold for connected bipartite graphs

## Finding
Let \(G\equiv_{C^2}H\) mean that the finite simple undirected graphs \(G,H\) satisfy exactly the same sentences of first-order logic with two variables and counting quantifiers. **Within the class of finite connected bipartite graphs**, every graph of order at most eight is distinguished by \(C^2\) from every nonisomorphic graph of the same order in that class. At order nine there are exactly \(730\) isomorphism types and \(728\) \(C^2\)-equivalence classes: precisely two doubletons and \(726\) singletons. The doubletons are represented by the four bipartite adjacency matrices below; rows are vertices in the four-vertex part, columns are vertices in the five-vertex part, and `1` means adjacency.

**First doubleton:**

```text
00111      01011
00011      10101
11100      00110
11000      11000
```

**Second doubleton:**

```text
10011      10011
10011      10101
11100      11010
11100      11100
```

In the order displayed, their numbers of four-cycles are \((2,0)\) and \((6,4)\), proving nonisomorphism without relying on a graph-isomorphism package. The first doubleton additionally separates a graph with four-cycles from one of girth six. Therefore nine is the sharp first order of *relative* indistinguishability in this graph class.

## Assumptions and scope
Graphs are nonempty, finite, simple, loopless, undirected, connected and bipartite. The language has just one symmetric adjacency predicate and equality, with **no names for the two bipartition sides**. The phrase *within the class* is essential: no claim is made that every graph of order at most eight is identified by \(C^2\) among arbitrary, possibly disconnected or nonbipartite graphs. Different orders are distinguishable by counting quantifiers; the census compares graphs with a fixed vertex count.

One-dimensional colour refinement starts with one colour on every vertex and simultaneously updates \(c_{t+1}(v)=(c_t(v),\{\!\{c_t(w):w\sim v\}\!\})\), with canonical names shared by all compared graphs. The Immerman–Lander characterization identifies equality of stable colour multisets with \(C^2\)-equivalence.

## Proof
**Exhaustive representative theorem.** Every connected bipartite graph on \(n\ge2\) vertices has a unique bipartition up to swapping its sides. Choose sizes \(1\le a\le b\), with \(a+b=n\). Every such graph is encoded by an \(a\)-by-\(b\) zero-one matrix. Enumerate every one of its \(2^{ab}\) possibilities and discard disconnected matrices. Two retained matrices with given \((a,b)\) encode isomorphic graphs exactly when one is obtained from the other by permuting rows and columns, and, when \(a=b\), possibly by transposition. Hence the lexicographically least encoding under these operations is a complete isomorphism key.

For each fixed row permutation, sorting the column bit-vectors yields the minimum under all column permutations. Enumerating only the \(a!\) row permutations (and the transpose case if \(a=b\)) is therefore enough to compute an exact canonical key, with no heuristic isomorphism test. The program `exhaustive.cpp` enumerates all masks, tests connectivity, retains one graph per canonical key, and writes `representatives.tsv`.

**Logical equivalence theorem.** For every retained graph of a given order, run colour refinement **with one global dictionary of colour names shared among all retained graphs**. Group representatives by their sorted stable vertex-colour lists. This is exactly the \(C^2\)-equivalence relation, not merely equality of degree sequences, by the stated colour-refinement theorem. Refinement runs through twice the order, more than sufficient to reach pairwise distinguishing information.

The complete counts \((\text{isomorphism types},\text{logical classes})\) for orders \(1,2,3,4,5,6,7,8,9\) are
\[
(1,1),(1,1),(1,1),(3,3),(5,5),(17,17),(44,44),(182,182),(730,728).
\]
Exactly two nonsingleton equivalence classes occur, both at order nine, and their masks in row-major least-significant-bit-first encoding are respectively \((106268,111290)\) and \((237369,241337)\). The four displayed matrices are precisely those masks. The exhaustive code asserts every count and both doubletons and exits with a failure status if they are not obtained.

**Independent structural witnesses.** In the first pair, the common stable equitable partition has four cells of sizes \(2,1,4,2\), with neighbour counts between them \(H\!\to\!Q:1\), \(H\!\to\!R:2\), \(Q\!\to\!H:2\), \(R\!\to\!H:1\), \(R\!\to\!S:1\), and \(S\!\to\!R:2\); all other cell-to-cell counts are zero. Here \(H\) is the degree-three cell, \(Q\) has two degree-three neighbours, and \(R,S\) are the other degree-two cells. In the second pair the common stable equitable partition has sizes \((1,4,4)\), with one degree-four hub adjacent to every degree-three vertex, and with every degree-three vertex adjacent to two degree-two vertices and every degree-two vertex adjacent to two degree-three vertices. The reduced \(4\)-by-\(4\) incidence structure is either two disjoint four-cycles or one eight-cycle. Both pairs therefore have identical stable colour histograms independently of the exhaustive grouping.

Finally, the exact four-cycle count of a bipartite adjacency matrix with row-neighbour sets \(N_i\) is \(\sum_{i<j}\binom{|N_i\cap N_j|}{2}\). Applying this formula gives \(2\ne0\) in the first pair and \(6\ne4\) in the second. Thus all doubletons are pairs of genuinely nonisomorphic graphs.

## Verification
Compile `exhaustive.cpp` with a standard C++17 compiler and execute `./exhaustive representatives.tsv`. Compare its standard output with `summary.txt`. Then run `python3 check_certificate.py representatives.tsv` and compare with `check_output.txt`. The Python code independently recomputes all representatives' canonical keys, checks connectivity and distinctness, uses a separate global refinement implementation, identifies both doubletons, and recalculates all four-cycle numbers. Every calculation is integer or finite combinatorial manipulation; no randomness or floating-point thresholds occur. The representative file is included to support examination and independent extension.

## Relationship to prior work
Arvind, Köbler, Rattan and Verbitsky (first public preprint 2015) give general colour-refinement and amenability theory, including the correspondence with two-variable counting logic and the behaviour of equitable cells and biregular replacements. Kiefer, Schweitzer and Selman (first public preprint 2015) give a broad characterization of structures identified by counting logic. Neither inspected work provides this **relative-to-connected-bipartite, exact order-nine census**. Their structural results help explain the collision mechanism but do not list the two complete exceptional classes.

The already documented sequence counting *all* connected bipartite graph isomorphism types, OEIS A005142, gives \(730\) at nine vertices; that number is not claimed as new. The claim here is the number \(728\) of logical equivalence classes, the first-order threshold, and the complete two-pair classification.

## Limitations
This is a finite classification through nine vertices, not an asymptotic classification or a theorem about all bipartite graphs of larger order. It is relative to connected bipartite graphs and does not establish global \(C^2\)-identifiability. The independently implemented validator checks the exhaustive C++ representative list and its equivalence census but relies on the C++ matrix sweep for completeness of that list. No formal proof assistant or independent human audit was used. An unindexed historical table of small colour-refinement equivalence classes could present a priority risk.

## References
1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public 2015-02-04), https://arxiv.org/abs/1502.01255.
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (first public 2015-03-30), https://arxiv.org/abs/1503.08792.
3. *Number of connected bipartite graphs with n nodes*, OEIS A005142, https://oeis.org/A005142.
