# Scientific review

## Correctness — PASS
The simultaneous induction on the full and one-symbol-truncated dyadic prefixes uses the exact decimation identity of the period-doubling morphism. Distinct factor-start parities cannot yield the same factor at lengths at least four because there is no four-zero run. Within each parity, factor occurrences are bijective to shorter-prefix factor occurrences, with boundary restrictions tabulated separately. This yields both the exact minimum and all starts. The finite base and the six further dyadic levels were tested by exact substrings; the infinite proof uses the structural induction, not extrapolation.

## Originality — PASS within inspected literature
General shortest-unique-substring algorithms (arXiv:2605.04826), known period-doubling attractor theorems (arXiv:2602.16152), generalized period-doubling kernel factorizations (arXiv:2511.20881), and OEIS A367184 concern distinct claims. In particular, attractor size and distinctness of every window do not logically determine the least length of a factor with exactly one occurrence. The compared sources did not establish this exact simultaneous dyadic full/truncated formula; unindexed equivalent work remains possible.

## Value — PASS
Globally shortest unique factors are a canonical finite-string invariant, and the period-doubling morphism is a fundamental automatic-word family. Exact length and complete positions in every dyadic prefix, including sharp behavior under deletion of its last symbol, provide a structural desubstitution rule useful when studying uniqueness and synchronization in automatic words. This is an infinite classification, not merely finite enumeration.

## Limits
Search incompleteness and lack of independent review remain. The result does not classify longer unique factors or general finite prefixes.

Self-review: passed. Independent audit: not yet performed.
