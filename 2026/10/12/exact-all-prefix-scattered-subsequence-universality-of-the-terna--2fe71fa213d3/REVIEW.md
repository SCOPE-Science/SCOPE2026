# Scientific review

## Correctness: PASS

The domain, alphabet, prefix origin, and subsequence convention are explicit. The standard greedy-arch characterization reduces the index to a finite-state scan. The Thue–Morse digit recurrences yield exactly four length-16 templates. Exhaustive finite inspection of those templates proves five arches per complete block for every input mask and singleton terminal states for each singleton input. Thue–Morse excludes constant length-three factors, so six and only six adjoining triples enter the remainder analysis. All sixteen remainder lengths for each triple give the stated formula. Substitution yields sharp discrepancy bounds, and explicit binary digit identities produce infinitely many equality positions. The packaged verifier reconstructs and checks the critical finite tables and a separate word generation; its finite prefix tests are corroboration rather than a substitute for the infinite proof.

## Originality: PASS

The 2020 Barker et al. paper provides the general invariant and arch characterization; the 2023 Schnoebelen–Veron work provides compositional algorithms for compressed words; and the 2024 Adamson et al. paper treats extremal absent-subsequence counts for fixed index. Readable primary source portions covering definitions, theorems, conclusions, and relevant algorithms contain no ternary Thue all-prefix formula. A targeted comparison against relevant indexed findings found no stronger theorem implying the exact result. An unindexed or independently known computation of the same word remains a residual risk; search nonappearance alone is not a proof of historical novelty.

## Value: PASS

The formula completely evaluates a standard subsequence-coverage invariant at every prefix of a canonical ternary square-free word, exposing the exact arithmetic obstruction at a single residue modulo sixteen. The slope \(5/16\) and the *sharp uniformly bounded* error characterize global behavior, rather than a sample of prefixes or an isolated numeric invariant. The result is mathematically motivated by the established literature on scattered-subsequence universality; it is neither a relabeling of a general arch algorithm nor an arbitrary short-length census.

## Limits and closest literature

The result does not claim a new algorithm for arbitrary compressed words, nor any classification of circular universality, substring spectra, or absent-subsequence multiplicities. The closest primary papers are Barker et al. (2020), Schnoebelen–Veron (2023), and Adamson et al. (2024). The exact finite transition table is fully included in the proof and checker. The residual literature risk is an earlier unindexed equivalence.

Self-review: passed. Independent audit: not yet performed.
