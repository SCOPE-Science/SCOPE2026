# Review: critical exponent five for sesquinary Thue–Morse

## Correctness — PASS

The factor-period quantifiers, alignment bounds and base-\(3/2\) normalization were checked directly. The argument passes through two exact three-letter macroblock identities. The absence of four alternating or six equal even-subsequence letters supplies local obstructions. For a factor of period coprime to three, three shifted adjacent-edge witnesses force it to be constant or alternating. For a divisible period, inverse decoding of complete blocks reduces the period by a factor \(2/3\) with an explicit boundary loss; iterating yields the forbidden threshold \(L\ge5q-1\). This excludes all length-\(5p+1\) periodic factors of the main word, with a separate exact case for \(p=3\). The fifteen-letter period-three fifth-power witness establishes equality. The Python verifier checks finite prefixes only; the above argument covers all periods.

## Originality — PASS within examined literature

Dekking [1], Sections 2–3, explicitly calls critical exponent five Conjecture 9. A recent same-object paper [2] relates the word to a normalized-base sibling and establishes uniform recurrence, reversal symmetry and word frequencies; inspection did not identify the critical exponent as one of its results. A 2025 paper [3] proving other Shallit conjectures concerns a different indexed family. mathematical research index and targeted text searches for the sequence name, number A357448, the exact period-length criterion and repetition aliases found no covering claim. Bibliographic risk remains: an unindexed equivalent proof could exist.

## Mathematical value — PASS

The result exactly resolves a natural infinite-word repetition invariant explicitly identified as an open conjecture in a foundational number-representation paper. The all-period exclusion is not a finite verification or arbitrary parameter slice, and the desubstitution estimate is a reusable structural tool for rational-base block words. The ordinary fractional critical exponent, not just the largest integer power, is determined.

## Limitations and sources

Scope: the unscaled base-\(3/2\) digit-sum parity sequence only. This finding does not provide factor counts or extensions to other bases. Closest sources: [1] F. M. Dekking, arXiv:2301.13563v1 (2023), Conjecture 9; [2] J. Cassaigne et al., arXiv:2602.21895v1 (2026), Sections 1.4–1.5; [3] L. Dvořáková et al., arXiv:2506.04407 (2025), a different sequence family. Independent verification has not been conducted.

Self-review: passed. Independent audit: not yet performed.
