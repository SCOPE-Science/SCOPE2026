# Scientific review

## Correctness

**PASS.** From each ordinary shuffle witness, matching equal-position subsequence letters yields a non-nesting perfect matching. From each reverse-shuffle witness, paired positions necessarily straddle the midpoint, and their right-endpoint permutation has no increasing triple because two decreasing subsequences cover it. Any three shared edges would be simultaneously increasing (forced by non-nesting) and forbidden (by increasing-triple avoidance). An alternating-component count bounds the number of distinct letters. The explicit palindromic construction supplies equality for every integer half-length; surjective relabeling proves the exact full-support threshold, and injective relabeling proves the asymptotic exponent. A standalone verifier checks 2,248,355 matching pairs, and an independent word-level enumeration checks binary and ternary cases up to length eight. These tests are finite; the all-length result follows from the combinatorial proof.

## Originality

**PASS, with residual risk.** The 2021 primary source arXiv:2109.12455 establishes the separate graph encodings and their one-language alphabet growth. Its inspected sections on ordinary and reverse shuffle squares do not state an extremal support theorem for the **intersection** or analyze the two matchings' shared-edge bound. The 2023 arXiv:2308.13882 studies variant shuffles and does not supply that joint threshold. The 2025 paper arXiv:2503.22043 discusses nest-free graph encodings and reverse shuffles without an equivalent support result in its inspected material. Related mathematical records were compared for literal and implied coverage, including other shuffle problems, but no stronger covering statement was identified. An unindexed equivalent theorem, particularly in matching-pair language, remains possible. No claim is made to independent novelty of the characterizations used as premises.

## Mathematical value

**PASS.** Shuffle squares and reverse shuffle squares are standard distinct families, and asking whether a word can satisfy both with many different symbols is a natural intersection problem. The exact support ceiling settles this question for *every* length; the sharp full-alphabet length threshold and halved large-alphabet counting exponent give useful consequences that cannot be read off from separate-language counts. The shared-edge obstruction isolates the structural reason for the reduction. Exact fixed-length enumerators and a classification of all maximizers remain open here.

Self-review: passed. Independent audit: not yet performed.
