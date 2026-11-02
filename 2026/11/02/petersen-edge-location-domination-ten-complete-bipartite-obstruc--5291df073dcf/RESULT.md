# Petersen edge-location-domination: ten complete-bipartite obstructions to geodesic exchanges

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, with its ten vertices the two-subsets of \(\{0,1,2,3,4\}\), adjacent when disjoint. Write \(H=L(P)\), the line graph on the fifteen edges of \(P\). A set \(C\subseteq E(P)\) is an **edge-locating-dominating set** when the signatures
\[
\sigma_C(e)=\{c\in C:c\ne e,\;c\cap e\ne\varnothing\},\qquad e\in E(P)\setminus C,
\]
are all nonempty and pairwise different. This is ordinary locating-domination of \(H\); it does **not** demand that the selected edges themselves be identified.

**Theorem (complete optimal reconfiguration geometry).** The minimum size of such a set is \(5\), and there are precisely \(246\) minimum sets. Form the exchange graph \(\mathcal R\) on these sets, joining \(C,D\) when \(|C\triangle D|=2\). Then \(\mathcal R\) is connected, has \(1470\) edges, and is self-centered with radius and diameter both \(5\). Under the natural \(S_5\) symmetry there are four orbits, with size/degree/distance-profile data

| Orbit size | Degree | Numbers of vertices at distances \(0,1,2,3,4,5\) |
|---:|---:|---|
| \(6\) | \(20\) | \((1,20,40,70,65,50)\) |
| \(60\) | \(12\) | \((1,12,36,81,84,32)\) |
| \(60\) | \(13\) | \((1,13,40,76,81,35)\) |
| \(120\) | \(11\) | \((1,11,45,73,80,36)\) |

For every pair of optimum sets,
\[
\boxed{\quad 5-|C\cap D|\;\le\;d_{\mathcal R}(C,D)\;\le\;6-|C\cap D|.\quad}
\]
Among the \(30{,}135\) unordered pairs, exactly \(90\) require the additional exchange. Connecting **only** these \(90\) pairs forms a graph comprising \(186\) isolated vertices and \(10\) vertex-disjoint copies of \(K_{3,3}\). The ten nontrivial components are canonically indexed by the ten vertices of \(P\).

For completeness, unordered-pair counts at exchange distances \(1\) through \(5\) are \((1470,5100,9300,9945,4320)\). The exact bound is a finite theorem about this specified fifteen-vertex line graph; no infinite-family claim is made.

## Assumptions and scope
Graphs are finite and simple. Two edges of \(P\) are neighbours in \(H\) exactly when they share an endpoint. The ordinary locating-dominating condition is imposed on the edges *outside* \(C\) only. Exchange moves replace precisely one selected edge with one unselected edge and keep the minimum cardinality and locating-domination property throughout. Distances are shortest-path distances in this exact exchange graph. A geodesic in the full Johnson graph of five-subsets has length \(5-|C\cap D|\); the theorem compares constrained shortest paths with that unconstrained lower bound.

The first orbit consists of the six perfect matchings of the Petersen graph. Each of the other \(240\) optimum sets selects the edge set of \(P_3\sqcup3K_2\): precisely one vertex of the original Petersen graph has selected-edge degree two (the **doubled vertex**), precisely one has degree zero (the **missed vertex**), and eight have degree one. In the \(60\)-element degree-\(12\) orbit, the doubled and missed vertices are adjacent; in the other two orbits they are not. All \(90\) exceptional pairs involve two states from the degree-\(12\) orbit with the same doubled vertex.

## Proof
The theorem admits a complete finite proof from explicit exhaustive enumeration, provided by the independently replayable standalone programs `verify_kneser.py` and `verify_generalized_petersen.py`. Here is the exhaustive search space, its predicate, the exact operations checked, and the reduction of the displayed conclusions to the checks.

**Exact graph construction.** Enumerate the ten two-subsets of \(\{0,1,2,3,4\}\) lexicographically and enumerate as graph edges those pairs of two-subsets that are disjoint. The result has exactly fifteen edges. Index these by \(0,1,\ldots,14\). For each edge index \(e\), form its line-graph open-neighbourhood bitmask \(N_e\), containing exactly those other indexed graph edges with a common endpoint. For any candidate five-element mask \(C\), accept it if and only if the ten signatures \(N_e\cap C\), for indices \(e\notin C\), are all nonempty and pairwise distinct. The same predicate applies at all smaller cardinalities.

**Exhaustive optimality and classification.** Inspect each of the \(\sum_{j=0}^5\binom{15}{j}=4944\) candidate subsets of cardinality at most five. There are no accepted sets of size less than five, and precisely \(246\) accepted five-subsets. The natural action of all \(5!\) permutations on the five ground elements permutes the fifteen graph edges and the accepted sets. Direct computation of the images of every accepted set gives precisely four orbits of sizes \(6,60,60,120\). Computing selected-edge incidence degrees in \(P\) shows the perfect-matching and \(P_3\sqcup3K_2\) classifications and the adjacency criterion for the doubled/missed vertices.

