# Scientific assessment

## Correctness — PASS

The theorem fixes the rank-standardized one-deletion channel and exact full-systematic embedding. For no markers, a counting obstruction applies at every length greater than one. With one marker, the number of codewords exactly equals the size of the received-word universe, so every shadow would have to be singleton; adjacent-deletion equality forces a monotone word, leaving only two possible codewords and excluding every length at least three. The displayed encoders meet every remaining case through length four. Their full message projection and pairwise shadow disjointness are independently reconstructed by `VERIFY.py`, giving 16 and 97 distinct descendants with no collision. Limits: codewords are certificates of finite upper bounds, not an unbounded construction.

## Originality — PASS, with residual risk

Wu et al., arXiv:2609.37578v1, Sections II-B, III and VI-A with Corollary 2, establish the matching full-systematic model and a four-marker one-PID construction for sufficiently large message lengths; their theorem is neither an exact finite two-marker classification nor a lower bound on the present small lengths. Zhou, Jiang, and Bruck (ISIT 2012) encode full-systematically with two extra labels, but for correcting Kendall adjacent-swap errors, not PID deletions. The respective error guarantees are not reducible: standardizing after deleting a moved entry can yield identical received orders even for words far apart in Kendall distance. Gabrys et al. (2014), including the first three pages and the signature-code construction, treat the same PID channel but only non-systematic code size, not preservation of every source message. Searches of indexed mathematical findings using full-systematic/PID/two-marker/finite-length aliases produced no equivalent statement, although index coverage cannot establish uniqueness. An unpublished enumeration could coincide with the finite witnesses.

## Value — PASS

Minimum added labeled markers is the direct systematic redundancy parameter for rank-modulated permutation storage. The complete initial profile identifies the first genuinely nontrivial full-systematic PID instances and proves that two markers suffice exactly at the six-message and twenty-four-message sizes; without the explicit constructions, the asymptotic four-marker sufficiency result does not answer either finite question. The general one-marker obstruction explains why this value is best possible. The finding is intentionally finite, and does not assert a broad family or asymptotic rate improvement.

Self-review: passed. Independent audit: not yet performed.
