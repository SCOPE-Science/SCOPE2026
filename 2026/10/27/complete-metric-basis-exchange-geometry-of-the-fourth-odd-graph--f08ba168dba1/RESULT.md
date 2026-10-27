# Complete metric-basis exchange geometry of the fourth Odd graph

## Finding

Let \(O_4=KG(7,3)\) be the fourth Odd graph: its vertices are the \(35\) three-subsets of \(\{1,2,3,4,5,6,7\}\), adjacent precisely when disjoint. Two distinct five-vertex subsets \(B,B'\) are adjacent in the **minimum metric-basis exchange graph** \(\mathcal B(O_4)\) exactly when \(|B\cap B'|=4\) and both resolve all vertices of \(O_4\).

The known metric dimension is \(\beta(O_4)=5\). Beyond this known cardinality, there are **exactly \(149{,}184\) minimum resolving sets**. Their exchange graph has \(6{,}331{,}500\) edges, is connected, and has
\[
\operatorname{rad}(\mathcal B(O_4))=5,\qquad
\operatorname{diam}(\mathcal B(O_4))=6.
\]
Its full eccentricity distribution is \(146{,}160\) vertices of eccentricity \(5\), and \(3{,}024\) of eccentricity \(6\). The natural action of \(S_7\) on the seven ground symbols has exactly \(48\) orbits on the metric bases; the two orbits of eccentricity \(6\) have cardinalities \(504\) and \(2{,}520\).

Exactly the same family of resolving subsets, and hence precisely the same exchange graph, occurs for the Johnson graph \(J(7,3)\), on the same vertex set.

## Assumptions and scope

All graphs are simple and finite. The graph \(O_4\) is defined on the \(35\) actual labeled three-subsets, not on isomorphism classes. For a graph \(G\), a set \(B\subseteq V(G)\) is **resolving** if for every pair of distinct vertices \(u,v\), there is \(b\in B\) with \(d_G(u,b)\ne d_G(v,b)\). A **metric basis** is a resolving subset of smallest cardinality. In \(\mathcal B(O_4)\), a legal move replaces exactly one chosen three-subset by exactly one unchosen three-subset while retaining minimum resolving size. The asserted radius and diameter are graph distances measured in these moves, not distances inside \(O_4\).

For three-subsets \(U,W\), the possible intersection sizes \(3,0,2,1\) correspond respectively to shortest-path distances \(0,1,2,3\) in \(O_4\). In \(J(7,3)\), the corresponding distance is \(3-|U\cap W|\). Thus both distances are injective functions of intersection size, so a vertex set resolves one graph if and only if it resolves the other. The ordinary vertex-to-vertex metric is used throughout, not edge metric dimension, strong metric dimension or a determining-set condition.

## Proof

**1. Exact resolving predicate and minimum size.** Enumerate the \(35\) three-subsets as increasing seven-bit integers with exactly three set bits. The adjacency predicate in \(O_4\) is bitwise disjointness, and breadth-first search in that graph computes all \(35\times35\) distances; independently, the intersection-size signatures distinguish precisely the same pairs. A candidate \(B=\{b_1,\ldots,b_r\}\) resolves if and only if the \(35\) vectors \((d_G(u,b_1),\ldots,d_G(u,b_r))\), as \(u\) varies over the graph vertices, are pairwise distinct. These predicates use integer data and no numerical tolerances.

The standalone programs `odd4_full.cpp` and `verify_intersection.py` enumerate **all** \(\binom{35}{5}=324{,}632\) distinct five-subsets and return \(149{,}184\) resolving ones. The independent intersection-based script enumerates **all** \(\binom{35}{4}=52{,}360\) four-subsets and finds none resolving. Since resolving sets are upward closed under inclusion, absence of resolving four-subsets rules out every smaller cardinality as well. The separate `odd4.cpp` checks the same minimum by enumerating candidates through a fixed graph vertex and using transitivity: it finds \(21{,}312\) five-bases containing a fixed vertex, giving \(21{,}312\cdot35/5=149{,}184\) in total.

**2. Exact exchange graph.** Represent each five-base as a \(35\)-bit subset mask. Every legal exchange deletes one of the five selected bits and inserts one of the thirty unselected bits. Lookup in the complete list of bases decides legality. Both `odd4_full.cpp` and `verify_intersection.py` exhaustively generate these exchanges. Their sum of degrees is \(12{,}663{,}000\), so undirected edge count is \(6{,}331{,}500\). Independently constructed disjoint-set connectivity tests show that all \(149{,}184\) vertices are in one component.

**3. Complete distance analysis by symmetry.** Each adjacent transposition of the seven ground symbols induces a permutation of all \(35\) three-subsets, preserves disjointness, and hence preserves both resolving sets and the exchange relation. The six adjacent transpositions generate \(S_7\). Applying these six maps to every metric basis and taking transitive closure partitions the complete list into exactly \(48\) orbits. Their sizes are: one orbit of \(420\), one of \(504\), one of \(840\), five of \(1{,}260\), twenty-four of \(2{,}520\), and sixteen of \(5{,}040\); their sum is \(149{,}184\).

