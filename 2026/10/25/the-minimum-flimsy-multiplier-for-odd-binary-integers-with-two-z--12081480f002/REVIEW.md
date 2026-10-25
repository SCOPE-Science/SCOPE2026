# Scientific review

## Correctness
PASS. The odd-multiplier reduction removes every even candidate. The elementary multiplication transducer proves that once a run contains four ones, extending it cannot change any digit-sum comparison for multipliers \(3,5,7,9\). Exactly 70 capped triples remain, all checked exhaustively with exact arithmetic and a distinct bit-serial implementation in `verify.py`. A separate proof using the minimum binary weight of a positive Mersenne multiple establishes sturdiness for the sole remaining run family. The counts follow by an explicit count of constrained triples. The unbounded result depends on these lemmas and the exhaustive finite set, not on the additional length-80 stress test.

## Originality
PASS within inspected literature. The motivating full text defines first flimsy multipliers and gives algorithms for individual inputs, but its two-zero theorem determines only sturdy versus flimsy status. Its upper bound of nine for candidate multipliers does not specify which is first for each input, nor the exact five-class count. The conference version likewise contains no run-length formula. Targeted searches of mathematical records and relevant prior findings revealed no stronger covering claim. An unpublished automata simplification or unindexed table is a genuine residual risk, and independent publication priority is not established.

## Mathematical value
PASS. Minimal witness size is one of four explicit invariants investigated in the motivating paper. A complete, uniform infinite classification of the first witness for the smallest nontrivial two-zero family gives strictly finer arithmetic information than sturdy/flimsy status, identifies the sharp multiplier spectrum, and supplies exact length profiles. The four-one finite-state reduction is structural; the result is not a mere repeated tabulation at fixed length.

## Scope and limitations
Only odd, exactly-two-zero binary numbers of length at least seven are covered. No general higher-zero classification or formula for the minimum binary digit sum over all multiples is claimed. The existing sturdy characterization is cited as prior work, not represented as new.

Self-review: passed. Independent audit: not yet performed.
