# Scientific assessment

## Correctness — PASS

The edge reduction follows from Kantorovich duality and edge-geodesic constraints. The transport norm formula holds by independent optimization of two equilateral-clique potentials and one bridge difference. Explicit invariant subspaces of the Markov generator prove the bridge-edge formula and the two strict inequalities against every other edge type, with positive coefficients for every positive time. The derivative of the two-exponential expression crosses zero exactly once. Taylor expansions give the stated peak and limiting transport bound. The standalone program independently checks graph distances, matrix exponentials, optimal-transport linear programs, orbit ordering, and asymptotic values, but cannot certify the all-time theorem on its own.

## Originality — PASS, qualified

Münch–Wojciechowski (arXiv:1712.00875v1) prove broad transport/curvature and heat-flow equivalences rather than an exact time-dependent optimal coefficient on bridge-barbell graphs. Cheng–Li–Wu (arXiv:1907.11036v1) derive graph Markov exponential convergence criteria, not the sharp all-time bridge-barbell formula. Banerjee et al. (arXiv:2208.03471v1) analyze one-step Markov contraction, not this continuous-time semigroup family. The closest visible barbell-specific database record concerns zero forcing, a distinct invariant. A prior equivalent statement under an alternate operator-norm formulation or in an unindexed source remains possible.

## Mathematical value — PASS

A single graph bottleneck between two dense communities creates large transient Wasserstein amplification despite ergodicity of the continuous-time walk. The theorem exactly identifies the worst edge and the unique amplification peak for a whole natural graph family, with the maximal amplification tending to the universal diameter bound three and an explicit logarithmic peak-time law. This provides a sharp stress test for curvature-based exponential estimates and transport stability, not a routine restatement of a convergence bound.

## Scope and limitations

The two complete graphs have equal size at least three. Every graph edge is unit length and has symmetric jump rate one; the generator is the unnormalized Laplacian. The checker performs finite tests and not independent mathematical validation. Historical-priority risk remains from other terminology or sources outside inspected literature.

Self-review: passed. Independent audit: not yet performed.