An exchange-graph automorphism preserves every shortest-path distance. Therefore eccentricity is constant on each of the \(48\) orbits. `odd4_full.cpp` runs a complete breadth-first search from one representative of **every orbit**, visits all \(149{,}184\) vertices on each search, and computes the farthest reached distance. Exactly two orbits have eccentricity \(6\), with sizes \(504\) and \(2{,}520\); all remaining orbits have eccentricity \(5\). Their total size gives the stated eccentricity distribution. In particular the global minimum and maximum eccentricities are \(5\) and \(6\), proving both radius and diameter, not only a sampled bound.

For an explicit lower-bound witness, encode each three-subset \(T\subseteq\{1,\ldots,7\}\) as \(\sum_{i\in T}2^{i-1}\). The bases with encoded five-element lists \((7,11,21,73,112)\) and \((38,42,52,81,104)\) have exchange distance exactly \(6\). A second pair is \((7,11,37,73,97)\) and \((22,26,52,88,112)\). These pairwise distances are recomputed independently by the Python script with direct neighborhood generation and breadth-first search. The complete orbit-representative searches prove the upper bound for every pair.

## Verification

The embedded standalone sources and their recorded exact output are `odd4_full.cpp`, `odd4_full.stdout`, `odd4.cpp`, `odd4.stdout`, `verify_intersection.py`, and `verify_intersection.stdout`. A reproducible run in a directory containing these files is:

```sh
g++ -std=c++17 -O3 odd4_full.cpp -o odd4_full
g++ -std=c++17 -O3 odd4.cpp -o odd4
./odd4_full
./odd4
python3 verify_intersection.py
```

The Python checker requires Python \(3.10\) or later, and the C++ programs a compiler supporting GNU C++17. All three tests use exact integer and bitset operations and deterministic enumeration. The full checker reports `minbases=149184`, `exchange_edges=6331500`, `components=1`, `orbits=48`, `radius=5`, `diameter=6`, and the exact stated orbit and eccentricity histograms; it does not infer diameter from a small sample. The independent checker reports no resolving four-sets, \(149{,}184\) resolving five-sets, \(6{,}331{,}500\) edges and one connected component, independently reconstructs the 48-orbit partition, and confirms two six-step witnesses.

## Relationship to prior work

Bailey, Cáceres, Garijo, González, Márquez, Meagher and Puertas (2012 preprint, 2013 journal) establish the definition of resolving sets for Johnson and Kneser graphs, the bijective intersection-distance correspondence for Odd graphs, and resolving constructions including a seven-element Fano-plane resolving set for \(O_4\). In that work the general exact metric dimension for three-subsets was not settled. Peng, Wang, Wang and Chen (2016) subsequently establish the specific cardinality \(\beta(KG(7,3))=5\), so the cardinality five is explicitly **prior work** here, not the newly claimed contribution. The present theorem adds the complete count of optimal bases, their \(S_7\)-orbit partition and the exact single-exchange graph, including its eccentricity distribution and diameter.

A known theorem about metric dimension alone gives no implication for the number of optimal sets or their exchange connectivity. The Johnson/Kneser resolving-set correspondence does transfer the new count and exchange graph to \(J(7,3)\); that equivalent formulation is explicitly part of the comparison rather than an independent novelty claim.

## Limitations

This is an exhaustive finite result for exactly the labeled graphs \(KG(7,3)\) and \(J(7,3)\). It does not establish a formula for higher Odd graphs, mixing times, or a non-computational classification of all bases. Although two independently organized enumeration predicates and connectivity implementations agree, the complete orbit-eccentricity upper bound currently uses a single exhaustive C++ search with the mathematically justified \(S_7\)-orbit reduction. The 2016 exact-dimension article was accessible at bibliographic and abstract level, not as primary full text; a previously unindexed table enumerating metric bases or their exchanges remains a literature-priority risk.

## References

1. R. F. Bailey, J. Cáceres, D. Garijo, A. González, A. Márquez, K. Meagher, M. L. Puertas, *Resolving sets for Johnson and Kneser graphs*, arXiv:1203.2660 (first public version 12 March 2012); *European Journal of Combinatorics* **34** (2013), 736–751, DOI:10.1016/j.ejc.2012.10.008. Open full text: https://arxiv.org/pdf/1203.2660.
2. H. Peng, X. Wang, J. Wang, S. Chen, *The Metric Dimension of Some Kneser Graphs*, *Journal of Computational and Theoretical Nanoscience* **13** (2016), 3013–3018, DOI:10.1166/jctn.2016.4951 (abstract consulted; full text not available in this review).
