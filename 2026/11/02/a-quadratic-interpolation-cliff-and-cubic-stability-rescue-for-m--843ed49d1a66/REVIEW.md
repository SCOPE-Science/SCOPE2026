# Scientific review

## Correctness — PASS
The projective harmonic reproducing kernel has normalized Jacobi/hypergeometric form, so its sample Gram is positive semidefinite with rank equal to evaluation rank. Three possible squared overlaps (one, zero, and \(1/d\)) reduce that Gram to an explicit three-idempotent algebra. Direct substitution at degrees zero through three proves every rank and the one-dimensional complete-quadratic kernel. The dimension-uniform cubic condition bound and the incomplete-quadratic condition formula follow from explicit signed rational differences, not numerical fitting. `CHECK.py` uses exact fractions, tests the qutrit construction via Eisenstein norms, and independently checks small Gram ranks. The proof—not the finite checks—covers all allowed dimensions.

## Originality — PASS under bounded literature comparison
Klappenecker–Rötteler prove that maximal mutually unbiased bases are complex-projective two-designs. Roy–Scott analyze weighted projective designs and tomography; Koornwinder and De Bie–Sommen–Wutzig provide Jacobi reproducing-kernel machinery. None of the specifically inspected material states the one-basis quadratic interpolation cliff, universal cubic surjectivity, or the contrasting sharp conditioning laws. The result is a derived spectral classification, not a claim that the MUB construction or two-design property is new. Search comparisons included projective harmonics, Jacobi Gram spectra, third-degree interpolation, and the related design literature. An earlier equivalent association-scheme or quantum-tomography spectral calculation remains a real historical risk; the search cannot establish absolute priority.

## Mathematical value — PASS
The theorem determines the minimum *single* harmonic degree for interpolation over entire families of natural quantum/projective configurations. Most significantly, inclusion of the last basis reverses quadratic invertibility while replacing poorly conditioned quadratic sampling (condition number \(d+1\)) with uniformly conditioned cubic sampling (at most \(9/2\)). Both bounds are sharp. This interprets the known two-design cancellation as an exact interpolation and stability transition, including its unique lost direction. The quantitative contrast is not implied merely by the qualitative two-design statement.

## Limits and closest literature
The result is conditional on the existence of the stated bases and restricted to exact degrees at most three, with \(d\ge3\). It says nothing about noisy/approximately unbiased systems. Closest primary literature: Klappenecker–Rötteler (2005), Roy–Scott (2007), and the projective Jacobi/zonal addition theorem. A 2024 projective-toric-design paper is related background but not a demonstrated covering source. Older projective design or Bose–Mesner calculations could implicitly contain these identities. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
