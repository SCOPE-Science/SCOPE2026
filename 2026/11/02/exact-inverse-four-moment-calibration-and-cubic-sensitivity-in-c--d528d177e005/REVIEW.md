# Scientific review

## Correctness

PASS. The model's absorption time is a geometric sum of independent Erlang circuit times, whose rational moment-generating function yields all four raw moments. The derivative is an explicit rational expression with a strictly positive polynomial numerator for all integers \(s\ge3\), all \(x\ge0\), and any rate \(\lambda>0\); thus inversion is unique and its endpoint values are sharp. The asymptotic expansion gives the exact cubic flattening constant \((s^2-1)/(18s^3)\). The pole argument excludes a finite acyclic representation in the genuinely cyclic range. The extracted exact-rational verifier reproduces 132 moment/derivative instances and further identities; those tests are checks of, not replacements for, the universal algebraic proof.

## Originality

PASS under available evidence, with residual priority risk. The 2025 fitting study discusses broad nonconvex optimization and exact/moment fitting history but gives no sharp inversion or conditioning formula for this homogeneous cyclic feedback family. The full author manuscript of the 2019 PH moment-bounds paper establishes stochastic-order and moment upper bounds without the stated normalized fourth-moment calibration. The 2026 RK/PH work proves general lower-order and acyclic higher-order bounds, but leaves general cyclic higher-order inequalities open; our result is a strict special case, not a proof of that general problem. Searches for geometric sums of Erlang variables, cyclic PH fourth-moment ratios and feedback-parameter identifiability, and comparisons against accessible related records, found no equivalent specialized formula. An unindexed or differently named older feedback-Erlang formula remains possible; the searched corpus does not prove uniqueness of discovery.

## Value

PASS. Moment fitting to Markovian PH models is used when moment data feed stochastic simulation and queueing computations. The specified feedback cycle is the simplest genuinely cyclic, fixed-length homogeneous chain; the exact attainable range and positive derivative of its fourth-moment shape ratio provide a non-acyclic test family for higher-order PH moment inequalities. The cubic flattening warns against high-order-ratio-only fitting near the exponential limit; the lower-order variance ratio actually gives an affine, better-conditioned alternative if it is available. The exact constraint remains useful as an independent consistency check and structural benchmark, not as the preferred estimator. The numerical-inverse interpretation is specific and intrinsic, not an arbitrary small example; it does not replace general-purpose PH fitting methods.

## Closest literature and limitations

Sherzer–Resheff–Telek (2025), arXiv:2505.20379, supplies the numerical fitting motivation. He–Horváth–Horváth–Telek (2019), DOI:10.1017/apr.2019.7, supplies general moment bounds. Yu–Zhu–Weng (2026), arXiv:2610.37425, supplies a later comparison to higher-order phase-type moment-ratio inequalities. None is credited with this formula. Unknown stage count, heterogeneous holding rates, arbitrary cyclic transition graphs, statistical sampling variability, and general optimizer convergence are excluded. Publication priority remains subject to additional specialist literature review.

Self-review: passed. Independent audit: not yet performed.
