# Review

## Correctness

PASS. For one filter block the source normalization is scalar, so the \(p=2\) ASAM perturbation simplifies exactly. The chosen mixed vector has unit norm and balanced gradient coordinates, which makes every inner product explicit. Expanding the update gives the claimed quadratic norm ratio and an exact if-and-only-if one-step threshold. The large-condition-number constant and pure-eigenmode comparison then follow analytically.

Scientific risk: one-step Euclidean expansion is not promoted to a global divergence statement.

## Originality

PASS. The defining ASAM paper gives the filter-wise normalization, additive stabilizer, and perturbation rule but does not give a condition-number-dependent quadratic nonexpansion frontier. The closest inspected quadratic dynamics work concerns fixed-radius SAM, whose perturbation does not scale with the parameter norm. Focused published-record and owned-ledger searches found no implication-equivalent filter-wise ASAM mixed-mode result.

Residual risk: an equivalent calculation may exist in unindexed technical notes.

## Value

PASS. Filter-wise normalization and its stability stabilizer are central to ASAM. The result identifies a mechanism-level failure of pure-eigenmode intuition: an apparently small high-curvature parameter component can create an order-one gradient component and then incur the high curvature a second time, shrinking the mixed-mode one-step scale from order \(\kappa^{-1}\) to order \(\kappa^{-2}\).

Self-review: passed. Independent audit: not yet performed.
