# The first orbit-refinement obstructions among split graphs

## Finding

Let \(G\) be a finite simple **split graph** (its vertex set is the disjoint union of a clique and an independent set). Start ordinary one-dimensional counting colour refinement with one common vertex colour; at each round retain the previous colour and refine according to the multiplicities of neighbour colours. Call \(G\) **orbit-exact** when its final colour classes are precisely the vertex orbits of \(\operatorname{Aut}(G)\).

**Sharp finite cutoff.** Every split graph with at most nine vertices is orbit-exact. Among split graphs with ten vertices, exactly **four nonisomorphic graphs** are not orbit-exact; all four are connected. Every one has just two stable colour classes (the clique and independent part), but more than two automorphism orbits.

The following four explicit graphs give the complete list. To decode each row, take clique vertices \(0,\ldots,k-1\) and one independent vertex for each listed integer mask \(b\); connect this vertex to clique vertex \(i\) exactly when the \(i\)-th binary bit of \(b\) is \(1\). Repeated masks designate distinct independent vertices. Each row has ten vertices.

| Clique size \(k\) | Independent-neighbourhood masks | Stable class sizes | Automorphism-orbit sizes | Automorphisms | Enumeration multiplicity |
| --- | --- | --- | --- | --- | --- |
| 4 | 3, 3, 5, 10, 12, 12 | 4, 6 | 2, 4, 4 | 16 | 6 |
| 5 | 3, 3, 12, 20, 24 | 5, 5 | 2, 2, 3, 3 | 24 | 10 |
| 5 | 7, 7, 25, 26, 28 | 5, 5 | 2, 2, 3, 3 | 24 | 10 |
| 6 | 7, 11, 52, 56 | 4, 6 | 2, 4, 4 | 16 | 45 |

Here *enumeration multiplicity* refers to labelled-clique/multiset-independent-set incidence descriptions, **not** to the number of isomorphism types. The multiplicities sum to \(71\), and every violating description belongs to exactly one of the four graph-isomorphism types.

## Assumptions and scope

