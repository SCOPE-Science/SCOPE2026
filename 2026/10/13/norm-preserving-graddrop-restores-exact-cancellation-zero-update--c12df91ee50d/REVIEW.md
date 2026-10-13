# Review

## Correctness

PASS. The norm-preserving map multiplies the raw masked vector by the ordinary incoming gradient norm divided by the masked norm plus a positive regularizer. Exact cancellation therefore forces zero for every mask. The scalar \(a,-a\) example verifies that pure GradDrop remains nonzero while the norm-preserved variant is zero.

Risk: the statement assumes the incoming original gradient is the ordinary aggregate of the supplied task losses.

## Originality

PASS. The defining paper states the pure stable-point theorem and separately describes norm renormalization used in many experiments; the supplement treats the unrescaled mask. The inspected implementation enables the rescaling by default. No inspected source or focused database result states the composed zero-set obstruction.

Residual risk: an equivalent observation may exist in unindexed implementation discussions.

## Value

PASS. Task-gradient cancellation is the central pathology motivating GradDrop. Showing that a common paper-described and default implementation option restores precisely those zero updates is a direct and mathematically sharp implementation/theory boundary.

Self-review: passed. Independent audit: not yet performed.
