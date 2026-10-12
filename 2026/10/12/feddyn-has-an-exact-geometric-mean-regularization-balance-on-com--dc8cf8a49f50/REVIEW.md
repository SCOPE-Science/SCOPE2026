# Review

## Correctness

PASS. The defining exact FedDyn update was reconstructed from the source. For common-Hessian quadratics, the first local solve and all subsequent stored-gradient updates reduce to two commuting resolvents. The full-participation server identity then yields exact closed powers for the mean-client residual, client disagreement, and server error. Endpoint spectral monotonicity proves the sharp factors and the geometric-mean minimax parameter.

Scientific risk: the common-Hessian assumption is essential; no heterogeneous-Hessian extension is claimed.

## Originality

PASS. The defining source gives general convergence rates and an empirical/theoretical discussion of the regularization parameter, but it does not state the exact common-Hessian mode decomposition, the geometric-mean balance, or the isotropic one-round server cancellation. Focused searches for those equivalent formulations and stronger coverage did not locate an implication-equivalent published statement.

Residual risk: an unindexed federated-optimization note may contain the same common-Hessian specialization under different notation.

## Value

PASS. The result identifies an exact tuning law for the defining FedDyn regularizer on a natural heterogeneous family. It separates global tracking from client consensus, quantifies their opposing dependence on the parameter, and gives a unique balance with square-root condition-number scaling. The isotropic cancellation also gives a concrete finite-round interpretation of dynamic regularization.

Self-review: passed. Independent audit: not yet performed.
