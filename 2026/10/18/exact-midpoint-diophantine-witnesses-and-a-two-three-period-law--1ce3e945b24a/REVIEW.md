# Review of the midpoint recurrence theorem

## Correctness: PASS

The proof derives the complementary Bézout representations directly, transports both modular-inverse witnesses under the determinant-one recurrence, and enumerates the complete six-state parity automaton. The explicit cycles give least periods rather than upper period bounds. Checked small instances confirm every claimed witness and the distinction between even and odd \(k\). Finite tests supplement but are not substituted for the universal proof.

## Originality: PASS within inspected evidence

Davala (2023, DOI 10.7546/nntdm.2023.29.3.495-502) already covers several balancing and Lucas-balancing instances, including the adjacent balancing case with \(k=6\). These are a strict subcase of the new theorem and are not claimed as new. Arachchi and collaborators (arXiv:2309.04488, Theorem 5.2) prove a different, additive-sign recurrence classification; their pairwise modular inverse criterion is an antecedent, not the claimed negative-sign transport and dichotomy. Chu, Miller and Tresch (arXiv:2512.12681) pose general recurrence questions. The 2025 survey and September 2026 preprint were additionally inspected; their arbitrary-seed and generalized-target results concern Fibonacci/additive sequences and other target values, respectively, not the full subtractive claim. Targeted result-record and literature searches did not identify a theorem dominating the complete arbitrary-seed subtractive case. Remaining risks: unindexed work and unnoticed implicit corollaries.

## Mathematical value: PASS

The classification directly addresses the natural extension from special balancing sequences to every positive, ordered initial pair and every subtractive recurrence coefficient \(k\ge2\). It resolves both which equation is solvable and its unique witness for all indices, with a sharp period and frequency distinction. This is a structural uniform extension rather than another finite computation or a renamed known example.

## Limits

The parameter domain excludes negative or unordered seeds and \(k<2\). The review is same-model, not independent. Prior work already proves the fixed-pair existence-and-uniqueness theorem and some balancing subfamilies.

Self-review: passed. Independent audit: not yet performed.
