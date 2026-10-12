# Review

## Correctness

PASS. From zero factor states, the printed row and column accumulators are positive multiples of row and column squared-gradient energies. The current normalized formula therefore satisfies \(V_{ij}=(1-\beta)R_iC_j/\|G\|_F^2\) for nonzero \(G\), while the original public formula has the same zero pattern. This proves the iff support criterion. Exhaustive finite enumeration and a strongly convex two-by-two witness reproduce the algebra.

Scientific risk: the result concerns the printed recurrence; the maintained implementation is different and safeguarded.

## Originality

PASS. Adafactor's factorization is prior, but its additive \(\epsilon\) after \(\sqrt V\) makes zero-support rows finite rather than undefined. The defining AdaLomo sources do not state the complete row–column criterion, and the maintained implementation avoids it by positive squared-gradient flooring plus inverse-square-root preconditioning. Focused indexed searches found no implication-equivalent AdaLomo support classification.

Residual risk: the printed quotient may be a notation discrepancy relative to the code, which is why the claim is explicitly about the paper formula.

## Value

PASS. The obstruction is a complete support boundary on a natural matrix class, not a single numerical corner case. It occurs at a nonstationary point of a \(1\)-strongly convex quadratic and is directly motivated by the paper's discussion of sparse data. Identifying the exact safeguard difference between the printed recurrence, Adafactor, and the maintained implementation is useful for rigorous analysis and reproducibility.

Self-review: passed. Independent audit: not yet performed.
