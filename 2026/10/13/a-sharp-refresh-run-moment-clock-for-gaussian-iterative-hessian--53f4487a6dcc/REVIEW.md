# Scientific review

## Correctness — PASS

The scalar sketched-Hessian law is exactly scaled chi-square. The negative-moment integrability condition follows by comparing the density near zero with a power, including equality. Conditional on any refresh partition, independent-block multiplication yields the necessary and sufficient moment condition. The all-retention event has probability \((1-p)^{k-1}\), which supplies divergence for every \(0<p<1\) at the exact boundary. The independent/full-refresh rate follows from the first two exact inverse moments; the refresh chain is stationary ergodic for positive refresh probability and its logarithmic multiplier is integrable, proving the almost-sure rate. The deterministic periodic comparison follows from the same block law. Exact rational checks reproduce the finite cases. No simulation is used as proof of an infinite moment.

## Originality — PASS, with residual risks

Lacotte–Pilanci [2] distinguishes fully fixed and fully refreshed sketches, but its conditional fixed-sketch guarantees and independent-sketch exact mean error do not state an exact finite-horizon moment clock for Bernoulli-held sketches, or the independence of the almost-sure Lyapunov exponent from the positive refresh probability. Wang–Ouyang–Xu [3] analyzes nested correlated Gaussian sketches for a different double-sketch algorithm and conditional asymptotics, not this scalar Hessian-only Bernoulli retention model. Pilanci–Wainwright [1] establishes the original IHS setting with different guarantees. Published mathematical finding searches found no covering statement. Unindexed equivalent work and deductions from specialized inverse-Wishart results remain priority risks.

## Value — PASS

The exact moment threshold resolves a concrete design choice: caching a Gaussian preconditioner at each step with even a tiny positive probability can make expected squared error undefined after two steps, despite a negative almost-sure convergence exponent equal to that of full refresh. A deterministic cap gives a checkable sharp integrability safeguard. The result identifies a failure of moment-based performance criteria, not a claim of typical numerical divergence or finite-precision breakdown. The unrestricted linear-algebra implications and runtime tradeoffs are not determined.

## Scientific limits and closest sources

The proof is exact for rank-one full-column-rank least squares, Gaussian Hessian sketches, full inverse steps, independent state-independent refresh decisions and nonzero deterministic starts. [2, Theorem 4.1] already supplies the full-refresh expected-rate calculation; it is expressly excluded from any novelty claim. [3] supplies a related correlated Gaussian-sketch construction but does not establish the stated refresh-probability discontinuity for the same update. Independent replication and broad bibliographic priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
