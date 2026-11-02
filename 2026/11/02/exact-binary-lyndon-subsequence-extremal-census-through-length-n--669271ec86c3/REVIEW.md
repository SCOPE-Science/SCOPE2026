# Scientific review

## Correctness — PASS

The theorem is explicitly finite. A unique sentinel-bit encoding of each binary string, the exact two-case recurrence for subsequences when the final host symbol is appended, and a complete direct rotation test for Lyndon membership reconstruct the score for every host. The implementation examines all \(2^n\) hosts separately for each \(1\le n\le19\), with no statistical sampling or missed symmetry classes. Tagged-set membership prevents duplicate patterns. The independent Python set-based computation matches all exact maxima, tie counts, first witnesses and aggregate scores at every length through \(16\). The C11 census completes the remaining three finite lengths and prints the stated values.

## Originality — PASS, subject to residual literature risk

The nearest established formula concerns maximum counts of **all positional occurrences** of Lyndon subsequences; that maximum cannot imply the maximum number of **distinct** patterns because repeated embeddings contribute more than one occurrence. Open-access work on computing a longest Lyndon subsequence concerns a different statistic. OEIS A290743 tabulates maxima for **contiguous Lyndon factors** and has different values. Actual semantic searches of mathematical result records for the distinct binary Lyndon *subsequence* maximum, its aliases and numeric profile found no equivalent enumeration or stronger formula. Unindexed finite tables remain possible, so this is not a guarantee of worldwide novelty.

## Value — PASS

A complete finite profile through length nineteen gives exact benchmark values and full optimizing-word multiplicities for the distinct-pattern variant of a published Lyndon-subsequence counting problem, in contrast to the known positional and contiguous variants. The two distinct optimizers at length twelve and changes in the shape of extremal words are nontrivial structural features, useful for formulating and testing future extremal classifications. No extension to arbitrarily large lengths is claimed.

## Closest literature and scientific limits

Hirakawa et al. (2021), arXiv:2106.01190; Bannai et al. (2022/2023), arXiv:2201.06773; Glen–Simpson–Smyth's 2017 Lyndon **factor** enumeration as recorded in OEIS A290743. Enumeration by correct exhaustive loops proves the finite census but not any infinite pattern. The final three lengths were exhaustively checked by C11; the second independent implementation stops at length sixteen.

Self-review: passed. Independent audit: not yet performed.
