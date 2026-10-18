# Review of six-pattern binary Parikh-matrix avoidance spectra

## Correctness — PASS

The exact statement specifies linear binary words, scattered subsequences, all \(A,B\ge1\), and all integer \(0\le K\le AB\), with zero-letter boundaries separately covered. The proof partitions \(abab\)-avoiders into unique four-run representations, the \(aabb\)-avoiders by the number of \(b\)'s after their second \(a\), and the \(abba\)-avoiders by the count between the first and last \(a\). Their \(ab\)-counts are evaluated explicitly. Reversal and letter exchange cover the other three patterns without dropped quantifiers. A partition bijection gives a nonzero Gaussian-binomial class size. The embedded checker uses independently derived subsequence-prefix DP and direct finite enumeration, with all reported comparisons passing. This testing corroborates the universal run proof, not replaces it.

## Originality — PASS within evidence examined

The motivating fixed-pattern paper of Fazekas, Huang and Mercaş (2026) announces a general additive probability approximation scheme; its full text was inaccessible, and exact special-case overlap cannot be ruled out. Golafshan (2026) gives the denominator and class-size distribution, but not the pattern-specific numerators. Atanasiu (2007) explicitly constructs a unique representative matching the \(abba\)-avoiding normal form, so the two unit-count rows are credited to existing work. The remaining divisor- and additive-window formulas, together with the complete six-pattern spectrum, were not covered in the accessed primary statements or searches. The exact novelty claim is therefore the remaining pattern-specific conditional census, not the normal form or the Gaussian denominator.

## Value — PASS

The complete natural family of the six balanced scattered patterns of length four is the smallest family exhibiting distinct arithmetic phenomena beyond short trivial patterns. Fixing the binary Parikh matrix changes the question from unweighted language avoidance to exact conditional probability. The formulas reveal that alternating patterns have bounded-divisor spectra whereas nested patterns have additive-window spectra; they provide exact probabilities where the motivating literature discusses general approximation. This is a structural all-parameter classification, not a small numerical increment or a known class-size table recalculation.

## Limitations and literature access

No general formula for arbitrary patterns is asserted. A primary 2026 paper and Richomme's related full text could not be inspected fully; the risks are described in the audit. Finite tests do not replace the proof. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
