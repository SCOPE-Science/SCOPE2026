# Scientific review: three escape exponents and logarithmic memory

## Correctness — PASS

For every positive initial pair, the velocity-as-a-function-of-position equation has a global positive graph; the proof excludes both zero crossing and finite-position divergence. For positive coupling, two successive substitutions yield the exact logarithmic coefficient \(-32/b^3\) and an integrable derivative remainder, ensuring the finite-part constant exists. Zero coupling has an exact first integral. Negative coupling has a strictly decreasing auxiliary orbital vector field with an attracting moving nullcline converging to \(-2/c^3\). In all three cases the original-time reciprocal-velocity integral converges, proving finite-time blow-up and all escape exponents. The exact two-orbit gap equation proves the memory trichotomy. The attached exact-symbolic and finite numerical programs passed, but general conclusions rely on the proof rather than finite tests.

## Originality — PASS under the inspected evidence

The closest primary source, Cao–Sadri–Tang–Wang (arXiv:2610.26699, first released 19 October 2026), was inspected through its full accessible HTML: Introduction, Theorems, Sections 3 and 4, including Lemma 4.7 on dynamics at infinity and associated near-infinity asymptotic branches. Its classification of compactified orbits is not claimed as new. No theorem in the inspected material asserts the complete positive-quadrant physical-time exponent trichotomy, the third-order logarithmic correction, or the exactly quantified change from finite speed-memory to algebraic and Gaussian-in-position erasure.

The closest published mathematical-record comparison is *Universal two-term finite-time escape in polynomial nilpotent Liénard systems* (2026), whose complete RESULT.md was inspected. The leading restoring force in its escape wedge has opposite sign; its result does not entail the all-quadrant statement, the three-way damping-sign transition, or the logarithmic finite part and two-trajectory comparison here. The 1999 Dumortier–Herssens near-infinity work was identified but its complete text could not be inspected; equivalent earlier hidden asymptotics remain a priority risk. No claim of absolute novelty is made.

## Mathematical value — PASS

The sign of a single physical coefficient produces three distinct finite-time exponents for **every** positive-quadrant orbit in a natural reversible polynomial vector field. The first beyond-leading term is a universal logarithmic coefficient and, independently, the finite-part constant carries strictly ordered information about initial velocity only on one side of the transition. These are structural and quantitative distinctions not supplied by a topological infinity portrait alone; they provide reproducible benchmarks for singular ODE asymptotics and parameter-dependent memory effects.

## Scope and residual risks

The result does not assert a full phase portrait or classify solutions outside the positive quadrant, does not give a closed elementary expression for the initial-data-dependent finite part, and offers no uniform remainder over all initial conditions. Earlier qualitative near-infinity theorems, including inaccessible full text from 1999, may contain equivalent formulae not uncovered by the inspected sources; historical priority requires independent investigation. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
