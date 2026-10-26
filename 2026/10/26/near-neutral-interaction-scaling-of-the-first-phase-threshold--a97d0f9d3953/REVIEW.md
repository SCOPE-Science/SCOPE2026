# Self-review

## Correctness — PASS

The threshold polynomial is taken from Proposition 3.3 of Costa–Jordan. On the only interval where the additional roots responsible for the lower threshold can appear, \(1<z<1/a\), the derivative with respect to \(\beta\) is strictly negative. Solving the root equation and rescaling \(z=1+(1-a)s\) gives an exact infimum representation. The compact-interior convergence and endpoint controls justify the limit of the infima. The derivative-sign argument establishes a unique minimizer, so the limiting constant is well-defined. The numerical script checks only the reported decimal approximation.

## Originality — PASS (best-evidence assessment)

The inspected primary source proves divergence and gives bounds but does not state the sharp scaled limit. Semantic searches using the source polynomial, the threshold name, and the near-neutral parameter limit returned no same-claim result; the closest indexed records concern other phase transitions and do not imply this constant. The related binary feedback-urn paper has a different stochastic model and order parameter. This is a focused asymptotic refinement, not a novelty claim for the underlying urn model. Unindexed literature on bifurcation asymptotics remains a risk.

## Value — PASS

The threshold separates the one-stationary-point regime from the regime with additional asymmetric stationary points. Its divergence as interaction becomes neutral was known, but the exact coefficient in the natural scale \((1-a)^{-1}\) determines the leading reinforcement cost of that phase onset. The minimization and uniqueness proof supply a precise, reproducible constant rather than only another qualitative bound.

## Closest literature and limitations

Costa and Jordan, Proposition 3.3, give \(\beta_1(a)\to\infty\), coarse scaled bounds with endpoints \(2\) and \(3\), and an auxiliary lower bound \(\beta_0(a)\) defined by equation (25). The latter has scaled limit \(2+\log2\approx2.693147\), below the new constant, so it does not identify the threshold asymptotic. Nakayama–Mori analyze a binary feedback urn's critical autocorrelation scaling, not the same three-colour stationary-point threshold. No second-order term, finite-\(a\) closed form, or extension to more colours is claimed.

Self-review: passed. Independent audit: not yet performed.
