# Review of the sharp minority-frequency bound

## Correctness
PASS. The binary append-recurrence cases are read from Petković–Ćirić–Bogdanović (2004, Theorem 4.1), and an induction separates source words ending in a singleton one-run from longer one-runs. This proves the uniform inequality for all finite sources, including empty and one-letter-only cases. A constructive induction on \((010)^k\) proves equality for all \(k\). The independent enumeration checker exhaustively tests all 32767 binary words of lengths 0–14 and eight equality examples; finite testing is corroborative only.

## Originality
PASS with historical priority risk. The 2004 paper directly supplies the recurrence and an extremal Fibonacci estimate by number of constant-symbol runs, but not this sharp estimate by number of occurrences of one symbol. The inspected 2022 survey gives general minimal-absent-subsequence algorithms and representations; research-index searches, including aliases, produced no equivalent sharp frequency theorem. The older result is neither hidden nor treated as independent proof of novelty. The 2021 detailed MAS paper was not fully inspected, leaving a residual priority risk.

## Value
PASS. A sharp output-size bound depending only on the sparse-letter frequency, independent of total word length, clarifies the extremal complexity of forbidden subsequence bases for low-weight strings. The extremal construction demonstrates optimality for every nonnegative parameter.

## Limits and closest sources
The paper Petković–Ćirić–Bogdanović (2004) is the primary comparison; its run-parameter bound does not yield the sharp occurrence-parameter constant. Further exact comparisons to unindexed or inaccessible full texts remain a priority risk. The proof makes no claim about larger alphabets or all maximizers.

Self-review: passed. Independent audit: not yet performed.
