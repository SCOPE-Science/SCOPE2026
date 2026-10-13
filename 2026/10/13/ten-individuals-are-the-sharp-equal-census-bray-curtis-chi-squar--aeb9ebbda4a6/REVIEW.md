# Self-review

## Correctness
**PASS.** For equal census \(N\), Bray–Curtis ordering reduces to \(\sum_i|x_i-y_i|\). For a two-row correspondence-analysis table, squared chi-square distance reduces, up to a common positive factor, to \(\sum_i (x_i-y_i)^2/(x_i+y_i)\). Exhaustive exact generation proves no strict inversion through \(N=9\) and verifies the stated \(N=10\) witness and first-layer richness support. The packaged verifier returns `VERIFY_OK`.

Risk: a larger correspondence-analysis table uses different global column masses.

## Originality
**PASS.** Greenacre establishes the ecological correspondence-analysis geometry and direct comparison with Bray–Curtis alternatives. Warton, Wright, and Wang explicitly contrast Bray–Curtis pairwise standardization with chi-square column standardization. Generic difference between the metrics is therefore prior context. The checked literature, exact-vector searches, and available historical claim records did not state the positive equal-census cutoff \(N=10\), the three-species witness, or the richness support of the first reversal layer.

Risk: an unindexed worked example or software test could contain the same vectors without identifying minimality.

## Value
**PASS.** Bray–Curtis and chi-square distance are standard ecological dissimilarities with different species-weighting principles. Fixing census and richness removes immediate comparability confounders, while positivity removes zero-cell pathologies. The sharp boundary identifies the smallest exact community size where metric choice alone reverses which pair is judged more dissimilar, and the witness exposes the rare-species weighting mechanism.

Self-review: passed. Independent audit: not yet performed.
