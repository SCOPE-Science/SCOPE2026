# Review

## Correctness

PASS. The explicit eleven-word set has load at most two for each of the thirty-two length-five words. The upper certificate assigns nonnegative weights with total numerator 326 over denominator 59; every length-seven word has weighted subsequence score at least 59 after adding 7 for the two constant words. Therefore any valid code has size at most \(666/59<12\), hence at most eleven. The included verifier checks the complete finite domain exactly.

## Originality

PASS, subject to the stated indexing limitation. The closest indexed finite result is the length-six binary two-list, two-deletion optimum. The recent general paper proves asymptotic lower bounds and common-subsequence/supersequence estimates but does not give the length-seven optimum. Exact-query searches did not locate this length-seven value. Search failure is not proof of global novelty; an unindexed independent result remains a residual risk.

## Value

PASS. Length seven is the immediate next blocklength after the recently indexed exact length-six case, and the recent list-deletion literature motivates the same natural finite extremal parameter. The finding closes that one finite case with a compact rational certificate; it does not claim a general formula or classify all optimal codes.

## Closest literature and limitations

Andrew D. Lin, “Lower Bounds for all List-Decodable Deletion Codes,” arXiv:2609.26650 (submitted 22 September 2026), gives a general asymptotic framework. The indexed published-finding corpus record “Exact length-six binary two-list two-deletion code size” supplies the adjacent length-six comparison, but its full repository record was not accessible here. No claim is made about larger lengths or the number of inequivalent optima.

Self-review: passed. Independent audit: not yet performed.
