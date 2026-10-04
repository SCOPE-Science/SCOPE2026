# Review of Stationary height balance and Lyapunov-sum law in the Dong–Wang four-dimensional flow

## Correctness
PASS. The generator calculation is exact: \(L(y^2+z^2)=-2cy^2-2bz\), while \(Lz=-b+xy\). Invariance on compact support therefore gives \(b\langle z\rangle=-c\langle y^2\rangle\) and \(\langle xy\rangle=b\). For \(b,c>0\), the latter excludes \(\langle y^2\rangle=0\), so the mean height is strictly negative. The compact-half-space obstruction follows by existence of an invariant probability measure on any compact invariant set. The Lyapunov-sum formula follows from Liouville's determinant identity plus ergodicity. The included exact polynomial replay checks the algebra and source-parameter arithmetic.

## Originality
PASS. The introducing four-dimensional article was inspected at the system definition, divergence analysis, Lyapunov calculations, multistability sections, conclusion, and references. It gives a pointwise divergence criterion but not the stationary \(y^2+z^2\) balance, negative mean-height theorem, compact half-space obstruction, or explicit invariant-measure Lyapunov-sum law. The three-dimensional precursor was separately inspected because it shares the same \(y,z\) core; it also does not state these invariant-measure consequences. Exact-title, equation, formula, alias, and semantic searches found analogous recurrence identities only for different flows. General mean-divergence/Lyapunov literature does not imply the system-specific height law.

## Value
PASS. The claim converts a pointwise, state-dependent divergence expression into an exact recurrent-statistics law valid for every compact invariant state. It forces all compact recurrence to have negative mean \(z\), rules out compact invariant dynamics in an entire half-space, and supplies an exact Lyapunov-sum consistency relation for the published hyperchaos model. These are structural constraints on the flow rather than a finite numerical recomputation.

## Closest literature and limitations
The closest same-object sources are the 2022 four-dimensional article and its 2022 three-dimensional precursor. The closest methodological literature concerns mean divergence and Lyapunov sums for smooth flows. Search coverage is not exhaustive, so a poorly indexed later derivation of the same balance remains a residual originality risk. The theorem is necessary, not sufficient, for any particular attractor or spectrum.

Same-model review: passed. Independent audit: not yet performed.
