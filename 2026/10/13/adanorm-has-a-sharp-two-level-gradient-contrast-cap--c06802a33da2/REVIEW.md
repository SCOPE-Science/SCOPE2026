# Review

## Correctness

PASS. The historical norm under alternating magnitudes is an exactly solvable two-step affine recurrence. The formulas show that high-norm steps remain below their current norm and are never corrected, while low-norm historical values increase monotonically past the low norm and converge to a larger fixed point. The onset index and contrast cap follow by exact inequality inversion and differentiation.

Risk: the final host optimizer can alter corrected-gradient amplitude through its own momentum or denominator.

## Originality

PASS. The defining AdaNorm paper gives the EMA-based norm correction and qualitatively motivates boosting low gradients, but the inspected full text does not state the two-level periodic response, finite correction-onset index, or sharp contrast cap. Focused published-record and web searches found no implication-equivalent result.

Residual risk: an equivalent short recurrence calculation may exist in unindexed implementation notes.

## Value

PASS. The result quantifies AdaNorm's defining mechanism directly and independently of any host optimizer. It shows that persistent arbitrarily large batch-to-batch norm contrast is compressed to a finite ratio determined solely by gamma; at the source's gamma equal to 0.95 the cap is only \(39/19\), so a vanishing alternating low norm is asymptotically raised to nearly half the high norm.

Self-review: passed. Independent audit: not yet performed.
