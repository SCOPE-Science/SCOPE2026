# Triangular blocks and shortest-path geometry of the Heawood metric-basis exchange graph

## Finding

Let \(H\) be the incidence graph of the Fano plane. Its fourteen vertices are seven points and seven lines, and a point is adjacent to the three lines containing it. A *resolving set* \(S\subseteq V(H)\) is a set for which the distance vectors \((d_H(v,s))_{s\in S}\), indexed by a fixed order of \(S\), distinguish all fourteen vertices. A *metric basis* is a resolving set of minimum size.

The known minimum basis size is five. Define \(\mathcal R(H)\) to have these minimum metric bases as vertices, with two bases adjacent when they differ by deleting one vertex and adding one other vertex. Then \(\mathcal R(H)\) has exactly \(168\) vertices and \(420\) edges, is connected and five-regular, and is vertex-transitive under the natural incidence-graph automorphism group of order \(336\). Its eccentricity is five at **every** vertex, so its radius and diameter are both five.

More precisely, each basis has precisely \(1,5,18,49,71,24\) bases at respective exchange distances \(0,1,2,3,4,5\). The numbers of *unordered* basis pairs at respective distances \(1,2,3,4,5\) are
\[
420,\quad1512,\quad4116,\quad5964,\quad2016.
\]
The graph's \(168\) vertices partition into \(56\) induced triangles, each consisting of the three bases determined by a fixed noncollinear triple of points (or its dual triple of lines). Each vertex has two neighbours in its own triangle and three neighbours of the opposite point/line-majority type.

For **every** pair of bases \(B,C\), the exchange distance satisfies
\[
5-|B\cap C|\ \le\ d_{\mathcal R}(B,C)\ \le\ 6-|B\cap C|.
\]
Exactly \(4368\) unordered pairs attain the upper rather than the lower value, and the remaining \(9660\) pairs attain the lower value. Thus, relative to unrestricted single-token replacements, every transformation needs at most one extra exchange to maintain a minimum resolving set at each step.

## Assumptions and scope

All graphs here are finite, simple, undirected, unweighted graphs and all distances are ordinary shortest-path distances. The Fano plane is the unique projective plane of order two. A fully explicit labelled construction uses point symbols \(0,\ldots,6\) and the seven three-point lines
\[
L_i=\{i,i+1,i+3\}\pmod 7\qquad (i=0,\ldots,6).
\]
The Heawood graph has point vertices \(0,\ldots,6\) and line vertices \(7,\ldots,13\), where point \(p\) is adjacent to line vertex \(7+i\) precisely when \(p\in L_i\).

A graph edge of \(\mathcal R(H)\) is an *unrestricted token jump* between valid metric bases: exactly one removed and one added graph vertex. Token sliding, temporary bases larger than five, multiset landmarks, or weighted distance are **not** considered. Results concern precisely \(H\), not all incidence graphs or all projective planes.

## Proof

**Classification of bases.** Let \(S\) contain \(p\) point vertices and \(q\) line vertices. Unselected points are at distance two from every selected point, while their distances to selected lines are either one or three. Thus the \(7-p\) unselected points must have pairwise distinct binary incidence signatures against the \(q\) selected lines. Necessarily \(7-p\le 2^q\). Dually, \(7-q\le2^p\). Checking the nonnegative values \(p+q\le4\) rules out every resolving set of size at most four. This reproduces the already-known metric dimension five without relying on its novelty.

For \(p+q=5\), the same inequalities leave only \((p,q)=(3,2)\) and \((2,3)\). Consider \((3,2)\) and write \(T\) for the selected three points. If \(T\) is collinear, the selected points give identical incidence signatures to too many unselected lines, and two selected lines cannot separate them. If \(T\) is noncollinear, the seven lines give seven incidence signatures relative to \(T\): the three distinct weight-two patterns (the sides of the triangle), three distinct weight-one patterns (the tangents), and the zero pattern (the disjoint line). All four unselected lines have distinct signatures if and only if the two chosen lines are two of the three tangents. For any such pair of tangents, the four unselected points have all four possible incidence patterns against those lines, and all fourteen vertices are distinguished: selected vertices have unique zero entries, and cross-part nonselected vertices are distinguished from each other by the parity of distance to any selected point. Hence every such five-set is resolving. By point-line duality the same result holds for \((2,3)\).

There are \(\binom73-7=28\) noncollinear triples of Fano points. Each has precisely three choices of two tangents, yielding \(84\) point-majority bases; duality gives another \(84\) line-majority bases. They exhaust the minimum bases.

**Exchange and triangle geometry.** For each noncollinear point triple, its three choices of two tangents form a three-vertex clique under one-token exchange, and the same is true for each nonconcurrent line triple. These \(28+28=56\) cliques partition the \(168\) bases. In the explicit construction below, exhaustive generation of every one-token exchange proves that every basis has exactly two neighbours from its own triple, three from the opposite majority type, and no other same-type neighbours. Therefore all \(56\) cliques are induced, the full graph is five-regular, and its number of edges is \(168\cdot5/2=420\).

The seven points of the Fano plane can alternatively be identified with nonzero vectors of \(\mathbb F_2^3\), and its seven lines with nonzero normal vectors. Incidence is orthogonality modulo two. The \(168\) invertible three-by-three binary matrices preserve incidence (with the contragredient action on line normals), and the point-line polarity doubles these to \(336\) automorphisms. The explicit action in the second supplied verifier has one orbit on the \(168\) bases; hence \(\mathcal R(H)\) is vertex-transitive.

