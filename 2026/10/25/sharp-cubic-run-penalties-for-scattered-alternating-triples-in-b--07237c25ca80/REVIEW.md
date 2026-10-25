# Scientific review

## Correctness — PASS

For each one after \(z\) preceding zeros, the exact scattered-\(010\) contribution is \(z(a-z)\). Compressing ones into positive-length runs gives strictly increasing productive zero cuts. Each boundary one-run must have length one in any nonzero optimum, and remaining one symbols must occur only at highest-weight productive cuts. Strict concavity of \(z(a-z)\) forces the \(t\) nearest integer cuts to the center. Their sorted deficits are \(0,1,1,4,4,\ldots\) or \(0,0,2,2,6,6,\ldots\), proving the cubic penalty. Every allowed run orientation and its feasibility are enumerated; comparison excludes the inferior odd one-ended orientation whenever a zero-ended word exists. All maximizing-cut ties and surplus-one allocations are counted. An independent brute-force checker compared maxima and maximizing-word multiplicities for 1,041 nonempty composition/run classes through length 18, and checked 126 center-deficit cases. These finite experiments are supporting checks only.

## Originality — PASS within inspected evidence

Bruda, *Enumerating binary words restricted by subsequence frequency* (arXiv:2607.02578v1, Theorem 1.8 and Section 4.4), proves general run-based bounds and proposes improvements for restricted classes, not the exact maximum and full equality classification for every binary composition and exact run count. Menon–Singh, *Subsequence frequency in binary words* (arXiv:2306.07870v1, Section 4), studies unconstrained maxima for patterns with up to three runs, including the baseline \(b\lfloor a^2/4\rfloor\); this alone does not imply the forced-run cubic loss or the count of equality cases. Fang, *Maximal number of subword occurrences in a word* (arXiv:2406.02971v1), concerns extremal subword entropy, not this fixed-pattern target. Related accessible mathematical-record entries address distinct reconstruction and universality parameters. No exact or dominating statement was found; equivalent unindexed results remain possible. The statement is not a claim about general patterns.

## Mathematical value — PASS

An exact run count is a substantive restriction of the underlying finite-word extremal problem. The theorem gives the complete infinite three-parameter answer, a universal parity-sensitive cubic penalty rather than a general upper bound, explicit sharp witnesses, and all equality multiplicities. These identify the precise cost of fragmentation into runs, an interpretable structural statistic in subsequence-based sequence analysis. The elementary central-cut optimization is reusable as an analytical method for related low-complexity patterns. The narrowness to \(010\), finite binary words, and fixed composition is stated explicitly.

## Limitations and verification

Independent scientific audit and independent certification of mathematical priority have not been performed. No finite calculation establishes the universal quantifiers. The proof is internal to `RESULT.md`; `verify.py` requires only standard Python and returned `CENTER_DEFICIT_CHECKS 126`, `FULL_COMPOSITION_RUN_AND_EXTREMIZER_CASES 1041`, `VERIFY_OK`. Primary citations are dated arXiv identifiers and the closest-source assessments refer to the actual mathematical statements, not merely keyword/title nonmatches.

Self-review: passed. Independent audit: not yet performed.
