# Review

## Correctness

PASS. The full four-state recurrence is linearized on the open inactive-maximum branch. The retained maximum contributes an explicit neutral tangent eigenvalue, the current second moment contributes \(\beta_2\), and the remaining exact two-dimensional block has determinant \(\beta_1\). Jury conditions give the necessary-and-sufficient transverse stability threshold, while the discriminant gives the exact complex-root plateau.

Risk: this is a local scalar theorem on a fixed-memory branch, not a global trajectory theorem.

## Originality

PASS. The defining paper explains AMSGrad through long-term maximum memory and nonincreasing learning rates. The direct proof correction concerns regret inequalities and hyperparameter handling. Neither inspected source states a memory-indexed equilibrium manifold, a sharp local threshold in the stored maximum, or the exact momentum-controlled damping plateau. Focused published-record searches found no implication-equivalent AMSGrad result.

Residual risk: an equivalent local reduction may exist in unindexed notes under generic heavy-ball terminology.

## Value

PASS. The nondecaying maximum is AMSGrad's defining difference from Adam. The theorem shows that this historical state selects the local spectrum itself: insufficient memory is unstable, an intermediate range has a fixed damping rate, and excessive memory is stable but arbitrarily slow. This is a direct structural characterization of the mechanism the algorithm was designed to introduce.

Same-model review: passed. Independent audit: not yet performed.
