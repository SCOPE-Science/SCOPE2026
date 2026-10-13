# Self-review

## Correctness
**PASS.** With \(u=(b+c)/a\) and \(v=bc/a^2\), Jaccard is \(1/(1+u)\) and squared Ochiai is \(1/(1+u+v)\), so the necessary-and-sufficient reversal criterion follows immediately from strict monotonicity. The complete positive-overlap Venn-signature domain through gamma richness \(5\) is generated independently from integer triples and from actual subset pairs. Exact rational comparison proves no strict reversal through \(4\), one unique reversal at \(5\), and the packaged verifier returns `VERIFY_OK`.

Risk: the result is a pairwise binary-presence theorem and does not extend automatically to abundance or functional/phylogenetic generalizations.

## Originality
**PASS.** Jackson, Somers and Harvey already compare Jaccard and Ochiai empirically and explain their different sensitivity to occurrence-frequency structure. Pavoine's full text gives the same coefficient family and compares their behavior in a broader community-similarity framework. Those sources do not state the exact two-comparison reversal criterion, the gamma-richness-three first tie split, the gamma-richness-five first strict reversal, uniqueness of the first pair, or the infinite witness family. Semantic-result and exact-pattern searches found no covering statement.

Risk: the criterion is an elementary algebraic consequence of standard formulas. A specialist exercise, software regression example, or unindexed note could contain an equivalent observation even though the sharp discrete boundary was not found.

## Value
**PASS.** Jaccard and Ochiai are established ecological presence–absence similarities whose differing response to occurrence frequency has been documented empirically. The theorem turns that qualitative distinction into a direct exact diagnostic for ranking disagreement, identifies the smallest possible strict reversal, and supplies a persistent family. The five-species witness is compact enough to serve as a benchmark for interpretation and software validation.

Self-review: passed. Independent audit: not yet performed.
