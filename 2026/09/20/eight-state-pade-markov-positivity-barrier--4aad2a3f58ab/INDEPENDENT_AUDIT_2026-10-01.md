# Independent audit — 2026-10-01

Final claim assessed: For the diagonal [2/2] Padé map, every fixed continuous-time Markov generator on at most seven states is positivity-safe for sufficiently small steps, while an eight-state pure-birth generator fails positivity for every sufficiently small positive step and has an exact stochasticity window.

## Correctness — PASS

The Maclaurin coefficients are positive through degree five, vanish at degree six, and are negative at degree seven. Shortest-path analysis gives a positive leading entry for every off-diagonal pair in dimensions at most seven, including the distance-six case where the degree-seven matrix coefficient is negative. The eight-state pure-birth Jordan calculation yields the stated first-to-absorbing polynomial boundary and nearest-neighbor upper boundary; symbolic identities independently reproduce the exact endpoints and row sums.

## Originality — PASS

Zappavigna–Colaneri–Kirkland–Shorten already exhibit an eight-by-eight nilpotent nonnegative shift with [2/2] Padé negativity for every positive step and a related Hurwitz Metzler example. Those matrices are not conservative Markov generators, and the paper does not give the seven-state lower bound or the exact pure-birth stochasticity window. Targeted searches found no prior theorem covering those conservative refinements.

## Scientific value — PASS

The result identifies a sharp state-space threshold under the conservation constraint and an exact nonmonotone stochasticity window for a canonical pure-birth witness, providing a meaningful boundary for Markov discretization.

## Sources and residual risks

- Zappavigna–Colaneri–Kirkland–Shorten, Essentially Negative News About Positive Systems (2012), full preprint inspected.
- Classical absolute-monotonicity literature cited in the package.
- Published-record semantic search for conservative CTMC [2/2] Padé positivity thresholds.
- The lower-dimensional result is local for each fixed generator, not a dimension-only step-size bound.
- The exact global window is for one witness and does not classify all eight-state generators.
- A recent Fokker–Planck rational-map preprint and some older absolute-monotonicity literature remain residual originality risks beyond the primary sources inspected.
