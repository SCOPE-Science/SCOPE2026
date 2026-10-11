# Scientific review — universal two-term finite-time escape

## Correctness — PASS

The proof is independent of computational sampling. Orient the escape direction by the leading coefficient, build a barrier \(v>Kz^{m+1}\), and show the normal component of the vector field points into that open wedge. Strict growth \(\dot z\ge Kz^{m+1}\) forces finite forward maximal time. Gronwall's inequality excludes divergence of velocity while the position remains bounded. The exact relation \(dv/dz=b(sz)-z^{2n-1}/v\) yields the two-term velocity expansion; reciprocal integration in physical time and algebraic inversion yield the finite-time coefficients. The restoring force enters the \(z^{m-1}\) velocity correction exactly at \(m=n\). The standalone checker validates representative rational coefficient balances only; it is not an infinite-degree proof.

## Originality — PASS, with disclosed priority risk

García–Llibre (2022 online) studies the same normalized nilpotent Liénard family but establishes global-center/non-global-center information. Chen–Li–Zhang (arXiv:2208.06184) and Han–Kong–Yu (2026, Theorem 3.5) provide broader qualitative classifications; the earlier global-center conjecture is already solved and is explicitly **not** claimed here. Matsue's Section 4.8 Liénard example is at a different restoring-to-damping-degree equality and deals with periodic blow-up; Bluman and collaborators treat a narrower linear-damping cubic oscillator. Comparisons covered physical-time statements, scalar-coordinate aliases, degree reductions and implications rather than word matching. The original Dumortier–Herssens (1999) near-infinity paper was identifiable but its entire text could not be inspected; it is a genuine remaining originality risk, as is other unindexed prior work.

## Mathematical value — PASS

The open wedge determines a whole positive-measure family of exploding trajectories in a system already known to have subtle local versus global center geometry. Beyond deciding whether motion is unbounded, the theorem separates finite from infinite forward escape time and computes a universal, initial-condition-independent two-term observable. The equality of damping degree and nilpotency index is a natural structural boundary where the restoring force first affects the correction, rather than an arbitrary specialized example.

## Scope and limitations

Only the stated forward escape wedge is covered; no claim is made for all nonperiodic trajectories, for full phase portraits, or for uniformity in initial data. The error terms are orbitwise. Absolute publication priority and independent verification remain open.

Same-model review: passed. Independent audit: not yet performed.
