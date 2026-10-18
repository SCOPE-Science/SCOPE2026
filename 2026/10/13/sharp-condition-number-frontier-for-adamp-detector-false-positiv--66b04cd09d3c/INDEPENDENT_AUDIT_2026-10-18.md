# Independent mathematical audit

## correctness

PASS

For H SPD with spectrum [mu,L], w!=0, min cos(w,Hw)=2sqrt(mu L)/(mu+L) follows from weighted eigenvalue moments m=sum p_i lambda_i and lambda_i^2<=(mu+L)lambda_i-mu L; optimization over m yields the sharp value attained by a two-eigenvector mixture. With detector cos<delta/sqrt(d), 0<delta<sqrt d, solving the strict equality gives kappa*=((sqrt(d)+sqrt(d-delta^2))/delta)^2. All w are safe exactly when kappa<=kappa*, while for larger kappa an open cone of SPD-quadratic false-positive states exists. The d=1 case is automatically kappa=1. Independent numerical spectral and symbolic diagnostics confirmed values and threshold, not an optimizer trajectory theorem.

## originality

PASS

Kantorovich's matrix angle or first antieigenvalue inequality already gives the extremal SPD cosine and 2-eigenvector equality, so neither this inequality nor its witness is new. Heo et al's AdamP defines a strict dimension-normalized cosine gate and tests it empirically for scale invariance, but the inspected public source does not state the precise SPD condition-number activation frontier with source default delta=.1 or the false-positive diagnostic. Related published SCOPE LAMB/LARS conditioning frontiers involve different update rules. The novelty claim is limited to this concrete AdamP gate interpretation and exact all-state frontier; priority remains vulnerable to unindexed optimizer-diagnostic discussions.

## value

PASS

Whether a scale-invariance detector triggers on a strictly scale-variant, strongly convex objective is a concrete interpretability gap for the method. The exact kappa* boundary certifies when curvature alone cannot spoof it, and explicit open cones show when it can; it supplies a testable, dimension-resolved guarantee (about 400d at delta=.1), not just renaming the underlying classical inequality. No claim of degraded final training performance is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
