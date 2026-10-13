# Review

## Correctness

PASS. On the isotropic quadratic, the gradient is the parameter matrix. Strictly ordered diagonal entries uniquely determine the refreshed top-\(r\) singular subspace. The unit projected step annihilates exactly that block, and projector reuse then yields zero compact gradient for \(T-1\) steps. Induction gives the closed convergence time.

Risk: the exact zero blocks use a unit SGD step; nearby steps yield near-zero rather than exactly zero retention.

## Originality

PASS. The defining paper gives a qualitative warning that infrequent subspace changes can leave GaLore optimizing a no-longer-important region. Later convergence work notes that a fixed projector can annihilate a nonzero gradient. The inspected literature does not state the stronger dynamic fact that GaLore's own current top-SVD projector can create this exact orthogonality after one deterministic step on a condition-number-one quadratic, nor the repeated dead blocks and exact staircase time.

Residual risk: later subspace-tracking papers discuss closely related staleness phenomena, and an equivalent elementary example may exist in unindexed notes.

## Value

PASS. GaLore's refresh period controls a central compute-versus-tracking trade-off. The result gives a sharp, parameter-transparent boundary case in which a previously optimal projector retains none of the current gradient for an entire block, directly separating progress inside a stored subspace from coverage of the current gradient.

Self-review: passed. Independent audit: not yet performed.
