# Self-review

## Correctness — PASS

For every strictly positive datum, the two-stage-rate matrix has positive diagonal denominators and yields strictly positive, conservative stage values. The exact two-by-two inversion is checked directly. Expanding its two nonnegative exchange rates at large offset and inducting through the fixed number of correction stages proves the coefficient \(m\eta_\ell ab(b-a)/[B_\ell(a+b)]\) with \(O(C^{-2})\) remainder. The Gauss–Lobatto endpoint weights are nonnegative, providing \(B_r=1\). The scalar exact flow gives the nonzero limiting local error. Rational checks reproduce the exact formulas, but are not substituted for the proof.

## Originality — PASS, residual risk

The closest sources are Öffner–Redle–Torlo, arXiv:2610.21857v1, §4, which formulates flux-globalization and nonnegative face-flux production/destruction terms; Öffner–Torlo, arXiv:1905.09237v2, which defines the generic mPDeC algorithm; and Izgin–Öffner, arXiv:2206.07371v4, §4, which derives stability maps in the canonical linear production-rate representation. The generic algorithm can be specialized to the present problem, but no inspected source supplies the quantified flux-offset stalling law, its arbitrary-finite-correction coefficient, or the representation comparison. A possible unindexed equivalent remains a bibliographic risk; search absence is not proof of novelty.

## Mathematical value — PASS

An additive constant to a conservative flux is ordinarily mathematically invisible, while flux-to-production/destruction splitting keeps the absolute face rates and makes the positive linearly implicit update representation-dependent. The sharp universal \(1/C\) coefficient gives the size of the resulting stalling for every finite correction budget and explains why positivity, conservation, and formal high order at fixed representation cannot guarantee uniform accuracy under flux gauges. This is a genuine structural limitation relevant to designing gauge-normalized flux-to-rate conversions rather than a check of a notational convention.

## Scope and open boundaries

Only a two-cell periodic upwind semidiscretization, exact arithmetic, fixed time step and finite corrections are covered. The source implementation fixes a flux convention and is not asserted to fail for its chosen convention. There is no claim of a universal instability for every flux or of nonconvergence as the step size tends to zero. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
