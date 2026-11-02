# Scientific review

## Correctness
**PASS.** The proof treats all real starting points, including the switching boundary, and separately checks all sign branches. The exact identity \(F^2(u,0)=((ab-d)u,0)\) for \(u>0\), together with the negative-axis three-step return and the right-side two-step entrance to the axis, establishes both the global five-iterate upper bound and the off-resonance obstruction. An open region of initial conditions has a nonzero fourth iterate, proving sharpness. Standalone symbolic and rational checks reproduce the cancellation and 11,817 regressions; those computations are supplementary, not an exhaustive proof for continuum parameters.

## Originality
**PASS on inspected evidence.** The source map appears in Simpson's 2024 study [1], where the zero-forcing case is explicitly excluded in §4.1. The scalar resonance factor also occurs in the source's known \(LR\)-monodromy trace, and is credited rather than presented as a discovery. The new statement requires a global quantification over all initial conditions, a sharp five-step bound, and the off-resonance necessity proof. Simpson's 2016 general asymptotic-stability analysis [2] does not assert the exact finite-time classification; the published homogeneous max-plus result [3] applies to a disjoint trace sector and left matrix. Searches for equivalent finite-time nilpotence, sign-reversed conjugacies and stronger prior normal-form coverage yielded no directly dominating result. Remaining risk: an earlier result in switched-system or border-collision literature may contain an equivalent cancellation criterion despite using other notation.

## Value
**PASS.** The question is the natural finite-time counterpart of the documented difficult zero-forcing fixed-point stability problem [1, §4.1], not an arbitrary parameter sample. The theorem provides a complete iff locus within a two-negative-trace quadrant, a parameter-independent sharp annihilation index, and a contrasting explicit persistent orbit for every parameter off that locus. Exact uniform extinction survives arbitrarily large one-sided determinants, so the phenomenon is not captured by ordinary one-branch spectral contraction arguments. This is an exact structural boundary, not a marginal numerical improvement.

## Scope and residual limitations
The classification is for exact zero forcing and \(a,b,d>0\), not arbitrary traces, nonzero input, or perturbations. The result does not assert what persistent orbits do asymptotically, and its publication priority is not independently settled. No claim of an independent external scientific audit is made.

## Prior work
[1] D. J. W. Simpson, arXiv:2408.04790v1 (2024), §§1, 4.1, 5.3.
[2] D. J. W. Simpson, arXiv:1612.02932v1 (2016), §§1, 6.
[3] *Sharp extinction and persistence at the homogeneous max-plus border collision* (2026), public mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-extinction-and-persistence-at-the-homogeneous-max-plus-bor--a2b1d9a86864.

Self-review: passed. Independent audit: not yet performed.
