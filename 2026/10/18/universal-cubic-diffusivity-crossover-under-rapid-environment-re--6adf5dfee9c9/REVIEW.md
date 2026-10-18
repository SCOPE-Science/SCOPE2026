# Scientific review: cubic diffusivity crossover

## Correctness — PASS

The regeneration formulas (3.1) and (3.15) of Martin–Nagel identify the exact variance. For all one-dimensional iid site laws, direct path-by-path factorization verifies the eight first/second moment identities for static displacements of lengths one through four. Substitution gives the exact cubic \(-8s^2\) after cancellation of the linear term and of the third-order speed coefficient. The explicit complex-analytic bound \(|\Sigma|\le2700\) on \(|r|\le1/2\) implies the claimed remainder \(\le86400r^4\), even for varying site laws. This bound proves the separated crossover signs with no simulation or formal-series leap. The standalone checker reruns the enumerations and coefficient algebra; the infinite-domain estimate is proved separately.

## Originality — PASS, with residual risk

The closest primary source is Martin–Nagel, arXiv:2610.11919v1, Theorem 2.4 and Lemma 3.3, which give local-minimum behavior only for nonzero drift and stop the explicitly evaluated derivatives at second order. Their more general series supplies a method that can in principle be further expanded, so neither regeneration nor the known first two coefficients is claimed as novel. The assessed result is the centered cubic local-maximum classification and the law-uniform sharp drift–refresh sign crossover, including a fourth-order explicit bound. The cooling papers arXiv:1610.00641 and arXiv:1803.03295 use different refresh schedules and neither states that sign law. Searches for higher-order diffusivity, equivalent Taylor expansions and cooling analogues located no decisive covering result. Residual priority risk remains from possibly unindexed higher-order computations or a reduction not detected in the available literature.

## Value — PASS

The motivating theorem leaves a mathematically natural boundary case unresolved: zero mean drift makes its second-order curvature vanish. The cubic term supplies the **opposite** local-extremum type at that boundary and the precise transition rate for drift shrinking simultaneously with nonrefresh probability, uniformly across all iid bounded site laws. Both sides are attainable with a simple nondegenerate two-point site law. This is a structural boundary result for a natural stochastic-process invariant, not a choice of arbitrary numerical parameters.

## Closest literature, unresolved scope and status

Martin–Nagel [arXiv:2610.11919v1] already give the regenerative CLT representation and the quadratic coefficient; the present claim does not cover the sign on the exact critical crossover line, the optimized remainder, or refresh rates far from one. Independent priority and scientific validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
