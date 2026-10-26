# Scientific review

## Correctness — PASS

The backward Robin problem follows from diffusion with boundary-local-time killing. The linear boundary system gives the exact first-passage mean; differentiation produces a quadratic numerator whose derivative is strictly positive across the entire feasible interval, and whose endpoint signs are opposite. This proves a unique **interior** global optimizer for all positive physical parameters and all starts, including endpoints. A separate implicit equation proves the monotonic switching of the allocation fraction. At strong reactivity the optimized asymptotic is derived from a uniform-in-fixed-parameter expansion for interior starts and an exact separate endpoint root. The included independent tridiagonal solver and numerical optimizer support the algebra. No finite experiment substitutes for the analytic argument.

## Originality — PASS, qualified by residual literature risk

The nearest primary materials were compared by their mathematical implications, not title similarity. Erban–Chapman derives and calibrates reactive boundaries without this fixed-budget capture-time allocation. Whitehouse–Evans–Majumdar optimizes resetting in a different forward first-passage model. Nicolaou–Mulder optimizes exterior steady diffusion flux into a partially reactive body; that objective does not determine the mean capture time in a bounded interval (where eventual capture is certain). No equivalent complete theorem or stronger implication was found in the queried mathematical records or accessible prior literature. The unexamined tails of specialized design literature remain a genuine risk; search absence is not a proof of originality.

## Mathematical value — PASS

The result addresses a natural resource-constraint question: distribute a fixed total reaction rate between two physically separate capture channels to minimize time to capture. It gives a complete optimizer, exact nontrivial weak/strong budget laws, and strict allocation monotonicity. The endpoint-start phenomenon is especially informative: the remote endpoint always receives a positive allocation; for a large budget its allocation grows like the square root of the total even though the allocated *fraction* vanishes. This is a structural, testable design principle, not just a forward mean calculation.

## Boundaries and residual risks

Point-mass start; one-dimensional constant diffusion; two Robin endpoints; fixed sum of reactivities; no noisy-inference or higher-dimensional claim. The relevant exterior reactivity optimization paper was assessed using accessible substantive text, not a claimed complete full-text reading. Equivalence under a different chemical engineering parametrization cannot be ruled out without a wider priority audit.

Self-review: passed. Independent audit: not yet performed.
