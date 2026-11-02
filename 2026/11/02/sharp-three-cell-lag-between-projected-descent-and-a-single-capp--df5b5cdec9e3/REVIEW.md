# Scientific review: sharp three-cell flow/projection lag

## Correctness — PASS

The exact trajectories are reconstructed from the tangent-cone projection of a constant linear gradient and from the capped-simplex projection KKT system, respectively. The first stage has velocity \((H/2,0,-H/2)\). After the third component reaches zero, continuous descent releases the second component with velocity \((a/2,-a/2,0)\), while the global one-shot projection remains pinned until \(b/a\). Their scalar ramp representation makes the displayed max-norm discrepancy and its family-optimal \(1/3\) envelope exact. The two-cell feasible set is an interval, proving equality in lower dimensions. The standalone exact-rational checker passed 7,307 comparisons, including separate two-cell cases. The numerical tests corroborate but do not replace the analytic proof. Boundary assumptions are strict; the one-third envelope is a supremum, not a maximum.

## Originality — PASS, with residual priority risk

The recent primary work, Langlois–Onwunta–Darbon, arXiv:2610.30300v1, sections 2.2–2.4, 4.3, 6.1, and conclusion, constructs exact piecewise minimal-selection trajectories and applies them to mass-conserving limiters. Its general algorithm computes trajectories for linear objectives, but does not state the quantified comparison with a single projection of the accumulated drift, three-cell sharp onset, \(1/3\) family envelope, or unbounded release ratio. Wang–Lu, arXiv:1503.01002, sections 1–3, supplies capped-simplex projection KKT conditions but no projected-flow time path. A 2024 overview of projected gradient flows defines the infinitesimal projected iteration and tangent cone, not this one-shot path comparison. Mathematical-record searches for the equivalent formulations and active-set latency returned different simplex projection sensitivity and optimization dynamics questions, not this claim. An older sweeping-process or projection-semigroup theorem might still dominate the finding; this risk is explicitly retained.

## Mathematical value — PASS

The result is a natural structural benchmark for using a one-shot bounded, mass-conserving Euclidean projection as a surrogate for a continuous projected linear optimization path. It identifies the smallest cell count where this surrogate fails, the exact worst family error, and an arbitrarily large delay in releasing a saturated cell. It distinguishes one-shot cumulative projection from the small-step projected iteration and can inform interpretation of active-set timing in conservative box-constraint algorithms. It does not assert failure of an actual PDE integrator, the source's limiter, or any general polyhedral upper bound.

## Closest literature and limitations

- Langlois, Onwunta and Darbon, *Continuous-time analysis and algorithms for linear and convex quadratic programs via exactly solvable differential inclusions*, arXiv:2610.30300v1, https://arxiv.org/html/2610.30300v1 (full relevant sections inspected).
- Wang and Lu, *Projection onto the capped simplex*, arXiv:1503.01002, https://arxiv.org/abs/1503.01002 (projection and KKT text inspected).
- *Optimization algorithms as robust feedback controllers* (2024), DOI:10.1016/j.arcontrol.2024.100941 (projected-gradient-flow discussion inspected).

The optimum of \(1/3\) is specific to the exhibited family. General coverage by older projection-semigroup theory is not excluded. Independent mathematical verification is still outstanding.

Self-review: passed. Independent audit: not yet performed.
