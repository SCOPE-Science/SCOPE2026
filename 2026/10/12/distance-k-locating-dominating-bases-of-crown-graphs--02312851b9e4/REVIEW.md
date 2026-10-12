# Review of Distance-\(k\) locating-dominating bases of crown graphs

## Correctness
PASS. For every same-side pair \(a_i,a_j\), the complete distance-\(k\) resolving neighborhood is \(P_i\cup P_j\), and similarly on the \(B\)-side. Hence every resolving set meets all but at most one matched pair, giving the sharp lower bound \(n-1\). Equality forces a one-endpoint transversal of all but one pair. For \(n\ge4\), direct pair-type comparisons show that every such transversal resolves the entire crown graph for every \(k\ge1\). When \(k\ge2\), all omitted vertices lie within distance two of the transversal. When \(k=1\), domination holds exactly when the transversal has at least two selected vertices in each bipartition class. The binomial counts follow immediately. Exhaustive computation for \(5\le n\le8\) and \(k=1,2,3\) matches every statement.

## Originality
PASS. The 2021 defining paper for distance-\(k\) location-domination was inspected at the definition, general-bound, extremal, and exact-family sections; it contains no crown occurrence and no \(K_{n,n}\) minus perfect matching specialization. The companion distance-\(k\) dimension paper supplies general truncated-distance theory and standard families, but no crown theorem. Semantic published-result searches and targeted literature searches under crown graph, perfect-matching-deleted complete bipartite graph, bipartite double cover, bipartite Kneser graph, adjacency dimension, and locating-dominating terminology did not locate the claimed phase transition or basis counts.

## Value
PASS. The result completely determines all minimum detector configurations, not just the scalar optimum, for a standard distance-transitive family. It exhibits a clean range transition: increasing the sensing radius from one to two leaves the optimum size unchanged but restores exactly the orientation patterns excluded by one-step domination. This refines the general bound \(\gamma_L^k-\dim_k\in\{0,1\}\) with an explicit infinite family where equality with distance-\(k\) dimension holds for all ranges while the optimizer geometry changes sharply.

Self-review: passed. Independent audit: not yet performed.
