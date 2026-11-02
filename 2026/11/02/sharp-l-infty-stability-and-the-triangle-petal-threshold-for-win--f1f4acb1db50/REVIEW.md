# Scientific review: metric-windmill spline projection

## Correctness
PASS. The proof defines the metric graph and nodal projection precisely; the element mass matrix is independently derived as \(6G=2D+A\). Inverting the block matrix gives the exact five types of kernel endpoint values. Their signs hold throughout the integer domain. The six-term endpoint sum counts every edge exactly once and an explicit sign-of-kernel input attains the bound. Two multivariate polynomial identities with strictly positive factored coefficients prove, without extrapolation, hub-versus-petal dominance and the \(s\ge3\) strict upper bound. The triangular-petal formula, cubic threshold, derivative and limit are exact. The verifier independently reconstructs full Gram inverses and passes 12,460 exact-rational assertions. The general theorem is proved algebraically, not merely sampled.

## Originality
PASS, qualified by ordinary priority uncertainty. The closest inspected primary sources are Kayumov (2004, arXiv:math/0408418), on interval \(L\)-spline projectors; Oswald (2006, arXiv:math/0611573), on unbounded projection norms on planar triangulations; and Arioli–Benzi (2017, DOI 10.1093/imanum/drx029), on finite-element mass matrices for metric-graph PDEs. None contains a windmill vertex-kernel formula or the triangular-clique cutoff. Also compared were exact projections on other graph families and finite-metric Banach spaces, whose spaces and operators differ. A possibly unindexed windmill or graph-FEM calculation remains a residual risk; absence from searches is not proof of novelty.

## Mathematical value
PASS. Complete cliques sharing a single vertex are a natural branched discretization with no leaves. The theorem exhibits a structurally sharp phenomenon: adding nine or more triangular petals forces norm above two, while increasing every petal to size four or more preserves strict sub-two stability for arbitrarily many petals. It gives an exact all-parameter stability classification, identifies where norm is attained, and determines the sharp global ceiling \(458/225\). These are natural robustness properties of graph spline approximation, not arbitrary isolated measurements.

## Limitations
The topology, edge length, density and one-element-per-edge spline order are essential hypotheses. Nothing is asserted for unequal clique orders or lengths, variable density, higher-degree splines, or independent external validation.

Self-review: passed. Independent audit: not yet performed.
