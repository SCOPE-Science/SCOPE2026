# Minimum zero-forcing configurations and their exchange geometry in the Petersen line graph

## Finding

For the Petersen graph \(P=\operatorname{KG}(5,2)\) and its line graph \(H=L(P)\), the minimum ordinary zero-forcing number is \(Z(H)=7\). Exactly \(2280\) minimum zero-forcing sets exist. The full automorphism group \(S_5\) partitions them into \(21\) orbits: \(17\) of length \(120\), and \(4\) of length \(60\). Their minimum parallel-forcing times have the exact distribution
\[
\#\{B:\operatorname{pt}(H,B)=3\}=120,\quad
\#\{B:\operatorname{pt}(H,B)=4\}=1440,\quad
\#\{B:\operatorname{pt}(H,B)=5\}=720.
\]
Let \(\mathcal R\) be the graph whose vertices are all \(2280\) minimum forcing sets, adjacent when one chosen vertex can be replaced by one unchosen vertex while remaining a minimum forcing set. Then \(\mathcal R\) is connected, has \(28650\) edges and diameter \(7\). Its full unordered-pair distance enumerator is
\[
D_{\mathcal R}(z)=28650z+234120z^2+765570z^3+1004640z^4
+483480z^5+78540z^6+3060z^7.
\]

## Assumptions and scope

All graphs are finite, simple, undirected and unweighted. Number the \(10\) Petersen vertices by the lexicographically sorted two-element subsets of \(\{0,1,2,3,4\}\), with two vertices adjacent if their subsets are disjoint. Enumerate the \(15\) Petersen edges lexicographically as unordered pairs of these vertex indices. Those \(15\) edges are the vertices of \(H\); two are adjacent if they share a Petersen endpoint. Thus \(H\) is a four-regular \(15\)-vertex graph with \(30\) edges.

A blue vertex of \(H\) forces its unique white neighbor when it has exactly one white neighbor. A set is zero forcing if repeated legal forces color every vertex blue. At a parallel forcing round, all available forces are executed simultaneously. The propagation time is the number of nonempty parallel rounds until all vertices are blue. A minimum forcing set has the smallest possible cardinality among forcing sets. No statement is made about larger forcing sets or a family of other line graphs.

The canonical binary mask \(m(B)=\sum_{i\in B}2^i\) represents a chosen set of Petersen edge indices. The following list gives a representative of every orbit; orbit sizes and propagation times are constant within each orbit. The file `ORBIT_TABLE.csv` contains the same complete list in machine-readable form.

| Canonical mask | Orbit cardinality | Parallel rounds |
| ---: | ---: | ---: |
| `239` | 120 | 5 |
| `247` | 120 | 5 |
| `253` | 60 | 3 |
| `254` | 120 | 4 |
| `439` | 60 | 4 |
| `687` | 120 | 5 |
| `695` | 120 | 5 |
| `699` | 120 | 5 |
| `701` | 120 | 4 |
| `702` | 120 | 4 |
| `762` | 120 | 5 |
| `979` | 120 | 4 |
| `981` | 60 | 4 |
| `4334` | 120 | 4 |
| `4341` | 120 | 4 |
| `4345` | 60 | 3 |
| `4346` | 120 | 4 |
| `4495` | 120 | 4 |
| `4503` | 120 | 4 |
| `4555` | 120 | 4 |
| `4781` | 120 | 4 |

## Proof

**Closure criterion.** For a blue vertex set \(B\subseteq V(H)\), let
\[
\Phi(B)=B\cup\{v:\exists u\in B,\ N_H(u)\setminus B=\{v\}\}.
\]
Iterate \(\Phi\) until a fixed point is reached. Every newly included vertex can legally be forced at that stage. If \(v\) is forceable from a subset \(B\subseteq C\), then either \(v\in C\), or it remains the only white neighbor of its forcing vertex in \(C\). Therefore the closure is independent of the order of legal moves and is the unique maximal attainable blue set. A seed is zero forcing exactly when its closure is \(V(H)\); the nontrivial fixed point cannot be extended by any force.

**Minimum size and complete enumeration.** The executable `verify.py` builds the Petersen graph from the disjointness rule above and obtains each line-graph neighborhood from edge incidence. It checks every one of the \(2^{15}=32768\) blue masks, with two independent implementations (integer masks and literal vertex sets) of the forcing closure. It then tests *every* subset of sizes \(0\) through \(6\), finding none with full closure. Exhaustive testing of the \(\binom{15}{7}=6435\) seven-element masks finds exactly \(2280\) whose closure is full. These mutually exhaustive finite ranges establish \(Z(H)=7\) and the asserted exact minimum-set count, without extrapolation.