**Shortest paths.** Label each of the fourteen vertices as above and encode a five-element subset as its fourteen-bit indicator. Compute the fourteen-by-fourteen graph distance matrix by breadth-first search; retain precisely the five-bit sets producing fourteen distinct landmark signatures. For each retained set \(A\), enumerate every removal \(a\in A\) and addition \(b\notin A\); retain the resulting indicator if it is another basis. This is every possible edge, not a sampled subgraph. Run breadth-first search in the resulting \(168\)-vertex exchange graph from all \(168\) starting bases. An explicit executable implementation is `scripts/direct_enumeration.py`.

The exhaustive result is that the distance-shell profile from each base is \((1,5,18,49,71,24)\); the unordered pair counts are \((420,1512,4116,5964,2016)\), whose sum equals \(\binom{168}{2}=14028\). These facts prove connectivity and exact radius and diameter five. For each unordered pair, the number \(5-|B\cap C|\) is the unavoidable count of removed elements; subtracting it from the computed shortest-path distance gives exactly \(9660\) zeros and \(4368\) ones, and no other differences. This proves the sharp detour statement.

An independent computation uses orthogonal-vector Fano incidence instead of the cyclic-line model, closed-form point/line distances instead of graph-search distances, direct pairwise intersection testing instead of replacement enumeration for exchange edges, and explicit incidence symmetries. It independently enumerates all \(168\) breadth-first distance maps; its full code is `scripts/fano_symmetry_check.py`. Both complete finite enumerations agree, including the vertex-disjoint triangle partition. The code and loops constitute explicit finite proof certificates for the graph-metric census; neither program assumes the desired distribution when constructing graph edges or distances.

## Verification

With Python 3.10 or newer, from the directory containing this file, run:

```sh
python3 scripts/direct_enumeration.py
python3 scripts/fano_symmetry_check.py
```

Successful outputs include `HEAWOOD_DIRECT_ALL_SOURCES_PASS` and `GF2_FANO_SYMMETRY_PASS`. The first verifies all \(\binom{14}{4}=1001\) four-subsets, all \(\binom{14}{5}=2002\) five-subsets, all available token replacements, and all \(168\) breadth-first traversals. The second checks the same claims through independent Fano coordinates, explicit automorphisms, pairwise-overlap adjacency and its own all-source shortest paths. Each checks the exact number and incidence of triangles. No probabilistic or floating-point procedure occurs.

## Relationship to prior work

Héger and Takáts explicitly gave the metric dimension five for the Fano plane's incidence graph in Remark 11 of their paper first publicly posted July 23, 2012. Their general finite-projective-plane work supplies the principal basis definitions and structural context, and is **not** superseded by claiming the known minimum as new. Tang, Zhou, Chen and Zhang studied metric bases of symmetric-design incidence graphs (published 2021); their accessible abstract and excerpts concern metric dimensions and bases, not the token-jump exchange metric. Their complete text was not available for a conclusive full-document comparison, so overlap in the basis classification remains possible and is not treated as independently novel.

The general topic of metric-basis reconfiguration has also been explored by Foster-Greenwood and collaborators, including student work on other graph families. The particular Heawood exchange graph's exact distance shells, triangular partition, transitivity and sharp detour census were not found in the accessible primary sources and mathematical-record searches. Matching words alone are not a novelty argument: the claimed new contribution is the **fully specified graph and its structural and metric invariants**, rather than metric dimension, generic token jumping or Fano incidence geometry.

## Limitations

The theorem is restricted to the unique projective plane of order two. It does not imply any analogous uniform distance distribution for larger projective planes. No independent scholarly audit has been performed. Although primary earlier literature and mathematical research records were compared, unpublished, unindexed or inaccessible historical computations could have covered these exact invariants. The 2021 Tang–Zhou–Chen–Zhang full paper and 2026 Morentin thesis were not comprehensively read; no absence of a Heawood example in their unseen material is asserted. Numeric graph-metric assertions are proved by the accompanying exhaustive finite checker programs rather than a short closed-form all-distance derivation.

## References

1. T. Héger and M. Takáts, *Resolving sets and semi-resolving sets in finite projective planes*, Electronic Journal of Combinatorics 19(4) (2012), #P30. First public arXiv posting July 23, 2012; arXiv:1207.5469; DOI: 10.37236/2582. Full-text PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i4p30/pdf/ .
2. L. Tang, S. Zhou, J. Chen and Z. Zhang, *Metric dimension and metric independence number of incidence graphs of symmetric designs*, Discrete Applied Mathematics (2021), DOI: 10.1016/j.dam.2020.12.001. Accessible abstract and page excerpts, not independently checked complete full text.
3. B. A. Foster-Greenwood and collaborators, *Metric Basis Reconfiguration*, project description (research on token sliding/jumping and distances among metric bases): https://www.cpp.edu/camp-reu/research_projects.shtml .
4. J. Morentin, *Reconfigurations of Metric Bases*, master's thesis (2026), listed at https://www.cpp.edu/faculty/brianaf/student-research.shtml ; complete thesis unavailable in the present source review.
