# Scientific review

## Correctness

**PASS.** The exact feasible line-search formula follows from the source algorithm. A strictly interior minimizer ensures the step-size bounds are inactive locally. The derivative is a rank-one metric-orthogonal projector, and its threefold product has the stated trace, norm, and nilpotency identities. Nonparallel vertex rays exclude two simultaneous orthogonal pairs. Taylor expansion of the analytic sweep yields one- or two-sweep quadratic convergence; the metric-circle condition follows from a quadratic identity and convexity of the corresponding disk. The concrete coefficient identities and 1840 exact checks are reproducible with `verify.py`. Finite checks do not establish the general theorem, which is separately proved in `RESULT.md`.

## Originality

**PASS, qualified.** Algorithm 2 and Theorem 3.2 of Mazumder–Wang, arXiv:2303.07642, provide the algorithm and a global linear rate, not the complete local metric-circle and sweep-order classification here. Klopfenstein et al., arXiv:2010.11825, address separable prox-linear coordinate descent. Beck–Pauwels–Sabach, arXiv:1502.03716, analyze a different cyclic block conditional gradient method. The projector multiplication identities themselves are elementary and not claimed as new. Specialized projection and optimization literature may contain an unrecognized stronger formulation; independent publication-priority assessment remains necessary.

## Value

**PASS.** The exact geometric locus and complete order classification explain a qualitative local rate transition for an established algorithm. They show why moving one vertex in the schedule can change an entire sweep from first-order to second-order error, or move the quadratic cancellation to pairs of sweeps, despite the same vanishing eigenvalue of the linearization. A rational example separates the effect from ordinary forward-only PolyCD. These statements do not assert global or generic superlinear convergence.

Self-review: passed. Independent audit: not yet performed.
