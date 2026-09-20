# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof has two independent components.

First, the dimension lower bound uses the directed shortest-path structure of a CTMC generator together with the exact Maclaurin coefficients of the \([2/2]\) Padé function. For distances at most five the first nonzero matrix-power term has a positive coefficient. The exceptional seven-state distance-six case is handled explicitly: the sixth Padé coefficient vanishes, every nonzero length-seven matrix-product contribution must contain exactly one negative diagonal factor, and therefore \((Q^7)_{ij}<0\); multiplying by the negative seventh Padé coefficient again gives a positive leading term. Diagonal and unreachable entries are straightforward. This establishes a genuine neighborhood of entrywise positivity for every fixed generator of size at most seven.

Second, the eight-state pure-birth witness is evaluated exactly. Its transient block is a Jordan block, so all transient entries are scaled derivatives of the scalar Padé function. The first-to-absorbing entry factors as
\[
12h^7p(h)/(h^2+6h+12)^7,
\]
where \(p\) is strictly increasing on the positive axis and has the stated unique root. The nearest-neighbor transient entry changes sign exactly at \(2\sqrt3\). All remaining transient derivatives and absorbing-column remainders are nonnegative between these boundaries. Symbolic verification independently reconstructs these identities and boundary signs.

Stress tests included the endpoint cases, zero/unreachable transitions, the distance-six lower-bound exception, denominator invertibility, mass conservation, and the possibility of seven-off-diagonal-step walks in the minimal-dimension argument.

## Originality

**PASS, qualified as “to the best of our knowledge.”** The closest source is Zappavigna–Colaneri–Kirkland–Shorten (2012). Its Example 3 explicitly identifies the same coefficient pattern \(a_6=0\), \(a_7=-1/1728\) and an \(8\times8\) nilpotent nonnegative shift for which the second diagonal Padé map has a negative entry for every positive step; it also gives a shifted Hurwitz Metzler example with small-step failure. That paper was inspected at the theorem/example level. Its displayed counterexamples are not conservative CTMC generators and it does not state the seven-state local-positivity lower bound, minimal conservative dimension eight, or the exact stochasticity window of the pure-birth generator.

Absolute-monotonicity theory is a second close line. Lóczi–Ketcheson (2014) records exact radius \(0\) for the \((s,p)=(2,4)\) rational class and cites the foundational 1986 van de Griend–Kraaijevanger work. This establishes a broad no-uniform-monotonicity fact, so the present result is not claimed as the first observation that fourth-order \([2/2]\) Padé can violate positivity. The new claim is the finite conservative Markov classification and sharp witness window.

Searches using Padé/Gauss–Legendre, Markov generator/CTMC, stochasticity, pure-birth, minimum dimension, and the exact boundary polynomial/root did not locate the same theorem. The recent Itkin–Kazbek (2026) preprint is highly relevant because it studies positivity of rational maps for Fokker–Planck generators, but only its abstract-level statement was available in the material inspected; it emphasizes large-step criteria and different rational choices. Its full theorem text remains the most important current-source uncertainty. The 1986 van de Griend–Kraaijevanger article was identified through bibliographic records and later exact-radius work but was not inspected end to end.

## Value

**PASS.** The result turns a general monotonicity warning into a sharp finite-state failure certificate under exact probability conservation. The dimension-eight lower bound shows that the small-step pathology cannot occur in smaller CTMCs, while the explicit pure-birth calculation reveals the stronger nonmonotone phenomenon that an intermediate step-size interval restores stochasticity even though all sufficiently small positive steps fail. This is directly relevant when a fourth-order A-stable Gauss–Legendre/Padé step is used as an approximate Markov transition operator.

The contribution is structural rather than performance-oriented: it does not propose a competing CTMC integrator or claim an accuracy advantage.

## Scientific limitations

- Exact arithmetic and finite real CTMC generators only.
- Positivity is for the end-step matrix, not internal Gauss–Legendre stages.
- The seven-state statement is local for each fixed generator, not uniform over unbounded generator rates.
- The exact global positivity window is proved for one unit-rate pure-birth witness, not all eight-state generators.
- No minimal-dimension classification is claimed for other Padé orders or Runge--Kutta methods.
- No floating-point, nonlinear, efficiency, or error-versus-cost claim is made.
- Full theorem-level comparison with Itkin–Kazbek (2026) and end-to-end inspection of van de Griend–Kraaijevanger (1986) were not completed, leaving residual prior-coverage risk.
