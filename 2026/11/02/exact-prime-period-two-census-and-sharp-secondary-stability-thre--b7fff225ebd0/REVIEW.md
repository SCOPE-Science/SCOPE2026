# Scientific review: exact prime-period-two census for a rational kinetic map

## Correctness

**PASS.** For every \(h>0\) and real \(x\), the positive-denominator factorization of \(T_h^2(x)-x\) reduces all possible periods dividing two to the fixed point, a symmetric quadratic factor, and the reciprocal-radius quartic. The positive solutions of the last factor exist precisely at \(h\ge4\), with coalescence at the boundary, yielding an exhaustive cycle count. The derivative formulas establish \((3-8/h)^2\) for the symmetric multiplier and \(9-2h\) for each asymmetric multiplier, with strict attraction precisely on the stated open parameter ranges. A standalone standard-library program checks the global polynomial identity and five diagnostic orbit substitutions. The proof, not the samples, establishes the quantified assertions.

## Originality

**PASS on inspected evidence, not a certification of global novelty.** Itin (arXiv:2610.27321v1, sections 2.2 and 3, Appendix A) establishes the symmetric branch and its \(2<h<4\) stability window and explicitly mentions asymmetric branches for \(h>4\), but does not present the full real period-two classification, asymmetric amplitudes, exact \(9-2h\) multiplier, or sharp secondary threshold \(h=5\). Ma et al. (arXiv:2204.11326, Theorem 1) require globally strictly decreasing curvature for their almost-everywhere convergence theorem; this requirement fails for the logarithmic potential associated with the rational speed. Yuan–Wen's clipped gradient maps and the original VRAdam optimizer analysis do not directly imply the claimed explicit branches. Generic period-doubling and pitchfork principles are acknowledged rather than claimed. Searches of published mathematical findings and the relevant recent-map literature found nearby but different models, including Duffing and Rulkov exact two-cycle classifications; no match with the current rational map was identified. Inaccessible or unindexed historical results remain a priority risk.

## Mathematical value

**PASS.** The motivating paper reports a change from stable symmetric oscillation to asymmetric cycles, period doubling and chaotic behavior but does not provide a complete exact diagram of prime-two orbits. The census proves there are precisely two additional and no other prime-two cycles after the symmetry-breaking threshold, identifies their amplitudes exactly, and gives a rigorous secondary loss-of-linear-stability point \(h=5\). That finite complete classification answers the natural dynamical question raised by the paper's numerical exploration and separates linear stability of the new branches from the previously analyzed symmetric branch.

## Limitations and closest literature

The result does not identify period-four cycles or chaotic attractors, establish basin boundaries, or classify nonlinear stability at the nonhyperbolic points \(h=4\) and \(h=5\). The rational reduction excludes moment memory and floor-clipping. The nearest source is Itin's 2026 analysis, which retains priority for the symmetric branch and the existence of asymmetric behavior. Broader priority against all possible historical rational-map literature has not been independently established.

Self-review: passed. Independent audit: not yet performed.