**Exact exchange graph and metric.** Two accepted size-five bitmasks are adjacent if and only if their symmetric difference has two bits. Check each of the \(\binom{246}{2}=30{,}135\) possible pairs, obtaining \(1470\) exchange edges and the stated degrees. Perform exact breadth-first search from each of the \(246\) states; this checks connectivity and all \(246\times245\) ordered inter-state distances, yielding the four complete distance profiles, pair-distance histogram, and eccentricity five for every state.

**Exceptional pairs and their canonical geometry.** For every unordered pair calculate the nonnegative difference \(d_{\mathcal R}(C,D)-(5-|C\cap D|)\). The exhaustive check confirms that this is always zero or one, with precisely \(90\) ones. There are \(60\) states incident with a positive difference, each incident with precisely three positive-difference pairs, the others isolated. The doubled vertices of the two ends of every such pair agree. Each of the ten original Petersen vertices is the common doubled vertex of exactly six nonisolated states. The positive-difference graph on each such six-vertex set is degree three and triangle-free. Every triangle-free cubic graph on six vertices is \(K_{3,3}\): the three neighbours of any vertex have no edges among them, while their two other neighbours must be the remaining two vertices, completing the bipartition. This proves the ten disjoint copies of \(K_{3,3}\) and the full claimed defect graph.

**Independent implementation.** `verify_generalized_petersen.py` independently constructs \(P\) from an outer five-cycle, inner step-two five-cycle, and five spokes; checks an explicit isomorphism with \(\operatorname{KG}(5,2)\); constructs neighbourhood sets rather than bitmasks; tests every subset up to size five; builds exchange adjacencies via pairwise symmetric differences; and independently performs every breadth-first search and defect-graph check. Its agreement with the first implementation is a cross-check, not a replacement for complete enumeration. Both scripts use only the Python standard library; running either with Python 3 from the package is sufficient to reproduce its assertions and concluding PASS marker.

## Verification
Executing `python verify_kneser.py` produced `KNESER_EXACT_RECONFIGURATION_PASS`; executing `python verify_generalized_petersen.py` produced `GENERALIZED_PETERSEN_DIRECT_PASS`. Both were executed against the packaged content. Neither program samples configurations or extrapolates from a truncated search: all \(4944\) candidate subsets at sizes up to five, all \(30{,}135\) unordered pairs of minima, and all \(246\) BFS sources are processed. The first implementation also enumerates every one of the \(120\) permutations of five symbols to verify the complete natural symmetry orbits.

## Relationship to prior work
Foucaud, Gravier, Naserasr, Parreau and Valicov's *Identifying Codes in Line Graphs* (first arXiv public posting 2011-07-01, arXiv:1107.0207) studies the strictly stronger edge-identifying-code condition and in particular obtains a five-edge identifying code for the Petersen graph from a perfect matching. This gives a known size-five *upper bound* for the weaker locating-dominating parameter but does not determine its minimum, all \(246\) weaker codes, their \(S_5\) orbits, or exchange metrics. In particular, identifying every vertex of the line graph is not the predicate enumerated here.

Foucaud and Henning's *Location-domination in line graphs* (first arXiv public posting 2015-06-08, arXiv:1506.02623) establishes broad upper bounds for locating-dominating and locating-total dominating sets in line graphs. Its general one-half-order bound is not an exact Petersen classification, and its inspected primary full text contains no determination of this exchange graph. General dominating-set token-jumping research concerns mobility but does not provide this specific constrained fifteen-vertex geometry. Exact comparisons, including related published mathematics records, are recorded in `AUDIT.json`.

## Limitations
This is a finite computer-assisted theorem. The exhaustive argument depends on the correctness of the two included, finite, readable source programs and their specified graph models, not on an independent external formal proof. No independent scholarly audit has been performed. A semantically equivalent earlier computation in unindexed literature or hidden tables cannot be categorically excluded; a negative search is not proof of novelty. These limitations do not change the precisely quantified finite search domain.

## References
- F. Foucaud, S. Gravier, R. Naserasr, A. Parreau, P. Valicov, *Identifying Codes in Line Graphs*, arXiv:1107.0207 (first public 2011-07-01), DOI:10.1002/jgt.21686; full-text open preprint https://www.lirmm.fr/~pvalicov/Files/LineGraphs.pdf.
- F. Foucaud, M. A. Henning, *Location-domination in line graphs*, arXiv:1506.02623 (first public 2015-06-08), DOI:10.1016/j.disc.2016.05.020; full text https://ffoucaud.github.io/new-backup/Publications/Papers/J17_LD-line_DM_2017.pdf.
- C. M. Mynhardt, S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey*, arXiv:2003.05956 (2020), for the context of token-jumping and domination exchange graphs.
