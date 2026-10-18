# Mathematical review

## Correctness — PASS

For the exact Alsedà–Misiurewicz piecewise-affine maps, the negative stationary exponent is independently recomputed from the uniform graph marginal: \(\lambda=(1-c)\log a+c\log b<0\). The critical nonstandard step is not to assume that Lyapunov linearization automatically controls finite gaps. Instead, breakpoint separation follows from the summable bound \(\mathbb P(d_n<e^{-\eta n})\le2e^{-\eta n}\) and the ergodic asymptotic \(D_n=e^{(\lambda+o(1))n}\), giving a positive random radius for which the entire future orbit is **exactly affine**. Recurrence of positive-radius shifts and the published all-interior qualitative synchronization then bring every interior initial point into such a radius. This is a common probability-one event, not merely an event separately chosen for each pair. Monotonicity ensures the multiplicative coefficient is positive. The proof also explicitly excludes boundary points and \(c=1/2\). The finite exact-arithmetic checker returned `VERIFY_OK`; infinite-time justification is analytical.

## Originality — PASS

Theorem 5.10 of Alsedà–Misiurewicz (arXiv:1212.4440v1) establishes simultaneous qualitative coalescence; their Section 6 gives the stationary exponent. Neither alone supplies that **every nonzero finite distance** eventually evolves by exactly the stationary derivative product, or that its logarithmic rate always equals that exponent. Malicet (arXiv:1412.8618v1) establishes broad local exponential contraction, so generic exponential decay is known and is not claimed as new. Its conclusions do not identify an exact model-specific exponent or eventual equality of affine branch histories. Gharaei–Homburg's C¹/C² setting and Czudek's C² annealed theory differ in scope; Barański–Śpiewak addresses stationary-measure regularity. Targeted literature and mathematical-result searches, plus available historical claim titles/statements, yielded no equivalent or stronger theorem. Priority remains subject to unindexed derivations.

## Mathematical value — PASS

The 2012 paper explicitly left the exponential nature of its contraction uncertain. A general exponential result became available later, but the **sharp value** for arbitrary pairs and the eventual exact co-branching mechanism still resolve a concrete quantitative problem for this benchmark nonsmooth random dynamical system. The result distinguishes a stationary infinitesimal Lyapunov exponent from an exact finite-separation exponent, and it explains how trajectories avoid moving kinks by a summable tail argument. This is a structural pathwise theorem for a natural one-parameter family, not a numerical experiment or a parameter substitution.

## Closest literature, scope, and residual risk

Closest are Alsedà–Misiurewicz [2012, arXiv:1212.4440v1], Malicet [2014, arXiv:1412.8618v1], Gharaei–Homburg [2016, arXiv:1611.07248v1], Barański–Śpiewak [2019, arXiv:1905.11048v1], and Czudek [2025, arXiv:2504.16549]. The evidence does not establish absolute novelty against every unindexed work. There is no uniform random entrance time over all interior starts, no control of the two fixed endpoints, and no asserted annealed contraction rate.

Self-review: passed. Independent audit: not yet performed.
