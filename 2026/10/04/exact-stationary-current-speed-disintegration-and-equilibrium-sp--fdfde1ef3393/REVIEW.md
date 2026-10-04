# Same-model review

## Correctness
PASS. Arbitrary antiderivative tests in the disk-speed and motor coordinates give
\[
\mathbb E[x^2\mid y]=1-\frac{\kappa}{\alpha}y,
\qquad
\mathbb E[x\mid z]=\lambda z.
\]
Quadratic stationarity gives the exact current-energy-weighted speed identity, and
\[
\mathbb E[(x-\lambda z)^2]
=
\mathbb E[x^2]-\lambda^2\mathbb E[z^2]
\]
is the nonnegative defect. Zero current energy forces the trivial equilibrium. Zero defect forces the invariant support onto \(x=\lambda z\), after which bounded completeness reduces every support trajectory to an available equilibrium.

Risk: the support-rigidity argument uses the standard invariance of the support of a compactly supported invariant probability measure.

## Originality
PASS. Full same-system integrability treatments from 2014 and 2025 were inspected directly; their results concern first integrals, invariant algebraic surfaces, Darboux invariants, and orbit geometry rather than stationary invariant-probability disintegration. Same-system bifurcation and hidden-attractor literature was compared, and targeted searches for conditional-current, current-weighted-speed, and motor-relaxation-defect formulations found no implication-level coverage.

Risk: the complete 2022 article was not fully inspected, and a short time-average identity could occur incidentally in older engineering notation.

## Value
PASS. The result relates three physically natural observables—current intensity, disk speed, and motor relaxation—at the level of every compact stationary state. The conditional law supplies an exact binwise consistency check, while the equality-rigid defect distinguishes pure equilibrium support from genuine recurrent dynamics without depending on a chosen numerical attractor.

Same-model review: passed. Independent audit: not yet performed.
