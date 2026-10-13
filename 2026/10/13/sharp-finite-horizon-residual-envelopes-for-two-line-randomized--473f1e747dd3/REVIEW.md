# Self-review

## Correctness: PASS

The exact conditional recurrence rests on two facts that have no additional probabilistic assumptions: every projected vector in the plane lies on one of the row-orthogonal lines, where its mean-row squared residual equals \((1-c^2)/2\) times squared norm; every later uniformly sampled projection preserves squared norm or multiplies it by \(c^2\), with equal conditional probabilities. The spectral maximization is exact because \(H\) has eigenvalues \((1\pm c)/2\). The explicit cubic controls the derivative. Its uniqueness cases, the increasing-horizon comparison, the limiting optimizer and the sharp constant are proved for the full parameter range. The one-step threshold follows from the generalized Rayleigh quotient; it does not assume per-realization monotonicity of the residual. The separate exact-rational checker returned `VERIFY_OK` for 1,491 enumerated path/initialization/horizon cases and 783 derivative identities. Finite tests support but do not replace the proof.

## Originality: PASS with literature risk

Agaskar, Wang, and Lu (2014), Proposition 1, provide a general Kronecker-based identity for expected squared *solution error*. Bai and Wu (2018) extend exact mean-square analysis. Their broad frameworks can be specialized algebraically, which is credited; the specific sharp **mean-row residual** envelope jointly optimized over angle and initial error, its unique cubic optimizer and \(1/\mathrm e\) limit, and the transient coherence threshold are not stated in the inspected portions. Dereziński and Dong's April 2026 analysis gives general last-iterate estimates; their later June 2026 analysis already establishes an order-\(1/t\) upper bound for general Kaczmarz. Accordingly no claim to novelty of the order of decay is made. The numerical-stability analysis by Dereziński, Epperly, Needell, and Xue (May 2026) has different finite-precision hypotheses and conclusions. A near-topic 2026 research record on maximal-distance selection analyzes a different row-selection rule. Residual risk includes an equivalent specialization in older/unindexed moment-operator literature, particularly the full Bai--Wu article.

## Value: PASS

The natural two-row minimax residual question has a complete, sharp answer at **every** horizon, rather than a generic rate estimate. The optimizing geometry itself changes with the horizon, approaching degeneracy on the precise \(1/t\) scale. The threshold \(\sqrt2-1\) separates universal first-step expected residual monotonicity from possible initial residual overshoot, despite the fact that Euclidean error under orthogonal projection cannot increase. These facts give quantitative diagnostics for residual-based stopping and stress testing of randomized projection solvers. The value is confined to this minimal two-row family; it is not presented as a new universal Kaczmarz rate theorem.

## Literature comparison and limitations

Most closely related primary sources: Agaskar–Wang–Lu (2014), Proposition 1; Bai–Wu (2018), exact MSE and convergence-rate discussion; Dereziński–Dong (2026), arXiv:2604.09909 Section 2 and arXiv:2606.29593 Theorem 3.1; Dereziński–Epperly–Needell–Xue (2026), arXiv:2605.17185. The full Bai–Wu paper was not fully available through the inspected open source; that access limitation is recorded rather than treated as evidence of absence. Unequal sampling, relaxations, dimension above two, noisy or inconsistent equations, and floating-point error are unproved here.

Self-review: passed. Independent audit: not yet performed.
