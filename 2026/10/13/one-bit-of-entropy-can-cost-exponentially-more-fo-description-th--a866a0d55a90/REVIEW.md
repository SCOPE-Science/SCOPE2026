# Review

## Correctness
PASS. The maximum-entropy model has every one of the \(2^k\) unary types with multiplicity \(n/2^k\), while the comparison model has exactly two types with multiplicity \(n/2\). Substitution into the published upper and lower bounds gives matching leading coefficients, hence the ratio \(2^{k-1}\). The entropy values are exactly \(k\) and \(1\) bits.

## Originality
PASS with residual folklore risk. The source paper already says that maximal entropy need not maximize FO description complexity, but the inspected text does not state the explicit one-bit versus maximum-entropy family or the exact exponential ratio \(2^{k-1}\). Targeted semantic, exact-phrase, and own-ledger searches found no equivalent statement.

## Value
PASS. The result turns a qualitative failure of entropy monotonicity into a sharp family whose gap grows exponentially with the number of unary predicates, directly sharpening the compression interpretation motivating the source paper.

Self-review: passed. Independent audit: not yet performed.
