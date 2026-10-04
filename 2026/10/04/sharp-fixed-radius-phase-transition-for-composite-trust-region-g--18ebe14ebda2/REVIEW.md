# Same-model review

## Correctness

PASS. The exact subproblem is piecewise linear after scaling by \(a>0\). Its two slopes are \(x-\theta\) and \(x+\theta\), where \(\theta=\lambda/a\), so the complete singleton/set-valued update map follows directly. For \(\eta<2\theta\), a first crossing from the outer region cannot jump across the entire interval \([-\theta,\theta]\); all subsequent admissible choices move into the strict inner region and then reach \(0\) after finitely many fixed-length moves. At \(\eta=2\theta\), the two threshold minimizer intervals contain the opposite threshold point. Above the threshold, every \(c\in(\theta,\eta-\theta)\) alternates uniquely with \(c-\eta<-\theta\).

The bundled exact-rational script checks representative trajectories in every regime, including branching at set-valued threshold states. It is supporting evidence only; the proof is the exact slope classification in `RESULT.md`.

## Originality

PASS. The recent primary paper states the same composite trust-region subproblem and proves local existence and uniqueness conditions, but it does not classify constant-radius trajectories. Kovalev's preceding full paper defines the same method and proves a generic best-iterate stationarity bound with a radius-dependent floor; no quadratic-plus-absolute-value phase transition or cycle family appears there.

The closest full-objective ball-oracle literature is materially different. The ball-proximal method minimizes the full convex objective in the ball and finitely terminates for every positive constant radius. That theorem does not cover the linearized-ball update here; instead, the contrast identifies the scientific point of the new result.

Targeted database searches over the algorithm name, aliases, the scalar composite model, fixed-radius cycling, overshoot, and finite termination returned no equivalent statement. Residual risk remains from older normalized-subgradient literature under different terminology.

## Value

PASS. The model is the standard scalar quadratic plus absolute-value regularizer, and its scale \(\lambda/a\) is intrinsic rather than chosen ad hoc. The exact threshold \(2\lambda/a\) distinguishes three qualitatively different dynamics, including an open tie-free cycling regime. This is useful for interpreting fixed trust radii in the new composite trust-region gradient framework and for understanding exactly how linearization can destroy the arbitrary-radius finite termination enjoyed by the full-objective ball oracle.

Same-model review: passed. Independent audit: not yet performed.
