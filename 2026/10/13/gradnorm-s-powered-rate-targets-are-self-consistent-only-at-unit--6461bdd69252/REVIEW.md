# Review

## Correctness

PASS. The source actual gradient norms sum to \(T\bar G\), while its powered targets sum to \(T\bar G M_\alpha\). The \(L_1\) triangle inequality gives the lower bound, explicit positive normalized allocations attain equality, and positive GradNorm weights realize those allocations for arbitrary positive base gradient magnitudes. Strict Jensen inequalities give the complete heterogeneous-rate transition at \(\alpha=1\).

Risk: the theorem is instantaneous and assumes positive task weights and nonzero shared-layer task gradients.

## Originality

PASS. The defining full text states every ingredient of the target construction but does not analyze the mean after exponentiation or give an irreducible target mismatch. Later scale-invariant multi-task work criticizes learned gradient balancing more broadly, without stating this exact mass identity, Jensen threshold, sharp residual, or mean-preserving correction. Focused published-record searches did not locate an implication-equivalent result.

Residual risk: the identity is elementary and could occur in unindexed implementation discussions.

## Value

PASS. The asymmetry exponent is GradNorm's central tuning parameter. The result shows that its powered targets are exactly compatible with their own mean only at unit asymmetry for heterogeneous tasks, quantifies the unavoidable mismatch at every other positive exponent, and gives the unique ratio-preserving correction. This directly clarifies what the auxiliary balancing objective can and cannot attain.

Self-review: passed. Independent audit: not yet performed.
