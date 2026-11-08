# Independent mathematical audit

## correctness

PASS

For a three-factor Hamming graph with a,b,c≥2, independently read RESULT.md and full actual Git tree (8 blobs). The known Theorem 6 of arXiv:2307.05168 equates total mutual visibility with pairwise avoidance of Hamming distance 2. A maximal set of size k<m=min(a,b,c) misses a symbol in every coordinate, allowing an all-three-different vertex, proving k≥m. A coordinate line along a minimum axis is maximal, proving equality. For a minimum set, at least one projection is bijective, since any three omitted symbols would give an extendible vertex; hence its two remaining coordinate equality partitions coincide (otherwise two selected triples are distance 2). A singleton partition block permits replacing one nonaxis symbol with an unused symbol, yielding a legal new vertex, unless both other projections are surjective; then r=m and a=b=c=m with all singleton blocks, giving the full transversals. If all blocks have sizes≥2, each omitted triple is conflict-adjacent either to its matching-index selected triple (two nonaxis changes) or to a different index in the same block (one nonaxis change), so the families are exactly maximal. Full transversals are similarly maximal by switching to the index matching the mismatched coordinate. Injections of r unordered partition blocks into the two remaining alphabets give S_{≥2}(m,r)(q_j)_{↓r}(q_k)_{↓r}; the chosen minimum-size axis is unique for nonsingletons because r≤m/2<m; exceptional equal-factor transversals have (m!)² representatives. Independent direct exact subset conflict-graph enumeration confirms (2,2,2):16,(2,2,3):12,(2,3,4):12,(3,3,3):63,(3,3,4):24,(4,4,4):1920,(4,4,5):1480, and independently checked all 256 vertex subsets of Q3 using original geodesic definition against the distance-two criterion. These are corroborations, while the partition proof is universal. Boundary m=2 and all equal/non-equal factors are covered; no claim for higher factor count.

## originality

PASS

The specific lower-total three-factor theorem (all cardinality-minimum inclusion-maximal families and their restricted-Stirling multiplicity) is not contained in the inspected foundational lower-parameter paper or the exact Hamming legality/maximum paper. These establish the notion, the two-factor lower cardinality, and the distance-two characterization; these ingredients are credited as old. A 2024 visibility-polynomial paper gives general inclusion-exclusion over maximal sets but not a three-factor minimum-maximal-set classification from which the numerical answer follows without proving the missing structural lemma. Published Resultary closest findings study k-distance mutual visibility of hypercube selected pairs and connected mutual visibility of high-girth products, neither of which is the total/minimum/maximal invariant here. Direct and stronger coverage was not found in the scoped searches; absence from retrieval alone is not novelty proof. Residual risks: other coding-theory treatments of minimum saturating independent sets in Hamming distance-two graphs or a not-indexed partition-classification preprint.

## value

PASS

The lower total mutual-visibility number is an established natural worst-case greedy/maximal-set graph invariant. Complete classification of every minimum optimizer for the first nontrivial three-factor family, plus its exact multiplicity as a restricted-Stirling/falling-factorial sum and a distinct all-bijective exceptional class, is a structural fact that a researcher studying domination or visibility on Hamming graphs can use directly. It is neither a trivial change of name from the known Hamming legality criterion nor a table recomputation: the coincidence of nonaxis partitions and singleton-block obstruction are substantive deductions. The full three-parameter infinite family and its exceptional symmetry are mathematically motivated, while larger Cartesian powers and all maximal sets remain outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
