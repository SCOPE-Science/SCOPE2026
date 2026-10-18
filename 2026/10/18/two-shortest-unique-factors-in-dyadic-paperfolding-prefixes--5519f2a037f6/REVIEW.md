# Scientific review: Two shortest unique factors in dyadic paperfolding prefixes

## Correctness — PASS
The 2-adic bit rule, repeated short-factor lifting, finite 36-template synchronization, dyadic decimation induction and complete endpoint table prove the exact threshold and the two starts for all dyadic exponents at least six. The length-64 base is exhaustively checked. `checker.py` confirms 36 pairwise distinct nine-bit templates and reproduces all smaller direct counts for exponents six to twelve. The finite tests are corroboration, not a substitute for the proof.

## Originality — PASS within examined evidence
Kishi et al. (2026) provide a known and stronger Thue–Morse minimal-unique-substring theorem; the new result concerns *paperfolding* instead. Banbara et al. (2026) and a published regular-paperfolding computation concern *string attractors*, not frequency-one factors. Allouche's classical factor-complexity theorem and OEIS A337120 count infinite factors, not their occurrences in finite dyadic prefixes. Targeted published-finding corpus and literature searches for aliases, equivalent formulas, the exact offsets, synchronization and broader theorems did not reveal a covering statement. The full regular-paperfolding attractor record and full 1992 paper were not inspected, and unindexed work remains a residual overlap risk.

## Value — PASS
This is a natural exact classification over an infinite family of a classical automatic word, settling the shortest uniqueness threshold and both positions. The proof exhibits a useful dyadic synchronization mechanism and makes explicit a difference between factor complexity, attractor coverage and finite-frequency-one statistics. Its significance is the complete structural formula, not the finite samples alone.

## Boundaries
Regular paperfolding convention explicitly fixed; dyadic exponents only. No assertion about all minimal unique substrings or arbitrary prefixes. Code checks the symbolic base and finite examples only. Independent mathematical validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