**The acting group and orbit certificate.** Permuting the five symbols of \(\operatorname{KG}(5,2)\) induces \(120\) distinct automorphisms of \(H\). They are all the automorphisms: \(P\) is triangle-free, so every triangle of \(H\) consists of the three original edges at a common Petersen vertex. Consequently each automorphism of \(H\) permutes those ten distinguished triangles and reconstructs an automorphism of \(P\). The complement of \(P\) is the line graph of \(K_5\), whose five maximal four-cliques are exactly the five stars, forcing every automorphism of \(P\) to arise from permuting the five symbols. The verifier computes the orbits of the \(2280\) masks under these \(120\) permutations, removes each entire orbit before choosing its next lexicographically least representative, and finds the \(21\) listed representatives. Their orbit cardinalities add to \(2280\), certifying that the orbit list is complete.

**Propagation and optimal-set exchanges.** The same closure iteration counts the strictly expanding parallel rounds for every one of the \(2280\) sets, giving \(120\) cases of three rounds, \(1440\) of four rounds, and \(720\) of five rounds. For optimal masks \(a,b\), exactly one selected vertex is exchanged precisely when \(|a\triangle b|=2\). The verifier constructs every such neighbor by trying all \(7\times8=56\) removed/inserted index pairs, keeping only masks in the independently enumerated optimal-set collection. This gives \(28650\) undirected edges. Exact breadth-first search from each of the \(2280\) vertices yields the full distance enumerator. Its coefficients sum to \(\binom{2280}{2}=2598060\), every distance is finite, and the largest is \(7\), proving connectivity and the diameter.

## Verification

Run `python3 verify.py` with Python 3.10 or later; no nonstandard modules or external data are required. The program independently builds incidence, compares two forcing implementations on all \(32768\) masks, checks the complete lower and upper extremal searches, verifies the \(21\) orbit representatives and sizes, and computes all ordered-source shortest paths in the exchange graph before summing each unordered pair once. The expected terminal marker is `VERIFY_OK`; the actual execution produced this marker and the distributions stated above. The complete binary-mask representatives appear in `ORBIT_TABLE.csv`.

## Relationship to prior work

Eroh, Kang and Yi introduced exact zero-forcing computations on the line graphs of wheels and bouquets and gave general comparisons between zero forcing and metric dimension of line graphs. Their 2012 preprint does not determine the minimum forcing sets of the Petersen line graph. Hogben and coauthors developed the parallel propagation-time invariant and discussed the *Petersen graph itself*, not its line graph, in their 2014 preprint. Erzurumluoğlu, Meagher and Pike established graph-independent comparisons involving brushing and zero forcing of line graphs. Their 2016 preprint gives inequalities but not the mask-by-mask, symmetry or reconfiguration classification here.

Knowledge of the ordinary Petersen zero-forcing number does not imply the value or multiplicity for its line graph. Likewise, neither the inequalities for arbitrary line graphs nor the propagation-time definitions yield the orbit or exchange-distance enumerator. The claim is a finite exact classification for this canonical line graph; it is not a strengthening of general bounds to arbitrary graphs.

## Limitations

The proof is exhaustive and finite, not a structural formula for an infinite graph family. Exactness relies on re-executing the provided deterministic Python verifier, whose input construction is fully specified and whose loops cover all needed finite states. An independent external mathematical audit has not been performed. Searches found no prior source implying this complete classification, but unindexed computational tables or unpublished enumerations may exist; absence of a search hit is not a proof of historical novelty. The graph is small, but the fully enumerated optimal-set symmetry, propagation and exchange geometry is the mathematical object of the finding.

## References

1. L. Eroh, C. X. Kang and E. Yi, *Metric Dimension and Zero Forcing Number of Two Families of Line Graphs*, arXiv:1207.6127, first posted 2012-07-25, https://arxiv.org/abs/1207.6127 .
2. L. Hogben et al., *Propagation time for zero forcing on a graph*, arXiv:1410.4191, first posted 2014-10-15, https://arxiv.org/abs/1410.4191 .
3. A. Erzurumluoğlu, K. Meagher and D. A. Pike, *Brushing Number and Zero-Forcing Number of Graphs and their Line Graphs*, arXiv:1609.05854, first posted 2016-09-19, https://arxiv.org/abs/1609.05854 .
