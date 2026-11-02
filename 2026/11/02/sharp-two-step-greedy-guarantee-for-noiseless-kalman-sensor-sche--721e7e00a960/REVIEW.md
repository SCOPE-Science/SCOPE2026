# Scientific review

## Correctness

**PASS.** The four possible two-time schedules are exhaustively tabulated from independent diagonal covariance propagation and exact coordinate-observation updates. The domination of schedule \(22\) when \(p_1\ge p_2\) is algebraic, giving the exact optimum; the one-step greedy policy follows by direct minimization at each time. The global ratio upper bound and a strictly positive-variance family attaining its supremum are both proved, with a separate zero-dynamics case. The verifier independently checks 20,000 rational examples and several sharpness instances. Risks: incorrect convention for pre/post-measurement covariance would change the statement; these conventions are explicitly fixed. No finite test is taken as a proof.

## Originality

**PASS, with residual priority risk.** Direct searches on two-step myopic Kalman scheduling, perfect coordinate observations, growth-dependent approximation ratios, and relevant research records found no equivalent explicit \(1+\max\{a_1^2,a_2^2\}\) guarantee or the exact two-time failure criterion. Dutta, Wilde and Smith (2023) solve general finite scheduling instances computationally rather than establish this analytical supremum. Jawaid and Smith (2015) treat terminal covariance and submodularity. Ye and collaborators (2020) show arbitrarily poor greedy steady-state design-time sensor selection; that stronger *negative* statement in a different model does not imply the sharp bound within diagonal two-step scheduling. Han and collaborators (2016) concern infinite-horizon remote scheduling. Risks: classical dynamic programming or adjacent age-based sensing work may contain an equivalent two-time formula; novelty is not certified independently.

## Value

**PASS.** Sensor scheduling is motivated by strict communication budgets and the widespread use of myopic trace minimization. The finding supplies a sharp quantitative approximation guarantee for the smallest genuinely dynamic problem, identifies exactly when lookahead is beneficial, separates contractive and expansive dynamics, and gives a minimal-dimension and minimal-horizon witness. Its stable-system factor is a natural global performance fact, not simply a computed instance or an arbitrary parameter slice. It may inform analysis of finite-horizon approximations even though it makes no claim about longer horizons.

## Closest literature and scientific limits

The 2023 mixed-integer formulation is the closest finite-horizon trace-scheduling benchmark. The 2015 sensor-scheduling submodularity paper addresses related greedy guarantees but a different terminal objective; the 2020 hardness paper has a different static/steady-state domain, and the 2016 independent-process scheduling paper is infinite horizon. Exact-observation and diagonal-independence assumptions are essential to the proof; a small positive observation-noise perturbation preserves strict examples, not the universal bound.

Self-review: passed. Independent audit: not yet performed.
