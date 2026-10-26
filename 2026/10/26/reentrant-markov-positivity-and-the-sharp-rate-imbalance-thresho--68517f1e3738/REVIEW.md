# Scientific review

## Correctness — PASS

The two-eigenvalue projector decomposition gives the exact endpoint matrix, with resolvent denominator positive for all nonnegative steps. Every off-diagonal is strictly positive at a positive step, and the least diagonal has numerator \(F_m(s)=ms^2+(6m-2)s+6\). The exact quadratic discriminant and roots establish all parameter regimes, their boundary cases, and the square-root opening of the failed-positivity interval. A separate identity proves strict stationary-weighted contraction and strict positivity of the squared endpoint matrix. The exact rational witness independently tests the interpretation. Finite checker tests support the derivation, rather than replacing the all-parameter proof.

## Originality — PASS, with priority limitations

Jiao–Sun–Wu's full 2026 source covers energy laws for the same Padé family but not the two-state Markov sign-phase classification. The published [2/2] Padé eight-state barrier, [1/1] Crank–Nicolson return law, and midpoint-square SSP-SDIRK2 endpoint theorem were inspected by mathematical implication and do not cover this rational function. Full Zappavigna–Colaneri–Kirkland–Shorten 2012 diagonal-Padé text gives a different rational family. Searches of historical and published records found no formula implying the sharp ratio, disconnected positive-step set, coincident endpoints, and strict two-step repair. Accessible Itkin–Kazbek material discusses broader eventual positivity but not the exact two-state theorem. Older Horváth papers and the full Itkin–Kazbek text remain incompletely accessible and are explicit priority risks. The absence of a located result does not prove novelty.

## Mathematical value — PASS

Preserving nonnegative probability data is a natural nonnegotiable structural requirement for integrating Markov-chain forward equations. This theorem establishes a sharp and nonmonotone positivity phase diagram for a named widely used stiff integrator: reducing the time step can restore positivity, but sufficiently increasing it also restores positivity. It quantifies the smallest rate imbalance producing that behavior, separates weighted-norm contractivity from simplex invariance, and proves that identical consecutive steps repair the one-step sign violation. Those statements specify a genuine parameter-selection boundary, not a small accuracy increment or a relabeling of generic A-stability.

## Scope and residual risks

The result is a complete exact classification only for irreducible two-state autonomous generators. No positivity is claimed for intermediate stages or unequal successive steps. Equivalent exact results might appear in inaccessible specialized literature; independent assessment of priority and correctness has not occurred.

Self-review: passed. Independent audit: not yet performed.
