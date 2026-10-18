# Scientific review

## Correctness — PASS

The closed-loop variance is the convergent scalar Lyapunov solution. Twice differentiating the rational stage-cost gives the exact directional Hessian identity. Completing a positive quadratic square and applying Cauchy–Schwarz gives the pointwise bound \(D^2J[v,v]\ge 2v^\mathsf TRv/(1+3y^2)\); its infimum on the stable pole interval is one half of the input quadratic form. Positive aggregation, compact interior sublevel sets, existence, uniqueness, and the Polyak–Łojasiewicz consequence follow with the stated hypotheses. The displayed explicit family, with positive state cost tending to zero, shows universal sharpness. The packaged program checks critical algebraic identities and finite matrix instances, but is not a replacement for the proof.

## Originality — PASS, with residual risks

The September 2026 domain-randomized LQR policy-iteration paper assumes gradient dominance for its linear-rate theorem; the March 2025 gradient paper uses heterogeneity restrictions. Neither states the native stationary-cost global strong-convexity matrix modulus for scalar states with arbitrarily many distinct plants and arbitrarily many actuators. The related 2026 semidefinite formulation uses a lifted iterative relaxation; the 2026 scalar ReLU LQR paper establishes strong convexity of a Bellman improvement surrogate and obtains a PL property in a different controller model, not the present uniform Hessian claim for a domain-randomized stationary objective. The closest matched mathematical objects and stronger-coverage possibilities were examined in the primary texts and publication database. Undetected equivalent consequences of classical quadratic-over-linear identities or older scalar-LQR analysis remain possible, despite the negative targeted comparisons; independent literature review is not claimed.

## Mathematical value — PASS

The result resolves a concrete gap: when one feedback law stabilizes many heterogeneous scalar-state systems, the sample-average control cost has a globally well-conditioned convex landscape even though the source's general-state convergence theory assumes gradient dominance or bounds plant heterogeneity. The coefficient is explicit, depends only on weighted input penalties, and is provably sharp over the natural problem class, so it supplies a reusable a-priori gradient-domination and policy-optimization benchmark rather than a merely numerical or renamed special case. One state dimension and exact linear feedback remain essential restrictions.

Self-review: passed. Independent audit: not yet performed.
