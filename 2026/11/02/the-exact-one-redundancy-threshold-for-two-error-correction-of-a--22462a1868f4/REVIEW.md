# Scientific review: exact two-error function-code threshold

## Correctness — PASS

The proof defines the code model, the universal quantifiers, and the integer obstruction exactly. Its reduction to a radius-four simplicial neighborhood is Rajput–Jagatti–Rajan, Theorem 3 (arXiv:2610.09011v1, pp. 12–13), itself relying on Harper–Räty. The new lex-prefix shadow count is derived by assigning each high-weight superset to its unique earliest lower-weight subset, giving a disjoint binomial count. The max-prefix recurrence is an exact finite identity. The included `verify.py` checks all 30 dimensions from 36 through 65 with exact arithmetic, and independently cross-checks its recurrence by direct Hamming-ball enumeration in small dimensions. For dimensions at least 66, the existing analytic Theorem 4 completes the infinite quantifier. The explicit class size at dimension 35 violates the necessary inequality. The boundary quantities are reported in RESULT.md and rechecked by the executable certificate.

## Originality — PASS, with residual priority risk

The closest directly relevant source, Rajput–Jagatti–Rajan (arXiv:2610.09011v1), explicitly leaves the exact threshold at two errors unknown and bounds it by 66; its complete first-error table and \(\kappa_1(1)=10\) are already credited. The new conclusion is \(\kappa_1(2)=36\). Its general isoperimetric criterion implies the result only after the new exact large-dimension shadow maximization; the cited paper does not evaluate these dimensions. Targeted mathematical-record searches for the two-error threshold, aliases and lexicographic neighborhoods did not identify a covering theorem. Searches cannot establish definitive priority, and an unindexed calculation remains possible. The primary 21-page PDF was materially inspected, including its definitions, Theorems 3–5, Appendix B and references.

## Value — PASS

This settles the specific unresolved universal one-redundancy threshold for two-error function-value protection, reduces the prior sufficient dimension from 66 to the optimal 36, and proves an explicit impossible immediately preceding case. The lexicographic compression avoids exponential enumeration and supplies a reproducible exact certificate, beyond a parameter substitution or isolated numerical instance. It bears directly on the distinction between protecting a function and protecting a full message.

## Limitations and sources

This is not a claim about systematic encoders, arbitrary message decoding or other error counts. The finite certificate has been replayed but no independent mathematical audit has been performed. Principal literature: Rajput, Jagatti and Rajan, *On Optimal Encodings and Systematicity in Function-Correcting Codes*, arXiv:2610.09011v1 (October 6, 2026); L. H. Harper (1966); E. Räty (2020). The latter two provide the known neighborhood-isoperimetry theorem, not the new numerical threshold.

Self-review: passed. Independent audit: not yet performed.
