# Scientific review

## Correctness

PASS. The scalar logit coordinate makes the full-period return displacement strictly increasing, proving unique interior periodicity and repelling separation. The original equations, normalized selection-weighted residence measure, and its zeroth and first moments independently fix the mean and permit differentiation of the variance. The strict bounded-support variance inequality gives \(V'(T)>0\); the Floquet formula gives a strictly decreasing but positive exponent. Endpoint limits are justified by the exact residence-time integrals, not extrapolated from finite simulation. The packaged checker reproduces 31 numerical parameter/period cases and verifies centered-difference period derivatives.

## Originality

PASS with residual bibliographic uncertainty. Shu and Fu's original full text supplies the switched scalar equations, selected recurrent constructions and amplitude/dwell-time formulas in the symmetric case. These are not claimed anew. The independently proved result here is the selection-weighted exact variance derivative and the strict monotone Floquet slowdown for every asymmetric two-stage coordination pair and every period, with its sharp limiting rates and basin-separating interpretation. The 2006 Abel uniqueness literature potentially covers some uniqueness/hyperbolicity statements; no direct prior coverage of the principal monotonicity law was identified. The general possibility of an older equivalent parametric identity remains a literature risk.

## Value

PASS. Switching-induced oscillations may be misread as persistent attracting mixed strategy coexistence. The result separates an exact but fragile periodic threshold from an attracting coexistence state, and gives a sharp quantitative law: slowing environmental switching strictly reduces the local selection-divergence rate but can never stabilize the cycle. The all-period identity explains this via a measurable state-variance penalty and admits exact small- and large-period comparisons, including asymmetric duty fractions and payoffs.

## Relationship to literature and limitations

The closest work is Shu and Fu (2022), arXiv:2208.13306, Sections 3.1–3.3. Álvarez, Gasull and Giacomini (2006), arXiv:math/0602468, supply general prior uniqueness results for Abel equations; Loginov (2021), arXiv:2106.08224, studies a different endogenous-payoff model. This contribution does not cover feedback-dependent schedules, multidimensional games or stochastic perturbations. Its Floquet monotonicity is per unit time; the per-cycle multiplier is a different quantity.

Self-review: passed. Independent audit: not yet performed.
