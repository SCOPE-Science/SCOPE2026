# Scientific review

## Correctness — PASS
The three transition probabilities are nonnegative and sum to one under the strict radius bound. The homogeneous formula is a finite geometric sum; minimization over the disk reduces to the lower boundary. The optimizer's localization to the logarithmic scale justifies the uniform exponential expansion and the explicit second-order constant in the deficit. The adaptive Bellman equation maximizes the exact support function of the disk, with a positive decreasing deficit; its reciprocal increments converge to \(r/2\). These are proofs for every fixed admissible radius, not extrapolations from finite samples. The independent angular-grid and direct propagation checks in `verify.py` agree with the formulas. No computation is used as an infinite proof.

## Originality — PASS, with residual risk
The nearest directly relevant result is Sangalli–Quaeghebeur–Krak (2026, arXiv:2603.16675v1, Example 1), which shows three-state nonattainment of eventual upper hitting probability but gives neither the disk construction nor finite-horizon stationary and adaptive asymptotics. Krak–T'Joens–De Bock (2019) give general operator characterizations; those imply the form of an adaptive Bellman *principle*, not the evaluated disk recurrence or sharp logarithmic comparison. The 2026 upper-operator convergence paper of De Bock–Erreygers–Persiau features a related quadratic transition curve but concerns qualitative convergence on a different network; no sharp rate of this claim is stated. The 2020 long-horizon MDP work assumes finitely many actions. Searches for quadratic tangency, absorbing three-state Markov uncertainty, stationary/nonstationary reachability, and exact asymptotic constants did not identify a covering published statement. Unindexed earlier asymptotics remain possible and warrant independent review.

## Mathematical value — PASS
Under smooth convex uncertainty with a quadratic failure-risk tangency, the infinite-horizon upper hitting value alone masks a diverging finite-horizon policy-class penalty. The explicitly proved \((\log t)/4\) ratio, full leading constants, and elementary three-state witness provide a calibrated boundary example for robust finite-horizon reachability and clarify why optimization before versus during evolution cannot be interchanged uniformly in horizon. This is not merely a rescaled expectation counterexample or a numerical instance; the nontrivial boundary-layer minimization and parabolic Bellman asymptotics are both required.

## Scope and reservations
Only fixed-radius disk uncertainty is covered. Literature screening is not a guarantee of priority, and the analytic review is not independent external validation.

Self-review: passed. Independent audit: not yet performed.
