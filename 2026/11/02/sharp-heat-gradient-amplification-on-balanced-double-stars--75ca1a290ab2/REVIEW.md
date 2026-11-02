# Scientific review: balanced double-star heat-gradient amplification

## Correctness — PASS

The claim is supported by a complete linear-algebraic proof on independent tree-edge gradients, not finite extrapolation. The heat-gradient generator separates into a scalar mode and a positive two-dimensional system whose characteristic polynomial is \(z^2-(m+3)z+2\). A positive Green-kernel convolution proves that every leaf-edge row has strictly smaller absolute row sum than the hub-edge row for every \(m\ge1\), \(t>0\). The positive and negative hub-row coefficients yield the precise norm and the full equality classification. Direct differentiation proves the one-peak law for \(m\ge2\); a coefficient inequality plus an explicit time scaling proves that three is a sharp but unattained family-wide bound. The standard-library checker reproduces 81 independent finite heat-row/Wasserstein comparisons and degree-eight exact coefficient identities; these corroborate, rather than establish, the all-parameter theorem.

## Originality — PASS, qualified

The nearest inspected research is Ollivier (arXiv:math/0701886, metric-Markov transport contraction), Lu--Liu (arXiv:1205.6027, spectral determination of double-starlike trees), Frank--Kovařík (arXiv:1108.6145, differential heat kernels on metric trees), and Münch--Wojciechowski (arXiv:1712.00875, curvature/Lipschitz exponential estimates). The first and last supply general principles; the spectral result identifies graph invariants but not the full semigroup norm; the metric-tree work uses a different operator and domain. None of the inspected relevant statements gives the exact two-exponential envelope, rigid maximizing slope pattern, or asymptotic amplification of three. The closest accessible earlier claims treat graph edge-total variation or different graph families; those do not imply this all-time graph-Lipschitz result. Search noncoverage is not proof of absolute novelty; an unindexed equivalent computation remains the concrete priority risk.

## Mathematical value — PASS

A balanced double star is the first natural symmetric tree beyond a single star with two branching hubs; it already has diameter three. The result gives a complete sharp continuum-in-time stability law on an infinite family, identifies the precise threshold between contraction and transient amplification, and proves asymptotic saturation of the trivial diameter-three transport ceiling. The maximizing potential is rigid at every positive time. These statements describe how cooperative branching affects heat transport and cannot be replaced by a routine fixed-time numerical evaluation or a generic curvature bound.

## Scope and residual risks

The unit-conductance, counting-measure combinatorial model and balanced leaf counts are essential. No conclusion is claimed for unequal double stars or metric-tree differential operators. An independent scientific assessment and fully exhaustive publication-priority search remain outstanding.

Self-review: passed. Independent audit: not yet performed.