Graphs are finite, simple, undirected and need not be connected a priori. A split representation is any partition \(V(G)=K\sqcup I\) with \(G[K]\) complete and \(G[I]\) edgeless. Colour refinement is the standard simultaneous counting process with initial vertex colours all equal and signatures \((c_t(v),(\#\{w\in N(v):c_t(w)=j\})_j)\). Equal signature means equal next colour. Stabilization means that the **partition**, rather than arbitrary numeric colour names, ceases to change. Automorphism orbits use the full uncoloured graph. No conclusions about larger split graphs, graph identification against other graphs, or higher-dimensional refinement are claimed.

## Proof

**1. Exhaustive family without omissions.** Fix order \(n\), a clique size \(k\) between \(0\) and \(n\), and put \(m=n-k\). Give clique vertices the names \(0,\dots,k-1\). The neighbourhood of each vertex of \(I\) in \(K\) is an arbitrary subset of those \(k\) vertices, encoded by an integer \(b\in\{0,\ldots,2^k-1\}\). Permutations of the independent vertices permit their \(m\) masks to be written in nondecreasing order. Conversely, every such sorted mask list defines a split graph. Thus running through all \(k\) and all multisets of \(m\) masks loses no split graph. It may enumerate the same unlabelled graph more than once; that redundancy cannot hide an obstruction. The number of tested presentations at order \(n\) is exactly

\[
N_n=\sum_{k=0}^n\binom{2^k+n-k-1}{n-k}.
\]

Direct substitution yields the exact verified presentation counts, for \(n=1,\ldots,10\):

\[
2,\ 4,\ 9,\ 24,\ 79,\ 331,\ 1803,\ 12954,\ 123983,\ 1592513.
\]

**2. Exact finite orbit and colour decisions.** For every presentation, the supplied finite checker first constructs its adjacency matrix. Its `stable_colors` procedure refines by the current colour and the entire neighbour-colour multiplicity vector; it stops only when pairwise equality classes are unchanged. Since every strict step increases the number of classes, its termination and equality with the stable partition follow for every finite input. All automorphisms preserve every refinement colour, by induction. Therefore orbit-exactness is equivalent to the assertion that for every pair of vertices remaining in one stable colour class, some graph automorphism sends the first vertex to the second.

For each such pair, `Automorphism::moves` fixes that image and executes a finite backtracking search for a bijection. At each recursive step it assigns one unassigned source vertex to a previously unused target of the same stable colour, checking both adjacency and nonadjacency with every previously assigned vertex. Every legitimate automorphism extending the partial mapping is among the branches, and any completed bijection preserves all adjacencies and nonadjacencies because every vertex pair has been tested at the time its later endpoint is assigned. Consequently a successful branch is exactly an automorphism witnessing orbit equivalence, and an exhausted search proves none exists. The `orbit_exact` test is therefore a finite exact decision procedure, not a sampling heuristic.

**3. Exhaustive output and sharp cutoff.** The checker runs all the representations just counted. At each \(n=1,\ldots,9\) it finds zero colour/orbit discrepancies. At \(n=10\) it finds exactly \(71\) failing presentations, each explicitly printed as a \(k\)-value and mask list in `cutoff_census.txt`. This proves the lower bound and supplies a finite, reconstructible complete list of the exceptional presentations. The independent code `verify_split_small_independent.cpp` enumerates the entire range \(1\le n\le9\) by a separate automorphism strategy using row permutations of the clique-to-independent incidence matrix and equal-mask column permutations. It checks separately that every cross-part co-coloured pair is a twin pair, hence exchangeable. Its output reproduces the zero-exception cutoff and the presentation counts.

**4. Four graph-isomorphism types, not seventy-one.** For every one of the \(71\) ten-vertex failing presentations, the checker verifies that (i) all clique vertices have a common degree, (ii) all independent vertices have another common degree, and (iii) the former is strictly greater. These two degree groups are therefore intrinsic to the unlabelled graph; every graph isomorphism must preserve the chosen split parts. For such a graph, isomorphism is equivalent to relabelling the clique vertices (permuting bit positions in every mask) and permuting the independent vertices (sorting the transformed mask multiset). The supplied `column_canonical` routine tries every one of the \(k!\) clique permutations, sorts all transformed masks, and takes their lexicographically minimum list. This is a canonical invariant which is also complete for these graphs. Applied to the \(71\) listed failing descriptions, it yields precisely the four canonical rows shown in the finding, occurring respectively \(6,10,10,45\) times. For each representative, `verify_split_ten.py` independently enumerates full degree-preserving graph automorphisms and checks every edge, producing the stable-class sizes, automorphism-orbit sizes and group orders in the table. All four are connected (indeed every independent vertex in the table has positive degree and the clique is nonempty). Since every split graph occurs among the tested presentations and every failing one belongs to one of these four orbits of representations, the classification is complete. \(\square\)

## Verification

The package contains standalone source and execution records. With C++17 and Python 3, from a directory containing these embedded files, execute:

```sh
g++ -std=c++17 -O3 -Wall -Wextra verify_split_cutoff.cpp -o verify_split_cutoff
./verify_split_cutoff > cutoff_census.txt
g++ -std=c++17 -O3 verify_split_small_independent.cpp -o verify_split_small_independent
./verify_split_small_independent > independent_census.txt
python3 verify_split_ten.py cutoff_census.txt > ten_replay.txt
```

`cutoff_census.txt` records every exceptional incidence presentation, all tested presentation counts, and the four canonical classes. `independent_census.txt` independently checks all orders through nine; `ten_replay.txt` independently checks the four exceptional ten-vertex groups. The original execution outputs are embedded. The proof of universality is the explicit finite exhaustive range and the verified completeness of its representation and decision procedures, not an extrapolation from a sample.

## Relationship to prior work

The general concept of a graph being *refinable* (stable counting-colour classes equal automorphism orbits) is treated in Arvind–Köbler–Rattan–Verbitsky, arXiv:1502.01255. Their general hierarchy does not state a sharp ten-vertex split-graph obstruction classification. Boros–Gurvich–Milanič, arXiv:1505.05683, gives structural background about split graphs but no such counting-refinement census. Arvind–Fuhlbrück–Köbler–Kuhnert–Rattan, arXiv:1606.04383, concerns individualization and fixing problems, not this exact split-graph cutoff. An existing eight-vertex obstruction for unrestricted chordal graphs would not imply the sharper cutoff in the proper hereditary subclass of split graphs. Published related constructions, general 1-WL refinability results and enumerations of split graphs were searched; no result directly covering the four-isomorphism-type theorem was identified. This negative search is **not** a claim of publication priority or an exhaustive guarantee that no stronger specialized theorem exists.

## Limitations

The theorem is a finite cutoff and complete first-obstruction layer, not an all-order characterization. The presentation counts are counts of multiset-encoded split representations, not counts of isomorphism classes. Full source listings and actual outputs are necessary to assess the exhaustive computation; bare logs, counts or nonexhaustive experiments alone would not certify the claim. An unlocated earlier specialized result might imply the classification. Scientific assessment is same-model only; independent audit and independent publication-priority determination have not been performed.

## References

- V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public 2015-02-04).
- E. Boros, V. Gurvich, M. Milanič, *On Equistable, Split, CIS, and Related Classes of Graphs*, arXiv:1505.05683 (2015).
- V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert, G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, arXiv:1606.04383 (2016).
