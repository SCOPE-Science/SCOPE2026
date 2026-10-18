# Exact reconfiguration phase portrait of dominating sets in the Heawood graph

## Finding
Let \(H\) be the Heawood graph, the bipartite incidence graph of the seven points and seven lines of the Fano plane. Let \(D_k(H)\) have as vertices all ordinary dominating vertex sets of cardinality at most \(k\), with an edge when one dominating set is obtained from another by adding or removing one vertex.

**Theorem (geometric classification and exact low-budget reconfiguration).** There are exactly \(65\) inclusion-minimal dominating sets of \(H\), comprising \(21\) four-sets, \(14\) five-sets, \(28\) six-sets and \(2\) seven-sets. They are precisely the four geometric families described below. For the five budgets \(4\le k\le8\), the full add/delete reconfiguration graph has the following exact data:

| Budget | Vertices | Edges | Connected-component orders | Radius of largest component | Diameter of largest component |
|:--|--:|--:|:--|--:|--:|
| \(4\) | \(21\) | \(0\) | \(1^{\times21}\) | \(0\) | \(0\) |
| \(5\) | \(245\) | \(210\) | \(11^{\times21},1^{\times14}\) | \(1\) | \(2\) |
| \(6\) | \(1176\) | \(2226\) | \(1148,1^{\times28}\) | \(10\) | \(12\) |
| \(7\) | \(3138\) | \(9674\) | \(3136,1^{\times2}\) | \(11\) | \(14\) |
| \(8\) | \(5532\) | \(23408\) | \(5532\) | \(12\) | \(14\) |

Here \(a^{\times b}\) means exactly \(b\) components of order \(a\). For \(k=5\), the nontrivial components are all stars \(K_{1,10}\). In particular \(D_k(H)\) is disconnected for each \(4\le k\le7\), and connected for every \(k\ge8\); the latter connectivity endpoint is a specialization of a previously known general bipartite-graph theorem, not claimed as novel by itself. The new exact information is the complete low-budget component census, geometrically identified isolated obstructions, and sharp component radii and diameters.

## Assumptions and scope
The Fano plane has point set \(P\) and line set \(L\), both of order seven, every line contains three points, every point lies on three lines, and every two points determine one line. The graph \(H\) has vertex set \(P\sqcup L\); a point and line are adjacent exactly when incident. A set \(S\) dominates if every vertex belongs to \(S\) or has a neighbor in \(S\). *Inclusion-minimal* refers to set containment, not minimum cardinality. Paths in \(D_k(H)\) retain domination at every intermediate step and never use more than \(k\) vertices; a color change, token slide, or two-vertex swap is not a valid single move. Graph eccentricity, radius, and diameter in the table refer to the **largest individual connected component**, not to the disconnected graph as a whole.

The \(65\) inclusion-minimal sets are these disjoint geometric families:

1. For each unordered pair of distinct points \(p,q\), select \(p,q\) and the **two lines incident with neither**. There are \(\binom72=21\) four-sets.
2. For each point \(p\), select \(p\) with the four lines not incident with \(p\); dually for each line \(\ell\), select \(\ell\) with the four points not incident with \(\ell\). There are \(14\) five-sets.
3. For each nonincident point-line pair \((p,\ell)\), select the three points of \(\ell\) and the three lines through \(p\). There are \(28\) six-sets, as \(p\notin\ell\).
4. The entire seven-point class and the entire seven-line class, comprising two seven-sets.

## Proof
**Step 1: exhaustive finite domination and minimality certificate.** Index the seven points by \(0,\ldots,6\). Put \(\ell_j=\{j,j+1,j+3\}\pmod7\) for \(0\le j<7\); the seven three-sets form a Fano plane, since each point pair occurs in precisely one line. Index the seven line vertices by \(7,\ldots,13\). For each graph vertex \(v\), let \(B_v\) be its closed-neighborhood bit mask. A mask \(s\) represents a dominating set if and only if \(s\mathbin{\&}B_v\ne0\) for all fourteen vertices \(v\). It is inclusion-minimal if and only if it dominates and, for every one-bit deletion \(s'\), the mask \(s'\) fails domination. The standalone `verify.py` applies exactly these necessary-and-sufficient tests to **every** integer mask \(0\le s<2^{14}\). Thus there are neither unexplored candidate sets nor an implicit extrapolation from smaller orders. It obtains the size distribution \((21,14,28,2)\) for all minimal sets.

It independently generates the four geometric families using incidence and nonincidence masks, verifies their respective sizes and pairwise distinctions, tests that every generated set is inclusion-minimal, and checks equality of their union with the entire exhaustive minimal-set list. This proves the stated geometric classification. The same complete mask enumeration gives the dominating-set cardinality counts in sizes \(4\) through \(14\):
\[
(21,224,931,1962,2394,1862,987,364,91,14,1).
\]

**Step 2: exact reconfiguration adjacency and components.** At budget \(k\), retain exactly those verified dominating masks of Hamming weight at most \(k\). Two masks are adjacent exactly when their exclusive-or contains one set bit. `verify.py` forms every such adjacency by toggling each of the fourteen vertex bits, then exhaustively visits every vertex by breadth-first search. There are no arbitrary pruning rules. Counts, edge totals (half of the sum of all degrees), and component sizes agree exactly with the displayed table. A second, independently formulated checker, `verify_fast.cpp`, constructs \(H\) instead from the seven nonzero binary three-vectors as points and nonzero linear forms as line labels, using zero dot product for incidence, and tests domination by union of closed-neighborhood masks. It separately reproduces each graph's orders, edges, component sizes, and distances.

