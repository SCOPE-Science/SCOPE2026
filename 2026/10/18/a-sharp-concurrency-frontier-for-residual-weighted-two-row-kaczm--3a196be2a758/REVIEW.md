# Scientific assessment

**Correctness (PASS).** The snapshot model is explicitly defined. The post-batch update is an exact binomial count, so conditional squared loss depends only on its first two moments. The resulting expression is affine in \(z(1-z)\), and both extreme directions are attainable. The branch comparison, convex minimization, and contraction criterion establish the claimed unique minimax relaxation for every positive integer batch size. Exact-rational checks of the identities and sampled parameter cases were executed successfully. Finite checks are supporting evidence only.

**Originality (PASS, with residual bibliographic risk).** Coleman's recent paper gives empirical concurrency/sampling tradeoffs, not the frozen-snapshot two-equation minimax formula. Moorman et al. analyze averaged independent updates using a fixed sampling distribution, and Steinerberger analyzes sequential residual-based selection. Those settings do not imply the claimed state-dependent full-batch worst-direction phase transition and \(1/9\) plateau. Earlier minibatch coordinate-descent equivalents remain a possible unlocated formulation; no claim of exhaustive literature uniqueness is made.

**Mathematical value (PASS).** The complete minimax solution identifies the exact onset of a duplicate-selection bottleneck at concurrency three: beyond that point, the relaxation needed to protect axis errors becomes incompatible with the balanced-error optimum. The resulting nonvanishing sharp batch factor contrasts with the zero limiting factor of uniform sampling on the same orthogonal benchmark. This gives a natural rigorous test case for adaptive sampler and relaxation designs under shared-snapshot parallelism.

**Scope and risks.** No claim is made for nonorthogonal rows, arbitrary asynchronous schedules, physical wall-clock speed, or nonuniform per-row relaxation. The main residual originality risk is an equivalent identity in prior stochastic minibatch optimization literature.

Self-review: passed. Independent audit: not yet performed.
