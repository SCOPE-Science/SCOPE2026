# Self-review

## Correctness — PASS

For each degree from one through five, the predictor is precisely the truncated exponential polynomial of the planar rotation generator. The explicit Runge–Kutta stage chain realizes this polynomial because its weights telescope; its first two stage derivatives span the plane for degrees at least two. The positive radial correction is therefore the quasi-orthogonal energy projection and preserves the quadratic invariant. The five phase-derivative identities are proved by exact differentiation. A positive cubic controls degrees up to four, and the quartic \(x^4-16x^3+2880\) has exactly two positive zeros, determined by strict monotonicity and exact rational sign brackets. Its corresponding angular turning points straddle \(\pi/2\). The three monotonic branches rigorously imply precisely three finite positive steps realizing each angle in the stated interval. Nonvanishing of all five predictor polynomials is separately established. An independent stage-level numerical implementation and exact-symbolic script passed 754 consistency assertions; finite experiments are supplementary, not infinite proofs.

## Originality — PASS, conditional on the material examined

Najafian and Vermeire (arXiv:2409.18328v1) establish the stage-span energy projection, not the global inverse-multiplicity classification for a degree-five Taylor oscillator. Earlier numerical-dispersion work by Chen (2012) and van der Houwen and Sommeijer (1987) addresses phase-lag and amplitude-fitting techniques, not the particular complete three-to-one classification in material inspected. The most pertinent possible coverage is Calvo, Laburta, Montijano and Rández, *Runge–Kutta projection methods with low dispersion and dissipation errors* (2015), DOI 10.1007/s10444-014-9355-2; only its abstract was accessible, and the full-text comparison remains unresolved. Mathematical-record queries for the degree-five normalized Taylor phase reversal, exact quartic turning equation, energy projection, and oscillator aliasing identified no covering published summary, but such negative searches alone do not establish novelty. Related studies of anisotropic explicit-midpoint energy projection and two-frequency RK4 modal selection do not imply the step-size aliasing theorem here. The risk that a less readily accessible phase-analysis result already contains this special case is genuine; independent priority verification is still required.

## Value — PASS

A projected integrator can preserve energy exactly for every finite step yet assign the *same numerical rotation to three unequal physical step sizes*. This sharp, global loss of time-step identifiability is not visible in energy drift or local order. The complete multiplicity classification and the minimal-degree boundary help interpret phase errors and phase-based step-size selection in geometric numerical integration. The result is limited to a simple, transparent planar test problem, but the structural failure mode itself is a motivated benchmark rather than a routine substitution or an unmotivated numerical constant.

## Boundaries and literature risk

Only the canonical linear oscillator, positive steps, specified stage-chain stability polynomials, positive radial projection, and exact arithmetic are treated. Standard phase-fitting, stage-span projection, and the Taylor polynomial are all established tools and are not claimed as original. The unresolved full-text comparison with the 2015 paper is a material originality risk, not evidence of coverage or noncoverage. Independent scientific audit and publication-priority review have not been performed.

Self-review: passed. Independent audit: not yet performed.
