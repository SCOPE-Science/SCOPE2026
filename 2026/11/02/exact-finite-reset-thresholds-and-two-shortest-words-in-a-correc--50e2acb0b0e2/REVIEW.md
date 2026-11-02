# Self-review

## Correctness
**PASS.** All thirteen integer parameters from \(3\) through \(15\) are covered by complete subset-graph breadth-first enumerations. The forward implementation starts with the complete state set and counts shortest paths toward any singleton; the independently written C++ implementation starts with singleton targets and searches their inverse preimages. Both give the same exact lengths and count two for every parameter. Explicit witnesses with central blocks `aaaa` and `abba` were evaluated letter by letter from the stated transitions and shown to be the only shortest words by the exhaustive two-path count. These computations prove only the specified finite range.

## Originality
**PASS, subject to ordinary priority uncertainty.** The closest directly inspected source (Wang, arXiv:2610.07044v1, Sections 2, 4, 5) proves a length-\(3p^2+4p-1\) reset *upper bound* and one explicit reset word, not an exact minimum-length theorem or two-word classification. Szykuła (arXiv:2608.24245v1, Figure 3 and Conjecture 8) treats the specified-state collision parameter rather than shortest global reset words. published-finding corpus research-record searches found nearby results on different automata but no implication yielding these thirteen exact cases. The supplementary/independent September work on this automaton was not fully inspected; it remains a priority risk, not evidence of coverage.

## Value
**PASS.** Minimum reset-word lengths and their multiplicities are natural global synchronization invariants, not the earlier specified-state pair-compression parameter. Establishing sharpness of the explicit published upper bound for thirteen successive parameters (up to 45 states) and classifying just two extremal words is a meaningful exact finite test range for the new construction. This neither substitutes for an all-parameter proof nor claims a general result.

## Residual limitations
The general sharpness conjecture and all-parameter uniqueness are unproved. Older or supplementary enumeration may preempt priority. This is a finite, reproducible self-review, not independent certification.

Self-review: passed. Independent audit: not yet performed.
