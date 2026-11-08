# Scientific review

## Correctness

PASS. The STFT convention, window length, circular support graph and precise separation parameter are fixed. The three possible translated window sums yield exact formulas in terms of \(S=|A|^2+|B|^2\) and \(P=A\overline B\). These prove pointwise spectrogram equality for every frequency and translation, every multiple of three of dimension at least six, and every positive unequal pair. A quadratic with roots \(|A|^2\), \(|B|^2\) establishes the complete two-orbit classification only within the stated periodic family. `VERIFY.py` checks the rational autocorrelations independently on six dimensions; no finite sample is used as an infinite proof.

## Originality

PASS with residual bibliographic risk. The 2022/2023 Bartusel primary paper states the half-window extension as a conjecture; its periodic Example 4.2.3 has one nonzero in each relevant block, whereas here two occupied sites per block make the support connected. The 2024 dissertation Theorem 7.2.12 expressly asserts the contrary connectedness equivalence; its narrow exceptional configuration again has just one occupied site per window block. Nonvanishing-signal and two-tap-window results do not imply the present three-tap connected ambiguity. Relevant published comparisons and independently searchable aliases did not identify an earlier exact statement; an unindexed specialist example remains possible. This establishes best-knowledge rather than absolute priority.

## Value

PASS. The example supplies a concrete infinite family that separates support connectivity from genuine magnitude identifiability exactly at the previously conjectured half-window separation threshold. It also resolves the number of phase-inequivalent solutions in the natural periodic two-site stratum. This is not just a computation for an arbitrary parameter slice: it tests a specific structural boundary of a named phase-retrieval assertion.

## Limitations

The fiber count applies only after restricting both signals to periodic blocks \((A,B,0)\). A complete classification of competing unrestricted signals or nonflat windows is not proved. The cited 2024 theorem is compared as printed; this analysis does not establish a reason for that source's proof behavior. The result has not received independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
