# Scientific review

## Correctness

The claim is restricted to SPD matrices with two eigenvalues, an exact one-dimensional normal-equations least-squares correction, and a single specified Richardson step. The derived error-propagation matrices are rank one; their Euclidean norm formulas follow from the single nonzero singular value. The elementary identity \((c^2+\kappa^2s^2)^2-s^2(\kappa^4s^2+c^2)=c^2[1+2(\kappa^2-1)s^2]\) gives the exact presmoothing bound; a one-variable derivative gives the post-smoothing extremum, and negativity of the cubic through 2 and strict monotonicity thereafter gives the unique nonexpansivity threshold. The rank-one matrix identity provides the all-integer power law. The code independently evaluates all matrices and tests 1,510 cases. Algebra, not numerical extrapolation, establishes the infinite and global assertions.

## Originality

Relevant public mathematical records and primary literature were compared by mathematical implication. Adler–He–Hu–Lefebvre establish the two-grid interpretation and the residual-minimal coarse correction formulas, and He establishes Richardson/NGMRES equivalences and monotonicity relationships. Neither inspected material states the exact maximization over every coarse line, its cubic Euclidean safety frontier, or the matching fixed-line finite-power law. Classical two-grid and oblique projection theory is acknowledged, not claimed as new. The motivating paper's later sections were not retrievable for complete inspection, so independent bibliographic overlap assessment remains important; this is not a proof of uniqueness.

## Value

There is a natural stability decision: whether to smooth before or after the same normal-equations least-squares coarse correction. The exact dimension-two classification shows that a strictly contracting base smoother and asymptotically stable two-grid propagator can still permit strict Euclidean error amplification when smoothing follows correction, whereas the opposite order is safe for every coarse line. The sharp condition-number cutoff and unbounded \(\kappa/2\) scaling quantify a concrete finite-horizon risk not captured by spectral-radius estimates. The two-dimensional setting and fixed coarse space are explicit limits, not arbitrary parameter slices.

## Closest literature and limitations

The nearest work is arXiv:2609.13091 (first public 2026-09-11), whose accessible initial sections supplied exact two-grid and normal-equation definitions. arXiv:2603.25983 studies preconditioned Richardson/NGMRES relations, and classical multigrid results address other norms and operators. Later sections and any unavailable appendices of the motivating preprint were not materially inspected. The claim does not cover adaptive changing coarse spaces or arbitrary nonlinear acceleration schemes.

Self-review: passed. Independent audit: not yet performed.
