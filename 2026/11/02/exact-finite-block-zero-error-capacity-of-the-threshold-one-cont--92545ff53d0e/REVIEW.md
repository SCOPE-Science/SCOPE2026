# Scientific review

## Correctness — PASS

The channel deletes exactly one letter for each noninitial original run. Hence every length-\(n\) input with \(s\) runs produces a word of length \(n-s+1\); a subsequence has no more constant runs than its source. This gives the sharp necessary minimum input length \(m+r-1\) for an output of length \(m\) with \(r\) runs. The explicit inverse increases every output run after the first by one letter and is the only minimal-length inverse. Appended singleton runs establish every larger input length when \(q\ge2\). Enumerating output run compositions gives the exact image count; a representative per image point attains the zero-error optimum. The rational generating function follows from a geometric sum of run-length compositions, and its positive dominant root gives the claimed rate.

The standalone `verify.py` confirms the image formula by exhaustive direct channel enumeration at the stated small alphabet sizes and by independent integer recurrences at larger sizes. The proof, not finite testing, establishes the result for all block lengths and alphabets in its scope.

## Originality — PASS (subject to publication-priority risk)

The directly motivating article (Chen–Milenkovic–Ribeiro–Sima, arXiv:2602.05072) defines the deterministic contextual mechanism and explicitly restricts its constant-threshold capacity arguments to \(k\ge2\). Its stated capacity bounds do not imply an exact \(k=1\) finite-block image characterization. We checked the model, relevant theorem statements and the Section V proof setup in the openly available complete text. Related run-length-limited code constructions and arbitrary-deletion capacity results use different output relations and do not mathematically cover the present theorem. Searches for the precise run-boundary transducer and its generalized Fibonacci image enumeration did not disclose an equivalent statement.

Residual risk: a separately published or unindexed special-case identity for this deterministic transducer may exist. Independent literature priority verification has not been completed.

## Value — PASS

The threshold-one endpoint of a recently studied nanopore-motivated channel admits a natural and previously unprovided complete answer: every finite-block optimal size, an explicit optimal code representative for each possible output, the unique shortest-preimage classification and an exact asymptotic capacity for every alphabet size. The ability to pad minimal representatives to arbitrary block lengths is a structural fact specific to the channel and explains how output run statistics control code size. The result is directly relevant to the boundary case of the motivating extremal channel, including the four-letter alphabet.

## Boundaries

This is a deterministic \(k=1\) result, not a solution for \(k\ge2\) or random/adversarial contexts; the interval of applicability and residual publication-priority risk are explicit in the manuscript.

Self-review: passed. Independent audit: not yet performed.