A useful structural explanation of the component barriers is the following lemma. Given a finite graph \(G\), connect two distinct inclusion-minimal dominating sets \(A,B\) of size at most \(k\) whenever \(|A\cup B|\le k\). This *minimal-set overlap graph* has the same connected-component partition of its minimal sets as \(D_k(G)\), and every component of \(D_k(G)\) contains a minimal set. Indeed every dominating set can delete vertices down to an inclusion-minimal one. If \(|A\cup B|\le k\), additions from \(A\) to \(A\cup B\), followed by deletions down to \(B\), give a valid path. Conversely, for adjacent states \(S,T\) of \(D_k(G)\), one contains the other, so both contain a common minimal dominating subset of their smaller state. More generally all minimal subsets of any single dominating state are connected through that state; tracing an arbitrary path in \(D_k(G)\) gives an overlap walk among minimal subsets. The component correspondence follows.

The geometric minimal-set classification shows explicitly why \(D_4(H)\) has \(21\) isolated vertices; why at \(k=5\) each four-set generates a separate \(K_{1,10}\) (its ten immediate supersets) and each minimal five-set is isolated; why \(28\) minimal six-sets remain isolated at \(k=6\); and why exactly the two size-seven bipartition classes remain isolated at \(k=7\). At \(k=8\), all minimal sets are in one component. Because every dominating set contains one of the classified minimal sets, connectedness persists for all larger budgets; it also follows from the pre-existing general bipartite bound at \(\Gamma(H)+1=8\).

**Step 3: exact distances.** For each \(k\in\{5,6,7,8\}\), the Python program performs a fresh full breadth-first search from **every vertex of the largest connected component**, checks that each search reaches the full component, and records the largest distance from its source. The minimum and maximum of these eccentricities are, by definition, the exact radius and diameter. This computes respectively \((1,2),(10,12),(11,14),(12,14)\); singleton components have radius and diameter zero. The C++ verifier repeats every all-source search with a distinct incidence and domination implementation. Hence these finite metric equalities are fully exhaustive mathematical proofs conditional only on the directly inspectable source programs, not samples of distances or unproved infinite generalizations. \(\square\)

## Verification
From the directory containing this file, run `python3 verify.py` with a Python 3 interpreter supporting integer `bit_count`; the program requires only the standard library and terminates with `VERIFY_OK full exhaustive classification` after checking every subset, every indicated budget, the geometric family equality and every all-source eccentricity. For a completely separate model and independent shortest-path implementation run `g++ -std=c++17 -O2 verify_fast.cpp -o verify_fast && ./verify_fast`. This terminates with `VERIFY_OK C++ independent graph and metrics`, or exits nonzero on a failed check. The two programs construct the graph from different Fano plane coordinatizations, and agree on all reported finite invariants. Neither calls a database, imports another packaged file, or relies on an external answer table at runtime.

## Relationship to prior work
Haas and Seyffarth introduced the exact add/delete \(D_k\) convention in *The \(k\)-Dominating Graph* (first publicly available 2012-09-24). Their Theorem 7 establishes connectivity of \(D_{\Gamma(G)+1}(G)\) for nontrivial bipartite graphs, and their general Lemma 3 establishes disconnectivity at \(k=\Gamma(G)\). Hence connectivity at \(k=8\), and isolation of a maximum-size minimal dominating set at \(k=7\), are **already covered in general form**. They do not give the Heawood-specific four geometric families, the exact cardinalities of the full reconfiguration graphs at budgets \(4\) through \(8\), the intermediate component multiplicities, or exact radii and diameters. Their concluding section explicitly identifies exact diameters as an interesting general question.

Suzuki, Mouawad and Nishimura (2014) provide general connectivity and exponential-diameter constructions for dominating-set reconfiguration, not the finite Heawood component metric. Alikhani, Fatehi and Klavžar (2015) study the structure of related dominating graphs, without deriving this exact Heawood TAR phase portrait. The later survey by Mynhardt and Nasserasr covers general reconfiguration results, not these enumerated Fano-incidence distances. Exact ordinary domination polynomials, if tabulated elsewhere, determine only vertex counts by budget; they do **not** imply component sizes, edge counts, eccentricities or geometric types. Other published work on Heawood coloring reconfiguration and homomorphism complexes uses different state spaces and cannot imply the stated theorem by a change of notation.

## Limitations
The exact distance classification is only for \(4\le k\le8\); connectivity but not the diameter is asserted for larger budgets. The work does not assert new general bipartite connectivity. The proof is a finite exhaustive certificate rather than a short closed-form case analysis, so recomputation and inspection of the included code are important. The findings have not received independent external validation. Although targeted published-source and indexed-result searches found no prior covering statement, obscure or unindexed exact Heawood tables remain a residual originality risk.

## References
1. R. Haas and K. Seyffarth, *The k-Dominating Graph*, arXiv:1209.5138v1 (2012-09-24), https://arxiv.org/abs/1209.5138 .
2. A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714v1 (2014-01-22), https://arxiv.org/abs/1401.5714 .
3. S. Alikhani, D. Fatehi and S. Klavžar, *On the Structure of Dominating Graphs*, arXiv:1512.07514 (2015), https://arxiv.org/abs/1512.07514 .
4. C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: A Survey*, arXiv:2003.05956 (2020), https://arxiv.org/abs/2003.05956 .
