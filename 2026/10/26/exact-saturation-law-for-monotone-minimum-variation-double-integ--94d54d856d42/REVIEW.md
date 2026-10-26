# Review

**Correctness — PASS.** The endpoint conditions reduce to two exact moments. The feasibility threshold follows from maximizing the first moment under a box cap; the monotone minimum-TV bound follows from a nonnegative derivative measure, the identity \(\int s(1-s)\,d\mu=1\), and Cauchy–Schwarz. Both step controls attain the stated bounds and satisfy the moments exactly.

**Originality — PASS, with residual risk.** The closest primary source is Kaya's unbounded double-integrator TV problem. The capped formula below \(U=3\) is not stated there. Searches for bounded-control variants did not find the same formula. Related switching-cost and bounded-variation literature may contain adjacent results; the theorem is limited to monotone controls and is not a claim of priority over all such literature.

**Value — PASS.** The exact feasibility cutoff \(U=1+\sqrt2\) and the cap-dependent TV law quantify how actuator saturation changes a standard minimum-variation benchmark. This is useful for testing capped-control solvers and for distinguishing the unconstrained midpoint step from the saturated regime.

Closest literature: C. Y. Kaya, “Optimal Control of the Double Integrator with Minimum Total Variation,” https://arxiv.org/abs/1901.00491; P. Manns and A. Schiemann, “On Integer Optimal Control with Total Variation Regularization on Multi-dimensional Domains,” https://arxiv.org/abs/2212.12226. The latter studies a different, integer-valued multidimensional control class.

Limitations: minimum-TV optimality is proved only among nondecreasing controls. The work does not establish that nonmonotone controls cannot do better, and it does not analyze energy-plus-TV scalarization.

Self-review: passed. Independent audit: not yet performed.
