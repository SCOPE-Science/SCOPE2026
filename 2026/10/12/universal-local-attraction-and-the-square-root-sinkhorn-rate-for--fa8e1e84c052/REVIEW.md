# Scientific assessment

## Correctness — PASS

The proof fixes the projective gauge, computes the exact logarithmic Sinkhorn Jacobian, shows it is weighted-self-adjoint and positive semidefinite, proves strict separation of the nontrivial spectrum by positivity, and derives the two-step modal characteristic polynomial. Its complex roots have modulus equal to the second singular value of the normalized balanced coupling; a standard derivative-norm argument supplies local exponential attraction. The matrix reconstruction and an explicit nonvanishing derivative show that the same rate is sharp for the physical coupling output. A standalone rational checker confirms recurrence identities and spectral exemplars; no finite experiment is treated as an infinite proof.

## Originality — PASS, with specified uncertainty

The September 2026 counterexample paper gives nonconvergent global BDRS trajectories but no local spectral theorem. Ma's May 2026 theorem uses a restrictive projective-diameter assumption to obtain global convergence and analyzes a *positive error envelope*, not the actual local Jacobian. Lehmann and collaborators compute the distinct ordinary and overrelaxed Sinkhorn Jacobians. Liang, Fadili and Peyré analyze Euclidean primal–dual/Douglas–Rachford splitting, not this entropy-Bregman matrix-scaling recurrence. These statements do not imply the unrestricted local BDRS rate without new reduction and stability arguments. The September 2026 *Annealed Sinkhorn with Momentum* manuscript was identified but its complete text was inaccessible: the coincidence of its formulation with the BDRS momentum update creates a meaningful residual risk of an equivalent unpublished-in-the-inspected-text local result. Unindexed prior analyses remain possible.

## Value — PASS

The result resolves a natural local-versus-global distinction left by an explicit strictly positive counterexample: fixed points have a rigorous attracting neighborhood although some distant initializations cycle. It supplies an exact conditioning-sensitive rate and a sharp negative acceleration comparison with ordinary Sinkhorn, valid without the earlier cross-ratio restriction. The two-by-two family exhibits arbitrarily slow local convergence. This is a structural algorithm-dynamics statement rather than a test-only computation or a restatement of existing sufficient global conditions.

## Scientific limits

No global attraction, numerical robustness, explicit basin radius or improvement in iteration complexity from arbitrary starts is claimed. The unresolved related preprint could narrow the novelty assessment; independent review remains necessary.

Self-review: passed. Independent audit: not yet performed.
