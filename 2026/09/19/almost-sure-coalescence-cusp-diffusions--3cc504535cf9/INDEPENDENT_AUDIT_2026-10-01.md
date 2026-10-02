# Independent audit — Almost-sure coalescence and shrinking-gap bounds for cusp diffusions

Date: 2026-10-01 UTC

Disposition: passed.

## Final claim

For the four subcritical cusp diffusion coefficients, shrinking symmetric gaps collide locally with probability tending to one and have the stated collision-time upper scale; every fixed ordered synchronous pair coalesces in finite time almost surely.

## Correctness

PASS. The current Larsen preprint was inspected through page 12, including its literature review, pathwise-uniqueness setup and the start of the strict-comparison machinery. The audited argument validly retunes Larsen’s local-time threshold, applies DDS and Brownian local-time laws for the quantitative bound, and uses recurrence plus quadratic-variation contradiction to rule out a positive limiting gap. On the no-collision event the midpoint returns to zero while the gap tends to zero, so the strong Markov property and the shrinking-gap bound force the conditional survival probability to zero.

## Originality

PASS. Larsen’s primary paper proves failure of strict comparison by positive-probability collision for small subcritical cusp gaps; it does not state probability tending to one, the collision-time upper scale, or almost-sure coalescence for every fixed ordered pair. Published-record searches found no earlier record with these three conclusions. Classical Yamada/Ouknine–Rutkowski work concerns sufficient non-confluence/strong-comparison criteria, while Barlow et al. concerns skew Brownian coalescence, not these uniformly elliptic cusp coefficients.

## Value

PASS. The result materially strengthens the interpretation of the source counterexample: collision is not merely possible but asymptotically certain at small gap and eventually certain for every fixed pair. The quantitative time scale is a natural boundary statistic of the same mechanism.

## Source inspections

- Kasper Larsen, arXiv:2609.19389v2, Strict SDE Comparison for Cusp Coefficients and Counterexamples: primary full-text pages 1–12, including introduction, literature comparison, assumptions, cusp examples and strict-comparison Lyapunov setup. Finding: Subcritical cusp coefficients are counterexamples via positive-probability collision; the audited strengthening is not stated there.
- Barlow, Burdzy, Kaspi, Mandelbaum (2001), Coalescence of skew Brownian motions: bibliographic/source record and Larsen’s primary-paper discussion. Finding: Prior a.s. synchronous coalescence phenomenon in a different skew-Brownian/local-time model.

## Residual risks

- Full primary texts of Yamada (1986) and Ouknine–Rutkowski (1990) were not independently retrieved; Larsen’s current primary paper describes them as non-confluence criteria and not as coalescence theorems for these cusp coefficients.

The assessment concerns the single final claim stated above. Existing reproducibility material is evidence only and is not treated as independent certification.
