# Two marked vertices in nonbinary Hamming graphs: scientific review

## Correctness — PASS

The proof gives a complete orbit parametrization by \((s,r,t)\). Explicit anchor-preserving coordinate and symbol permutations are transitive on each parameter class. Distances to individually coloured anchor vertices become distinguishable in at most \(d\) refinement rounds; the following round counts neighbors whose distances to both anchors fall by one, a count exactly equal to \(s\). The other parameters follow from two verified distance identities. This proves orbit equality and the \(d+1\) bound for all \(q\ge3\) and \(d\ge1\). Independent implementations of explicit edge refinement and neighbour-distance statistics pass 52 finite configurations and 16,043 vertex instances; the proof does not rely on extrapolating those tests.

## Originality — PASS, subject to literature priority risk

Arvind–Köbler–Rattan–Verbitsky (2015) develops general refinability theory but does not state the exact marked nonbinary Hamming orbit formula in the portions inspected. Arvind–Fuhlbrück–Köbler–Kuhnert–Rattan (2016) studies computational difficulty of individualization, not the present uniform structural classification. Mogilnykh–Valyuzhenich (2019) studies eigenvalue-restricted equitable two-cell partitions of Hamming graphs, a different object. Boutin (2009) establishes determining-number results for Cartesian powers; identifying a determining set does not imply stable colour refinement equals all pointwise-stabilizer orbits, and this result does not compute such a determining number. A related binary hypercube theorem treats \(q=2\), and a distance-regular-graph theorem concerns two-dimensional refinement of ordered pairs rather than the one-dimensional marked-vertex procedure. Targeted published-result searches located no exact equivalent statement. Residual risk: specialized equitable-partition or association-scheme literature, including inaccessible publisher text, could contain a reduction of this formula; failed searches are not a proof of global novelty.

## Value — PASS

This is a complete, parameter-uniform classification for a canonical infinite family of finite graphs, rather than a small isolated example. Its exact orbit count and class sizes determine the information content of two landmarks under the weakest widely used graph refinement. The explicit \(H(3,3)\) witness shows that the usual two-landmark distance partition fails to capture stable refinement, while one further intrinsic local statistic does. The result distinguishes automorphism fixing from orbit reconstruction. This is useful for studying equitable partitions, individualization, and graph-refinement expressiveness; no claim is made of a downstream complexity improvement or graph identification against arbitrary competitors.

## Evidence and limitations

The two included reproducible standard-library programs corroborate the proof, with outputs recorded separately. Full text was inspected for relevant portions of Arvind et al. (2015), Arvind et al. (2016), the Hamming-specific introductory and two-cell partition sections of Mogilnykh–Valyuzhenich (2019), and the accessible material from Grohe et al. (2013); the Boutin (2009) public abstract, not full text, was accessible. The \(d+1\) refinement bound is not claimed optimal. Formal independent checking has not been performed. The source priority assessment has limited coverage of unpublished work.

Self-review: passed. Independent audit: not yet performed.
