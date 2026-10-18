# Mathematical review

## Correctness
PASS. At each zero in a rook-graph labeling, the neighbor-weight sum is exactly its row sum plus its column sum. The dichotomy between a zero column (forcing every row sum at least two) and no zero column (forcing total weight at least the number of columns) proves the minimum. Equality forces the stated two optimizer families, and counting their intersection at the boundary yields the exact formula. Nineteen small profiles were checked against direct graph adjacency and all lower weights; the proof, not finite enumeration, establishes arbitrary sizes.

## Originality
PASS, subject to an identified bibliographic limitation. Alizadeh et al. (arXiv:1701.01416) give Roman \(\{2\}\)-domination framework and product bounds; Klostermeyer and MacGillivray (2019) already prove the square rook-graph **numerical value**, which is not claimed new. The perfect-Italian theorem of Varghese and Lakshmanan (2023) has a stricter zero-neighborhood equality condition. The recent Italian-polynomial work of Shao and Zhao (2026) concerns paths, trees, and cycles. The current claim instead enumerates **all** ordinary minimum labelings of rectangular rook graphs and identifies a structural transition at \(n=2m\). The 2019 PDF could not be read completely because of retrieval limitations, although indexed relevant text was examined; its uninspected material and other unindexed literature leave a residual risk.

## Value
PASS. The exact optimizer classification of an infinite natural product family distinguishes a surjection regime from an independent weighted-row regime, with a nontrivial correction where they coincide. The resulting Stirling-number and product formulas determine the least-degree nonzero coefficient of the Italian domination polynomial, quantify optimizer multiplicity, and sharpen the prior scalar square-case result without claiming it to be new.

## Scientific scope
Finite checks do not establish the theorem and are treated only as corroboration. No independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
