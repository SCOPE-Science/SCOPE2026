# Independent mathematical audit

## correctness

PASS

PASS. For each n≥2, vertices are labeled permutations, deletion retains labels and order. Adjacent permutations have inversion disagreement graph a nonempty star. For any triple of permutations, pairwise disagreement edge sets have symmetric difference zero; classification of three nonempty stars forces either a common center (unique common deletion symbol) or a triangle of three two-edge stars on three symbols. In exceptional case the marked symbols form the three cyclic orders within a consecutive length-three block. Common-read triangles count n! binom(n,3) and exceptional triples n!(n−2)/3, giving n!(n−2)(n²−n+2)/6. Degree is (n−1)²; clustering coefficient equals (n²−n+2)/[n(n−1)²] for n≥3, undefined n=2. Independent brute-force literal-label deletion through n=6 produced 0,8,112,1320,15360 triangles and correct degrees, and brute enumerated the three-star lemma configurations at small n. Finite checks only corroborate the all-n classification proof.

## originality

PASS

PASS best-of-knowledge. Wang–Nguyen–Chee–Vu Section III Lemma 4 bounds triangles in t-deletion permutation graph by O_t(n! n^{3t}); its t=1 specialization does not give exact count or classification. Kong has Ulam radius-one sphere size/degree, not triangles; Farnoud–Skachek–Milenkovic develop metric and codes. Resultary published exact binary single-deletion graph triangle count concerns repeated binary words, not permutations of all distinct labels. The presented exact constant and exceptional rotation class are a genuinely additional classification on inspected evidence, with unindexed translocation-graph risks.

## value

PASS

PASS. Triangle count and local clustering are motivated natural invariants of the permutation one-deletion confusability graph used in coding estimates. An exact all-n enumerator with a complete classification of the only obstruction to common-deletion triples is useful beyond an asymptotic upper bound or sphere-degree identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
