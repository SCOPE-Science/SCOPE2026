# Independent mathematical audit

## correctness

PASS

I reconstructed the correction by projecting the residual orthogonally off Ap. Let u be a unit vector orthogonal to Ap, so C_p=A^(-1) u u^T A and all unit directions u occur. Set d=1-1/k and t=u_1^2. The pre-order norm is d |u_1| ||A^(-1)u||<=d, attained at t=1. The post-order squared norm is d^2 t[k^2-(k^2-1)t], a concave quadratic with optimizer t=min(1,k^2/[2(k^2-1)]). This proves both sharp envelopes including the transition at sqrt(2). Above sqrt(2), max squared norm minus one equals (k^3-k^2-4k-4)/(4(k+1)). The cubic is negative up through 2 for k>1, strictly increasing thereafter, and has a root between 2 and 3 (2.875129794162778826...). For k=3, p=(sqrt(7),1) gives the optimizer and post norm 3 sqrt(2)/4. Both rank-at-most-one products have trace dt and obey T^2=(dt)T, proving the power law. At t=0 both matrices are zero: the finding's phrase 'common nonzero eigenvalue' should be read as 'common trace, the only potentially nonzero eigenvalue'; the formula includes zero. Both orders are contractions in the residual norm because their A-conjugates replace C_p by an orthogonal projection. Thus the effect is genuinely Euclidean solution-error amplification, not divergence, residual growth or a claim about adaptive history spaces. The exact argument does not rely on the package's floating-point grid.

## originality

PASS

The residual-minimal correction and the two product orderings are prior art. The supported distinct claim is their contrasting sharp worst-case Euclidean error norms over all fixed coarse lines with the endpoint Richardson step, including the cubic all-line stability threshold. Neither general projector obliquity nor prior residual monotonicity is equivalent to this directional rank-one product optimization. The rank-one power identity itself is standard and is not credited as a separate novelty.

## value

PASS

There is a real order decision even for the same coarse line and the same strictly contracting smoother. The exact all-line envelope identifies when smoothing last can cause transient solution-error growth, quantifies its unbounded size with conditioning, and sharply separates it from asymptotic convergence and residual contraction. The calculation is short, but the arbitrary-line worst-case threshold provides a useful fixed-space benchmark rather than a routine application of a general norm bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
