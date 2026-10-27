# Seven injective edge colors suffice, and are necessary, for the five-cube

## Finding
Let \(Q_5\) be the simple binary five-dimensional hypercube. An *injective edge coloring* is an assignment of colors to its edges in which any two edges joined by a distinct third edge must receive different colors; adjacent edges themselves need not have different colors. Then
\[
\boxed{\chi'_i(Q_5)=7.}
\]
Moreover, the seven colors can be assigned equitably: three color classes have twelve edges and four have eleven. Each color class is an edge-open packing.

## Assumptions and scope
Identify cube vertices with integers \(0,\ldots,31\), regarded as five-bit words. Distinct vertices are adjacent exactly when their bitwise XOR has one nonzero bit. Order all eighty undirected edges lexicographically by the following unambiguous procedure: loop \(u=0,1,\ldots,31\), then \(j=0,1,\ldots,4\); append \((u,u\mathbin{\mathrm{xor}}2^j)\) only when the second endpoint exceeds the first. An injective coloring forbids equal colors on distinct edges \(e,f\) if some graph edge \(g\notin\{e,f\}\) has one endpoint on \(e\) and another on \(f\). In this triangle-free graph, incident edges cannot conflict; two disjoint edges conflict exactly when one of the four cross-endpoint pairs forms a cube edge. This definition is not proper or strong edge coloring.

## Proof
**Lower bound.** We verify exhaustively, using an exact integer branch-and-bound search with a fully specified completeness argument, that every edge-open packing of \(Q_5\) contains at most twelve edges. The cube is edge-transitive: coordinate permutations together with bit-flip translations send any chosen cube edge to \((0,1)\). Therefore a hypothetical packing of size thirteen may be assumed to contain \((0,1)\). Exactly fifty-one of the other seventy-nine edges can coexist with this anchor. On those fifty-one candidate edges, join two vertices of an auxiliary compatibility graph when their corresponding cube edges have no third-edge conflict. A thirteen-edge packing containing the anchor is equivalent to a clique of order twelve in this compatibility graph.

The supplied exhaustive checker proves that there is no clique of size twelve, as follows. At each recursive call a current candidate set is greedily colored into independent classes of the compatibility graph; a clique can contain at most one vertex from each such class. The checker lists candidates in nondecreasing class order and branches over every possible final clique vertex, intersecting the remaining candidates with that vertex's neighbors. It prunes only when the current clique cardinality plus the number of available classes is less than twelve. The graph is rebuilt solely from the displayed binary adjacency definition. The search finishes after 59 recursive calls and 58 branches. The statement does not depend on a floating-point solver, on randomized sampling, or on assuming a precomputed optimum. Consequently every edge-open packing has size at most twelve, and a partition of eighty edges into color classes requires at least \(\lceil80/12\rceil=7\) colors.

**Upper bound.** In the explicit edge order defined above, assign the following eighty entries as colors \(0,\ldots,6\), consecutively in five groups of sixteen:

```
0 6 5 3 2 0 0 0 0 1 1 6 6 4 2 3
5 5 5 5 6 3 2 4 2 3 6 6 1 3 1 3
2 4 6 5 0 4 5 2 4 2 6 3 3 0 2 1
1 2 1 2 3 4 6 5 0 4 5 3 4 3 6 2
2 0 3 1 5 4 0 6 5 4 4 1 0 6 1 1
```

The separate checker reconstructs all eighty edges, independently evaluates all \(\binom{80}{2}\) unordered pairs, and finds exactly 1120 conflicting pairs. It verifies that each has different colors. The color-class sizes, sorted ascending, are \(11,11,11,11,12,12,12\). Thus seven colors suffice, with an equitable assignment. The matching upper and lower bounds establish the theorem.

## Verification
The standalone source `verify_q5.py` uses only the Python standard library. Run `python3 verify_q5.py` in a directory containing that file. The second independent implementation `verify_q5.cpp` may be compiled with `g++ -std=c++17 -O3 verify_q5.cpp -o verify_q5` and run as `./verify_q5`; it checks the same twelve-edge upper bound and an explicit twelve-edge packing. The supplied `checks.txt` contains the exact output recorded from each executable. The Python checker confirms 51 anchor-compatible edges, 59 exact-search calls, all 1120 conflicting pairs, and the seven-color distribution. This is a finite exhaustive proof: the bitset search covers every candidate, with mathematically justified clique bounds. It does not rely on an extrapolation from finite experiments.

## Relationship to prior work
The 2024 study by Brešar and Samadi (arXiv:2403.00750, §1) explicitly identifies injective edge coloring with partitioning the edges into edge-open packings, but primarily studies packing complexity and bounds. Brešar, Dravec, Hedžet and Samadi (arXiv:2406.04020, §5.1, especially Table 1 and Theorem 5.10) prove exact edge-open packing numbers for cube dimensions that are powers of two, and give a lower bound of ten for the five-cube. The 2023 article of Bhanupriya, Dominic and Sunitha analyzes injective edge indices for several Cartesian graph products involving paths and cycles, not the five-fold Cartesian product of \(K_2\). The present statement determines a distinct quantity, the **minimum number of edge-open-packing classes needed to partition all eighty edges**. Knowing the maximum size of a packing alone supplies the lower bound, but not a seven-class partition; the explicit equitable certificate is therefore essential.

## Limitations
This result treats the labeled five-dimensional binary cube and ordinary injective edge coloring only. It does not assert a formula for other cube dimensions or enumerate all optimal colorings. The lower bound uses a reproducible finite exhaustive search, rather than a short manual inequality; independent human verification of the source and an external audit remain outstanding. Despite searches, unindexed equivalent literature remains a possible priority risk.

## References
1. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1 (first public 1 March 2024), §1 and §4, https://arxiv.org/abs/2403.00750.
2. B. Brešar, T. Dravec, J. Hedžet, B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020v1 (first public 6 June 2024), §5.1, https://arxiv.org/abs/2406.04020.
3. Bhanupriya C. K., C. Dominic and M. S. Sunitha, *Injective edge coloring of product graphs and some complexity results*, Filomat 37 (2023), 3963–3983, doi:10.2298/FIL2312963K, §2 and §4.
