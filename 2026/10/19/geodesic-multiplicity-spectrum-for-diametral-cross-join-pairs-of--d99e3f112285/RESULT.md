# Geodesic multiplicity spectrum for diametral cross-join pairs of order-five binary de Bruijn cycles

## Finding

Let \(\mathcal B_5\) be the 2,048 binary de Bruijn cycles of order five, with cyclic rotations identified. Form the undirected *cross-join graph* \(G_5\): its vertices are \(\mathcal B_5\), and an edge is a single cross-join pair operation, which exchanges successors at two pairs of conjugate states and produces another single Eulerian circuit. A geodesic means a shortest path in this graph, counted as an ordered sequence of vertices between specified endpoints; different intermediate sequences count separately. For any unordered pair of distinct endpoints, the number of such paths is the same in either direction.

**Exact classification.** There are precisely \(368\) unordered vertex pairs at the graph diameter \(7\). The number of distinct length-seven cross-join paths between a diametral pair takes exactly fourteen values, with the following full frequency spectrum:

| Number of shortest cross-join paths between the endpoints | Unordered endpoint pairs |
| ---: | ---: |
| 3,617,656 | 16 |
| 3,781,260 | 32 |
| 3,840,330 | 32 |
| 3,910,424 | 32 |
| 3,933,668 | 32 |
| 3,972,200 | 16 |
| 4,094,570 | 32 |
| 4,185,332 | 32 |
| 4,245,320 | 16 |
| 4,697,036 | 32 |
| 4,807,588 | 32 |
| 4,908,248 | 16 |
| 5,096,758 | 32 |
| 5,954,072 | 16 |
| **Total pairs** | **368** |

The sharp minimum geodesic multiplicity among diametral pairs is \(3{,}617{,}656\) (attained by 16 pairs); the sharp maximum is \(5{,}954{,}072\) (attained by 16 pairs). The full listing of all \(368\) endpoint pairs, by canonical feedback masks and exact geodesic counts, is in `diametral_pairs.csv`. The count of diametral endpoints, their distance, and the full one-source distance profiles are used to specify the domain and are **not** asserted as independently new results.

## Assumptions and scope

A binary order-five de Bruijn cycle is a length-\(32\) circular binary word in which each of the \(32\) length-five binary words appears exactly once. We identify rotations, but not reversal or complementation. Each vertex has its standard nonsingular feedback representation: the \(32\) length-five states are indexed \(e=16a+v\), where \(a\in\{0,1\}\) is the leading bit and \(v\in\{0,\ldots,15\}\) is the last four-bit integer. For a feedback table \(m\in\{0,1\}^{16}\), the successor of state \(e\) is

\[
T_m(16a+v)=2v+(a\mathbin\oplus m_v).
\]

The successor map is always a permutation of the \(32\) states. It defines a de Bruijn cycle if and only if it is a single permutation cycle. A cross-join operation toggles exactly two distinct entries of \(m\) and preserves the one-cycle property. This is exactly the conventional cross-join operation because toggling one entry splits the cyclic tour into two circuits, and toggling another interlacing conjugate pair joins them. The checker verifies this equivalence in both directions for every candidate vertex and every one of the \(120\) coordinate pairs.

The table concerns only order five and the unweighted shortest-path metric. It does not count arbitrary walks, algorithms with redundant operations, or multiple orientations of the same unordered endpoint pair.

## Proof

**Exhausting the domain.** Every nonsingular binary order-five feedback permutation has exactly one table \(m\) of length \(16\). Enumerating all \(2^{16}=65{,}536\) tables and retaining the single-cycle permutations yields exactly \(2{,}048\) valid tables. Independently, depth-first enumeration of Euler tours in the corresponding four-bit binary de Bruijn graph, with the `00000` state fixed, yields the identical set of tables. Since every order-five de Bruijn cycle contains that state exactly once, this independent enumeration neither omits nor duplicates rotation classes.

**Exhausting legal operations.** For each valid table and each distinct pair of coordinates, the checker tests whether toggling the pair remains valid. It independently verifies the conjugate-interleaving criterion along the original length-\(32\) tour, for all coordinate pairs. Thus the induced undirected graph contains exactly \(2{,}048\) vertices and \(38{,}704\) edges; no additional moves exist under the definition.

