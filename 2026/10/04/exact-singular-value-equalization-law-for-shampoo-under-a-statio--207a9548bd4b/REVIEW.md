# Review

## Correctness

PASS. The stationary-gradient assumption makes both source Shampoo accumulators explicit. Their shared singular bases give the preconditioned singular values exactly, and all stated condition-number, target-time, polar-error, and cumulative-displacement formulas follow from those scalars.

Risk: the result is for the original additive accumulator and does not include later practical heuristics.

## Originality

PASS. The defining paper does not state the repeated-gradient singular equalization law. The closest later geometric result derives a polar update only after disabling accumulation, and the inspected modern decomposition work addresses eigenscaling, grafting, and staleness without the exact stationary-history formula or target iteration threshold.

Residual risk: the SVD calculation may appear in unindexed optimizer notes.

## Value

PASS. The result gives a direct finite-time account of what the defining accumulated Shampoo preconditioner does to matrix-gradient anisotropy. It bridges the original additive algorithm and later polar interpretations, quantifies the damping transient, and identifies an exact time scale for spectral equalization.

Same-model review: passed. Independent audit: not yet performed.
