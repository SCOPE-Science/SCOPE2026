# Scientific review: ternary palindromic-duplication congruence

## Correctness
PASS. The invariant argument accounts for first two letters, position parity of first appearances, total parity, and the unmoving short words. The finite-representative construction requires at most seven letters. The supplied verifier enumerates every elementary edge between ternary words of length at most fourteen and establishes all 354 generator transitions of the 118-state representative system. Right congruence and right-compatibility of the signature then prove the infinite classification by induction. Exact-length counts follow from combinatorial enumeration; the checker reproduces the small counts independently of connectivity. Finite graph tests are not substituted for the induction.

## Originality
PASS, subject to the stated priority risk. Zeraatpisheh–Esmaeili–Gulliver (2020) study duplication-correcting codes and rooted deduplications. Yohananov–Schwartz (2025), Theorem 12 and Section 5, give a disjoint-block-summary sufficient condition for common descendants and rate bounds, not the present necessary-and-sufficient ternary signature. The congruent pair `0120` and `0121` has unequal disjoint-pair summaries, exhibiting the gap in direct implication. An exact classification under alternate rewriting terminology cannot be ruled out by literature searches. A recent related arXiv item's abstract was available but its full text was inaccessible.

## Value
PASS. The statement supplies a complete natural quotient-monoid classification, including an exact finite index of 118, a sharp stable 57-class count at each sufficiently large word length, and a linear-time word-equivalence test. The third letter introduces ordered first-occurrence information absent from the two-symbol case. The result does not make claims about directed channels or coding optimality.

## Limits and independent status
The computational bound fourteen proves the finite transition table only, while the infinite scope depends on the explicit induction. Potential hidden equivalent prior formulations remain a priority risk. No independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