**Distances and endpoints.** A breadth-first search from every vertex reaches every other vertex and determines its shortest distance; the complete histogram of unordered pairs at distances \(1,\ldots,7\) is
\[
(38{,}704,305{,}376,758{,}800,710{,}976,254{,}800,27{,}104,368).
\]
The diameter is \(7\). In each valid table, entries zero and fifteen are fixed to one. All the remaining fourteen entries may differ between a pair. A graph edge flips two entries. The full distance computation also verifies that, for every pair, distance equals half the Hamming difference of their feedback masks. In particular, the diametral endpoint pairs are exactly the \(368\) pairs with all fourteen variable entries complementary: their mask difference is hexadecimal `0x7ffe`. Distance seven requires each of these fourteen entries to be changed once, in seven successive disjoint pairs.

**Independently counting geodesics.** The first exact-count procedure performs breadth-first traversal from each vertex, propagating the number of shortest paths forward along edges that increase the BFS level by one. For each of the \(368\) diametral endpoint pairs \((m,n)\), an independent dynamic program uses only subsets of the fourteen differing feedback coordinates: it starts at the empty subset, adds each possible pair of previously unflipped coordinates only when the resulting feedback table remains a single cycle, and after seven stages reads the count at the full fourteen-coordinate set. The two algorithms produce exactly the same counts for **each** of the \(368\) endpoint pairs. Every shortest path is counted once, because a path of length seven changes fourteen distinct coordinates (any repeated flip would fail to reach the complementary endpoint in only seven moves). Every legal ordering of seven disjoint coordinate-pair flips is counted by both methods. Grouping the resulting integers produces exactly the fourteen frequencies in the table, and the full per-pair table is included.

A minimum example has feedback masks `886d` and `f793` (hexadecimal), with exactly \(3{,}617{,}656\) shortest paths; a maximum example has masks `88ef` and `f711`, with exactly \(5{,}954{,}072\) shortest paths. The hexadecimal masks, rather than a chosen cyclic rotation, fix the endpoint representations unambiguously.

## Verification

Run `python3 verify.py` next to `diametral_pairs.csv` with Python 3.9 or newer; the code uses only the standard library. It regenerates the complete domain, independently enumerates Euler tours, verifies the cross-join/interlacing equivalence, performs all-source BFS and path-count accumulation, checks every diametral pair with the independent subset dynamic program, and compares the resulting complete \(368\)-row dataset against the supplied CSV. Run `python3 verify.py --emit` to regenerate the CSV from exact arithmetic. All assertions complete without failure on the delivered files. The verifier is finite and exhaustive at order five; it is not a claim about general orders.

## Relationship to prior work

Mykkeltveit and Szmidt prove cross-join connectivity and give the feedback-table description and legal cross-join operation. Alhakim proves graph Hamiltonicity and already tabulates all order-five **vertex degrees**; that article's auxiliary common-prefix distance is explicitly distinguished from the cross-join graph metric. Dąbrowski, Rachwalik and Szmidt present algorithms, Fryers polynomials, and tabulations of order-five **one-source reachability/distance shells**. Those shell polynomials count endpoints at a distance; they do not count multiple shortest transformation paths leading to one fixed endpoint. General even-delta-matroid exchange results supply structural context for transition-distance formulas, not this fourteen-valued multiplicity spectrum. The present claim is limited to the exact shortest-path multiplicities between all diametral order-five pairs, not any of these existing constructions, degrees, or reachability counts.

## Limitations

This is a computer-assisted complete finite classification. Its proof depends on the supplied, human-readable, executable exhaustive checker, rather than a closed-form all-order formula. The investigation does not settle analogous path counts for order six or higher. No assertion is made that no unpublished or unindexed enumeration of the same spectrum exists; independent priority and scientific audit remain outstanding. The 2026 study was compared using its available indexed article sections and tabular descriptions; full-page retrieval was limited, leaving residual priority risk from inaccessible supplementary materials.

## References

1. J. Mykkeltveit and J. Szmidt, *On cross joining de Bruijn sequences*, 2013, https://eprint.iacr.org/2013/760 (first public eprint date 2013-11-21).
2. A. Alhakim, *Hamiltonicity of the Cross-Join Graph*, arXiv:1805.12059, https://arxiv.org/abs/1805.12059 .
3. P. Dąbrowski, T. Rachwalik and J. Szmidt, *The Cross-Joint Method and Generation of De Bruijn Sequences*, *Mathematics* 14(9), 1424 (2026), https://doi.org/10.3390/math14091424 .
4. H. Kim and S. Oum, *Note on Hamiltonicity of Basis Graphs of Even Delta-Matroids*, *Journal of Graph Theory*, https://doi.org/10.1002/jgt.23237 .
