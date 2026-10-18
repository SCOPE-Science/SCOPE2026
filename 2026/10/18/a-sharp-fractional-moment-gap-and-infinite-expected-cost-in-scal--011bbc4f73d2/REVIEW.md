# Scientific review

## Correctness — PASS

The sampled finite-horizon quadratic program is strictly convex, and the costate boundary system yields an exact closed-form control. Direct variation of constants produces the true-plant endpoint multiplier. The first and second absolute-moment inequalities and the signs of both multipliers are rigorously enclosed by the accompanying rational-interval Taylor certificate, without dependence on finite Monte Carlo enumeration. Strict convexity of the moment growth factor proves a unique positive moment threshold; a bounded-log strong law proves pathwise decay; interval-cost independence and Tonelli prove infinite expected quadratic cost but finite pathwise cost. The standalone verifier runs successfully and matches independent Runge–Kutta endpoint integration. Limits: this is one scalar, unregularized, exact arithmetic two-model example with a fixed prediction horizon, and the printed threshold decimal is approximate.

## Originality — PASS, subject to residual priority risk

The principal RBM-MPC paper (`arXiv:2211.05463`, full HTML, Sections II, IV–V) establishes an *expected absolute-state* stability estimate and approximation results, not the complete sharp fractional-moment product law for the present explicit pair, its first-vs-second moment reversal, or an almost-sure-finite/infinite-expected quadratic-cost separation. The open-access predecessor (`arXiv:2109.13798`, full published HTML, Sections 2–3) gives fair two-singleton randomization and open-loop control convergence, but not repeated closed-loop scalar multipliers or the claimed exact risk split. Comparisons also considered abstracts for `arXiv:2405.15552` and targeted mathematical-record queries; no covering specific result was identified. The iid scalar multiplier identity and classical logarithmic Lyapunov criteria are prior mathematics; only their Riccati/MPC-specific instantiation and quantitative witness are claimed. A broader theorem for random switching MPC may subsume the claim; no failed search is treated as proof of novelty.

## Value — PASS

The gap matters because an expected-absolute-state stability guarantee does not control the quadratic performance objective used to design the controller. The example exhibits a robust (strict inequalities persist under small model/horizon perturbations), exactly reproducible risk reversal in a stabilizable/detectable scalar linear-quadratic system with an unbiased randomized model and identifies the complete positive moment boundary, rather than just a single failed second-moment inequality. The strictly positive expected stage-cost coefficient makes infinite expected accumulated actual cost a genuine performance failure despite typical exponential stabilization. The example is a risk diagnostic and method benchmark, not a computational-speed contribution.

Self-review: passed. Independent audit: not yet performed.
